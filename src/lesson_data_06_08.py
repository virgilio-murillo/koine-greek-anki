"""Lesson data 6-8"""
M = "el-GR-Chirp3-HD-Charon"
F = "el-GR-Chirp3-HD-Kore"

L6 = {
    "num": 6, "intro_es": "Μάθημα ἕξ. Lección seis. Hoy repasaremos todo lo que has aprendido con un diálogo completo. También aprenderás palabras de lugar. Escucha la conversación.",
    "dialogue": [(M,"Χαῖρε!"),(F,"Εἰρήνη σοι. Τί ὄνομά σοι;"),(M,"Σίμων. Καὶ σοί;"),(F,"Μαρία. Πόθεν εἶ;"),(M,"ἀπὸ Ἰερουσαλήμ. Καὶ σύ;"),(F,"ἀπὸ Γαλιλαίας."),(M,"Γινώσκεις τὸν ἄνθρωπον ἐκεῖνον;"),(F,"ναί, γινώσκω αὐτόν. Αὐτός ἐστιν ὁ διδάσκαλος.")],
    "context_es": "Escuchaste una conversación completa. Saludos, nombres, origen, y una pregunta sobre alguien. ¿Cuánto entendiste? Vamos a reconstruirlo.",
    "vocab": [
        {"gr":"ποῦ","es":"dónde","note_es":"ποῦ significa dónde. No confundas con πόθεν que es de dónde. ποῦ es dónde está algo. Escucha."},
        {"gr":"ὧδε","es":"aquí","note_es":"ὧδε significa aquí. Escucha."},
        {"gr":"ἐκεῖ","es":"allí","note_es":"ἐκεῖ significa allí. Escucha."},
        {"gr":"τίς","es":"quién","note_es":"τίς con acento significa quién. Sin acento, τις, significa alguien. Escucha la forma con acento."},
    ],
    "phrases": [
        {"gr":"ποῦ ἐστιν;","es":"¿dónde está?","prompt_es":"Pregunta dónde está."},
        {"gr":"ὧδε ἐστιν","es":"está aquí","prompt_es":"Di está aquí."},
        {"gr":"ἐκεῖ ἐστιν","es":"está allí","prompt_es":"Di está allí."},
        {"gr":"τίς ἐστιν;","es":"¿quién es?","prompt_es":"Pregunta quién es."},
        {"gr":"ποῦ ἐστιν ὁ ἄνθρωπος;","es":"¿dónde está el hombre?","prompt_es":"Pregunta dónde está el hombre."},
        {"gr":"ὁ ἄνθρωπος ἐκεῖ ἐστιν","es":"el hombre está allí","prompt_es":"Di el hombre está allí."},
    ],
    "recon": [
        {"other_gr":"Χαῖρε!","other_voice":F,"prompt_es":"Respóndele con paz a ti y pregunta su nombre.","answer_gr":"Εἰρήνη σοι. Τί ὄνομά σοι;","answer_voice":M},
        {"other_gr":"Μαρία. Καὶ σοί;","other_voice":F,"prompt_es":"Di tu nombre.","answer_gr":"Σίμων.","answer_voice":M},
        {"other_gr":"Πόθεν εἶ;","other_voice":F,"prompt_es":"Di que eres de Jerusalén y pregúntale.","answer_gr":"ἀπὸ Ἰερουσαλήμ. Καὶ σύ;","answer_voice":M},
        {"other_gr":"ἀπὸ Γαλιλαίας.","other_voice":F,"prompt_es":"Pregúntale si conoce a aquel hombre.","answer_gr":"Γινώσκεις τὸν ἄνθρωπον ἐκεῖνον;","answer_voice":M},
        {"other_gr":"ναί, γινώσκω αὐτόν.","other_voice":F,"prompt_es":"Pregunta quién es.","answer_gr":"Τίς ἐστιν;","answer_voice":M},
        {"other_gr":"Οὗτός ἐστιν ὁ διδάσκαλος.","other_voice":F,"prompt_es":"Di he aquí el maestro.","answer_gr":"ἰδοὺ ὁ διδάσκαλος.","answer_voice":M},
    ],
    "verse": {"gr":"Οὐκ ἔστιν ὧδε· ἠγέρθη.","voice":M,"ref_es":"En Mateo veintiocho seis, el ángel dijo a las mujeres en la tumba vacía:","explain_es":"No está aquí. Ha resucitado. Reconoces οὐκ, no. ἔστιν, está. ὧδε, aquí. La palabra ἠγέρθη significa fue levantado, resucitó."},
    "closing_es": "Felicidades. Has completado seis lecciones. Ya puedes saludar, presentarte, decir de dónde eres, y tener una conversación básica en el idioma del Nuevo Testamento. En la siguiente lección aprenderás verbos de movimiento. Εἰρήνη σοι.",
}

L7 = {
    "num": 7, "intro_es": "Μάθημα ἑπτά. Lección siete. Esta es la última lección a velocidad lenta. Hoy aprenderás a decir ir, venir, y caminar. Escucha.",
    "dialogue": [(F,"Ποῦ πορεύῃ;"),(M,"Πορεύομαι εἰς τὸ ἱερόν."),(F,"Ἔρχου μετ᾽ ἐμοῦ."),(M,"ναί, ἔρχομαι.")],
    "context_es": "La mujer preguntó a dónde va el hombre. Él va al templo. Ella le dijo ven conmigo, y él aceptó.",
    "vocab": [
        {"gr":"ἔρχομαι","es":"venir, ir","note_es":"ἔρχομαι significa venir o ir. Tiene forma pasiva pero significado activo. Esto se llama verbo deponente. No te preocupes por eso, solo aprende la palabra. Escucha."},
        {"gr":"ἔρχου","es":"ven (orden)","note_es":"Para decir ven, como una orden, se dice ἔρχου. Jesús dijo a Felipe: ἔρχου. Ven. Escucha."},
        {"gr":"πορεύομαι","es":"ir, caminar","note_es":"πορεύομαι significa ir o caminar. También es deponente. Escucha."},
        {"gr":"εἰς","es":"hacia, a","note_es":"εἰς significa hacia o a. Indica movimiento. πορεύομαι εἰς τὸ ἱερόν, voy hacia el templo. Escucha."},
        {"gr":"ἐν","es":"en","note_es":"ἐν significa en. Indica ubicación, no movimiento. εἰς es hacia, ἐν es en. ἐν τῷ ἱερῷ, en el templo. Escucha."},
        {"gr":"οἶκος","es":"casa","note_es":"οἶκος significa casa. ὁ οἶκος, la casa. Escucha."},
        {"gr":"ὁδός","es":"camino","note_es":"ὁδός significa camino. ἐν τῇ ὁδῷ, en el camino. Escucha."},
        {"gr":"δεῦτε","es":"vengan","note_es":"δεῦτε significa vengan. Es una invitación plural. Jesús dijo a los pescadores: δεῦτε ὀπίσω μου, vengan tras de mí. ὀπίσω significa detrás. Escucha."},
    ],
    "phrases": [
        {"gr":"πορεύομαι εἰς τὸ ἱερόν","es":"voy al templo","prompt_es":"Di voy al templo. ἱερόν es templo."},
        {"gr":"ἐν τῇ ὁδῷ","es":"en el camino","prompt_es":"Di en el camino."},
        {"gr":"ἔρχου μετ᾽ ἐμοῦ","es":"ven conmigo","prompt_es":"Di ven conmigo. μετ᾽ ἐμοῦ significa conmigo."},
        {"gr":"πορεύομαι εἰς τὸν οἶκον","es":"voy a la casa","prompt_es":"Di voy a la casa."},
        {"gr":"Δεῦτε ὀπίσω μου","es":"vengan tras de mí","prompt_es":"Di vengan tras de mí. Como Jesús dijo a los pescadores."},
        {"gr":"ἐν τῷ ἱερῷ","es":"en el templo","prompt_es":"Di en el templo. Nota: εἰς es hacia, ἐν es en."},
        {"gr":"ποῦ πορεύῃ;","es":"¿a dónde vas?","prompt_es":"Pregunta a dónde vas."},
    ],
    "recon": [
        {"other_gr":"Ποῦ πορεύῃ;","other_voice":F,"prompt_es":"Te preguntan a dónde vas. Di que vas al templo.","answer_gr":"Πορεύομαι εἰς τὸ ἱερόν.","answer_voice":M},
        {"prompt_es":"Invítala a venir contigo.","answer_gr":"Ἔρχου μετ᾽ ἐμοῦ.","answer_voice":M},
        {"other_gr":"ναί, ἔρχομαι.","other_voice":F,"prompt_es":"Ella acepta. Dile paz a ti.","answer_gr":"Εἰρήνη σοι.","answer_voice":M},
        {"prompt_es":"Ahora di vengan tras de mí, como Jesús.","answer_gr":"Δεῦτε ὀπίσω μου.","answer_voice":M},
    ],
    "verse": {"gr":"Δεῦτε ὀπίσω μου, καὶ ποιήσω ὑμᾶς ἁλιεῖς ἀνθρώπων.","voice":M,"ref_es":"En Mateo cuatro diecinueve, Jesús vio a Simón y Andrés pescando y les dijo:","explain_es":"Vengan tras de mí, y los haré pescadores de hombres. Reconoces δεῦτε, vengan. ὀπίσω μου, tras de mí. καί, y. ἀνθρώπων, de hombres."},
    "closing_es": "Aprendiste verbos de movimiento: ἔρχομαι venir, πορεύομαι ir, y las preposiciones εἰς hacia y ἐν en. A partir de la siguiente lección, el griego sonará un poco más rápido. Εἰρήνη σοι.",
}

L8 = {
    "num": 8, "intro_es": "Μάθημα ὀκτώ. Lección ocho. Nota que el griego ahora suena un poco más rápido. Hoy aprenderás vocabulario del mercado: pan, agua, vino. Escucha.",
    "dialogue": [(F,"Θέλεις ἄρτον;"),(M,"ναί, θέλω ἄρτον καὶ ὕδωρ."),(F,"Ἰδού. Λάβε."),(M,"Εὐχαριστῶ.")],
    "context_es": "Una vendedora ofrece pan. El hombre quiere pan y agua. Ella le dice toma. Él da gracias.",
    "vocab": [
        {"gr":"θέλω","es":"quiero","note_es":"θέλω significa quiero. θέλεις es quieres. θέλει es quiere. Escucha."},
        {"gr":"ἄρτος","es":"pan","note_es":"ἄρτος significa pan. Es la palabra que Jesús usa en la última cena. Nunca uses la palabra moderna ψωμί. En koiné siempre es ἄρτος. Escucha."},
        {"gr":"ὕδωρ","es":"agua","note_es":"ὕδωρ significa agua. Nunca uses la palabra moderna νερό. En koiné siempre es ὕδωρ. Escucha."},
        {"gr":"οἶνος","es":"vino","note_es":"οἶνος significa vino. Escucha."},
        {"gr":"ἰχθύς","es":"pez","note_es":"ἰχθύς significa pez. Los primeros cristianos usaban el pez como símbolo. Escucha."},
        {"gr":"ἐσθίω","es":"comer","note_es":"ἐσθίω significa comer. Escucha."},
        {"gr":"πίνω","es":"beber","note_es":"πίνω significa beber. Escucha."},
        {"gr":"λάβε","es":"toma (orden)","note_es":"λάβε significa toma. Es una orden. Viene del verbo λαμβάνω, tomar o recibir. Jesús dijo λάβετε, tomen, en la última cena. Escucha."},
    ],
    "phrases": [
        {"gr":"θέλω ἄρτον","es":"quiero pan","prompt_es":"Di quiero pan. Nota que ἄρτον termina en ον porque es objeto directo."},
        {"gr":"θέλω ὕδωρ","es":"quiero agua","prompt_es":"Di quiero agua."},
        {"gr":"θέλω οἶνον","es":"quiero vino","prompt_es":"Di quiero vino."},
        {"gr":"θέλεις ἄρτον;","es":"¿quieres pan?","prompt_es":"Pregunta quieres pan."},
        {"gr":"ἐσθίω ἄρτον","es":"como pan","prompt_es":"Di como pan."},
        {"gr":"πίνω οἶνον","es":"bebo vino","prompt_es":"Di bebo vino."},
        {"gr":"ἐσθίω ἄρτον καὶ πίνω οἶνον","es":"como pan y bebo vino","prompt_es":"Di como pan y bebo vino."},
        {"gr":"θέλω ἄρτον καὶ ὕδωρ","es":"quiero pan y agua","prompt_es":"Di quiero pan y agua."},
        {"gr":"εὐχαριστῶ","es":"doy gracias","prompt_es":"Da gracias. En koiné, εὐχαριστῶ es formal, es dar gracias a Dios. No es el gracias casual del griego moderno. Escucha."},
    ],
    "recon": [
        {"other_gr":"Θέλεις ἄρτον;","other_voice":F,"prompt_es":"Te ofrecen pan. Di que sí, quieres pan y agua.","answer_gr":"ναί, θέλω ἄρτον καὶ ὕδωρ.","answer_voice":M},
        {"other_gr":"Ἰδού. Λάβε.","other_voice":F,"prompt_es":"Te dicen toma. Da gracias.","answer_gr":"Εὐχαριστῶ.","answer_voice":M},
        {"prompt_es":"Pregúntale si quiere vino.","answer_gr":"Θέλεις οἶνον;","answer_voice":M},
        {"other_gr":"ναί, θέλω.","other_voice":F,"prompt_es":"Dile toma.","answer_gr":"Λάβε.","answer_voice":M},
    ],
    "verse": {"gr":"Πόθεν ἀγοράσωμεν ἄρτους ἵνα φάγωσιν οὗτοι;","voice":M,"ref_es":"En Juan seis cinco, Jesús vio una gran multitud y le preguntó a Felipe:","explain_es":"¿De dónde compraremos panes para que estos coman? Reconoces πόθεν, de dónde. ἄρτους, panes en plural. οὗτοι, estos."},
    "closing_es": "Aprendiste vocabulario del mercado: ἄρτος pan, ὕδωρ agua, οἶνος vino, ἰχθύς pez. Y los verbos θέλω querer, ἐσθίω comer, πίνω beber. En la siguiente lección aprenderás los números del uno al diez. Εἰρήνη σοι.",
}
