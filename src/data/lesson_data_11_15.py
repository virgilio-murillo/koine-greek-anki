"""Lesson data 11-15: Directions, Family, Giving, Wanting/Needing, Review"""
from src.tts import M, F

L11 = {
    "num":11,"intro_es":"Μάθημα ἕνδεκα. Lección once. Hoy aprenderás lugares: el templo, la sinagoga, la ciudad, y a preguntar dónde están. Escucha.",
    "dialogue":[(M,"Ποῦ ἐστιν τὸ ἱερόν;"),(F,"Ἐκεῖ ἐστιν, ἐν τῇ πόλει."),(M,"Θέλω πορεύεσθαι πρὸς τὸ ἱερόν."),(F,"Ἔρχου μετ᾽ ἐμοῦ.")],
    "context_es":"El hombre pregunta dónde está el templo. La mujer dice que está allí, en la ciudad. Él quiere ir al templo. Ella le dice ven conmigo.",
    "vocab":[
        {"gr":"ἱερόν","es":"templo","note_es":"ἱερόν significa templo. Aparece setenta y una veces en el Nuevo Testamento. τὸ ἱερόν, el templo. Es neutro. Escucha."},
        {"gr":"συναγωγή","es":"sinagoga","note_es":"συναγωγή significa sinagoga o lugar de reunión. Viene de σύν, juntos, y ἄγω, conducir. ἡ συναγωγή, la sinagoga. Es femenino. Escucha."},
        {"gr":"πόλις","es":"ciudad","note_es":"πόλις significa ciudad. Aparece ciento sesenta y dos veces. ἡ πόλις, la ciudad. Escucha."},
        {"gr":"θάλασσα","es":"mar","note_es":"θάλασσα significa mar. ἡ θάλασσα, el mar. En griego es femenino. Escucha."},
        {"gr":"ὄρος","es":"monte, montaña","note_es":"ὄρος significa monte o montaña. τὸ ὄρος, el monte. Es neutro. Escucha."},
        {"gr":"πρός","es":"hacia, con","note_es":"πρός significa hacia o con. πρὸς τὸ ἱερόν, hacia el templo. Escucha."},
        {"gr":"μετά","es":"con, después","note_es":"μετά significa con cuando va con genitivo, y después cuando va con acusativo. μετ᾽ ἐμοῦ, conmigo. Escucha."},
    ],
    "phrases":[
        {"gr":"ποῦ ἐστιν τὸ ἱερόν;","es":"¿dónde está el templo?","prompt_es":"Pregunta dónde está el templo."},
        {"gr":"ἐν τῇ πόλει","es":"en la ciudad","prompt_es":"Di en la ciudad."},
        {"gr":"πρὸς τὸ ἱερόν","es":"hacia el templo","prompt_es":"Di hacia el templo."},
        {"gr":"πρὸς τὴν θάλασσαν","es":"hacia el mar","prompt_es":"Di hacia el mar."},
        {"gr":"ἐν τῷ ὄρει","es":"en el monte","prompt_es":"Di en el monte."},
        {"gr":"ποῦ ἐστιν ἡ συναγωγή;","es":"¿dónde está la sinagoga?","prompt_es":"Pregunta dónde está la sinagoga."},
        {"gr":"πορεύομαι μετὰ σοῦ","es":"voy contigo","prompt_es":"Di voy contigo. σοῦ es de ti, con genitivo."},
    ],
    "recon":[
        {"other_gr":"Ποῦ πορεύῃ;","other_voice":F,"prompt_es":"Te preguntan a dónde vas. Di que vas hacia el templo.","answer_gr":"Πορεύομαι πρὸς τὸ ἱερόν.","answer_voice":M},
        {"prompt_es":"Pregúntale dónde está la sinagoga.","answer_gr":"Ποῦ ἐστιν ἡ συναγωγή;","answer_voice":M},
        {"other_gr":"Ἐν τῇ πόλει.","other_voice":F,"prompt_es":"Dile ven conmigo.","answer_gr":"Ἔρχου μετ᾽ ἐμοῦ.","answer_voice":M},
        {"other_gr":"ναί, ἔρχομαι.","other_voice":F,"prompt_es":"Di paz a ti.","answer_gr":"Εἰρήνη σοι.","answer_voice":M},
    ],
    "verse":{"gr":"Εἰσῆλθεν εἰς τὴν συναγωγήν.","voice":M,"ref_es":"En Lucas cuatro dieciséis, Jesús entró en la sinagoga de Nazaret:","explain_es":"Entró en la sinagoga. εἰσῆλθεν significa entró. Viene de εἰς, hacia adentro, y ἔρχομαι, ir. Reconoces τὴν συναγωγήν, la sinagoga."},
    "closing_es":"Aprendiste lugares: ἱερόν templo, συναγωγή sinagoga, πόλις ciudad, θάλασσα mar, ὄρος monte. Y las preposiciones πρός hacia y μετά con. En la siguiente lección aprenderás la familia. Εἰρήνη σοι.",
}

L12 = {
    "num":12,"intro_es":"Μάθημα δώδεκα. Lección doce. Hoy aprenderás palabras de la familia: padre, madre, hijo, hermano. Escucha.",
    "dialogue":[(M,"Ποῦ ἐστιν ὁ πατήρ σου;"),(F,"Ὁ πατήρ μου ἐν τῷ οἴκῳ ἐστίν."),(M,"Ἔχεις ἀδελφούς;"),(F,"ναί, ἔχω δύο ἀδελφοὺς καὶ μίαν ἀδελφήν.")],
    "context_es":"El hombre pregunta dónde está su padre. Ella dice que está en la casa. Él pregunta si tiene hermanos. Ella tiene dos hermanos y una hermana.",
    "vocab":[
        {"gr":"πατήρ","es":"padre","note_es":"πατήρ significa padre. Aparece cuatrocientas trece veces. ὁ πατήρ, el padre. Para decir padre como vocativo, se dice Πάτερ. Escucha."},
        {"gr":"μήτηρ","es":"madre","note_es":"μήτηρ significa madre. ἡ μήτηρ, la madre. Escucha."},
        {"gr":"υἱός","es":"hijo","note_es":"υἱός significa hijo. Aparece trescientas setenta y cinco veces. ὁ υἱός, el hijo. Escucha."},
        {"gr":"θυγάτηρ","es":"hija","note_es":"θυγάτηρ significa hija. ἡ θυγάτηρ, la hija. Escucha."},
        {"gr":"ἀδελφός","es":"hermano","note_es":"ἀδελφός significa hermano. Viene de ἀ, mismo, y δελφύς, vientre. Literalmente, del mismo vientre. Aparece trescientas cuarenta y dos veces. Escucha."},
        {"gr":"ἀδελφή","es":"hermana","note_es":"ἀδελφή significa hermana. La misma raíz que ἀδελφός. Escucha."},
        {"gr":"δοῦλος","es":"esclavo, siervo","note_es":"δοῦλος significa esclavo o siervo. En koiné NO significa trabajador como en griego moderno. ὁ δοῦλος, el siervo. Escucha."},
    ],
    "phrases":[
        {"gr":"ὁ πατήρ μου","es":"mi padre","prompt_es":"Di mi padre."},
        {"gr":"ἡ μήτηρ σου","es":"tu madre","prompt_es":"Di tu madre."},
        {"gr":"ὁ υἱὸς αὐτοῦ","es":"su hijo (de él)","prompt_es":"Di su hijo. αὐτοῦ significa de él."},
        {"gr":"ἡ ἀδελφή μου","es":"mi hermana","prompt_es":"Di mi hermana."},
        {"gr":"Πάτερ","es":"¡Padre! (vocativo)","prompt_es":"Llama a tu padre. Se dice Πάτερ, con la terminación cambiada."},
        {"gr":"ἔχω δύο ἀδελφούς","es":"tengo dos hermanos","prompt_es":"Di tengo dos hermanos."},
        {"gr":"ὁ πατήρ ἡμῶν","es":"nuestro padre","prompt_es":"Di nuestro padre. ἡμῶν significa nuestro o de nosotros."},
    ],
    "recon":[
        {"other_gr":"Ποῦ ἐστιν ὁ πατήρ σου;","other_voice":M,"prompt_es":"Te preguntan dónde está tu padre. Di que está en la casa.","answer_gr":"Ὁ πατήρ μου ἐν τῷ οἴκῳ ἐστίν.","answer_voice":F},
        {"other_gr":"Ἔχεις ἀδελφούς;","other_voice":M,"prompt_es":"Te preguntan si tienes hermanos. Di que tienes dos hermanos y una hermana.","answer_gr":"ναί, ἔχω δύο ἀδελφοὺς καὶ μίαν ἀδελφήν.","answer_voice":F},
        {"prompt_es":"Pregúntale dónde está su madre.","answer_gr":"Ποῦ ἐστιν ἡ μήτηρ σου;","answer_voice":F},
    ],
    "verse":{"gr":"Πάτερ, ἥμαρτον εἰς τὸν οὐρανὸν καὶ ἐνώπιόν σου.","voice":M,"ref_es":"En Lucas quince veintiuno, el hijo pródigo regresó a su padre y le dijo:","explain_es":"Padre, he pecado contra el cielo y delante de ti. Reconoces Πάτερ, padre en vocativo. εἰς, hacia. οὐρανόν, cielo. σου, de ti."},
    "closing_es":"Aprendiste la familia: πατήρ padre, μήτηρ madre, υἱός hijo, θυγάτηρ hija, ἀδελφός hermano, ἀδελφή hermana, δοῦλος siervo. En la siguiente lección aprenderás a dar y recibir. Εἰρήνη σοι.",
}

L13 = {
    "num":13,"intro_es":"Μάθημα δεκατρία. Lección trece. Hoy aprenderás a dar, recibir, y llevar. Escucha.",
    "dialogue":[(M,"Λάβετε, φάγετε· τοῦτό ἐστιν τὸ σῶμά μου."),(F,"Κύριε, δὸς ἡμῖν τοῦτον τὸν ἄρτον πάντοτε.")],
    "context_es":"Escuchaste dos frases bíblicas famosas. La primera es de la última cena: tomen, coman, esto es mi cuerpo. La segunda es del evangelio de Juan: Señor, danos siempre este pan.",
    "vocab":[
        {"gr":"δίδωμι","es":"dar","note_es":"δίδωμι significa dar. Aparece cuatrocientas quince veces. Es un verbo irregular. La orden es δός, da. Escucha."},
        {"gr":"λαμβάνω","es":"tomar, recibir","note_es":"λαμβάνω significa tomar o recibir. La orden es λάβε, toma. En plural, λάβετε, tomen. Escucha."},
        {"gr":"φέρω","es":"llevar, traer","note_es":"φέρω significa llevar o traer. Escucha."},
        {"gr":"ἡμεῖς","es":"nosotros","note_es":"ἡμεῖς significa nosotros. ἡμῖν es a nosotros, en dativo. ἡμῶν es de nosotros. Escucha."},
        {"gr":"ὑμεῖς","es":"ustedes","note_es":"ὑμεῖς significa ustedes. ὑμῖν es a ustedes. ὑμῶν es de ustedes. Escucha."},
        {"gr":"αὐτῷ","es":"a él (dativo)","note_es":"αὐτῷ significa a él. Es el dativo de αὐτός. δίδωμι αὐτῷ, le doy a él. Escucha."},
    ],
    "phrases":[
        {"gr":"δίδωμί σοι","es":"te doy","prompt_es":"Di te doy."},
        {"gr":"δὸς ἡμῖν","es":"danos","prompt_es":"Di danos. δός es la orden de dar. ἡμῖν es a nosotros."},
        {"gr":"λάβε","es":"toma","prompt_es":"Di toma."},
        {"gr":"Λάβετε, φάγετε","es":"tomen, coman","prompt_es":"Di tomen, coman. Como Jesús en la última cena."},
        {"gr":"φέρε ὧδε","es":"trae aquí","prompt_es":"Di trae aquí."},
        {"gr":"δίδωμι αὐτῷ ἄρτον","es":"le doy pan","prompt_es":"Di le doy pan a él."},
        {"gr":"λαμβάνω ἀπὸ σοῦ","es":"recibo de ti","prompt_es":"Di recibo de ti."},
    ],
    "recon":[
        {"other_gr":"Δός μοι ὕδωρ.","other_voice":M,"prompt_es":"Te piden agua. Di toma.","answer_gr":"Ἰδού, λάβε.","answer_voice":F},
        {"prompt_es":"Pídele pan. Di dame pan. δός μοι.","answer_gr":"Δός μοι ἄρτον.","answer_voice":F},
        {"other_gr":"Ἰδού, λάβε.","other_voice":M,"prompt_es":"Da gracias.","answer_gr":"Εὐχαριστῶ.","answer_voice":F},
        {"prompt_es":"Di tomen, coman, como Jesús.","answer_gr":"Λάβετε, φάγετε.","answer_voice":F},
    ],
    "verse":{"gr":"Λάβετε, φάγετε· τοῦτό ἐστιν τὸ σῶμά μου.","voice":M,"ref_es":"En Mateo veintiséis veintiséis, Jesús tomó el pan y dijo:","explain_es":"Tomen, coman. Esto es mi cuerpo. Reconoces λάβετε, tomen. τοῦτο, esto. ἐστιν, es. μου, mi. σῶμα significa cuerpo."},
    "closing_es":"Aprendiste a dar y recibir: δίδωμι dar, λαμβάνω tomar, φέρω llevar. Y los pronombres ἡμεῖς nosotros y ὑμεῖς ustedes. En la siguiente lección aprenderás querer, poder, y deber. Εἰρήνη σοι.",
}

L14 = {
    "num":14,"intro_es":"Μάθημα δεκατέσσαρα. Lección catorce. Hoy aprenderás a decir quiero, puedo, y debo. Escucha.",
    "dialogue":[(M,"Τί θέλεις;"),(F,"Θέλω ἰδεῖν τὸν διδάσκαλον."),(M,"Οὐ δύνασαι νῦν. Δεῖ σε μεῖναι ὧδε.")],
    "context_es":"El hombre pregunta qué quiere ella. Ella quiere ver al maestro. Él dice que no puede ahora. Debe quedarse aquí.",
    "vocab":[
        {"gr":"δύναμαι","es":"poder","note_es":"δύναμαι significa poder. Es deponente. δύνασαι es puedes. δύναται es puede. οὐ δύναμαι, no puedo. Escucha."},
        {"gr":"δεῖ","es":"es necesario, se debe","note_es":"δεῖ significa es necesario o se debe. Es impersonal. δεῖ με πορεύεσθαι, debo ir. Literalmente, es necesario que yo vaya. Escucha."},
        {"gr":"ζητέω","es":"buscar","note_es":"ζητέω significa buscar. Aparece ciento diecisiete veces. Escucha."},
        {"gr":"εὑρίσκω","es":"encontrar","note_es":"εὑρίσκω significa encontrar. Escucha."},
        {"gr":"νῦν","es":"ahora","note_es":"νῦν significa ahora. Escucha."},
        {"gr":"ὅς","es":"quien, que (relativo)","note_es":"ὅς significa quien o que. Es el pronombre relativo. ὁ ἄνθρωπος ὃς ἔρχεται, el hombre que viene. Escucha."},
    ],
    "phrases":[
        {"gr":"οὐ δύναμαι","es":"no puedo","prompt_es":"Di no puedo."},
        {"gr":"δύνασαι;","es":"¿puedes?","prompt_es":"Pregunta puedes."},
        {"gr":"δεῖ με πορεύεσθαι","es":"debo ir","prompt_es":"Di debo ir. Literalmente, es necesario que yo vaya."},
        {"gr":"ζητῶ τὸν κύριον","es":"busco al Señor","prompt_es":"Di busco al Señor. κύριος significa Señor."},
        {"gr":"ζητεῖτε καὶ εὑρήσετε","es":"busquen y encontrarán","prompt_es":"Di busquen y encontrarán. Como Jesús dijo en Mateo siete siete."},
        {"gr":"θέλω ἰδεῖν","es":"quiero ver","prompt_es":"Di quiero ver. ἰδεῖν es el infinitivo de ver."},
        {"gr":"νῦν δέ","es":"pero ahora","prompt_es":"Di pero ahora. Recuerda, δέ va en segundo lugar."},
    ],
    "recon":[
        {"other_gr":"Τί θέλεις;","other_voice":M,"prompt_es":"Te preguntan qué quieres. Di que quieres ver al maestro.","answer_gr":"Θέλω ἰδεῖν τὸν διδάσκαλον.","answer_voice":F},
        {"other_gr":"Οὐ δύνασαι νῦν.","other_voice":M,"prompt_es":"Te dicen que no puedes ahora. Pregunta por qué. διὰ τί significa por qué.","answer_gr":"Διὰ τί;","answer_voice":F},
        {"prompt_es":"Di debo ir.","answer_gr":"Δεῖ με πορεύεσθαι.","answer_voice":F},
        {"prompt_es":"Di busquen y encontrarán.","answer_gr":"Ζητεῖτε καὶ εὑρήσετε.","answer_voice":F},
    ],
    "verse":{"gr":"Ζητεῖτε καὶ εὑρήσετε.","voice":M,"ref_es":"En Mateo siete siete, Jesús dice:","explain_es":"Busquen y encontrarán. ζητεῖτε es busquen, imperativo plural. εὑρήσετε es encontrarán, futuro. καί, y."},
    "closing_es":"Aprendiste δύναμαι poder, δεῖ deber, ζητέω buscar, εὑρίσκω encontrar, νῦν ahora, y ὅς quien. En la siguiente lección haremos un repaso del primer bloque. Εἰρήνη σοι.",
}

L15 = {
    "num":15,"intro_es":"Μάθημα δεκαπέντε. Lección quince. Hoy repasaremos todo lo aprendido con una escena en el mercado de Jerusalén. También aprenderás a comprar y vender. Escucha.",
    "dialogue":[(M,"Χαῖρε! Θέλω ἀγοράσαι ἄρτον."),(F,"Πόσους ἄρτους θέλεις;"),(M,"Πέντε. Πόσου;"),(F,"Δύο ἀργυρίων."),(M,"Ἔχω. Λάβε."),(F,"Εἰρήνη σοι.")],
    "context_es":"Un hombre quiere comprar pan en el mercado. Pregunta cuántos, el precio, paga, y se despiden con paz.",
    "vocab":[
        {"gr":"ἀγοράζω","es":"comprar","note_es":"ἀγοράζω significa comprar. Viene de ἀγορά, mercado o plaza. Escucha."},
        {"gr":"πωλέω","es":"vender","note_es":"πωλέω significa vender. Escucha."},
        {"gr":"ἀγορά","es":"mercado, plaza","note_es":"ἀγορά significa mercado o plaza pública. Escucha."},
        {"gr":"ἀργύριον","es":"plata, dinero","note_es":"ἀργύριον significa plata o dinero. Escucha."},
    ],
    "phrases":[
        {"gr":"θέλω ἀγοράσαι ἄρτον","es":"quiero comprar pan","prompt_es":"Di quiero comprar pan. ἀγοράσαι es el infinitivo de comprar."},
        {"gr":"πόσους ἄρτους θέλεις;","es":"¿cuántos panes quieres?","prompt_es":"Pregunta cuántos panes quieres. πόσους significa cuántos."},
        {"gr":"πωλεῖς ἰχθύας;","es":"¿vendes peces?","prompt_es":"Pregunta si vende peces."},
        {"gr":"ἐν τῇ ἀγορᾷ","es":"en el mercado","prompt_es":"Di en el mercado."},
        {"gr":"δὸς ἡμῖν ἄρτον","es":"danos pan","prompt_es":"Di danos pan."},
        {"gr":"οὐκ ἔχω ἀργύριον","es":"no tengo dinero","prompt_es":"Di no tengo dinero."},
    ],
    "recon":[
        {"prompt_es":"Saluda al vendedor y di que quieres comprar pan.","answer_gr":"Χαῖρε! Θέλω ἀγοράσαι ἄρτον.","answer_voice":M},
        {"other_gr":"Πόσους ἄρτους θέλεις;","other_voice":F,"prompt_es":"Te pregunta cuántos. Di cinco.","answer_gr":"Πέντε.","answer_voice":M},
        {"other_gr":"Δύο ἀργυρίων.","other_voice":F,"prompt_es":"Cuesta dos monedas de plata. Di tengo, toma.","answer_gr":"Ἔχω. Λάβε.","answer_voice":M},
        {"prompt_es":"Pregúntale si vende peces también.","answer_gr":"Πωλεῖς ἰχθύας;","answer_voice":M},
        {"other_gr":"ναί.","other_voice":F,"prompt_es":"Di quiero dos peces.","answer_gr":"Θέλω δύο ἰχθύας.","answer_voice":M},
        {"prompt_es":"Despídete.","answer_gr":"Εἰρήνη σοι.","answer_voice":M},
    ],
    "verse":{"gr":"Μὴ ποιεῖτε τὸν οἶκον τοῦ πατρός μου οἶκον ἐμπορίου.","voice":M,"ref_es":"En Juan dos dieciséis, Jesús entró al templo y dijo a los vendedores:","explain_es":"No hagan de la casa de mi padre una casa de comercio. Reconoces μή, no. ποιεῖτε, hagan. οἶκον, casa. πατρός μου, de mi padre. ἐμπορίου significa de comercio."},
    "closing_es":"Felicidades. Has completado quince lecciones, la mitad del primer nivel. Ya puedes saludar, presentarte, comprar en el mercado, hablar de tu familia, y moverte por la ciudad. Todo en griego koiné auténtico. Εἰρήνη σοι.",
}
