"""Lesson data 21-25: Speaking/Teaching, Believing, Loving, Body, Past tense intro"""
M = "el-GR-Chirp3-HD-Charon"
F = "el-GR-Chirp3-HD-Kore"

L21 = {
    "num":21,"intro_es":"Μάθημα εἴκοσι ἕν. Lección veintiuno. Hoy aprenderás a hablar, enseñar, preguntar y responder. Escucha.",
    "dialogue":[(F,"Διδάσκαλε, ἐρωτῶ σε."),(M,"Λάλει."),(F,"Τί διδάσκεις τοὺς μαθητάς;"),(M,"Διδάσκω αὐτοὺς τὸν λόγον τοῦ θεοῦ.")],
    "context_es":"La mujer llama al maestro y le hace una pregunta. Él le dice que hable. Ella pregunta qué enseña a los discípulos. Él enseña la palabra de Dios.",
    "vocab":[
        {"gr":"λαλέω","es":"hablar","note_es":"λαλέω significa hablar. Aparece doscientas noventa y seis veces. λάλει es la orden: habla. Escucha."},
        {"gr":"διδάσκω","es":"enseñar","note_es":"διδάσκω significa enseñar. Aparece noventa y siete veces. Escucha."},
        {"gr":"ἐρωτάω","es":"preguntar","note_es":"ἐρωτάω significa preguntar. Aparece sesenta y tres veces. Escucha."},
        {"gr":"ἀποκρίνομαι","es":"responder","note_es":"ἀποκρίνομαι significa responder. Es deponente. Aparece doscientas treinta y una veces. Viene de ἀπό y κρίνω. Escucha."},
        {"gr":"διδάσκαλος","es":"maestro","note_es":"διδάσκαλος significa maestro. Aparece cincuenta y nueve veces. Es como los discípulos llamaban a Jesús. Escucha."},
        {"gr":"μαθητής","es":"discípulo","note_es":"μαθητής significa discípulo o estudiante. Aparece doscientas sesenta y una veces. Viene de μανθάνω, aprender. Escucha."},
    ],
    "phrases":[
        {"gr":"ὁ διδάσκαλος λαλεῖ","es":"el maestro habla","prompt_es":"Di el maestro habla."},
        {"gr":"διδάσκω τοὺς μαθητάς","es":"enseño a los discípulos","prompt_es":"Di enseño a los discípulos."},
        {"gr":"ἐρωτῶ σε","es":"te pregunto","prompt_es":"Di te pregunto. σε es a ti, acusativo."},
        {"gr":"ἀποκρίνεται αὐτοῖς","es":"les responde","prompt_es":"Di les responde. αὐτοῖς es a ellos, dativo."},
        {"gr":"τὸν λόγον τοῦ θεοῦ","es":"la palabra de Dios","prompt_es":"Di la palabra de Dios."},
        {"gr":"οἱ μαθηταί","es":"los discípulos","prompt_es":"Di los discípulos. οἱ es el artículo masculino plural."},
    ],
    "recon":[
        {"other_gr":"Τί διδάσκεις;","other_voice":F,"prompt_es":"Te preguntan qué enseñas. Di que enseñas la palabra de Dios.","answer_gr":"Διδάσκω τὸν λόγον τοῦ θεοῦ.","answer_voice":M},
        {"prompt_es":"Pregúntale algo. Di te pregunto.","answer_gr":"Ἐρωτῶ σε.","answer_voice":M},
        {"prompt_es":"Di el maestro habla a los discípulos.","answer_gr":"Ὁ διδάσκαλος λαλεῖ τοῖς μαθηταῖς.","answer_voice":M},
    ],
    "verse":{"gr":"Ἐλάλησεν αὐτοῖς πολλὰ ἐν παραβολαῖς.","voice":M,"ref_es":"En Mateo trece tres, Jesús les habló muchas cosas en parábolas:","explain_es":"Les habló muchas cosas en parábolas. ἐλάλησεν es habló, pasado de λαλέω. αὐτοῖς, a ellos. πολλά, muchas cosas. παραβολαῖς, parábolas."},
    "closing_es":"Aprendiste a hablar y enseñar: λαλέω hablar, διδάσκω enseñar, ἐρωτάω preguntar, ἀποκρίνομαι responder, διδάσκαλος maestro, μαθητής discípulo. Εἰρήνη σοι.",
}

L22 = {
    "num":22,"intro_es":"Μάθημα εἴκοσι δύο. Lección veintidós. Hoy aprenderás a creer, saber, y pensar. Escucha.",
    "dialogue":[(F,"Πιστεύεις ὅτι οὗτός ἐστιν ὁ Χριστός;"),(M,"ναί, οἶδα ὅτι σὺ εἶ ὁ Χριστὸς ὁ υἱὸς τοῦ θεοῦ τοῦ ζῶντος.")],
    "context_es":"La mujer pregunta si cree que este es el Cristo. El hombre responde con la confesión de Pedro: sé que tú eres el Cristo, el hijo del Dios viviente.",
    "vocab":[
        {"gr":"πιστεύω","es":"creer","note_es":"πιστεύω significa creer. Aparece doscientas cuarenta y una veces. πιστεύεις es crees. Escucha."},
        {"gr":"οἶδα","es":"saber","note_es":"οἶδα significa saber. Es un verbo especial: tiene forma de pasado pero significado de presente. Yo sé. Aparece trescientas dieciocho veces. Escucha."},
        {"gr":"πίστις","es":"fe","note_es":"πίστις significa fe. Aparece doscientas cuarenta y tres veces. ἡ πίστις, la fe. Escucha."},
        {"gr":"ἀλήθεια","es":"verdad","note_es":"ἀλήθεια significa verdad. Viene de ἀ, sin, y λήθη, olvido. Lo que no se oculta. Aparece ciento nueve veces. Escucha."},
        {"gr":"δοκέω","es":"pensar, parecer","note_es":"δοκέω significa pensar o parecer. δοκεῖς es piensas. Escucha."},
        {"gr":"Χριστός","es":"Cristo, Ungido","note_es":"Χριστός significa Ungido o Cristo. Viene de χρίω, ungir. Aparece quinientas veintiocho veces. Escucha."},
    ],
    "phrases":[
        {"gr":"πιστεύω","es":"creo","prompt_es":"Di creo."},
        {"gr":"πιστεύεις;","es":"¿crees?","prompt_es":"Pregunta crees."},
        {"gr":"οἶδα ὅτι","es":"sé que","prompt_es":"Di sé que."},
        {"gr":"ἡ ἀλήθεια","es":"la verdad","prompt_es":"Di la verdad."},
        {"gr":"σὺ εἶ ὁ Χριστός","es":"tú eres el Cristo","prompt_es":"Di tú eres el Cristo. La confesión de Pedro."},
        {"gr":"ὁ υἱὸς τοῦ θεοῦ","es":"el hijo de Dios","prompt_es":"Di el hijo de Dios."},
        {"gr":"πιστεύω εἰς τὸν κύριον","es":"creo en el Señor","prompt_es":"Di creo en el Señor. πιστεύω εἰς significa creer en."},
    ],
    "recon":[
        {"other_gr":"Πιστεύεις ὅτι οὗτός ἐστιν ὁ Χριστός;","other_voice":F,"prompt_es":"Te preguntan si crees. Di que sí, creo.","answer_gr":"ναί, πιστεύω.","answer_voice":M},
        {"prompt_es":"Di sé que tú eres el Cristo.","answer_gr":"Οἶδα ὅτι σὺ εἶ ὁ Χριστός.","answer_voice":M},
        {"prompt_es":"Di creo en el Señor.","answer_gr":"Πιστεύω εἰς τὸν κύριον.","answer_voice":M},
    ],
    "verse":{"gr":"Σὺ εἶ ὁ Χριστὸς ὁ υἱὸς τοῦ θεοῦ τοῦ ζῶντος.","voice":M,"ref_es":"En Mateo dieciséis dieciséis, Pedro le dijo a Jesús:","explain_es":"Tú eres el Cristo, el hijo del Dios viviente. Reconoces cada palabra excepto ζῶντος, que significa viviente, del verbo ζάω, vivir."},
    "closing_es":"Aprendiste a creer y saber: πιστεύω creer, οἶδα saber, πίστις fe, ἀλήθεια verdad, Χριστός Cristo. Εἰρήνη σοι.",
}

L23 = {
    "num":23,"intro_es":"Μάθημα εἴκοσι τρία. Lección veintitrés. Hoy aprenderás emociones: amar, temer, alegrarse. Escucha.",
    "dialogue":[(M,"Ἀγαπήσεις κύριον τὸν θεόν σου."),(F,"Καὶ τὸν πλησίον σου ὡς σεαυτόν."),(M,"Μὴ φοβεῖσθε.")],
    "context_es":"El hombre cita el gran mandamiento: amarás al Señor tu Dios. La mujer completa: y a tu prójimo como a ti mismo. El hombre dice no teman.",
    "vocab":[
        {"gr":"ἀγαπάω","es":"amar","note_es":"ἀγαπάω significa amar. Es el amor más alto en el Nuevo Testamento. Aparece ciento cuarenta y tres veces. Escucha."},
        {"gr":"ἀγάπη","es":"amor","note_es":"ἀγάπη significa amor. Aparece ciento dieciséis veces. ἡ ἀγάπη, el amor. Escucha."},
        {"gr":"φοβέομαι","es":"temer","note_es":"φοβέομαι significa temer. Es deponente. Aparece noventa y cinco veces. μὴ φοβοῦ es no temas. Escucha."},
        {"gr":"χαίρω","es":"alegrarse","note_es":"χαίρω significa alegrarse. Ya conoces χαῖρε como saludo. Literalmente significa alégrate. Escucha."},
        {"gr":"χαρά","es":"gozo, alegría","note_es":"χαρά significa gozo o alegría. Aparece cincuenta y nueve veces. Escucha."},
        {"gr":"μισέω","es":"odiar","note_es":"μισέω significa odiar. Aparece cuarenta veces. Escucha."},
    ],
    "phrases":[
        {"gr":"ἀγαπήσεις κύριον τὸν θεόν σου","es":"amarás al Señor tu Dios","prompt_es":"Di amarás al Señor tu Dios. ἀγαπήσεις es amarás, futuro."},
        {"gr":"ἀγαπᾶτε ἀλλήλους","es":"ámense unos a otros","prompt_es":"Di ámense unos a otros. ἀλλήλους significa unos a otros."},
        {"gr":"μὴ φοβεῖσθε","es":"no teman","prompt_es":"Di no teman. μή con imperativo es prohibición."},
        {"gr":"μὴ φοβοῦ","es":"no temas","prompt_es":"Di no temas. Singular."},
        {"gr":"χαίρετε","es":"alégrense","prompt_es":"Di alégrense. Es también un saludo plural."},
        {"gr":"ἡ ἀγάπη τοῦ θεοῦ","es":"el amor de Dios","prompt_es":"Di el amor de Dios."},
    ],
    "recon":[
        {"prompt_es":"Di el gran mandamiento: amarás al Señor tu Dios.","answer_gr":"Ἀγαπήσεις κύριον τὸν θεόν σου.","answer_voice":M},
        {"prompt_es":"Completa: y a tu prójimo como a ti mismo. πλησίον es prójimo, σεαυτόν es a ti mismo.","answer_gr":"Καὶ τὸν πλησίον σου ὡς σεαυτόν.","answer_voice":M},
        {"prompt_es":"Di no teman.","answer_gr":"Μὴ φοβεῖσθε.","answer_voice":M},
        {"prompt_es":"Di ámense unos a otros.","answer_gr":"Ἀγαπᾶτε ἀλλήλους.","answer_voice":M},
    ],
    "verse":{"gr":"Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν.","voice":M,"ref_es":"En Mateo veintidós treinta y nueve, Jesús dice el segundo mandamiento:","explain_es":"Amarás a tu prójimo como a ti mismo. ἀγαπήσεις, amarás. πλησίον, prójimo. ὡς, como. σεαυτόν, a ti mismo."},
    "closing_es":"Aprendiste emociones: ἀγαπάω amar, ἀγάπη amor, φοβέομαι temer, χαίρω alegrarse, χαρά gozo, μισέω odiar. Εἰρήνη σοι.",
}

L24 = {
    "num":24,"intro_es":"Μάθημα εἴκοσι τέσσαρα. Lección veinticuatro. Hoy aprenderás partes del cuerpo: mano, pie, corazón, boca. Escucha.",
    "dialogue":[(M,"Ἐκ τοῦ περισσεύματος τῆς καρδίας τὸ στόμα λαλεῖ."),(F,"ἀληθῆ λέγεις.")],
    "context_es":"El hombre cita a Jesús: de la abundancia del corazón habla la boca. La mujer dice que habla verdad.",
    "vocab":[
        {"gr":"σῶμα","es":"cuerpo","note_es":"σῶμα significa cuerpo. Aparece ciento cuarenta y dos veces. τὸ σῶμα, el cuerpo. Es neutro. Escucha."},
        {"gr":"κεφαλή","es":"cabeza","note_es":"κεφαλή significa cabeza. Aparece setenta y cinco veces. Escucha."},
        {"gr":"χείρ","es":"mano","note_es":"χείρ significa mano. Aparece ciento setenta y siete veces. ἡ χείρ, la mano. Escucha."},
        {"gr":"πούς","es":"pie","note_es":"πούς significa pie. Aparece noventa y tres veces. ὁ πούς, el pie. Escucha."},
        {"gr":"στόμα","es":"boca","note_es":"στόμα significa boca. Aparece setenta y ocho veces. τὸ στόμα, la boca. Escucha."},
        {"gr":"καρδία","es":"corazón","note_es":"καρδία significa corazón. Aparece ciento cincuenta y seis veces. ἡ καρδία, el corazón. En koiné el corazón es el centro del pensamiento y la voluntad, no solo emociones. Escucha."},
    ],
    "phrases":[
        {"gr":"ἐν τῇ καρδίᾳ","es":"en el corazón","prompt_es":"Di en el corazón."},
        {"gr":"ἐκ τοῦ στόματος","es":"de la boca","prompt_es":"Di de la boca."},
        {"gr":"τὰς χεῖρας","es":"las manos","prompt_es":"Di las manos. χεῖρας es el acusativo plural."},
        {"gr":"τοὺς πόδας","es":"los pies","prompt_es":"Di los pies. πόδας es el acusativo plural."},
        {"gr":"τὸ σῶμα τοῦ Χριστοῦ","es":"el cuerpo de Cristo","prompt_es":"Di el cuerpo de Cristo."},
        {"gr":"ἐπέθηκεν τὰς χεῖρας","es":"impuso las manos","prompt_es":"Di impuso las manos. ἐπέθηκεν es puso sobre, pasado."},
    ],
    "recon":[
        {"prompt_es":"Di de la abundancia del corazón habla la boca. περισσεύματος es abundancia.","answer_gr":"Ἐκ τοῦ περισσεύματος τῆς καρδίας τὸ στόμα λαλεῖ.","answer_voice":M},
        {"prompt_es":"Di el cuerpo de Cristo.","answer_gr":"Τὸ σῶμα τοῦ Χριστοῦ.","answer_voice":M},
        {"prompt_es":"Di en el corazón.","answer_gr":"Ἐν τῇ καρδίᾳ.","answer_voice":M},
    ],
    "verse":{"gr":"Ἐκ γὰρ τοῦ περισσεύματος τῆς καρδίας τὸ στόμα λαλεῖ.","voice":M,"ref_es":"En Mateo doce treinta y cuatro, Jesús dice:","explain_es":"Porque de la abundancia del corazón habla la boca. γάρ es porque, postpositiva. καρδίας, del corazón. στόμα, boca. λαλεῖ, habla."},
    "closing_es":"Aprendiste el cuerpo: σῶμα cuerpo, κεφαλή cabeza, χείρ mano, πούς pie, στόμα boca, καρδία corazón. Εἰρήνη σοι.",
}

L25 = {
    "num":25,"intro_es":"Μάθημα εἴκοσι πέντε. Lección veinticinco. Hoy aprenderás a hablar en pasado. Escucharás las formas más comunes del aoristo: vine, dije, vi. Escucha.",
    "dialogue":[(F,"Τί ἐγένετο;"),(M,"Ἦλθεν ὁ διδάσκαλος καὶ εἶπεν ἡμῖν λόγους μεγάλους."),(F,"Εἶδες αὐτόν;"),(M,"ναί, εἶδον αὐτὸν καὶ ἤκουσα τὴν φωνὴν αὐτοῦ.")],
    "context_es":"La mujer pregunta qué pasó. El hombre dice que vino el maestro y les dijo grandes palabras. Ella pregunta si lo vio. Él lo vio y oyó su voz.",
    "vocab":[
        {"gr":"ἦλθον","es":"vine, fui (pasado de ἔρχομαι)","note_es":"ἦλθον es el pasado de ἔρχομαι, venir. ἦλθον es vine o fui. ἦλθεν es vino o fue. Son formas irregulares. Memorízalas. Escucha."},
        {"gr":"εἶπον","es":"dije (pasado de λέγω)","note_es":"εἶπον es el pasado de λέγω, decir. εἶπον es dije. εἶπεν es dijo. Irregular. Escucha."},
        {"gr":"εἶδον","es":"vi (pasado de ὁράω)","note_es":"εἶδον es el pasado de ὁράω, ver. εἶδον es vi. εἶδεν es vio. Irregular. Escucha."},
        {"gr":"ἤκουσα","es":"oí (pasado de ἀκούω)","note_es":"ἤκουσα es el pasado de ἀκούω, oír. ἤκουσα es oí. ἤκουσεν es oyó. Escucha."},
        {"gr":"ἐποίησα","es":"hice (pasado de ποιέω)","note_es":"ἐποίησα es el pasado de ποιέω, hacer. ἐποίησα es hice. ἐποίησεν es hizo. Escucha."},
        {"gr":"ἐγένετο","es":"sucedió (pasado de γίνομαι)","note_es":"ἐγένετο significa sucedió o aconteció. Es el pasado de γίνομαι. Aparece doscientas dos veces. Es la forma más común de empezar una narración bíblica. Escucha."},
    ],
    "phrases":[
        {"gr":"ἦλθεν ὁ κύριος","es":"vino el Señor","prompt_es":"Di vino el Señor."},
        {"gr":"εἶπεν αὐτοῖς","es":"les dijo","prompt_es":"Di les dijo."},
        {"gr":"εἶδον τὸν κύριον","es":"vi al Señor","prompt_es":"Di vi al Señor."},
        {"gr":"ἤκουσα τὴν φωνήν","es":"oí la voz","prompt_es":"Di oí la voz. φωνή significa voz."},
        {"gr":"τί ἐποίησας;","es":"¿qué hiciste?","prompt_es":"Pregunta qué hiciste."},
        {"gr":"ἐγένετο ἐν ταῖς ἡμέραις ἐκείναις","es":"sucedió en aquellos días","prompt_es":"Di sucedió en aquellos días. Así empiezan muchas narraciones bíblicas."},
    ],
    "recon":[
        {"other_gr":"Τί ἐγένετο;","other_voice":F,"prompt_es":"Te preguntan qué pasó. Di que vino el maestro.","answer_gr":"Ἦλθεν ὁ διδάσκαλος.","answer_voice":M},
        {"other_gr":"Τί εἶπεν;","other_voice":F,"prompt_es":"Te preguntan qué dijo. Di que dijo grandes palabras.","answer_gr":"Εἶπεν λόγους μεγάλους.","answer_voice":M},
        {"other_gr":"Εἶδες αὐτόν;","other_voice":F,"prompt_es":"Te preguntan si lo viste. Di que sí, lo vi.","answer_gr":"ναί, εἶδον αὐτόν.","answer_voice":M},
        {"prompt_es":"Di oí su voz.","answer_gr":"Ἤκουσα τὴν φωνὴν αὐτοῦ.","answer_voice":M},
    ],
    "verse":{"gr":"Ἐδάκρυσεν ὁ Ἰησοῦς.","voice":M,"ref_es":"En Juan once treinta y cinco, el versículo más corto del Nuevo Testamento:","explain_es":"Jesús lloró. ἐδάκρυσεν es lloró, pasado de δακρύω. Solo dos palabras, pero muy poderosas."},
    "closing_es":"Aprendiste el pasado de los verbos más comunes: ἦλθον vine, εἶπον dije, εἶδον vi, ἤκουσα oí, ἐποίησα hice, ἐγένετο sucedió. Estas formas son irregulares pero muy frecuentes. En la siguiente lección practicarás más narración. Εἰρήνη σοι.",
}
