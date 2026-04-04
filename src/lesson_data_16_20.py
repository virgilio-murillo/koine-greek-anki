"""Lesson data 16-20: Hospitality, Time, Seeing, Doing, Good/Bad"""
M = "el-GR-Chirp3-HD-Charon"
F = "el-GR-Chirp3-HD-Kore"

L16 = {
    "num":16,"intro_es":"Μάθημα δεκαέξ. Lección dieciséis. A partir de ahora el griego suena a velocidad normal. Hoy aprenderás sobre hospitalidad: entrar, sentarse, quedarse. Escucha.",
    "dialogue":[(F,"Εἴσελθε εἰς τὴν οἰκίαν."),(M,"Εὐχαριστῶ."),(F,"Κάθισον. Θέλεις ἄρτον καὶ οἶνον;"),(M,"ναί. Μένω μετὰ σοῦ σήμερον;")],
    "context_es":"La mujer invita al hombre a entrar a la casa. Le ofrece pan y vino. Él pregunta si puede quedarse hoy.",
    "vocab":[
        {"gr":"οἰκία","es":"casa, hogar","note_es":"οἰκία significa casa o hogar. Es similar a οἶκος pero más personal. Aparece noventa y tres veces. Escucha."},
        {"gr":"θύρα","es":"puerta","note_es":"θύρα significa puerta. Nunca uses la palabra moderna πόρτα. En koiné siempre es θύρα. Aparece treinta y nueve veces. Escucha."},
        {"gr":"καθίζω","es":"sentarse","note_es":"καθίζω significa sentarse. La orden es κάθισον, siéntate. Escucha."},
        {"gr":"μένω","es":"permanecer, quedarse","note_es":"μένω significa permanecer o quedarse. Aparece ciento dieciocho veces. Jesús dijo μείνατε ἐν ἐμοί, permanezcan en mí. Escucha."},
        {"gr":"εἰσέρχομαι","es":"entrar","note_es":"εἰσέρχομαι significa entrar. Viene de εἰς, hacia adentro, y ἔρχομαι, ir. La orden es εἴσελθε, entra. Escucha."},
        {"gr":"ἐξέρχομαι","es":"salir","note_es":"ἐξέρχομαι significa salir. Viene de ἐκ, fuera, y ἔρχομαι. Escucha."},
    ],
    "phrases":[
        {"gr":"εἴσελθε εἰς τὴν οἰκίαν","es":"entra a la casa","prompt_es":"Di entra a la casa."},
        {"gr":"κάθισον","es":"siéntate","prompt_es":"Di siéntate."},
        {"gr":"μεῖνον μεθ᾽ ἡμῶν","es":"quédate con nosotros","prompt_es":"Di quédate con nosotros. Como los discípulos de Emaús le dijeron a Jesús."},
        {"gr":"ἐξέρχομαι ἐκ τοῦ οἴκου","es":"salgo de la casa","prompt_es":"Di salgo de la casa."},
        {"gr":"κλεῖσον τὴν θύραν","es":"cierra la puerta","prompt_es":"Di cierra la puerta. κλεῖσον es la orden de cerrar."},
        {"gr":"εἰσέρχομαι εἰς τὸ ἱερόν","es":"entro al templo","prompt_es":"Di entro al templo."},
    ],
    "recon":[
        {"other_gr":"Εἴσελθε εἰς τὴν οἰκίαν.","other_voice":F,"prompt_es":"Te invitan a entrar. Da gracias.","answer_gr":"Εὐχαριστῶ.","answer_voice":M},
        {"other_gr":"Κάθισον. Θέλεις ἄρτον;","other_voice":F,"prompt_es":"Te ofrecen pan. Di que sí.","answer_gr":"ναί, θέλω.","answer_voice":M},
        {"prompt_es":"Pregunta si puedes quedarte hoy.","answer_gr":"Δύναμαι μεῖναι ὧδε σήμερον;","answer_voice":M},
        {"other_gr":"ναί, μεῖνον μεθ᾽ ἡμῶν.","other_voice":F,"prompt_es":"Di paz a ti.","answer_gr":"Εἰρήνη σοι.","answer_voice":M},
    ],
    "verse":{"gr":"Μεῖνον μεθ᾽ ἡμῶν, ὅτι πρὸς ἑσπέραν ἐστίν.","voice":M,"ref_es":"En Lucas veinticuatro veintinueve, los discípulos de Emaús le dijeron a Jesús:","explain_es":"Quédate con nosotros, porque atardece. Reconoces μεῖνον, quédate. μεθ᾽ ἡμῶν, con nosotros. ὅτι, porque. ἑσπέραν significa tarde."},
    "closing_es":"Aprendiste sobre hospitalidad: εἰσέρχομαι entrar, ἐξέρχομαι salir, καθίζω sentarse, μένω quedarse, οἰκία casa, θύρα puerta. En la siguiente lección aprenderás el tiempo. Εἰρήνη σοι.",
}

L17 = {
    "num":17,"intro_es":"Μάθημα δεκαεπτά. Lección diecisiete. Hoy aprenderás palabras de tiempo: hoy, mañana, día, noche. Escucha.",
    "dialogue":[(M,"Τί ποιεῖς σήμερον;"),(F,"Πορεύομαι εἰς τὴν συναγωγήν. Σάββατόν ἐστιν."),(M,"Καὶ αὔριον;"),(F,"Αὔριον ἐργάζομαι.")],
    "context_es":"El hombre pregunta qué hace hoy. Ella va a la sinagoga porque es sábado. Mañana trabaja.",
    "vocab":[
        {"gr":"σήμερον","es":"hoy","note_es":"σήμερον significa hoy. Aparece cuarenta y una veces. Escucha."},
        {"gr":"αὔριον","es":"mañana","note_es":"αὔριον significa mañana. Escucha."},
        {"gr":"ἡμέρα","es":"día","note_es":"ἡμέρα significa día. Aparece trescientas ochenta y nueve veces. ἡ ἡμέρα, el día. Escucha."},
        {"gr":"νύξ","es":"noche","note_es":"νύξ significa noche. ἡ νύξ, la noche. Escucha."},
        {"gr":"ὥρα","es":"hora","note_es":"ὥρα significa hora. Aparece ciento seis veces. ἡ ὥρα, la hora. Escucha."},
        {"gr":"σάββατον","es":"sábado","note_es":"σάββατον significa sábado. Viene del hebreo shabbat. Aparece sesenta y ocho veces. Escucha."},
        {"gr":"καιρός","es":"tiempo oportuno, momento","note_es":"καιρός significa tiempo oportuno o momento. No es el tiempo cronológico sino el momento adecuado. Aparece ochenta y cinco veces. Escucha."},
    ],
    "phrases":[
        {"gr":"σήμερον","es":"hoy","prompt_es":"Di hoy."},
        {"gr":"αὔριον","es":"mañana","prompt_es":"Di mañana."},
        {"gr":"ἐν τῇ ἡμέρᾳ","es":"en el día, durante el día","prompt_es":"Di en el día."},
        {"gr":"ἐν τῇ νυκτί","es":"en la noche","prompt_es":"Di en la noche."},
        {"gr":"τί ποιεῖς σήμερον;","es":"¿qué haces hoy?","prompt_es":"Pregunta qué haces hoy. ποιεῖς es haces."},
        {"gr":"σάββατόν ἐστιν","es":"es sábado","prompt_es":"Di es sábado."},
        {"gr":"ἦλθεν ἡ ὥρα","es":"llegó la hora","prompt_es":"Di llegó la hora. ἦλθεν es llegó, pasado de ἔρχομαι."},
    ],
    "recon":[
        {"other_gr":"Τί ποιεῖς σήμερον;","other_voice":M,"prompt_es":"Te preguntan qué haces hoy. Di que vas a la sinagoga.","answer_gr":"Πορεύομαι εἰς τὴν συναγωγήν.","answer_voice":F},
        {"other_gr":"Καὶ αὔριον;","other_voice":M,"prompt_es":"Te preguntan y mañana. Di que mañana vas al mercado.","answer_gr":"Αὔριον πορεύομαι εἰς τὴν ἀγοράν.","answer_voice":F},
        {"prompt_es":"Pregúntale qué hace él hoy.","answer_gr":"Καὶ σύ; Τί ποιεῖς σήμερον;","answer_voice":F},
    ],
    "verse":{"gr":"Μὴ οὖν μεριμνήσητε εἰς τὴν αὔριον.","voice":M,"ref_es":"En Mateo seis treinta y cuatro, Jesús dice:","explain_es":"No se preocupen por el mañana. Reconoces μή, no. οὖν, entonces. αὔριον, mañana. μεριμνήσητε significa preocúpense."},
    "closing_es":"Aprendiste el tiempo: σήμερον hoy, αὔριον mañana, ἡμέρα día, νύξ noche, ὥρα hora, σάββατον sábado, καιρός momento oportuno. En la siguiente lección aprenderás a ver y mirar. Εἰρήνη σοι.",
}

L18 = {
    "num":18,"intro_es":"Μάθημα δεκαοκτώ. Lección dieciocho. Hoy aprenderás a ver, mirar, y hablar de luz y oscuridad. Escucha.",
    "dialogue":[(M,"Βλέπεις τὸ φῶς ἐκεῖνο;"),(F,"ναί, βλέπω. Τί ἐστιν;"),(M,"Οὐ γινώσκω. Ἀλλὰ ὁ τυφλὸς οὐ βλέπει οὐδέν.")],
    "context_es":"El hombre pregunta si ella ve aquella luz. Ella la ve. Él no sabe qué es. Pero el ciego no ve nada.",
    "vocab":[
        {"gr":"ὁράω","es":"ver","note_es":"ὁράω significa ver. Aparece cuatrocientas setenta y seis veces. Es uno de los verbos más frecuentes. Escucha."},
        {"gr":"βλέπω","es":"mirar, ver","note_es":"βλέπω significa mirar o ver. Es más concreto que ὁράω. βλέπεις, miras. Escucha."},
        {"gr":"ὀφθαλμός","es":"ojo","note_es":"ὀφθαλμός significa ojo. Aparece cien veces. Escucha."},
        {"gr":"τυφλός","es":"ciego","note_es":"τυφλός significa ciego. Aparece cincuenta veces. Escucha."},
        {"gr":"φῶς","es":"luz","note_es":"φῶς significa luz. Aparece setenta y tres veces. τὸ φῶς, la luz. Jesús dijo ἐγώ εἰμι τὸ φῶς τοῦ κόσμου. Escucha."},
        {"gr":"σκοτία","es":"oscuridad","note_es":"σκοτία significa oscuridad. ἡ σκοτία, la oscuridad. Escucha."},
    ],
    "phrases":[
        {"gr":"βλέπεις;","es":"¿ves?","prompt_es":"Pregunta ves."},
        {"gr":"βλέπω τὸ φῶς","es":"veo la luz","prompt_es":"Di veo la luz."},
        {"gr":"ὁ τυφλὸς οὐ βλέπει","es":"el ciego no ve","prompt_es":"Di el ciego no ve."},
        {"gr":"ἐγώ εἰμι τὸ φῶς τοῦ κόσμου","es":"yo soy la luz del mundo","prompt_es":"Di yo soy la luz del mundo. κόσμου significa del mundo."},
        {"gr":"ἐν τῇ σκοτίᾳ","es":"en la oscuridad","prompt_es":"Di en la oscuridad."},
        {"gr":"τυφλὸς ἦν, νῦν δὲ βλέπω","es":"era ciego, pero ahora veo","prompt_es":"Di era ciego, pero ahora veo. ἦν significa era."},
    ],
    "recon":[
        {"other_gr":"Βλέπεις τὸ φῶς;","other_voice":M,"prompt_es":"Te preguntan si ves la luz. Di que sí.","answer_gr":"ναί, βλέπω.","answer_voice":F},
        {"prompt_es":"Di yo soy la luz del mundo, como Jesús.","answer_gr":"Ἐγώ εἰμι τὸ φῶς τοῦ κόσμου.","answer_voice":F},
        {"prompt_es":"Di era ciego, pero ahora veo.","answer_gr":"Τυφλὸς ἦν, νῦν δὲ βλέπω.","answer_voice":F},
    ],
    "verse":{"gr":"Ἐγώ εἰμι τὸ φῶς τοῦ κόσμου.","voice":M,"ref_es":"En Juan nueve cinco, Jesús dice:","explain_es":"Yo soy la luz del mundo. Reconoces cada palabra. ἐγώ εἰμι, yo soy. τὸ φῶς, la luz. τοῦ κόσμου, del mundo."},
    "closing_es":"Aprendiste a ver y mirar: ὁράω ver, βλέπω mirar, ὀφθαλμός ojo, τυφλός ciego, φῶς luz, σκοτία oscuridad. En la siguiente lección aprenderás a hacer y trabajar. Εἰρήνη σοι.",
}

L19 = {
    "num":19,"intro_es":"Μάθημα δεκαεννέα. Lección diecinueve. Hoy aprenderás a decir hacer, trabajar, y oficios del siglo primero. Escucha.",
    "dialogue":[(F,"Τί ποιεῖς;"),(M,"Ἁλιεύς εἰμι. Ἐργάζομαι ἐν τῇ θαλάσσῃ."),(F,"Ὁ πατήρ μου τέκτων ἐστίν.")],
    "context_es":"La mujer pregunta qué hace. Él es pescador, trabaja en el mar. El padre de ella es carpintero.",
    "vocab":[
        {"gr":"ποιέω","es":"hacer","note_es":"ποιέω significa hacer. Aparece quinientas sesenta y ocho veces. ποιεῖς es haces. ποιεῖ es hace. Escucha."},
        {"gr":"ἐργάζομαι","es":"trabajar","note_es":"ἐργάζομαι significa trabajar. Es deponente. Viene de ἔργον, obra. Escucha."},
        {"gr":"ἔργον","es":"obra, trabajo","note_es":"ἔργον significa obra o trabajo. Aparece ciento sesenta y nueve veces. Escucha."},
        {"gr":"ἁλιεύς","es":"pescador","note_es":"ἁλιεύς significa pescador. Los primeros discípulos eran pescadores. Escucha."},
        {"gr":"τέκτων","es":"carpintero","note_es":"τέκτων significa carpintero. Jesús era llamado ὁ τέκτων, el carpintero, en Marcos seis tres. Escucha."},
        {"gr":"πλοῖον","es":"barca","note_es":"πλοῖον significa barca. Aparece sesenta y siete veces. Los discípulos pescaban desde πλοῖα, barcas. Escucha."},
    ],
    "phrases":[
        {"gr":"τί ποιεῖς;","es":"¿qué haces?","prompt_es":"Pregunta qué haces."},
        {"gr":"ἁλιεύς εἰμι","es":"soy pescador","prompt_es":"Di soy pescador."},
        {"gr":"ἐργάζομαι ἐν τῇ θαλάσσῃ","es":"trabajo en el mar","prompt_es":"Di trabajo en el mar."},
        {"gr":"ὁ πατήρ μου τέκτων ἐστίν","es":"mi padre es carpintero","prompt_es":"Di mi padre es carpintero."},
        {"gr":"τὰ ἔργα αὐτοῦ","es":"sus obras","prompt_es":"Di sus obras. τά es el artículo neutro plural."},
        {"gr":"ἐν τῷ πλοίῳ","es":"en la barca","prompt_es":"Di en la barca."},
        {"gr":"τί ποιοῦμεν;","es":"¿qué hacemos?","prompt_es":"Pregunta qué hacemos. ποιοῦμεν es la forma para nosotros."},
    ],
    "recon":[
        {"other_gr":"Τί ποιεῖς;","other_voice":F,"prompt_es":"Te preguntan qué haces. Di que eres pescador.","answer_gr":"Ἁλιεύς εἰμι.","answer_voice":M},
        {"other_gr":"Ποῦ ἐργάζῃ;","other_voice":F,"prompt_es":"Te preguntan dónde trabajas. Di en el mar.","answer_gr":"Ἐν τῇ θαλάσσῃ.","answer_voice":M},
        {"prompt_es":"Pregúntale qué hace su padre.","answer_gr":"Τί ποιεῖ ὁ πατήρ σου;","answer_voice":M},
        {"other_gr":"Τέκτων ἐστίν.","other_voice":F,"prompt_es":"Di que tu padre también es carpintero.","answer_gr":"Καὶ ὁ πατήρ μου τέκτων ἐστίν.","answer_voice":M},
    ],
    "verse":{"gr":"Ποιήσω ὑμᾶς ἁλιεῖς ἀνθρώπων.","voice":M,"ref_es":"En Mateo cuatro diecinueve, Jesús dijo a los pescadores:","explain_es":"Los haré pescadores de hombres. ποιήσω es haré, futuro de ποιέω. ὑμᾶς es a ustedes. ἁλιεῖς, pescadores. ἀνθρώπων, de hombres."},
    "closing_es":"Aprendiste a hacer y trabajar: ποιέω hacer, ἐργάζομαι trabajar, ἔργον obra, y oficios como ἁλιεύς pescador y τέκτων carpintero. En la siguiente lección aprenderás bueno, malo, grande, pequeño. Εἰρήνη σοι.",
}

L20 = {
    "num":20,"intro_es":"Μάθημα εἴκοσι. Lección veinte. Hoy aprenderás adjetivos: bueno, malo, grande, pequeño, verdadero. Escucha.",
    "dialogue":[(M,"Τὸ δένδρον ἀγαθὸν καρποὺς καλοὺς ποιεῖ."),(F,"ναί, ἀλλὰ τὸ δένδρον τὸ πονηρὸν καρποὺς κακοὺς ποιεῖ.")],
    "context_es":"El hombre dice que el árbol bueno da frutos buenos. La mujer dice que el árbol malo da frutos malos. Es la enseñanza de Jesús en Mateo siete.",
    "vocab":[
        {"gr":"ἀγαθός","es":"bueno","note_es":"ἀγαθός significa bueno. Aparece ciento dos veces. Escucha."},
        {"gr":"κακός","es":"malo","note_es":"κακός significa malo. Aparece cincuenta veces. Escucha."},
        {"gr":"καλός","es":"hermoso, bueno","note_es":"καλός significa hermoso o bueno. Es diferente de ἀγαθός. καλός es más estético, ἀγαθός más moral. Aparece cien veces. Escucha."},
        {"gr":"πονηρός","es":"malvado","note_es":"πονηρός significa malvado. Es más fuerte que κακός. Aparece setenta y ocho veces. Escucha."},
        {"gr":"μέγας","es":"grande","note_es":"μέγας significa grande. Aparece doscientas cuarenta y tres veces. Escucha."},
        {"gr":"μικρός","es":"pequeño","note_es":"μικρός significa pequeño. Escucha."},
        {"gr":"ἀληθής","es":"verdadero","note_es":"ἀληθής significa verdadero. Viene de ἀ, sin, y λήθη, olvido. Lo que no se oculta es verdadero. Escucha."},
    ],
    "phrases":[
        {"gr":"ἀγαθός ἐστιν","es":"es bueno","prompt_es":"Di es bueno."},
        {"gr":"ὁ ἄνθρωπος ὁ ἀγαθός","es":"el hombre bueno","prompt_es":"Di el hombre bueno. En griego el adjetivo lleva su propio artículo."},
        {"gr":"ἡ γυνὴ ἡ καλή","es":"la mujer hermosa","prompt_es":"Di la mujer hermosa."},
        {"gr":"ὁ πονηρός","es":"el malvado","prompt_es":"Di el malvado. Cuando el adjetivo va solo con artículo, funciona como sustantivo."},
        {"gr":"μέγας ἐστιν ὁ θεός","es":"grande es Dios","prompt_es":"Di grande es Dios."},
        {"gr":"ὁ μικρὸς καὶ ὁ μέγας","es":"el pequeño y el grande","prompt_es":"Di el pequeño y el grande."},
        {"gr":"ἀληθῆ λέγεις","es":"dices la verdad","prompt_es":"Di dices la verdad. Literalmente, dices cosas verdaderas."},
    ],
    "recon":[
        {"other_gr":"Ἀγαθός ἐστιν ὁ διδάσκαλος;","other_voice":M,"prompt_es":"Te preguntan si el maestro es bueno. Di que sí, es bueno.","answer_gr":"ναί, ἀγαθός ἐστιν.","answer_voice":F},
        {"prompt_es":"Di el árbol bueno da frutos buenos. δένδρον es árbol, καρπός es fruto.","answer_gr":"Τὸ δένδρον τὸ ἀγαθὸν καρποὺς καλοὺς ποιεῖ.","answer_voice":F},
        {"prompt_es":"Di grande es Dios.","answer_gr":"Μέγας ἐστιν ὁ θεός.","answer_voice":F},
    ],
    "verse":{"gr":"Πᾶν δένδρον ἀγαθὸν καρποὺς καλοὺς ποιεῖ.","voice":M,"ref_es":"En Mateo siete diecisiete, Jesús dice:","explain_es":"Todo árbol bueno da frutos buenos. πᾶν significa todo. δένδρον, árbol. ἀγαθόν, bueno. καρπούς, frutos. καλούς, buenos. ποιεῖ, hace o da."},
    "closing_es":"Aprendiste adjetivos: ἀγαθός bueno, κακός malo, καλός hermoso, πονηρός malvado, μέγας grande, μικρός pequeño, ἀληθής verdadero. Has completado veinte lecciones. Εἰρήνη σοι.",
}
