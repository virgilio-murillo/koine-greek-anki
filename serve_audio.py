#!/usr/bin/env python3
"""Auto-serve MP3 files with a 6-file safety buffer. Phone auto-downloads new files."""

import http.server
import json
import os
import re
import socketserver
import ssl

PORT = 8080
LESSONS_DIR = os.path.join(os.path.dirname(__file__), "decks", "lessons")
BUFFER = 6

def get_safe_files():
    files = [f for f in os.listdir(LESSONS_DIR) if f.endswith(".mp3")]
    numbered = {}
    for f in files:
        m = re.search(r"(\d+)", f)
        if m:
            numbered[int(m.group(1))] = f
    if not numbered:
        return []
    max_num = max(numbered)
    return sorted(numbered[n] for n in numbered if n <= max_num - BUFFER)

INDEX_HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>Audio Sync</title>
<style>
body{font-family:sans-serif;padding:16px;background:#111;color:#eee}
h2{color:#4fc3f7} .done{color:#66bb6a} .new{color:#ffa726} .pending{color:#888}
a{color:#4fc3f7} #status{margin:12px 0;font-size:1.1em}
</style></head><body>
<h2>Audio Auto-Downloader</h2>
<p id="status">Scanning...</p>
<ul id="list"></ul>
<script>
const downloaded = new Set(JSON.parse(localStorage.getItem('downloaded') || '[]'));
const list = document.getElementById('list');
const status = document.getElementById('status');

async function poll() {
  try {
    const r = await fetch('/api/files');
    const files = await r.json();
    status.textContent = `${files.length} files ready | ${downloaded.size} downloaded`;
    list.innerHTML = '';
    const toDownload = [];
    for (const f of files) {
      const li = document.createElement('li');
      if (downloaded.has(f)) {
        li.className = 'done';
        li.textContent = f + ' ✓';
      } else {
        li.className = 'new';
        li.textContent = f + ' ⬇';
        toDownload.push(f);
      }
      list.appendChild(li);
    }
    for (const f of toDownload) {
      const a = document.createElement('a');
      a.href = '/audio/' + f;
      a.download = f;
      document.body.appendChild(a);
      a.click();
      a.remove();
      downloaded.add(f);
      await new Promise(r => setTimeout(r, 500));
    }
    localStorage.setItem('downloaded', JSON.stringify([...downloaded]));
  } catch(e) { status.textContent = 'Connection error, retrying...'; }
}
poll();
setInterval(poll, 10000);
</script></body></html>"""

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(INDEX_HTML.encode())
        elif self.path == "/api/files":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(get_safe_files()).encode())
        elif self.path.startswith("/audio/"):
            fname = os.path.basename(self.path[7:])
            fpath = os.path.join(LESSONS_DIR, fname)
            if fname in get_safe_files() and os.path.isfile(fpath):
                self.send_response(200)
                self.send_header("Content-Type", "audio/mpeg")
                self.send_header("Content-Disposition", f'attachment; filename="{fname}"')
                self.send_header("Content-Length", str(os.path.getsize(fpath)))
                self.end_headers()
                with open(fpath, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"  {args[0]}")

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(os.path.join(os.path.dirname(__file__), "cert.pem"),
                        os.path.join(os.path.dirname(__file__), "key.pem"))
    httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
    print(f"\n🎵 Audio server running at https://192.168.1.76:{PORT}")
    print(f"   Watching: {LESSONS_DIR}")
    print(f"   Buffer: {BUFFER} files behind latest\n")
    safe = get_safe_files()
    print(f"   Ready now: {len(safe)} files")
    if safe:
        print(f"   Latest safe: {safe[-1]}\n")
    httpd.serve_forever()
