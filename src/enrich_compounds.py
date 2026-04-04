"""Enrich compound cards with suffix explanations, root-change notes, and better mnemonics."""
import json

# === SUFFIX REFERENCE ===
SUFFIX_DB = {
    "τός": {
        "label": "-τός",
        "type": "adjetivo verbal",
        "explanation_es": "Sufijo que convierte verbos en adjetivos. Indica 'que ha sido X' o 'capaz de ser X'. Como '-do' o '-ble' en español. Ej: ἀγαπάω→ἀγαπητός (amado), ἐκλέγω→ἐκλεκτός (elegido)."
    },
    "σις": {
        "label": "-σις",
        "type": "sustantivo de acción/proceso (fem.)",
        "explanation_es": "Sufijo que crea sustantivos de acción o proceso. Como '-ción' en español. Indica 'el acto de X'. Ej: κρίνω→κρίσις (juicio), πράσσω→πρᾶξις (acción)."
    },
    "μα": {
        "label": "-μα",
        "type": "sustantivo de resultado (neutro)",
        "explanation_es": "Sufijo que crea sustantivos de resultado. Indica 'lo que resulta de X'. Ej: γράφω→γράμμα (letra/escrito), βάπτω→βάπτισμα (bautismo)."
    },
    "ία": {
        "label": "-ία",
        "type": "sustantivo de cualidad/estado (fem.)",
        "explanation_es": "Sufijo que crea sustantivos abstractos de cualidad o estado. Como '-ía' o '-eza' en español. Ej: σοφός→σοφία (sabiduría), ἀληθής→ἀλήθεια (verdad)."
    },
    "εια": {
        "label": "-εια",
        "type": "sustantivo de cualidad/estado (fem.)",
        "explanation_es": "Variante de -ία. Crea sustantivos abstractos de cualidad. Ej: ἀληθής→ἀλήθεια (verdad)."
    },
    "μός": {
        "label": "-μός",
        "type": "sustantivo de acción/proceso (masc.)",
        "explanation_es": "Sufijo que crea sustantivos de acción o proceso. Ej: σείω→σεισμός (terremoto), βάπτω→βαπτισμός (lavamiento)."
    },
    "ή": {
        "label": "-ή",
        "type": "sustantivo de acción/resultado (fem.)",
        "explanation_es": "Sufijo que crea sustantivos de acción o su resultado. Muy productivo en compuestos. Ej: βάλλω→βολή (lanzamiento), γράφω→γραφή (escritura)."
    },
    "ικός": {
        "label": "-ικός",
        "type": "adjetivo de relación",
        "explanation_es": "Sufijo adjetival que indica 'que tiene la característica de'. Como '-ico' en español. Ej: βασιλεύς→βασιλικός (real/regio)."
    },
    "ιος": {
        "label": "-ιος",
        "type": "adjetivo de pertenencia",
        "explanation_es": "Sufijo adjetival que indica 'perteneciente a' o 'relacionado con'. Ej: θάλασσα→θαλάσσιος (marino)."
    },
    "ών": {
        "label": "-ών",
        "type": "sustantivo de lugar (masc.)",
        "explanation_es": "Sufijo que indica lugar donde algo ocurre. Ej: ἄμπελος→ἀμπελών (viñedo), ἕδρα→ἀφεδρών (letrina)."
    },
    "τής": {
        "label": "-τής",
        "type": "sustantivo de agente (masc.)",
        "explanation_es": "Sufijo que indica 'el que hace X'. Como '-dor'/'-ista' en español. Ej: κρίνω→κριτής (juez), βάπτω→βαπτιστής (bautizador)."
    },
}

# === ROOT CHANGES: verb → derived form ===
ROOT_CHANGES = {
    # lemma: (parent_verb, root_note_es)
    "διαθήκη": ("τίθημι", "La raíz de τίθημι (poner) es θε-/θη-. El τι- del inicio es reduplicación. En sustantivos aparece como -θηκ-: δια-θήκ-η."),
    "καταβολή": ("βάλλω", "La raíz de βάλλω (lanzar) cambia de βαλ- a βολ- en sustantivos (como en español: 'cantar'→'canción'). κατα-βολ-ή."),
    "παραβολή": ("βάλλω", "La raíz de βάλλω (lanzar) cambia de βαλ- a βολ- en sustantivos. παρα-βολ-ή = 'lanzamiento al lado' = comparación."),
    "πρόθεσις": ("τίθημι", "La raíz de τίθημι (poner) es θε-. El τι- es reduplicación. πρό-θε-σις = 'acción de poner delante'."),
    "ἀποθήκη": ("τίθημι", "La raíz de τίθημι (poner) es θη-/θε-. ἀπο-θήκ-η = 'lugar para poner aparte' = almacén."),
    "ἀνάστασις": ("ἵστημι", "La raíz de ἵστημι (poner de pie) es στα-/στη-. El ἱ- es reduplicación. ἀνά-στα-σις = 'acción de ponerse de pie' = resurrección."),
    "ἀποστάσιον": ("ἵστημι", "La raíz de ἵστημι (poner de pie) es στα-. ἀπο-στά-σιον = 'ponerse aparte' = certificado de divorcio."),
    "ἀπόστολος": ("στέλλω", "La raíz de στέλλω (enviar) cambia de στελ- a στολ- en sustantivos. ἀπό-στολ-ος = 'el enviado lejos' = apóstol."),
    "συνετός": ("ἵημι", "Viene del verbo συνίημι (entender) = σύν + ἵημι (lanzar). La raíz de ἵημι es solo ε- (el ἱ- es reduplicación). συν-ε-τός = 'el que junta/entiende'."),
    "ἀνεκτός": ("ἔχω", "Viene de ἀνέχομαι (soportar) = ἀνά + ἔχω. La raíz de ἔχω aparece como εκ- en derivados. ἀν-εκ-τός = 'que se puede soportar'."),
    "ἐκλεκτός": ("λέγω", "λέγω puede significar 'escoger' (no solo 'decir'). La raíz aparece como λεκ- en derivados. ἐκ-λεκ-τός = 'escogido de entre' = elegido."),
    "ἐκκλησία": ("καλέω", "Viene de καλέω (llamar), NO de λέγω. La raíz de καλέω aparece como κλη- en derivados. ἐκ-κλη-σία = 'los llamados fuera' = asamblea."),
    "ἀντάλλαγμα": ("ἀλλάσσω", "La raíz de ἀλλάσσω (cambiar) aparece como ἀλλαγ- en sustantivos. ἀντ-άλλαγ-μα = 'lo intercambiado'."),
    "διαλογισμός": ("λογίζομαι", "De λογίζομαι (razonar), raíz λογ- (de λόγος, palabra/razón). δια-λογ-ισμός = 'proceso de razonar a fondo'."),
    "κατακλυσμός": ("κλύζω", "La raíz de κλύζω (inundar) aparece como κλυσ- en sustantivos. κατα-κλυσ-μός = 'proceso de inundar sobre' = diluvio."),
    "κατασκήνωσις": ("σκηνόω", "De σκηνόω (habitar en tienda), de σκηνή (tienda). κατα-σκήνω-σις = 'acción de establecer tienda' = nido/morada."),
    "συντέλεια": ("τελέω", "De τελέω (completar), raíz τελ- (de τέλος, fin). συν-τέλ-εια = 'estado de completar juntos' = consumación."),
    "ἀνατολή": ("τέλλω", "La raíz de τέλλω (brotar/surgir) aparece como τολ- en sustantivos. ἀνα-τολ-ή = 'acción de surgir arriba' = salida del sol = oriente."),
    "συναγωγή": ("ἄγω", "La raíz de ἄγω (conducir) se extiende a ἀγωγ- en sustantivos. συν-αγωγ-ή = 'acción de conducir juntos' = lugar de reunión."),
    "προσευχή": ("εὔχομαι", "De εὔχομαι (orar/hacer voto), raíz εὐχ-. προσ-ευχ-ή = 'acción de orar hacia' = oración."),
    "ἐντολή": ("τέλλω", "La raíz de τέλλω (cumplir) aparece como τολ- en sustantivos. ἐν-τολ-ή = 'lo que se cumple dentro' = mandamiento."),
    "καταπέτασμα": ("πετάννυμι", "La raíz de πετάννυμι (extender) aparece como πετασ- en sustantivos. κατα-πέτασ-μα = 'lo extendido hacia abajo' = velo/cortina."),
    "ἀπάντησις": ("ἀντάω", "De ἀντάω (encontrar), raíz ἀντ-. ἀπ-άντη-σις = 'acción de salir al encuentro'."),
    "ἐνθύμησις": ("ἐνθυμέομαι", "De ἐνθυμέομαι (reflexionar) = ἐν + θυμός (ánimo). ἐνθύμη-σις = 'acción de reflexionar' = pensamiento."),
    "ἀνάπαυσις": ("παύω", "De παύω (cesar), raíz παυ-. ἀνά-παυ-σις = 'acción de hacer cesar' = descanso."),
    "ὑποκριτής": ("κρίνω", "De ὑποκρίνομαι (actuar en teatro) = ὑπό + κρίνω. En griego antiguo, un ὑπο-κρι-τής era un actor de teatro. Luego pasó a significar 'el que finge' = hipócrita."),
    "προσήλυτος": ("ἔρχομαι", "La raíz antigua de ἔρχομαι (venir) es ἐλυθ-/ηλυ-. προσ-ήλυ-τος = 'el que ha venido hacia' = converso/prosélito."),
    "ἀπώλεια": ("ἀπόλλυμι", "De ἀπόλλυμι (destruir). La raíz de ὄλλυμι aparece como ωλ- en sustantivos. ἀπ-ώλ-εια = 'estado de destrucción completa' = perdición."),
    "ἀφίημι": ("ἵημι", "ἀφ- es la forma de ἀπό ante aspiración (ἀπό + ἵημι → ἀφίημι). ἵημι = enviar/soltar. ἀφ-ίημι = 'soltar lejos' = perdonar/dejar."),
    "ἀφεδρών": ("ἕδρα", "ἀφ- es la forma de ἀπό ante aspiración (ἀπό + ἕδρα → ἀφεδρών). ἕδρα = asiento. ἀφ-εδρ-ών = 'lugar del asiento apartado' = letrina."),
    "εὐδοκία": ("δοκέω", "De εὐδοκέω (complacerse) = εὐ + δοκέω (pensar/parecer). εὐ-δοκ-ία = 'estado de pensar bien' = beneplácito."),
    "εὐκαιρία": ("καιρός", "De εὔκαιρος (oportuno) = εὐ + καιρός (momento). εὐ-καιρ-ία = 'estado de buen momento' = oportunidad."),
    "ἀκαθαρσία": ("καθαρός", "De ἀκάθαρτος (impuro) = ἀ- + καθαρός (limpio). ἀ-καθαρσ-ία = 'estado de no estar limpio' = impureza."),
    "ἀκρασία": ("κράτος", "ἀ- (sin) + κράτος (dominio/fuerza). ἀ-κρασ-ία = 'estado de no tener dominio' = falta de autocontrol."),
    "ἀνομία": ("νόμος", "ἀ- (sin) + νόμος (ley). ἀ-νομ-ία = 'estado de estar sin ley' = iniquidad."),
    "ἀπιστία": ("πίστις", "ἀ- (sin) + πίστις (fe). ἀ-πιστ-ία = 'estado de no tener fe' = incredulidad."),
    "πολυλογία": ("λόγος", "πολύς (mucho) + λόγος (palabra). πολυ-λογ-ία = 'estado de muchas palabras' = palabrería."),
    "ὀλιγοπιστία": ("πίστις", "ὀλίγος (poco) + πίστις (fe). ὀλιγο-πιστ-ία = 'estado de poca fe'."),
    "ἀδελφή": (None, "ἀ- aquí es copulativo (= 'mismo'), NO privativo. δελφύς = vientre/útero. ἀ-δελφ-ή = 'del mismo vientre' = hermana."),
    "ἀδελφός": (None, "ἀ- aquí es copulativo (= 'mismo'), NO privativo. δελφύς = vientre/útero. ἀ-δελφ-ός = 'del mismo vientre' = hermano."),
    "παραλυτικός": ("λύω", "De παραλύω (aflojar al lado) = παρά + λύω (soltar). παρα-λυ-τικός = 'que tiene la característica de estar aflojado' = paralítico."),
    "παραθαλάσσιος": ("θάλασσα", "παρά (junto a) + θάλασσα (mar). παρα-θαλάσσ-ιος = 'perteneciente a lo que está junto al mar' = costero."),
    "ἀκέραιος": (None, "ἀ- (sin) + κεράννυμι (mezclar). ἀ-κέρα-ιος = 'sin mezcla' = puro, inocente, sin malicia."),
    "ἀναίτιος": (None, "ἀν- (sin) + αἴτιος (culpable). ἀν-αίτ-ιος = 'sin culpa' = inocente."),
    "ἀλλήλων": (None, "ἄλλος (otro) + ἄλλος (otro). Pronombre recíproco: 'unos a otros'. Se formó duplicando ἄλλος."),
}

def detect_suffix(lemma, pos):
    """Detect the most specific suffix in a lemma."""
    if pos == "V-":
        return None  # Verbs don't get suffix explanations
    # Check longest suffixes first
    for suf in ["ικός","ιος","τής","σις","μός","τός","ία","εια","μα","ών","ή"]:
        if lemma.endswith(suf):
            return suf
    return None

def enrich_card(card):
    """Add suffix, root_note, derivation_chain to a card."""
    lemma = card["lemma"]
    pos = card.get("pos", "")

    # Suffix
    suf = detect_suffix(lemma, pos)
    if suf and suf in SUFFIX_DB:
        card["suffix"] = SUFFIX_DB[suf]["label"]
        card["suffix_type_es"] = SUFFIX_DB[suf]["type"]
        card["suffix_explanation_es"] = SUFFIX_DB[suf]["explanation_es"]

    # Root change / derivation note
    if lemma in ROOT_CHANGES:
        parent, note = ROOT_CHANGES[lemma]
        card["root_note_es"] = note
        if parent:
            card["parent_verb"] = parent

    return card

# Load and enrich
with open("data/matthew/compounds_enriched.json") as f:
    cards = json.load(f)

for card in cards:
    enrich_card(card)

# Stats
has_suffix = sum(1 for c in cards if "suffix" in c)
has_root = sum(1 for c in cards if "root_note_es" in c)
print(f"Total cards: {len(cards)}")
print(f"Cards with suffix explanation: {has_suffix}")
print(f"Cards with root-change note: {has_root}")

with open("data/matthew/compounds_enriched.json", "w") as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)
print("Saved to data/matthew/compounds_enriched.json")
