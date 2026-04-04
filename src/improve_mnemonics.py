"""Improve mnemonics for all 290 cards using enriched data."""
import json

with open("data/matthew/compounds_enriched.json") as f:
    cards = json.load(f)

# Better mnemonics map: lemma -> improved mnemonic
# Only for cards that need improvement (short or unhelpful mnemonics)
BETTER_MNEMONICS = {
# δια- verbs: add context about what "through/completely" means here
"διαβλέπω": "δια (a través) + βλέπω (ver). Literalmente 'ver a través' de algo — como cuando se aclara la vista y puedes ver con claridad total.",
"διακαθαρίζω": "δια (completamente) + καθαρίζω (limpiar). El prefijo δια- intensifica: no solo limpiar, sino limpiar A FONDO, sin dejar nada sucio.",
"διακονέω": "δια (a través) + κόνις (polvo). Imagen: el sirviente que corre a través del polvo para atender. De aquí viene 'diácono' en español.",
"διακωλύω": "δια (completamente) + κωλύω (impedir). Impedir de manera total, bloquear por completo.",
"διαλογισμός": "δια (a través) + λογίζομαι (razonar). El proceso de razonar algo a fondo, darle vueltas en la mente. De aquí viene 'diálogo' en español.",
"διαπεράω": "δια (a través) + περάω (cruzar). Cruzar de un lado al otro — como cruzar un lago o un río.",
"διαρρήγνυμι": "δια (a través) + ῥήγνυμι (rasgar). Rasgar de lado a lado — como el sumo sacerdote rasgando sus vestiduras (Mt 26:65).",
"διαστρέφω": "δια (completamente) + στρέφω (torcer). Torcer algo por completo hasta deformarlo — pervertir, distorsionar la verdad.",
"διασῴζω": "δια (completamente) + σῴζω (salvar). Salvar de manera completa, rescatar totalmente del peligro.",
"εἰσέρχομαι": "εἰς (hacia adentro) + ἔρχομαι (ir/venir). Ir hacia adentro = entrar. Muy frecuente en los evangelios: 'entró en la casa', 'entró en el reino'.",
"εἰσπορεύομαι": "εἰς (hacia adentro) + πορεύομαι (ir/caminar). Caminar hacia adentro = entrar. Similar a εἰσέρχομαι pero enfatiza el caminar.",
"εἰσφέρω": "εἰς (hacia adentro) + φέρω (llevar/cargar). Llevar algo hacia adentro = introducir. 'No nos lleves (εἰσφέρω) a tentación' (Mt 6:13).",
"εὐαγγέλιον": "εὐ (bueno) + ἄγγελος (mensaje/mensajero). Literalmente 'buen mensaje'. De aquí viene 'evangelio' en español. Un ángel (ἄγγελος) trae el buen (εὐ) mensaje.",
"εὐαγγελίζω": "εὐ (bueno) + ἄγγελος (mensaje). Verbo: anunciar el buen mensaje = evangelizar.",
"εὐνοῦχος": "εὐνή (cama) + ἔχω (guardar/tener). El 'guardián de la cama' — originalmente el encargado del harén real. De aquí viene 'eunuco' en español.",
"εὐρύχωρος": "εὐρύς (ancho) + χῶρος (espacio). Espacio ancho = espacioso. Jesús habla del camino εὐρύχωρος (espacioso) que lleva a la perdición (Mt 7:13).",
"καταβαίνω": "κατά (hacia abajo) + βαίνω (ir). Ir hacia abajo = descender. Lo opuesto de ἀναβαίνω (subir).",
"καταγελάω": "κατά (contra) + γελάω (reír). Reír contra alguien = burlarse. Cuando Jesús dijo que la niña dormía, 'se burlaban de él' (Mt 9:24).",
"καταδικάζω": "κατά (contra) + δικάζω (juzgar). Juzgar contra alguien = condenar. El juicio va EN CONTRA del acusado.",
"κατακαίω": "κατά (completamente) + καίω (quemar). Quemar por completo, reducir a cenizas. Juan Bautista: 'quemará la paja con fuego' (Mt 3:12).",
"κατακρίνω": "κατά (contra) + κρίνω (juzgar). Juzgar en contra = condenar. Similar a καταδικάζω pero más judicial.",
"καταλείπω": "κατά (completamente) + λείπω (dejar). Dejar completamente = abandonar. 'Dejará el hombre a su padre y madre' (Mt 19:5).",
"καταλύω": "κατά (abajo) + λύω (soltar/desatar). Soltar hacia abajo = derribar, destruir. 'No vine a destruir la ley' (Mt 5:17). De aquí viene 'catálisis' (descomposición).",
"καταμαρτυρέω": "κατά (contra) + μαρτυρέω (testificar). Testificar EN CONTRA de alguien. 'Mártir' viene de μάρτυς (testigo).",
"κατανοέω": "κατά (completamente) + νοέω (percibir con la mente). Percibir algo a fondo = considerar, observar con atención.",
"καταπατέω": "κατά (abajo) + πατέω (pisar). Pisar hacia abajo = pisotear. 'No echéis perlas a los cerdos, no sea que las pisoteen' (Mt 7:6).",
"καταράομαι": "κατά (contra) + ἀρά (maldición). Lanzar una maldición contra alguien = maldecir.",
"καταρτίζω": "κατά (completamente) + ἀρτίζω (preparar/ajustar). Preparar completamente = restaurar, perfeccionar. 'Remendaban sus redes' (Mt 4:21).",
"κατασκευάζω": "κατά (completamente) + σκευάζω (preparar/equipar). Preparar completamente = construir. Juan Bautista 'preparará tu camino' (Mt 11:10).",
"καταστρέφω": "κατά (abajo) + στρέφω (voltear). Voltear hacia abajo = derribar. Jesús 'volcó las mesas' de los cambistas (Mt 21:12). De aquí: 'catástrofe'.",
"καταφιλέω": "κατά (intensamente) + φιλέω (besar). Besar con intensidad/afecto. Judas 'besó' a Jesús para identificarlo (Mt 26:49).",
"καταφρονέω": "κατά (contra) + φρονέω (pensar). Pensar contra/en contra de alguien = despreciar, menospreciar.",
"μεταίρω": "μετά (cambio de lugar) + αἴρω (levantar). Levantar y cambiar de lugar = partir, mudarse.",
"μεταβαίνω": "μετά (cambio) + βαίνω (ir). Ir con cambio de lugar = trasladarse, pasar de un sitio a otro.",
"μεταμέλομαι": "μετά (cambio) + μέλομαι (importar/preocupar). Cambiar lo que te importa = arrepentirse. Diferente de μετανοέω: este es arrepentimiento emocional (remordimiento).",
"μεταμορφόομαι": "μετά (cambio) + μορφή (forma). Cambiar de forma = transfigurarse. De aquí viene 'metamorfosis'. La transfiguración de Jesús (Mt 17:2).",
"μετανοέω": "μετά (cambio) + νοέω (pensar). Cambiar de mente/pensamiento = arrepentirse. Este es arrepentimiento intelectual/volitivo (decisión de cambiar).",
"περιάγω": "περί (alrededor) + ἄγω (conducir). Conducir alrededor = recorrer. 'Jesús recorría todas las ciudades' (Mt 9:35).",
"περιβάλλω": "περί (alrededor) + βάλλω (lanzar). Lanzar alrededor = envolver, vestir. Echar tela alrededor del cuerpo = vestir.",
"περιπατέω": "περί (alrededor) + πατέω (caminar). Caminar alrededor = andar. Jesús 'andaba junto al mar' (Mt 4:18). Muy frecuente en el NT.",
"περιτίθημι": "περί (alrededor) + τίθημι (poner). Poner alrededor = colocar encima. 'Le pusieron una corona de espinas' (Mt 27:29).",
"προσέρχομαι": "πρός (hacia) + ἔρχομαι (venir). Venir hacia alguien = acercarse. Palabra muy frecuente: 'se le acercaron los discípulos'.",
"προσέχω": "πρός (hacia) + ἔχω (tener/dirigir). Dirigir la atención hacia = prestar atención, tener cuidado. 'Guardaos de los falsos profetas' (Mt 7:15).",
"προσδοκάω": "πρός (hacia) + δοκάω (esperar/mirar). Mirar hacia adelante esperando = aguardar. '¿Eres tú el que había de venir, o esperaremos a otro?' (Mt 11:3).",
"προσκυνέω": "πρός (hacia) + κυνέω (besar). Besar hacia = postrarse en adoración. En la antigüedad, adorar implicaba besar la mano o el suelo hacia la deidad.",
"προσκόπτω": "πρός (contra) + κόπτω (golpear). Golpear contra algo = tropezar. 'No sea que tropieces tu pie contra una piedra' (Mt 4:6).",
"συνάγω": "σύν (juntos) + ἄγω (conducir). Conducir juntos = reunir, congregar. De aquí viene 'sinagoga' (συναγωγή = lugar de reunión).",
"συνέδριον": "σύν (juntos) + ἕδρα (asiento). Sentarse juntos = concilio. El Sanedrín era el consejo supremo judío. De aquí: 'cátedra' (de ἕδρα).",
"συνέρχομαι": "σύν (juntos) + ἔρχομαι (venir). Venir juntos = reunirse.",
"συνέχω": "σύν (juntos) + ἔχω (tener/sostener). Sostener junto = apretar, oprimir, constreñir. Como cuando algo te aprieta por todos lados.",
"συνίημι": "σύν (juntos) + ἵημι (lanzar/enviar). Lanzar juntos = juntar ideas en la mente = entender, comprender. De aquí: συνετός (inteligente).",
"συναίρω": "σύν (juntos) + αἴρω (levantar). Levantar juntos = hacer balance, ajustar cuentas. 'Un rey que quiso ajustar cuentas con sus siervos' (Mt 18:23).",
"συνανάκειμαι": "σύν (con) + ἀνά (arriba) + κεῖμαι (estar reclinado). Estar reclinado juntos a la mesa = comer juntos. En la antigüedad se comía reclinado.",
"συναυξάνομαι": "σύν (juntos) + αὐξάνω (crecer). Crecer juntos. 'Dejad crecer juntamente el trigo y la cizaña' (Mt 13:30).",
"συντάσσω": "σύν (juntos) + τάσσω (ordenar/organizar). Ordenar juntos = dar instrucciones coordinadas.",
"συντηρέω": "σύν (juntos) + τηρέω (guardar). Guardar junto = preservar, mantener intacto.",
"συντρίβω": "σύν (junto) + τρίβω (frotar/moler). Frotar junto hasta pulverizar = quebrantar, romper en pedazos.",
"ἀδικέω": "ἀ- (sin) + δίκη (justicia). Actuar sin justicia = ser injusto, hacer daño. De aquí: 'injusticia' (ἀδικία).",
"ἀδυνατέω": "ἀ- (sin) + δυνατός (posible/capaz). Estar sin capacidad = ser imposible. 'Para Dios nada es imposible' (Mt 19:26).",
"ἀδύνατος": "ἀ- (sin) + δυνατός (posible). Sin poder = imposible. De aquí viene 'adinámico' (sin fuerza).",
"ἀθῷος": "ἀ- (sin) + θωή (castigo/pena). Sin castigo = inocente, libre de culpa. Pilato: 'Soy inocente de la sangre de este justo' (Mt 27:24).",
"ἀκάθαρτος": "ἀ- (sin) + καθαρτός (limpio, de καθαρός). Sin limpieza = impuro, inmundo. 'Espíritu inmundo' es πνεῦμα ἀκάθαρτον.",
"ἀκολουθέω": "ἀ- (copulativo: 'mismo') + κέλευθος (camino). Ir por el mismo camino = seguir. 'Sígueme' (ἀκολούθει μοι) — una de las palabras más frecuentes en los evangelios.",
"ἀκυρόω": "ἀ- (sin) + κῦρος (autoridad/validez). Quitar la autoridad = invalidar, anular. 'Invalidáis la palabra de Dios por vuestra tradición' (Mt 15:6).",
"ἀμέριμνος": "ἀ- (sin) + μέριμνα (preocupación/ansiedad). Sin preocupación = libre de ansiedad.",
"ἀμελέω": "ἀ- (sin) + μέλω (importar). No importar = descuidar, no hacer caso. 'Ellos, sin hacer caso, se fueron' (Mt 22:5).",
"ἀμφίβληστρον": "ἀμφί (alrededor) + βάλλω (lanzar). Lo que se lanza alrededor = red de pesca. Imagen: el pescador lanza la red en círculo alrededor de los peces.",
"ἀμφιέννυμι": "ἀμφί (alrededor) + ἕννυμι (vestir). Vestir alrededor = cubrir con ropa. 'Si Dios así viste la hierba del campo' (Mt 6:30).",
"ἀργός": "ἀ- (sin) + ἔργον (trabajo/obra). Sin trabajo = ocioso, inútil. De aquí viene 'energía' (ἐν + ἔργον = en obra). Lo contrario: sin obra = ἀργός.",
"ἀρχιερεύς": "ἀρχι- (principal/primero) + ἱερεύς (sacerdote). El sacerdote principal = sumo sacerdote. De ἀρχι- viene 'archi-' en español (arzobispo, arquitecto).",
"ἀσθένεια": "ἀ- (sin) + σθένος (fuerza). Sin fuerza = debilidad, enfermedad. De aquí: 'astenia' en medicina (falta de fuerza).",
"ἀσθενέω": "ἀ- (sin) + σθένος (fuerza). Estar sin fuerza = estar enfermo/débil.",
"ἀσθενής": "ἀ- (sin) + σθένος (fuerza). Sin fuerza = débil, enfermo.",
"ἀσύνετος": "ἀ- (sin) + συνετός (inteligente). Sin inteligencia = insensato. Nota: συνετός viene de συνίημι (entender).",
"ἀσφαλίζω": "ἀ- (sin) + σφάλλω (tropezar/caer). Hacer que no se pueda tropezar = asegurar, hacer firme. 'Asegurad el sepulcro' (Mt 27:65).",
"ἀφανίζω": "ἀ- (sin) + φαίνω (aparecer/mostrar). Hacer que no aparezca = desfigurar, hacer desaparecer. 'Desfiguran sus rostros' los hipócritas (Mt 6:16).",
"ἀχρεῖος": "ἀ- (sin) + χρεία (utilidad/necesidad). Sin utilidad = inútil. 'Somos siervos inútiles' (Lc 17:10).",
"ἀνοίγω": "ἀνά (arriba) + οἴγω (abrir). Abrir hacia arriba = abrir. 'Se le abrieron los cielos' (Mt 3:16).",
"ἀνθίστημι": "ἀντί (contra) + ἵστημι (poner de pie). Ponerse de pie contra = resistir. 'No resistáis al que es malo' (Mt 5:39).",
"ἀντίδικος": "ἀντί (contra) + δίκη (justicia/juicio). El que está contra ti en juicio = adversario. 'Ponte de acuerdo con tu adversario' (Mt 5:25).",
"ἀπαρνέομαι": "ἀπό (lejos) + ἀρνέομαι (negar). Negar alejándose = negar rotundamente. Pedro 'negó' a Jesús tres veces (Mt 26:34).",
"ἀποκαλύπτω": "ἀπό (lejos) + καλύπτω (cubrir). Quitar la cubierta = revelar. De aquí viene 'Apocalipsis' = revelación.",
"ἀποκεφαλίζω": "ἀπό (lejos/separar) + κεφαλή (cabeza). Separar la cabeza = decapitar. Juan el Bautista fue decapitado (Mt 14:10).",
"ἀπολύω": "ἀπό (lejos) + λύω (soltar). Soltar lejos = liberar, despedir, divorciar. Pilato 'soltó' a Barrabás (Mt 27:26).",
"ἀποστέλλω": "ἀπό (lejos) + στέλλω (enviar). Enviar lejos con una misión = enviar. De aquí viene ἀπόστολος (apóstol = el enviado).",
"ἐκβάλλω": "ἐκ (fuera) + βάλλω (lanzar). Lanzar fuera = expulsar. Jesús 'echaba fuera' demonios. Palabra muy frecuente en los evangelios.",
"ἐκπλήσσομαι": "ἐκ (fuera) + πλήσσω (golpear). Ser golpeado fuera de sí = quedar asombrado, atónito. 'Las multitudes se asombraban de su enseñanza' (Mt 7:28).",
"ἐκπορεύομαι": "ἐκ (fuera) + πορεύομαι (ir). Ir fuera = salir, proceder. 'Lo que sale de la boca, eso contamina' (Mt 15:11).",
"ἐκριζόω": "ἐκ (fuera) + ῥίζα (raíz). Sacar la raíz fuera = arrancar de raíz, desarraigar. 'Toda planta que no plantó mi Padre será desarraigada' (Mt 15:13).",
"ἐνδύω": "ἐν (dentro) + δύω (meter/vestir). Meter dentro de la ropa = vestir, revestir. Lo opuesto de ἐκδύω (desvestir).",
"ἐνεργέω": "ἐν (en) + ἔργον (obra). Obrar en = estar activo, producir efecto. De aquí viene 'energía' en español.",
"ἐνθυμέομαι": "ἐν (en) + θυμός (ánimo/corazón). Tener algo en el ánimo = reflexionar, pensar internamente.",
"ἐπιγινώσκω": "ἐπί (sobre) + γινώσκω (conocer). Conocer sobre/encima = reconocer, conocer plenamente. Un conocimiento más profundo que simple γινώσκω.",
"ἐπιθυμέω": "ἐπί (sobre) + θυμός (ánimo/deseo). Poner el ánimo sobre algo = desear ardientemente, codiciar. 'No codiciarás' usa esta palabra.",
"ἐπικαλέω": "ἐπί (sobre) + καλέω (llamar). Llamar sobre = invocar, dar sobrenombre. 'Invocar el nombre del Señor'.",
"ἐπιστρέφω": "ἐπί (de vuelta) + στρέφω (voltear). Voltear de vuelta = volverse, convertirse. 'Si no os volvéis como niños' (Mt 18:3).",
"ἐπιτίθημι": "ἐπί (sobre) + τίθημι (poner). Poner sobre = imponer. 'Imponían las manos' sobre los enfermos.",
"ἐπιτιμάω": "ἐπί (sobre) + τιμάω (valorar/honrar). Poner valor/peso sobre = reprender, censurar. Jesús 'reprendió' al viento y al mar (Mt 8:26).",
"ἐπιτρέπω": "ἐπί (sobre) + τρέπω (voltear/dirigir). Dirigir sobre alguien = confiar, permitir. 'Permíteme ir primero a enterrar a mi padre' (Mt 8:21).",
"ὁμολογέω": "ὁμός (mismo) + λέγω (decir). Decir lo mismo = estar de acuerdo, confesar. Confesar es 'decir lo mismo' que Dios dice sobre el pecado.",
"ὑποδείκνυμι": "ὑπό (debajo) + δείκνυμι (mostrar). Mostrar por debajo = dar indicios, advertir secretamente. '¿Quién os enseñó a huir de la ira?' (Mt 3:7).",
"ὑποζύγιον": "ὑπό (debajo) + ζυγόν (yugo). Lo que está debajo del yugo = animal de carga, burro.",
"ὑποκάτω": "ὑπό (debajo) + κάτω (abajo). Debajo + abajo = por debajo de. Doble énfasis en la posición inferior.",
"ὑπομένω": "ὑπό (debajo) + μένω (permanecer). Permanecer debajo de la carga = perseverar, soportar con paciencia.",
"ὑποπόδιον": "ὑπό (debajo) + πούς (pie). Lo que está debajo del pie = estrado, escabel. 'Hasta que ponga a tus enemigos por estrado de tus pies' (Mt 22:44).",
}

# Apply improved mnemonics
improved = 0
for card in cards:
    if card["lemma"] in BETTER_MNEMONICS:
        card["mnemonic_es"] = BETTER_MNEMONICS[card["lemma"]]
        improved += 1

# For remaining cards with short mnemonics, auto-improve using enriched data
for card in cards:
    if len(card["mnemonic_es"]) < 40 and card["lemma"] not in BETTER_MNEMONICS:
        parts = " + ".join(f"{c['greek']} ({c['meaning_es']})" for c in card["components"])
        base = f"{parts} = {card['meaning_es']}."
        if "root_note_es" in card:
            base += f" {card['root_note_es']}"
        elif "suffix_explanation_es" in card:
            base += f" El sufijo {card.get('suffix','')} {card['suffix_type_es']}."
        card["mnemonic_es"] = base
        improved += 1

with open("data/matthew/compounds_enriched.json", "w") as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print(f"Improved {improved} mnemonics")
print(f"Total cards: {len(cards)}")

# Check remaining short ones
short = [(c["lemma"], len(c["mnemonic_es"]), c["mnemonic_es"][:60]) for c in cards if len(c["mnemonic_es"]) < 40]
if short:
    print(f"\nStill short ({len(short)}):")
    for s in short:
        print(f"  {s[0]}: ({s[1]} chars) {s[2]}")
