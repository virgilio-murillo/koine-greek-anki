"""Lesson data 31-35: Level 2 — Aorist narratives, Imperfect"""
from src.tts import M, F

L31 = {
    "num":31,"intro_es":"Μάθημα τριάκοντα ἕν. Lección treinta y uno. Bienvenido al segundo nivel: Ὁ Μαθητής, el discípulo. Hoy narrarás la historia de Lázaro. Escucha.",
    "dialogue":[(F,"Κύριε, ἴδε ὃν φιλεῖς ἀσθενεῖ."),(M,"Αὕτη ἡ ἀσθένεια οὐκ ἔστιν πρὸς θάνατον."),(F,"Κύριε, εἰ ἦς ὧδε, οὐκ ἂν ἀπέθανεν ὁ ἀδελφός μου.")],
    "context_es":"Escuchaste la historia de Lázaro. Marta dice: Señor, mira, el que amas está enfermo. Jesús dice que la enfermedad no es para muerte. Marta dice: si hubieras estado aquí, mi hermano no habría muerto.",
    "vocab":[
        {"gr":"ἀσθενέω","es":"estar enfermo","note_es":"ἀσθενέω significa estar enfermo o débil. Viene de ἀ, sin, y σθένος, fuerza. Sin fuerza. Escucha."},
        {"gr":"θάνατος","es":"muerte","note_es":"θάνατος significa muerte. Aparece ciento veinte veces. ὁ θάνατος, la muerte. Escucha."},
        {"gr":"ἀποθνῄσκω","es":"morir","note_es":"ἀποθνῄσκω significa morir. ἀπέθανεν es murió, aoristo. Escucha."},
        {"gr":"κλαίω","es":"llorar","note_es":"κλαίω significa llorar. Aparece cuarenta veces. ἔκλαυσεν es lloró. Escucha."},
        {"gr":"ζάω","es":"vivir","note_es":"ζάω significa vivir. ζῇ es vive. Escucha."},
        {"gr":"ἐγείρω","es":"levantar, resucitar","note_es":"ἐγείρω significa levantar o resucitar. Aparece ciento cuarenta y cuatro veces. ἠγέρθη es fue levantado, resucitó. Escucha."},
    ],
    "phrases":[
        {"gr":"ἀσθενεῖ","es":"está enfermo","prompt_es":"Di está enfermo."},
        {"gr":"ἀπέθανεν","es":"murió","prompt_es":"Di murió."},
        {"gr":"ἐδάκρυσεν ὁ Ἰησοῦς","es":"Jesús lloró","prompt_es":"Di Jesús lloró. El versículo más corto del Nuevo Testamento."},
        {"gr":"Λάζαρε, δεῦρο ἔξω","es":"Lázaro, ven fuera","prompt_es":"Di Lázaro, ven fuera. ἔξω significa fuera."},
        {"gr":"ἐγώ εἰμι ἡ ἀνάστασις καὶ ἡ ζωή","es":"yo soy la resurrección y la vida","prompt_es":"Di yo soy la resurrección y la vida. ἀνάστασις es resurrección."},
        {"gr":"ὁ πιστεύων εἰς ἐμὲ ζήσεται","es":"el que cree en mí vivirá","prompt_es":"Di el que cree en mí vivirá. ζήσεται es vivirá."},
    ],
    "recon":[
        {"other_gr":"Τί ἐγένετο;","other_voice":F,"prompt_es":"Te preguntan qué pasó. Di que Lázaro murió.","answer_gr":"Λάζαρος ἀπέθανεν.","answer_voice":M},
        {"prompt_es":"Di que Jesús lloró.","answer_gr":"Ἐδάκρυσεν ὁ Ἰησοῦς.","answer_voice":M},
        {"prompt_es":"Di que Jesús dijo: Lázaro, ven fuera.","answer_gr":"Εἶπεν ὁ Ἰησοῦς· Λάζαρε, δεῦρο ἔξω.","answer_voice":M},
        {"prompt_es":"Di yo soy la resurrección y la vida.","answer_gr":"Ἐγώ εἰμι ἡ ἀνάστασις καὶ ἡ ζωή.","answer_voice":M},
    ],
    "verse":{"gr":"Ἐγώ εἰμι ἡ ἀνάστασις καὶ ἡ ζωή· ὁ πιστεύων εἰς ἐμὲ κἂν ἀποθάνῃ ζήσεται.","voice":M,"ref_es":"En Juan once veinticinco, Jesús dijo a Marta:","explain_es":"Yo soy la resurrección y la vida. El que cree en mí, aunque muera, vivirá. ἀνάστασις, resurrección. ζωή, vida. πιστεύων, el que cree. ἀποθάνῃ, muera. ζήσεται, vivirá."},
    "closing_es":"Aprendiste a narrar la historia de Lázaro: ἀσθενέω estar enfermo, θάνατος muerte, ἀποθνῄσκω morir, κλαίω llorar, ζάω vivir, ἐγείρω resucitar. Εἰρήνη σοι.",
}

L32 = {
    "num":32,"intro_es":"Μάθημα τριάκοντα δύο. Lección treinta y dos. Hoy aprenderás el imperfecto: describir acciones continuas en el pasado. Escucha.",
    "dialogue":[(M,"Ὁ Ἰησοῦς περιῆγεν ἐν ὅλῃ τῇ Γαλιλαίᾳ, διδάσκων ἐν ταῖς συναγωγαῖς αὐτῶν καὶ θεραπεύων πᾶσαν νόσον.")],
    "context_es":"Jesús recorría toda Galilea, enseñando en sus sinagogas y sanando toda enfermedad. El imperfecto describe acciones que se repetían o continuaban en el pasado.",
    "vocab":[
        {"gr":"θεραπεύω","es":"sanar, curar","note_es":"θεραπεύω significa sanar o curar. Aparece cuarenta y tres veces. ἐθεράπευεν es sanaba, imperfecto. Escucha."},
        {"gr":"νόσος","es":"enfermedad","note_es":"νόσος significa enfermedad. Escucha."},
        {"gr":"ὄχλος","es":"multitud","note_es":"ὄχλος significa multitud o muchedumbre. Aparece ciento setenta y cinco veces. Escucha."},
        {"gr":"ἀκολουθέω","es":"seguir","note_es":"ἀκολουθέω significa seguir. Viene de ἀ, mismo, y κέλευθος, camino. Ir por el mismo camino. Aparece noventa veces. ἠκολούθουν es seguían, imperfecto. Escucha."},
        {"gr":"ὅλος","es":"todo, entero","note_es":"ὅλος significa todo o entero. ἐν ὅλῃ τῇ Γαλιλαίᾳ, en toda Galilea. Escucha."},
        {"gr":"πᾶς","es":"todo, cada","note_es":"πᾶς significa todo o cada. Aparece mil doscientas cuarenta y cuatro veces. πᾶσαν νόσον, toda enfermedad. Escucha."},
    ],
    "phrases":[
        {"gr":"ἐδίδασκεν","es":"enseñaba","prompt_es":"Di enseñaba. Es el imperfecto de διδάσκω. Describe una acción continua en el pasado."},
        {"gr":"ἐθεράπευεν","es":"sanaba","prompt_es":"Di sanaba. Imperfecto de θεραπεύω."},
        {"gr":"ἠκολούθουν αὐτῷ ὄχλοι πολλοί","es":"le seguían grandes multitudes","prompt_es":"Di le seguían grandes multitudes."},
        {"gr":"ἐν ὅλῃ τῇ Γαλιλαίᾳ","es":"en toda Galilea","prompt_es":"Di en toda Galilea."},
        {"gr":"πᾶσαν νόσον","es":"toda enfermedad","prompt_es":"Di toda enfermedad."},
        {"gr":"ἐδίδασκεν ἐν ταῖς συναγωγαῖς","es":"enseñaba en las sinagogas","prompt_es":"Di enseñaba en las sinagogas."},
    ],
    "recon":[
        {"prompt_es":"Narra: Jesús recorría toda Galilea.","answer_gr":"Ὁ Ἰησοῦς περιῆγεν ἐν ὅλῃ τῇ Γαλιλαίᾳ.","answer_voice":M},
        {"prompt_es":"Di enseñaba en las sinagogas.","answer_gr":"Ἐδίδασκεν ἐν ταῖς συναγωγαῖς.","answer_voice":M},
        {"prompt_es":"Di sanaba toda enfermedad.","answer_gr":"Ἐθεράπευεν πᾶσαν νόσον.","answer_voice":M},
        {"prompt_es":"Di le seguían grandes multitudes.","answer_gr":"Ἠκολούθουν αὐτῷ ὄχλοι πολλοί.","answer_voice":M},
    ],
    "verse":{"gr":"Περιῆγεν ὁ Ἰησοῦς τὰς πόλεις πάσας καὶ τὰς κώμας, διδάσκων ἐν ταῖς συναγωγαῖς αὐτῶν.","voice":M,"ref_es":"En Mateo nueve treinta y cinco:","explain_es":"Jesús recorría todas las ciudades y aldeas, enseñando en sus sinagogas. περιῆγεν, recorría. πόλεις, ciudades. κώμας, aldeas. διδάσκων, enseñando, es un participio."},
    "closing_es":"Aprendiste el imperfecto para describir el pasado continuo: ἐδίδασκεν enseñaba, ἐθεράπευεν sanaba, ἠκολούθουν seguían. Y vocabulario: θεραπεύω sanar, νόσος enfermedad, ὄχλος multitud, ἀκολουθέω seguir. Εἰρήνη σοι.",
}

L33 = {
    "num":33,"intro_es":"Μάθημα τριάκοντα τρία. Lección treinta y tres. Hoy aprenderás más narración combinando aoristo e imperfecto. Escucha la historia de la tempestad calmada.",
    "dialogue":[(M,"Καὶ ἰδοὺ σεισμὸς μέγας ἐγένετο ἐν τῇ θαλάσσῃ."),(M,"Αὐτὸς δὲ ἐκάθευδεν."),(F,"Κύριε, σῶσον ἡμᾶς, ἀπολλύμεθα!"),(M,"Τί δειλοί ἐστε, ὀλιγόπιστοι;")],
    "context_es":"Una gran tempestad surgió en el mar. Pero Jesús dormía. Los discípulos gritaron: Señor, sálvanos, perecemos. Jesús dijo: por qué tienen miedo, hombres de poca fe.",
    "vocab":[
        {"gr":"σῴζω","es":"salvar","note_es":"σῴζω significa salvar. Aparece ciento seis veces. σῶσον es sálvanos, imperativo aoristo. Escucha."},
        {"gr":"σεισμός","es":"terremoto, tempestad","note_es":"σεισμός significa terremoto o tempestad. Viene de σείω, sacudir. Escucha."},
        {"gr":"ἀπόλλυμι","es":"destruir, perecer","note_es":"ἀπόλλυμι significa destruir o perecer. ἀπολλύμεθα es perecemos. Viene de ἀπό y ὄλλυμι. Escucha."},
        {"gr":"δειλός","es":"cobarde, temeroso","note_es":"δειλός significa cobarde o temeroso. Escucha."},
        {"gr":"ὀλιγόπιστος","es":"de poca fe","note_es":"ὀλιγόπιστος significa de poca fe. Viene de ὀλίγος, poco, y πίστις, fe. Escucha."},
        {"gr":"ἐπιτιμάω","es":"reprender","note_es":"ἐπιτιμάω significa reprender. Jesús reprendió al viento y al mar. Viene de ἐπί, sobre, y τιμάω, valorar. Escucha."},
    ],
    "phrases":[
        {"gr":"σῶσον ἡμᾶς","es":"sálvanos","prompt_es":"Di sálvanos. σῶσον es la orden de salvar."},
        {"gr":"σεισμὸς μέγας ἐγένετο","es":"surgió una gran tempestad","prompt_es":"Di surgió una gran tempestad."},
        {"gr":"αὐτὸς δὲ ἐκάθευδεν","es":"pero él dormía","prompt_es":"Di pero él dormía. ἐκάθευδεν es dormía, imperfecto."},
        {"gr":"ἐπετίμησεν τοῖς ἀνέμοις","es":"reprendió a los vientos","prompt_es":"Di reprendió a los vientos. ἀνέμοις es vientos en dativo."},
        {"gr":"ἐγένετο γαλήνη μεγάλη","es":"se hizo gran calma","prompt_es":"Di se hizo gran calma. γαλήνη es calma."},
        {"gr":"τίς ἐστιν οὗτος;","es":"¿quién es este?","prompt_es":"Di quién es este. Los discípulos se asombraron."},
    ],
    "recon":[
        {"prompt_es":"Narra: surgió una gran tempestad en el mar.","answer_gr":"Σεισμὸς μέγας ἐγένετο ἐν τῇ θαλάσσῃ.","answer_voice":M},
        {"prompt_es":"Di pero él dormía.","answer_gr":"Αὐτὸς δὲ ἐκάθευδεν.","answer_voice":M},
        {"prompt_es":"Grita: Señor, sálvanos.","answer_gr":"Κύριε, σῶσον ἡμᾶς!","answer_voice":F},
        {"prompt_es":"Di reprendió a los vientos y se hizo gran calma.","answer_gr":"Ἐπετίμησεν τοῖς ἀνέμοις καὶ ἐγένετο γαλήνη μεγάλη.","answer_voice":M},
    ],
    "verse":{"gr":"Τί δειλοί ἐστε, ὀλιγόπιστοι;","voice":M,"ref_es":"En Mateo ocho veintiséis, Jesús dijo a los discípulos:","explain_es":"¿Por qué tienen miedo, hombres de poca fe? δειλοί, temerosos. ἐστε, son. ὀλιγόπιστοι, de poca fe. Reconoces ὀλίγος, poco, y πίστις, fe."},
    "closing_es":"Aprendiste a narrar combinando aoristo e imperfecto: ἐγένετο surgió, ἐκάθευδεν dormía, ἐπετίμησεν reprendió. Y vocabulario: σῴζω salvar, σεισμός tempestad, ἀπόλλυμι perecer. Εἰρήνη σοι.",
}

L34 = {
    "num":34,"intro_es":"Μάθημα τριάκοντα τέσσαρα. Lección treinta y cuatro. Hoy aprenderás mandamientos del Sermón del Monte. Escucha.",
    "dialogue":[(M,"Ἀγαπᾶτε τοὺς ἐχθροὺς ὑμῶν."),(M,"Προσεύχεσθε ὑπὲρ τῶν διωκόντων ὑμᾶς."),(M,"Αἰτεῖτε καὶ δοθήσεται ὑμῖν.")],
    "context_es":"Jesús enseña: amen a sus enemigos. Oren por los que los persiguen. Pidan y se les dará.",
    "vocab":[
        {"gr":"αἰτέω","es":"pedir","note_es":"αἰτέω significa pedir. Aparece setenta veces. αἰτεῖτε es pidan, imperativo plural. Escucha."},
        {"gr":"διώκω","es":"perseguir","note_es":"διώκω significa perseguir. Aparece cuarenta y cinco veces. Escucha."},
        {"gr":"ὑπέρ","es":"por, a favor de","note_es":"ὑπέρ significa por o a favor de. Con genitivo. προσεύχεσθε ὑπὲρ αὐτῶν, oren por ellos. Escucha."},
        {"gr":"κρίνω","es":"juzgar","note_es":"κρίνω significa juzgar. Aparece ciento catorce veces. μὴ κρίνετε, no juzguen. Escucha."},
        {"gr":"κρίσις","es":"juicio","note_es":"κρίσις significa juicio. Viene de κρίνω. Aparece cuarenta y siete veces. Escucha."},
        {"gr":"ἁμαρτία","es":"pecado","note_es":"ἁμαρτία significa pecado. Aparece ciento setenta y tres veces. ἡ ἁμαρτία, el pecado. Escucha."},
    ],
    "phrases":[
        {"gr":"αἰτεῖτε καὶ δοθήσεται ὑμῖν","es":"pidan y se les dará","prompt_es":"Di pidan y se les dará. δοθήσεται es será dado, futuro pasivo."},
        {"gr":"μὴ κρίνετε","es":"no juzguen","prompt_es":"Di no juzguen."},
        {"gr":"προσεύχεσθε ὑπὲρ αὐτῶν","es":"oren por ellos","prompt_es":"Di oren por ellos."},
        {"gr":"ἄφες ἡμῖν τὰς ἁμαρτίας ἡμῶν","es":"perdónanos nuestros pecados","prompt_es":"Di perdónanos nuestros pecados. ἄφες es perdona, de ἀφίημι."},
        {"gr":"ἡ κρίσις τοῦ θεοῦ","es":"el juicio de Dios","prompt_es":"Di el juicio de Dios."},
        {"gr":"ζητεῖτε καὶ εὑρήσετε","es":"busquen y encontrarán","prompt_es":"Di busquen y encontrarán."},
    ],
    "recon":[
        {"prompt_es":"Di amen a sus enemigos.","answer_gr":"Ἀγαπᾶτε τοὺς ἐχθροὺς ὑμῶν.","answer_voice":M},
        {"prompt_es":"Di pidan y se les dará.","answer_gr":"Αἰτεῖτε καὶ δοθήσεται ὑμῖν.","answer_voice":M},
        {"prompt_es":"Di no juzguen.","answer_gr":"Μὴ κρίνετε.","answer_voice":M},
        {"prompt_es":"Di perdónanos nuestros pecados.","answer_gr":"Ἄφες ἡμῖν τὰς ἁμαρτίας ἡμῶν.","answer_voice":M},
    ],
    "verse":{"gr":"Αἰτεῖτε καὶ δοθήσεται ὑμῖν· ζητεῖτε καὶ εὑρήσετε· κρούετε καὶ ἀνοιγήσεται ὑμῖν.","voice":M,"ref_es":"En Mateo siete siete, Jesús dice:","explain_es":"Pidan y se les dará. Busquen y encontrarán. Llamen y se les abrirá. κρούετε es llamen, toquen la puerta. ἀνοιγήσεται es será abierto."},
    "closing_es":"Aprendiste mandamientos: αἰτέω pedir, διώκω perseguir, κρίνω juzgar, κρίσις juicio, ἁμαρτία pecado. Y frases del Sermón del Monte. Εἰρήνη σοι.",
}

L35 = {
    "num":35,"intro_es":"Μάθημα τριάκοντα πέντε. Lección treinta y cinco. Hoy aprenderás parábolas y comparaciones: el reino de Dios es semejante a. Escucha.",
    "dialogue":[(M,"Ὁμοία ἐστὶν ἡ βασιλεία τῶν οὐρανῶν κόκκῳ σινάπεως."),(M,"Ὃ μικρότερον μέν ἐστιν πάντων τῶν σπερμάτων, ὅταν δὲ αὐξηθῇ, μεῖζον τῶν λαχάνων ἐστίν.")],
    "context_es":"El reino de los cielos es semejante a un grano de mostaza. Es la más pequeña de todas las semillas, pero cuando crece, es la mayor de las hortalizas.",
    "vocab":[
        {"gr":"ὅμοιος","es":"semejante","note_es":"ὅμοιος significa semejante o parecido. ὁμοία ἐστίν, es semejante. Escucha."},
        {"gr":"παραβολή","es":"parábola","note_es":"παραβολή significa parábola o comparación. Viene de παρά, al lado, y βάλλω, lanzar. Poner al lado para comparar. Aparece cincuenta veces. Escucha."},
        {"gr":"κόκκος","es":"grano, semilla","note_es":"κόκκος significa grano o semilla. κόκκῳ σινάπεως, grano de mostaza. Escucha."},
        {"gr":"αὐξάνω","es":"crecer","note_es":"αὐξάνω significa crecer. αὐξηθῇ es crezca, subjuntivo pasivo. Escucha."},
        {"gr":"δένδρον","es":"árbol","note_es":"δένδρον significa árbol. Aparece veinticinco veces. Escucha."},
        {"gr":"ζύμη","es":"levadura","note_es":"ζύμη significa levadura. Jesús compara el reino con levadura que una mujer escondió en la masa. Escucha."},
    ],
    "phrases":[
        {"gr":"ὁμοία ἐστὶν ἡ βασιλεία τῶν οὐρανῶν","es":"el reino de los cielos es semejante a","prompt_es":"Di el reino de los cielos es semejante a. Esta frase introduce muchas parábolas."},
        {"gr":"ἐν παραβολαῖς","es":"en parábolas","prompt_es":"Di en parábolas."},
        {"gr":"κόκκῳ σινάπεως","es":"un grano de mostaza","prompt_es":"Di un grano de mostaza."},
        {"gr":"γίνεται δένδρον","es":"se convierte en árbol","prompt_es":"Di se convierte en árbol."},
        {"gr":"ἡ βασιλεία τῶν οὐρανῶν","es":"el reino de los cielos","prompt_es":"Di el reino de los cielos."},
        {"gr":"ἐλάλησεν αὐτοῖς ἐν παραβολαῖς","es":"les habló en parábolas","prompt_es":"Di les habló en parábolas."},
    ],
    "recon":[
        {"prompt_es":"Di el reino de los cielos es semejante a un grano de mostaza.","answer_gr":"Ὁμοία ἐστὶν ἡ βασιλεία τῶν οὐρανῶν κόκκῳ σινάπεως.","answer_voice":M},
        {"prompt_es":"Di se convierte en árbol.","answer_gr":"Γίνεται δένδρον.","answer_voice":M},
        {"prompt_es":"Di les habló en parábolas.","answer_gr":"Ἐλάλησεν αὐτοῖς ἐν παραβολαῖς.","answer_voice":M},
    ],
    "verse":{"gr":"Ὁμοία ἐστὶν ἡ βασιλεία τῶν οὐρανῶν κόκκῳ σινάπεως, ὃν λαβὼν ἄνθρωπος ἔσπειρεν ἐν τῷ ἀγρῷ αὐτοῦ.","voice":M,"ref_es":"En Mateo trece treinta y uno:","explain_es":"El reino de los cielos es semejante a un grano de mostaza que un hombre tomó y sembró en su campo. λαβών, habiendo tomado. ἔσπειρεν, sembró. ἀγρῷ, campo."},
    "closing_es":"Aprendiste parábolas: ὅμοιος semejante, παραβολή parábola, κόκκος grano, αὐξάνω crecer, δένδρον árbol, ζύμη levadura. Εἰρήνη σοι.",
}
