"""Lesson data 41-45: Oración/Templo, Viajes, Participios, Pronombres, Condicionales"""
M = "el-GR-Chirp3-HD-Charon"
F = "el-GR-Chirp3-HD-Kore"

L41 = {
    "num":41,"intro_es":"Μάθημα τεσσαράκοντα ἕν. Lección cuarenta y uno. Hoy aprenderás más sobre la oración y el templo. Escucha.",
    "dialogue":[(M,"Ὁ οἶκός μου οἶκος προσευχῆς κληθήσεται."),(F,"Κύριε, δίδαξον ἡμᾶς προσεύχεσθαι.")],
    "context_es":"Mi casa será llamada casa de oración. Señor, enséñanos a orar.",
    "vocab":[
        {"gr":"κηρύσσω","es":"predicar, proclamar","note_es":"κηρύσσω significa predicar o proclamar. Aparece sesenta y una veces. Escucha."},
        {"gr":"εὐαγγέλιον","es":"evangelio, buena noticia","note_es":"εὐαγγέλιον significa buena noticia o evangelio. Viene de εὐ, bueno, y ἄγγελος, mensaje. Aparece setenta y seis veces. Escucha."},
        {"gr":"βαπτίζω","es":"bautizar, sumergir","note_es":"βαπτίζω significa bautizar o sumergir. Aparece setenta y siete veces. Escucha."},
        {"gr":"ἱερεύς","es":"sacerdote","note_es":"ἱερεύς significa sacerdote. Aparece treinta y una veces. Escucha."},
        {"gr":"θυσία","es":"sacrificio","note_es":"θυσία significa sacrificio. Aparece veintiocho veces. Escucha."},
        {"gr":"λατρεύω","es":"servir, adorar","note_es":"λατρεύω significa servir o adorar a Dios. Aparece veintiuna veces. Escucha."},
    ],
    "phrases":[
        {"gr":"οἶκος προσευχῆς","es":"casa de oración","prompt_es":"Di casa de oración."},
        {"gr":"δίδαξον ἡμᾶς προσεύχεσθαι","es":"enséñanos a orar","prompt_es":"Di enséñanos a orar. δίδαξον es enseña, imperativo de διδάσκω."},
        {"gr":"κηρύσσων τὸ εὐαγγέλιον","es":"predicando el evangelio","prompt_es":"Di predicando el evangelio. κηρύσσων es un participio: predicando."},
        {"gr":"ἐβαπτίσθη ὑπὸ Ἰωάννου","es":"fue bautizado por Juan","prompt_es":"Di fue bautizado por Juan. ὑπό con genitivo indica por quién."},
        {"gr":"ὁ ἀρχιερεύς","es":"el sumo sacerdote","prompt_es":"Di el sumo sacerdote. ἀρχι significa principal."},
        {"gr":"λατρεύω τῷ θεῷ","es":"sirvo a Dios","prompt_es":"Di sirvo a Dios. Con dativo."},
    ],
    "recon":[
        {"prompt_es":"Di mi casa será llamada casa de oración.","answer_gr":"Ὁ οἶκός μου οἶκος προσευχῆς κληθήσεται.","answer_voice":M},
        {"prompt_es":"Di enséñanos a orar.","answer_gr":"Δίδαξον ἡμᾶς προσεύχεσθαι.","answer_voice":F},
        {"prompt_es":"Di predicando el evangelio.","answer_gr":"Κηρύσσων τὸ εὐαγγέλιον.","answer_voice":M},
    ],
    "verse":{"gr":"Κύριε, δίδαξον ἡμᾶς προσεύχεσθαι.","voice":M,"ref_es":"En Lucas once uno, los discípulos pidieron a Jesús:","explain_es":"Señor, enséñanos a orar. δίδαξον, enseña. ἡμᾶς, a nosotros. προσεύχεσθαι, a orar, infinitivo."},
    "closing_es":"Aprendiste sobre oración y templo: κηρύσσω predicar, εὐαγγέλιον evangelio, βαπτίζω bautizar, ἱερεύς sacerdote, θυσία sacrificio. Εἰρήνη σοι.",
}

L42 = {
    "num":42,"intro_es":"Μάθημα τεσσαράκοντα δύο. Lección cuarenta y dos. Hoy aprenderás participios: el que cree, el que viene, los que oyen. Escucha.",
    "dialogue":[(M,"Ὁ πιστεύων εἰς ἐμὲ ἔχει ζωὴν αἰώνιον."),(F,"Μακάριοι οἱ ἀκούοντες τὸν λόγον τοῦ θεοῦ.")],
    "context_es":"El que cree en mí tiene vida eterna. Bienaventurados los que oyen la palabra de Dios.",
    "vocab":[
        {"gr":"ὁ πιστεύων","es":"el que cree","note_es":"ὁ πιστεύων significa el que cree. Es un participio con artículo. El artículo más el participio crea una frase como el que hace algo. Escucha."},
        {"gr":"ὁ ἐρχόμενος","es":"el que viene","note_es":"ὁ ἐρχόμενος significa el que viene. Otro participio con artículo. Escucha."},
        {"gr":"οἱ ἀκούοντες","es":"los que oyen","note_es":"οἱ ἀκούοντες significa los que oyen. Participio plural. Escucha."},
        {"gr":"μακάριος","es":"bienaventurado, feliz","note_es":"μακάριος significa bienaventurado o feliz. Aparece cincuenta veces. Es la primera palabra de las bienaventuranzas. Escucha."},
        {"gr":"ὁ λέγων","es":"el que dice","note_es":"ὁ λέγων significa el que dice. Escucha."},
        {"gr":"ὁ ἔχων","es":"el que tiene","note_es":"ὁ ἔχων significa el que tiene. Escucha."},
    ],
    "phrases":[
        {"gr":"ὁ πιστεύων εἰς ἐμέ","es":"el que cree en mí","prompt_es":"Di el que cree en mí."},
        {"gr":"ὁ ἐρχόμενος ἐν ὀνόματι κυρίου","es":"el que viene en nombre del Señor","prompt_es":"Di el que viene en nombre del Señor."},
        {"gr":"μακάριοι οἱ πτωχοὶ τῷ πνεύματι","es":"bienaventurados los pobres en espíritu","prompt_es":"Di bienaventurados los pobres en espíritu."},
        {"gr":"ὁ ἔχων ὦτα ἀκουέτω","es":"el que tiene oídos, oiga","prompt_es":"Di el que tiene oídos, oiga. ὦτα es oídos."},
        {"gr":"οἱ ἀκούοντες τὸν λόγον","es":"los que oyen la palabra","prompt_es":"Di los que oyen la palabra."},
        {"gr":"μακάριοι οἱ εἰρηνοποιοί","es":"bienaventurados los pacificadores","prompt_es":"Di bienaventurados los pacificadores."},
    ],
    "recon":[
        {"prompt_es":"Di el que cree en mí tiene vida eterna.","answer_gr":"Ὁ πιστεύων εἰς ἐμὲ ἔχει ζωὴν αἰώνιον.","answer_voice":M},
        {"prompt_es":"Di bienaventurados los pobres en espíritu.","answer_gr":"Μακάριοι οἱ πτωχοὶ τῷ πνεύματι.","answer_voice":M},
        {"prompt_es":"Di el que tiene oídos, oiga.","answer_gr":"Ὁ ἔχων ὦτα ἀκουέτω.","answer_voice":M},
    ],
    "verse":{"gr":"Ὁ πιστεύων εἰς τὸν υἱὸν ἔχει ζωὴν αἰώνιον.","voice":M,"ref_es":"En Juan tres treinta y seis:","explain_es":"El que cree en el Hijo tiene vida eterna. ὁ πιστεύων, el que cree. υἱόν, Hijo. ζωὴν αἰώνιον, vida eterna."},
    "closing_es":"Aprendiste participios sustantivados: ὁ πιστεύων el que cree, ὁ ἐρχόμενος el que viene, οἱ ἀκούοντες los que oyen. Y μακάριος, bienaventurado. Εἰρήνη σοι.",
}

L43 = {
    "num":43,"intro_es":"Μάθημα τεσσαράκοντα τρία. Lección cuarenta y tres. Hoy aprenderás pronombres: a mí, a ti, a él, a nosotros, a ellos. Escucha.",
    "dialogue":[(F,"Ἀγαπᾷ με ὁ πατήρ."),(M,"Κἀγὼ ἀγαπῶ ὑμᾶς."),(F,"Μένετε ἐν ἐμοί, κἀγὼ ἐν ὑμῖν.")],
    "context_es":"El Padre me ama. Y yo los amo a ustedes. Permanezcan en mí, y yo en ustedes.",
    "vocab":[
        {"gr":"με","es":"me, a mí (acusativo)","note_es":"με significa me o a mí. Es el acusativo de ἐγώ. ἀγαπᾷ με, me ama. Escucha."},
        {"gr":"σε","es":"te, a ti (acusativo)","note_es":"σε significa te o a ti. Es el acusativo de σύ. Escucha."},
        {"gr":"αὐτόν","es":"lo, a él (acusativo)","note_es":"αὐτόν significa lo o a él. αὐτήν es a ella. αὐτό es a ello. Escucha."},
        {"gr":"ἡμᾶς","es":"nos, a nosotros","note_es":"ἡμᾶς significa nos o a nosotros. Acusativo de ἡμεῖς. Escucha."},
        {"gr":"ὑμᾶς","es":"los, a ustedes","note_es":"ὑμᾶς significa los o a ustedes. Acusativo de ὑμεῖς. Escucha."},
        {"gr":"αὐτούς","es":"los, a ellos","note_es":"αὐτούς significa los o a ellos. Acusativo plural de αὐτός. Escucha."},
    ],
    "phrases":[
        {"gr":"ἀγαπᾷ με","es":"me ama","prompt_es":"Di me ama."},
        {"gr":"ἀγαπῶ ὑμᾶς","es":"los amo a ustedes","prompt_es":"Di los amo a ustedes."},
        {"gr":"μένετε ἐν ἐμοί","es":"permanezcan en mí","prompt_es":"Di permanezcan en mí. ἐμοί es en mí, dativo."},
        {"gr":"ἀπέστειλέν με","es":"me envió","prompt_es":"Di me envió. ἀπέστειλεν es envió, de ἀποστέλλω."},
        {"gr":"γινώσκω αὐτόν","es":"lo conozco","prompt_es":"Di lo conozco."},
        {"gr":"ἠγάπησεν ἡμᾶς","es":"nos amó","prompt_es":"Di nos amó."},
        {"gr":"κἀγώ","es":"y yo, yo también","prompt_es":"Di y yo. κἀγώ es la contracción de καὶ ἐγώ."},
    ],
    "recon":[
        {"prompt_es":"Di el Padre me ama.","answer_gr":"Ἀγαπᾷ με ὁ πατήρ.","answer_voice":M},
        {"prompt_es":"Di y yo los amo a ustedes.","answer_gr":"Κἀγὼ ἀγαπῶ ὑμᾶς.","answer_voice":M},
        {"prompt_es":"Di permanezcan en mí y yo en ustedes.","answer_gr":"Μένετε ἐν ἐμοί, κἀγὼ ἐν ὑμῖν.","answer_voice":M},
        {"prompt_es":"Di me envió.","answer_gr":"Ἀπέστειλέν με.","answer_voice":M},
    ],
    "verse":{"gr":"Μείνατε ἐν ἐμοί, κἀγὼ ἐν ὑμῖν.","voice":M,"ref_es":"En Juan quince cuatro, Jesús dice:","explain_es":"Permanezcan en mí, y yo en ustedes. μείνατε, permanezcan. ἐν ἐμοί, en mí. κἀγώ, y yo. ἐν ὑμῖν, en ustedes."},
    "closing_es":"Aprendiste pronombres acusativos: με a mí, σε a ti, αὐτόν a él, ἡμᾶς a nosotros, ὑμᾶς a ustedes, αὐτούς a ellos. Εἰρήνη σοι.",
}

L44 = {
    "num":44,"intro_es":"Μάθημα τεσσαράκοντα τέσσαρα. Lección cuarenta y cuatro. Hoy aprenderás conectores lógicos: porque, entonces, pero, para que. Escucha.",
    "dialogue":[(M,"Οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον, ὥστε τὸν υἱὸν τὸν μονογενῆ ἔδωκεν, ἵνα πᾶς ὁ πιστεύων εἰς αὐτὸν μὴ ἀπόληται ἀλλ᾽ ἔχῃ ζωὴν αἰώνιον.")],
    "context_es":"Porque de tal manera amó Dios al mundo, que dio a su Hijo unigénito, para que todo el que cree en él no perezca sino tenga vida eterna. Juan tres dieciséis.",
    "vocab":[
        {"gr":"γάρ","es":"porque, pues (postpositiva)","note_es":"γάρ significa porque o pues. Es postpositiva, nunca va primero. Aparece mil treinta y nueve veces. Escucha."},
        {"gr":"ἵνα","es":"para que (+ subjuntivo)","note_es":"ἵνα significa para que. Se usa con subjuntivo para expresar propósito. Aparece seiscientas sesenta y dos veces. Escucha."},
        {"gr":"ὥστε","es":"de modo que, así que","note_es":"ὥστε significa de modo que o así que. Indica resultado. Aparece ochenta y tres veces. Escucha."},
        {"gr":"διότι","es":"porque, por lo cual","note_es":"διότι significa porque. Viene de διά y ὅτι. Escucha."},
        {"gr":"κόσμος","es":"mundo","note_es":"κόσμος significa mundo. Aparece ciento ochenta y seis veces. ὁ κόσμος, el mundo. Escucha."},
        {"gr":"μονογενής","es":"unigénito, único","note_es":"μονογενής significa unigénito o único. Viene de μόνος, solo, y γένος, nacimiento. Escucha."},
    ],
    "phrases":[
        {"gr":"οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον","es":"porque de tal manera amó Dios al mundo","prompt_es":"Di porque de tal manera amó Dios al mundo. οὕτως significa de tal manera."},
        {"gr":"ἵνα πᾶς ὁ πιστεύων","es":"para que todo el que cree","prompt_es":"Di para que todo el que cree."},
        {"gr":"ἔχῃ ζωὴν αἰώνιον","es":"tenga vida eterna","prompt_es":"Di tenga vida eterna. ἔχῃ es tenga, subjuntivo."},
        {"gr":"τὸν υἱὸν τὸν μονογενῆ","es":"al Hijo unigénito","prompt_es":"Di al Hijo unigénito."},
        {"gr":"ὁ κόσμος","es":"el mundo","prompt_es":"Di el mundo."},
        {"gr":"ἐν τῷ κόσμῳ","es":"en el mundo","prompt_es":"Di en el mundo."},
    ],
    "recon":[
        {"prompt_es":"Recita Juan tres dieciséis. Empieza: porque de tal manera amó Dios al mundo.","answer_gr":"Οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον.","answer_voice":M},
        {"prompt_es":"Continúa: que dio a su Hijo unigénito.","answer_gr":"Ὥστε τὸν υἱὸν τὸν μονογενῆ ἔδωκεν.","answer_voice":M},
        {"prompt_es":"Continúa: para que todo el que cree en él tenga vida eterna.","answer_gr":"Ἵνα πᾶς ὁ πιστεύων εἰς αὐτὸν ἔχῃ ζωὴν αἰώνιον.","answer_voice":M},
    ],
    "verse":{"gr":"Οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον, ὥστε τὸν υἱὸν τὸν μονογενῆ ἔδωκεν, ἵνα πᾶς ὁ πιστεύων εἰς αὐτὸν μὴ ἀπόληται ἀλλ᾽ ἔχῃ ζωὴν αἰώνιον.","voice":M,"ref_es":"Juan tres dieciséis, el versículo más famoso del Nuevo Testamento:","explain_es":"Porque de tal manera amó Dios al mundo, que dio a su Hijo unigénito, para que todo el que cree en él no perezca sino tenga vida eterna. Ya conoces casi cada palabra."},
    "closing_es":"Aprendiste conectores: γάρ porque, ἵνα para que, ὥστε de modo que. Y aprendiste Juan tres dieciséis completo. Εἰρήνη σοι.",
}

L45 = {
    "num":45,"intro_es":"Μάθημα τεσσαράκοντα πέντε. Lección cuarenta y cinco. Mitad del segundo nivel. Hoy repasaremos con la historia de la mujer samaritana. Escucha.",
    "dialogue":[(M,"Δός μοι πεῖν."),(F,"Πῶς σὺ Ἰουδαῖος ὢν παρ᾽ ἐμοῦ πεῖν αἰτεῖς;"),(M,"Εἰ ᾔδεις τὴν δωρεὰν τοῦ θεοῦ, σὺ ἂν ᾔτησας αὐτόν.")],
    "context_es":"Dame de beber. ¿Cómo tú, siendo judío, me pides de beber? Si conocieras el don de Dios, tú le habrías pedido.",
    "vocab":[
        {"gr":"πίνω","es":"beber","note_es":"Ya conoces πίνω, beber. πεῖν es el infinitivo aoristo: beber. δός μοι πεῖν, dame de beber. Escucha."},
        {"gr":"δωρεά","es":"don, regalo","note_es":"δωρεά significa don o regalo gratuito. ἡ δωρεὰ τοῦ θεοῦ, el don de Dios. Escucha."},
        {"gr":"πηγή","es":"fuente, manantial","note_es":"πηγή significa fuente o manantial. πηγὴ ὕδατος, fuente de agua. Escucha."},
        {"gr":"ἀληθινός","es":"verdadero, genuino","note_es":"ἀληθινός significa verdadero o genuino. Diferente de ἀληθής. ἀληθινός enfatiza lo genuino versus lo falso. Escucha."},
        {"gr":"προσκυνέω","es":"adorar","note_es":"προσκυνέω significa adorar o postrarse. Viene de πρός, hacia, y κυνέω, besar. Besar hacia la deidad. Aparece sesenta veces. Escucha."},
        {"gr":"πνεῦμα καὶ ἀλήθεια","es":"espíritu y verdad","note_es":"Los verdaderos adoradores adorarán al Padre en espíritu y verdad. ἐν πνεύματι καὶ ἀληθείᾳ. Escucha."},
    ],
    "phrases":[
        {"gr":"δός μοι πεῖν","es":"dame de beber","prompt_es":"Di dame de beber."},
        {"gr":"ἡ δωρεὰ τοῦ θεοῦ","es":"el don de Dios","prompt_es":"Di el don de Dios."},
        {"gr":"πηγὴ ὕδατος ζῶντος","es":"fuente de agua viva","prompt_es":"Di fuente de agua viva. ζῶντος es viva, participio de ζάω."},
        {"gr":"ἐν πνεύματι καὶ ἀληθείᾳ","es":"en espíritu y verdad","prompt_es":"Di en espíritu y verdad."},
        {"gr":"οἱ ἀληθινοὶ προσκυνηταί","es":"los verdaderos adoradores","prompt_es":"Di los verdaderos adoradores."},
        {"gr":"ἐγώ εἰμι, ὁ λαλῶν σοι","es":"yo soy, el que te habla","prompt_es":"Di yo soy, el que te habla. Jesús se revela a la samaritana."},
    ],
    "recon":[
        {"other_gr":"Δός μοι πεῖν.","other_voice":M,"prompt_es":"Jesús te pide agua. Pregúntale cómo, siendo judío, te pide de beber.","answer_gr":"Πῶς σὺ παρ᾽ ἐμοῦ πεῖν αἰτεῖς;","answer_voice":F},
        {"prompt_es":"Di fuente de agua viva.","answer_gr":"Πηγὴ ὕδατος ζῶντος.","answer_voice":F},
        {"prompt_es":"Di los verdaderos adoradores adorarán en espíritu y verdad.","answer_gr":"Οἱ ἀληθινοὶ προσκυνηταὶ προσκυνήσουσιν ἐν πνεύματι καὶ ἀληθείᾳ.","answer_voice":M},
    ],
    "verse":{"gr":"Ἐγώ εἰμι, ὁ λαλῶν σοι.","voice":M,"ref_es":"En Juan cuatro veintiséis, Jesús le dijo a la samaritana:","explain_es":"Yo soy, el que te habla. ἐγώ εἰμι, yo soy. ὁ λαλῶν, el que habla, participio. σοι, a ti."},
    "closing_es":"Repasaste con la historia de la samaritana. Aprendiste δωρεά don, πηγή fuente, ἀληθινός verdadero, προσκυνέω adorar. Has completado cuarenta y cinco lecciones. Εἰρήνη σοι.",
}
