"""Lesson data 26-30: More past tense, Commands, Prayer, God/Lord, Level 1 Review"""
from src.tts import M, F

L26 = {
    "num":26,"intro_es":"Μάθημα εἴκοσι ἕξ. Lección veintiséis. Hoy practicarás más narración en pasado con aoristos regulares. Escucha.",
    "dialogue":[(F,"Τί ἐγένετο χθές;"),(M,"Ἀπῆλθον εἰς τὴν ἀγοράν, ἠγόρασα ἄρτον, καὶ ἔδωκα τοῖς πτωχοῖς.")],
    "context_es":"La mujer pregunta qué pasó ayer. El hombre fue al mercado, compró pan, y lo dio a los pobres.",
    "vocab":[
        {"gr":"ἀπῆλθον","es":"me fui (pasado de ἀπέρχομαι)","note_es":"ἀπῆλθον es el pasado de ἀπέρχομαι, irse. ἀπῆλθεν es se fue. Escucha."},
        {"gr":"ἔλαβον","es":"tomé (pasado de λαμβάνω)","note_es":"ἔλαβον es el pasado de λαμβάνω, tomar. ἔλαβεν es tomó. Escucha."},
        {"gr":"ἔδωκεν","es":"dio (pasado de δίδωμι)","note_es":"ἔδωκεν es el pasado de δίδωμι, dar. ἔδωκα es di. Escucha."},
        {"gr":"ἔγραψεν","es":"escribió (pasado de γράφω)","note_es":"ἔγραψεν es el pasado de γράφω, escribir. ἔγραψα es escribí. Escucha."},
        {"gr":"πτωχός","es":"pobre","note_es":"πτωχός significa pobre. Aparece treinta y cuatro veces. οἱ πτωχοί, los pobres. Escucha."},
        {"gr":"φωνή","es":"voz","note_es":"φωνή significa voz. Aparece ciento treinta y nueve veces. ἡ φωνή, la voz. Escucha."},
    ],
    "phrases":[
        {"gr":"ἀπῆλθον εἰς τὴν ἀγοράν","es":"fui al mercado","prompt_es":"Di fui al mercado."},
        {"gr":"ἔλαβεν τὸν ἄρτον","es":"tomó el pan","prompt_es":"Di tomó el pan."},
        {"gr":"ἔδωκεν αὐτοῖς","es":"les dio","prompt_es":"Di les dio."},
        {"gr":"ἔγραψεν ἐπιστολήν","es":"escribió una carta","prompt_es":"Di escribió una carta. ἐπιστολή es carta."},
        {"gr":"ἤκουσα φωνήν","es":"oí una voz","prompt_es":"Di oí una voz."},
        {"gr":"ἔδωκα τοῖς πτωχοῖς","es":"di a los pobres","prompt_es":"Di di a los pobres."},
    ],
    "recon":[
        {"other_gr":"Τί ἐποίησας χθές;","other_voice":F,"prompt_es":"Te preguntan qué hiciste ayer. Di que fuiste al mercado.","answer_gr":"Ἀπῆλθον εἰς τὴν ἀγοράν.","answer_voice":M},
        {"prompt_es":"Di que compraste pan.","answer_gr":"Ἠγόρασα ἄρτον.","answer_voice":M},
        {"prompt_es":"Di que lo diste a los pobres.","answer_gr":"Ἔδωκα τοῖς πτωχοῖς.","answer_voice":M},
    ],
    "verse":{"gr":"Ἔλαβεν ἄρτον καὶ εὐχαριστήσας ἔκλασεν καὶ ἔδωκεν αὐτοῖς.","voice":M,"ref_es":"En Lucas veintidós diecinueve, en la última cena:","explain_es":"Tomó pan, dio gracias, lo partió y les dio. ἔλαβεν tomó. εὐχαριστήσας habiendo dado gracias. ἔκλασεν partió. ἔδωκεν dio."},
    "closing_es":"Practicaste más pasado: ἀπῆλθον fui, ἔλαβον tomé, ἔδωκεν dio, ἔγραψεν escribió. En la siguiente lección aprenderás mandamientos. Εἰρήνη σοι.",
}

L27 = {
    "num":27,"intro_es":"Μάθημα εἴκοσι ἑπτά. Lección veintisiete. Hoy aprenderás mandamientos: haz esto, no hagas aquello. Escucha.",
    "dialogue":[(M,"Ἀγαπᾶτε τοὺς ἐχθροὺς ὑμῶν."),(F,"Μὴ θησαυρίζετε ὑμῖν θησαυροὺς ἐπὶ τῆς γῆς."),(M,"Γέγραπται.")],
    "context_es":"El hombre dice amen a sus enemigos. La mujer dice no acumulen tesoros en la tierra. El hombre dice está escrito.",
    "vocab":[
        {"gr":"ἐντολή","es":"mandamiento","note_es":"ἐντολή significa mandamiento. Aparece sesenta y siete veces. Viene de ἐν y τέλλω, cumplir. Escucha."},
        {"gr":"νόμος","es":"ley","note_es":"νόμος significa ley. Aparece ciento noventa y cuatro veces. ὁ νόμος, la ley. Escucha."},
        {"gr":"γράφω","es":"escribir","note_es":"γράφω significa escribir. Aparece ciento noventa y una veces. Escucha."},
        {"gr":"γραφή","es":"escritura","note_es":"γραφή significa escritura. ἡ γραφή, la escritura. αἱ γραφαί, las escrituras. Escucha."},
        {"gr":"γέγραπται","es":"está escrito","note_es":"γέγραπται significa está escrito. Es el perfecto pasivo de γράφω. Aparece unas setenta veces. Jesús lo usa para citar las escrituras. Escucha."},
        {"gr":"ἐχθρός","es":"enemigo","note_es":"ἐχθρός significa enemigo. Aparece treinta y dos veces. Escucha."},
    ],
    "phrases":[
        {"gr":"ἀγαπᾶτε τοὺς ἐχθροὺς ὑμῶν","es":"amen a sus enemigos","prompt_es":"Di amen a sus enemigos."},
        {"gr":"μὴ κρίνετε","es":"no juzguen","prompt_es":"Di no juzguen. κρίνετε es juzguen."},
        {"gr":"γέγραπται","es":"está escrito","prompt_es":"Di está escrito."},
        {"gr":"ἡ ἐντολὴ τοῦ κυρίου","es":"el mandamiento del Señor","prompt_es":"Di el mandamiento del Señor."},
        {"gr":"ὁ νόμος καὶ οἱ προφῆται","es":"la ley y los profetas","prompt_es":"Di la ley y los profetas. προφῆται es profetas."},
        {"gr":"αἱ γραφαί","es":"las escrituras","prompt_es":"Di las escrituras."},
    ],
    "recon":[
        {"prompt_es":"Di amen a sus enemigos.","answer_gr":"Ἀγαπᾶτε τοὺς ἐχθροὺς ὑμῶν.","answer_voice":M},
        {"prompt_es":"Di no juzguen.","answer_gr":"Μὴ κρίνετε.","answer_voice":M},
        {"prompt_es":"Di está escrito.","answer_gr":"Γέγραπται.","answer_voice":M},
        {"prompt_es":"Di la ley y los profetas.","answer_gr":"Ὁ νόμος καὶ οἱ προφῆται.","answer_voice":M},
    ],
    "verse":{"gr":"Γέγραπται, Οὐκ ἐπ᾽ ἄρτῳ μόνῳ ζήσεται ὁ ἄνθρωπος.","voice":M,"ref_es":"En Mateo cuatro cuatro, Jesús respondió al diablo:","explain_es":"Está escrito: no solo de pan vivirá el hombre. γέγραπται, está escrito. ἄρτῳ, pan en dativo. μόνῳ, solo. ζήσεται, vivirá. ἄνθρωπος, hombre."},
    "closing_es":"Aprendiste mandamientos: ἐντολή mandamiento, νόμος ley, γράφω escribir, γραφή escritura, γέγραπται está escrito. Εἰρήνη σοι.",
}

L28 = {
    "num":28,"intro_es":"Μάθημα εἴκοσι ὀκτώ. Lección veintiocho. Hoy aprenderás la oración. Escucharás y aprenderás el Padre Nuestro. Escucha.",
    "dialogue":[(M,"Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς, ἁγιασθήτω τὸ ὄνομά σου, ἐλθέτω ἡ βασιλεία σου.")],
    "context_es":"Escuchaste el inicio del Padre Nuestro. Padre nuestro que estás en los cielos, santificado sea tu nombre, venga tu reino.",
    "vocab":[
        {"gr":"προσεύχομαι","es":"orar","note_es":"προσεύχομαι significa orar. Es deponente. Viene de πρός, hacia, y εὔχομαι, hacer voto. Aparece ochenta y cinco veces. Escucha."},
        {"gr":"προσευχή","es":"oración","note_es":"προσευχή significa oración. Aparece treinta y seis veces. Escucha."},
        {"gr":"οὐρανός","es":"cielo","note_es":"οὐρανός significa cielo. Aparece doscientas setenta y tres veces. ὁ οὐρανός, el cielo. Escucha."},
        {"gr":"γῆ","es":"tierra","note_es":"γῆ significa tierra. Aparece doscientas cincuenta veces. ἡ γῆ, la tierra. Escucha."},
        {"gr":"βασιλεία","es":"reino","note_es":"βασιλεία significa reino. Aparece ciento sesenta y dos veces. ἡ βασιλεία τοῦ θεοῦ, el reino de Dios. Escucha."},
        {"gr":"ἅγιος","es":"santo","note_es":"ἅγιος significa santo. Aparece doscientas treinta y tres veces. τὸ πνεῦμα τὸ ἅγιον, el Espíritu Santo. Escucha."},
    ],
    "phrases":[
        {"gr":"Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς","es":"Padre nuestro que estás en los cielos","prompt_es":"Di Padre nuestro que estás en los cielos."},
        {"gr":"ἁγιασθήτω τὸ ὄνομά σου","es":"santificado sea tu nombre","prompt_es":"Di santificado sea tu nombre. ἁγιασθήτω es sea santificado."},
        {"gr":"ἐλθέτω ἡ βασιλεία σου","es":"venga tu reino","prompt_es":"Di venga tu reino. ἐλθέτω es venga, imperativo de ἔρχομαι."},
        {"gr":"ἡ βασιλεία τοῦ θεοῦ","es":"el reino de Dios","prompt_es":"Di el reino de Dios."},
        {"gr":"ἐν οὐρανῷ καὶ ἐπὶ γῆς","es":"en el cielo y en la tierra","prompt_es":"Di en el cielo y en la tierra."},
        {"gr":"τὸ πνεῦμα τὸ ἅγιον","es":"el Espíritu Santo","prompt_es":"Di el Espíritu Santo."},
    ],
    "recon":[
        {"prompt_es":"Comienza el Padre Nuestro.","answer_gr":"Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς.","answer_voice":M},
        {"prompt_es":"Continúa: santificado sea tu nombre.","answer_gr":"Ἁγιασθήτω τὸ ὄνομά σου.","answer_voice":M},
        {"prompt_es":"Continúa: venga tu reino.","answer_gr":"Ἐλθέτω ἡ βασιλεία σου.","answer_voice":M},
        {"prompt_es":"Di el reino de Dios.","answer_gr":"Ἡ βασιλεία τοῦ θεοῦ.","answer_voice":M},
    ],
    "verse":{"gr":"Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς, ἁγιασθήτω τὸ ὄνομά σου, ἐλθέτω ἡ βασιλεία σου, γενηθήτω τὸ θέλημά σου, ὡς ἐν οὐρανῷ καὶ ἐπὶ γῆς.","voice":M,"ref_es":"Mateo seis nueve al diez, el Padre Nuestro:","explain_es":"Padre nuestro que estás en los cielos, santificado sea tu nombre, venga tu reino, hágase tu voluntad, como en el cielo también en la tierra. θέλημα significa voluntad."},
    "closing_es":"Aprendiste la oración: προσεύχομαι orar, οὐρανός cielo, γῆ tierra, βασιλεία reino, ἅγιος santo. Y el inicio del Padre Nuestro. Εἰρήνη σοι.",
}

L29 = {
    "num":29,"intro_es":"Μάθημα εἴκοσι ἐννέα. Lección veintinueve. Hoy aprenderás vocabulario teológico central: Dios, Señor, espíritu, vida. Escucha.",
    "dialogue":[(M,"Κύριος ὁ θεὸς ἡμῶν κύριος εἷς ἐστιν."),(F,"Ἀγαπήσεις κύριον τὸν θεόν σου ἐξ ὅλης τῆς καρδίας σου.")],
    "context_es":"El hombre recita el Shemá: el Señor nuestro Dios, el Señor es uno. La mujer completa: amarás al Señor tu Dios con todo tu corazón.",
    "vocab":[
        {"gr":"θεός","es":"Dios","note_es":"θεός significa Dios. Aparece mil trescientas siete veces. Es la cuarta palabra más frecuente con contenido del Nuevo Testamento. Escucha."},
        {"gr":"κύριος","es":"Señor","note_es":"κύριος significa Señor o amo. Aparece setecientas trece veces. Escucha."},
        {"gr":"πνεῦμα","es":"espíritu, viento","note_es":"πνεῦμα significa espíritu o viento. Aparece trescientas setenta y nueve veces. τὸ πνεῦμα, el espíritu. Escucha."},
        {"gr":"ψυχή","es":"alma, vida","note_es":"ψυχή significa alma o vida. En koiné es el aliento vital, la vida misma. No es el concepto psicológico moderno. Aparece ciento tres veces. Escucha."},
        {"gr":"ζωή","es":"vida","note_es":"ζωή significa vida. Es diferente de ψυχή. ζωή es la vida en sentido pleno, especialmente la vida eterna. Aparece ciento treinta y cinco veces. Escucha."},
        {"gr":"αἰώνιος","es":"eterno","note_es":"αἰώνιος significa eterno. ζωὴ αἰώνιος, vida eterna. Aparece setenta y una veces. Escucha."},
    ],
    "phrases":[
        {"gr":"ὁ θεός","es":"Dios","prompt_es":"Di Dios, con artículo."},
        {"gr":"ὁ κύριος","es":"el Señor","prompt_es":"Di el Señor."},
        {"gr":"τὸ πνεῦμα τὸ ἅγιον","es":"el Espíritu Santo","prompt_es":"Di el Espíritu Santo."},
        {"gr":"ζωὴ αἰώνιος","es":"vida eterna","prompt_es":"Di vida eterna."},
        {"gr":"κύριος εἷς ἐστιν","es":"el Señor es uno","prompt_es":"Di el Señor es uno."},
        {"gr":"ἐξ ὅλης τῆς καρδίας","es":"con todo el corazón","prompt_es":"Di con todo el corazón. ὅλης significa todo, entero."},
        {"gr":"ἡ ψυχή μου","es":"mi alma","prompt_es":"Di mi alma."},
    ],
    "recon":[
        {"prompt_es":"Recita el Shemá: el Señor nuestro Dios, el Señor es uno.","answer_gr":"Κύριος ὁ θεὸς ἡμῶν κύριος εἷς ἐστιν.","answer_voice":M},
        {"prompt_es":"Di vida eterna.","answer_gr":"Ζωὴ αἰώνιος.","answer_voice":M},
        {"prompt_es":"Di el Espíritu Santo.","answer_gr":"Τὸ πνεῦμα τὸ ἅγιον.","answer_voice":M},
        {"prompt_es":"Di amarás al Señor tu Dios con todo tu corazón.","answer_gr":"Ἀγαπήσεις κύριον τὸν θεόν σου ἐξ ὅλης τῆς καρδίας σου.","answer_voice":M},
    ],
    "verse":{"gr":"Κύριος ὁ θεὸς ἡμῶν κύριος εἷς ἐστιν.","voice":M,"ref_es":"En Marcos doce veintinueve, Jesús cita el Shemá:","explain_es":"El Señor nuestro Dios, el Señor es uno. Reconoces cada palabra. κύριος, Señor. θεός, Dios. ἡμῶν, nuestro. εἷς, uno. ἐστιν, es."},
    "closing_es":"Aprendiste vocabulario teológico: θεός Dios, κύριος Señor, πνεῦμα espíritu, ψυχή alma, ζωή vida, αἰώνιος eterno. Εἰρήνη σοι.",
}

L30 = {
    "num":30,"intro_es":"Μάθημα τριάκοντα. Lección treinta. Última lección del primer nivel. Hoy escucharás la parábola del sembrador y repasarás todo. Escucha.",
    "dialogue":[(M,"Ἰδοὺ ἐξῆλθεν ὁ σπείρων τοῦ σπείρειν."),(M,"Καὶ ἐν τῷ σπείρειν αὐτόν, ἃ μὲν ἔπεσεν παρὰ τὴν ὁδόν."),(M,"Ἄλλα δὲ ἔπεσεν ἐπὶ τὴν γῆν τὴν καλὴν καὶ ἐδίδου καρπόν.")],
    "context_es":"Escuchaste parte de la parábola del sembrador. He aquí salió el sembrador a sembrar. Unas semillas cayeron junto al camino. Otras cayeron en buena tierra y dieron fruto.",
    "vocab":[
        {"gr":"σπείρω","es":"sembrar","note_es":"σπείρω significa sembrar. Aparece cincuenta y dos veces. ὁ σπείρων es el sembrador, literalmente el que siembra. Escucha."},
        {"gr":"σπέρμα","es":"semilla","note_es":"σπέρμα significa semilla. Aparece cuarenta y tres veces. Escucha."},
        {"gr":"καρπός","es":"fruto","note_es":"καρπός significa fruto. Aparece sesenta y seis veces. Escucha."},
    ],
    "phrases":[
        {"gr":"ὁ σπείρων","es":"el sembrador","prompt_es":"Di el sembrador. Es un participio: el que siembra."},
        {"gr":"ἐπὶ τὴν γῆν τὴν καλήν","es":"en la buena tierra","prompt_es":"Di en la buena tierra."},
        {"gr":"ἐδίδου καρπόν","es":"daba fruto","prompt_es":"Di daba fruto. ἐδίδου es daba, imperfecto de δίδωμι."},
        {"gr":"ἔπεσεν παρὰ τὴν ὁδόν","es":"cayó junto al camino","prompt_es":"Di cayó junto al camino. ἔπεσεν es cayó."},
    ],
    "recon":[
        {"prompt_es":"Comienza la parábola. Di he aquí salió el sembrador a sembrar.","answer_gr":"Ἰδοὺ ἐξῆλθεν ὁ σπείρων τοῦ σπείρειν.","answer_voice":M},
        {"prompt_es":"Di cayó en buena tierra y daba fruto.","answer_gr":"Ἔπεσεν ἐπὶ τὴν γῆν τὴν καλὴν καὶ ἐδίδου καρπόν.","answer_voice":M},
        {"prompt_es":"Di el reino de Dios.","answer_gr":"Ἡ βασιλεία τοῦ θεοῦ.","answer_voice":M},
        {"prompt_es":"Di está escrito.","answer_gr":"Γέγραπται.","answer_voice":M},
        {"prompt_es":"Di Padre nuestro que estás en los cielos.","answer_gr":"Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς.","answer_voice":M},
    ],
    "verse":{"gr":"Ὁ ἔχων ὦτα ἀκουέτω.","voice":M,"ref_es":"En Mateo trece nueve, Jesús termina la parábola diciendo:","explain_es":"El que tiene oídos, oiga. ὁ ἔχων, el que tiene. ὦτα, oídos. ἀκουέτω, que oiga. Reconoces ἔχω, tener, y ἀκούω, oír."},
    "closing_es":"Felicidades. Has completado el primer nivel, treinta lecciones. Conoces más de doscientas palabras que cubren casi el setenta y cinco por ciento del texto del Nuevo Testamento. Puedes saludar, presentarte, comprar, narrar en pasado, dar mandamientos, orar, y entender vocabulario teológico básico. En el segundo nivel aprenderás a narrar historias completas, entender parábolas, y leer textos bíblicos. Εἰρήνη σοι.",
}
