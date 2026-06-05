"""AnkiConnect client with thread-safe locking."""
import json
import threading
import urllib.request
from typing import Any


class AnkiConnectError(Exception):
    pass


class AnkiClient:
    def __init__(self, url: str = "http://localhost:8765"):
        self.url = url
        self._lock = threading.Lock()

    def call(self, action: str, **params: Any) -> Any:
        body = json.dumps({"action": action, "version": 6, "params": params}).encode()
        with self._lock:
            try:
                req = urllib.request.Request(self.url, body, headers={"Content-Type": "application/json"})
                resp = urllib.request.urlopen(req, timeout=30)
                result = json.loads(resp.read())
            except (ConnectionRefusedError, OSError) as e:
                raise AnkiConnectError(f"AnkiConnect unreachable: {e}")
        if result.get("error"):
            raise AnkiConnectError(result["error"])
        return result.get("result")
