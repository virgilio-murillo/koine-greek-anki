"""Lesson data 9-10"""
M = "el-GR-Chirp3-HD-Charon"
F = "el-GR-Chirp3-HD-Kore"

L9 = {
    "num": 9, "intro_es": "Μάθημα ἐννέα. Lección nueve. Hoy aprenderás los números del uno al diez en griego koiné. Escucha.",
    "dialogue": [(M,"Πόσους ἄρτους ἔχετε;"),(F,"Πέντε ἄρτους καὶ δύο ἰχθύας.")],
    "context_es": "El hombre preguntó cuántos panes tienen. La mujer respondió cinco panes y dos peces. Es la escena de la alimentación de los cinco mil.",
    "vocab": [
        {"gr":"εἷς","es":"uno","note_es":"Uno se dice εἷς para masculino, μία para femenino, ἕν para neutro. εἷς ἄρτος, un pan. Escucha."},
        {"gr":"δύο","es":"dos","note_es":"Dos se dice δύο. No cambia con el género. Escucha."},
        {"gr":"τρεῖς","es":"tres","note_es":"Tres se dice τρεῖς. Escucha."},
        {"gr":"τέσσαρες","es":"cuatro","note_es":"Cuatro se dice τέσσαρες. Escucha."},
        {"gr":"πέντε","es":"cinco","note_es":"Cinco se dice πέντε. Escucha."},
        {"gr":"ἕξ","es":"seis","note_es":"Seis se dice ἕξ. Escucha."},
        {"gr":"ἑπτά","es":"siete","note_es":"Siete se dice ἑπτά. Un número muy importante en la Biblia. Escucha."},
        {"gr":"ὀκτώ","es":"ocho","note_es":"Ocho se dice ὀκτώ. Escucha."},
        {"gr":"ἐννέα","es":"nueve","note_es":"Nueve se dice ἐννέα. Escucha."},
        {"gr":"δέκα","es":"diez","note_es":"Diez se dice δέκα. Escucha."},
    ],
    "phrases": [
        {"gr":"εἷς ἄρτος","es":"un pan","prompt_es":"Di un pan."},
        {"gr":"δύο ἰχθύες","es":"dos peces","prompt_es":"Di dos peces. El plural de ἰχθύς es ἰχθύες."},
        {"gr":"πέντε ἄρτοι","es":"cinco panes","prompt_es":"Di cinco panes. El plural de ἄρτος es ἄρτοι."},
        {"gr":"πέντε ἄρτοι καὶ δύο ἰχθύες","es":"cinco panes y dos peces","prompt_es":"Di cinco panes y dos peces. Exactamente lo que tenían los discípulos."},
        {"gr":"τρεῖς ἡμέραι","es":"tres días","prompt_es":"Di tres días. ἡμέραι es el plural de ἡμέρα, día."},
        {"gr":"ἑπτά","es":"siete","prompt_es":"Di siete."},
        {"gr":"δέκα","es":"diez","prompt_es":"Di diez."},
        {"gr":"εἷς","es":"uno","prompt_es":"Di uno."},
    ],
    "recon": [
        {"other_gr":"Πόσους ἄρτους ἔχεις;","other_voice":M,"prompt_es":"Te preguntan cuántos panes tienes. Di que tienes cinco.","answer_gr":"ἔχω πέντε ἄρτους.","answer_voice":F},
        {"prompt_es":"Pregúntale cuántos peces tiene. πόσους ἰχθύας.","answer_gr":"Πόσους ἰχθύας ἔχεις;","answer_voice":F},
        {"other_gr":"δύο ἰχθύας.","other_voice":M,"prompt_es":"Di cinco panes y dos peces.","answer_gr":"πέντε ἄρτοι καὶ δύο ἰχθύες.","answer_voice":F},
    ],
    "verse": {"gr":"Οὐκ ἔχομεν ὧδε εἰ μὴ πέντε ἄρτους καὶ δύο ἰχθύας.","voice":M,"ref_es":"En Mateo catorce diecisiete, los discípulos le dijeron a Jesús:","explain_es":"No tenemos aquí sino cinco panes y dos peces. Reconoces οὐκ ἔχομεν, no tenemos. ὧδε, aquí. πέντε, cinco. ἄρτους, panes. δύο, dos. ἰχθύας, peces."},
    "closing_es": "Aprendiste los números del uno al diez: εἷς, δύο, τρεῖς, τέσσαρες, πέντε, ἕξ, ἑπτά, ὀκτώ, ἐννέα, δέκα. En la siguiente lección aprenderás el verbo tener. Εἰρήνη σοι.",
}

L10 = {
    "num": 10, "intro_es": "Μάθημα δέκα. Lección diez. Hoy aprenderás a decir tengo, no tengo, y a hablar de necesidades. Escucha.",
    "dialogue": [(F,"Ἔχεις ἄρτον;"),(M,"Οὐκ ἔχω. Χρείαν ἔχω ἄρτου."),(F,"Ἰδού, λάβε τοῦτον.")],
    "context_es": "La mujer preguntó si tiene pan. El hombre no tiene. Tiene necesidad de pan. Ella le dice mira, toma este.",
    "vocab": [
        {"gr":"ἔχω","es":"tengo","note_es":"ἔχω significa tengo. Es uno de los verbos más frecuentes del Nuevo Testamento, más de setecientas veces. ἔχεις es tienes. ἔχει es tiene. ἔχομεν es tenemos. Escucha."},
        {"gr":"πολύς","es":"mucho","note_es":"πολύς significa mucho. πολλά es la forma neutra plural: muchas cosas. ἔχω πολλά, tengo mucho. Escucha."},
        {"gr":"ὀλίγος","es":"poco","note_es":"ὀλίγος significa poco. ἔχω ὀλίγον, tengo poco. Escucha."},
        {"gr":"οὐδείς","es":"nadie, nada","note_es":"οὐδείς significa nadie. οὐδέν es la forma neutra: nada. οὐκ ἔχω οὐδέν, no tengo nada. Escucha."},
        {"gr":"χρεία","es":"necesidad","note_es":"χρεία significa necesidad. χρείαν ἔχω significa tengo necesidad. χρείαν ἔχω ἄρτου, tengo necesidad de pan. Nota: ἄρτου con ου al final es el genitivo, significa de pan. Escucha."},
        {"gr":"τοῦτον","es":"este (acusativo)","note_es":"τοῦτον significa este, cuando es objeto directo. λάβε τοῦτον, toma este. Escucha."},
    ],
    "phrases": [
        {"gr":"ἔχω","es":"tengo","prompt_es":"Di tengo."},
        {"gr":"οὐκ ἔχω","es":"no tengo","prompt_es":"Di no tengo."},
        {"gr":"ἔχεις ἄρτον;","es":"¿tienes pan?","prompt_es":"Pregunta tienes pan."},
        {"gr":"ἔχω πολλά","es":"tengo mucho","prompt_es":"Di tengo mucho."},
        {"gr":"ἔχω ὀλίγον","es":"tengo poco","prompt_es":"Di tengo poco."},
        {"gr":"οὐκ ἔχω οὐδέν","es":"no tengo nada","prompt_es":"Di no tengo nada."},
        {"gr":"χρείαν ἔχω ἄρτου","es":"tengo necesidad de pan","prompt_es":"Di tengo necesidad de pan."},
        {"gr":"χρείαν ἔχω ὕδατος","es":"tengo necesidad de agua","prompt_es":"Di tengo necesidad de agua. ὕδατος es el genitivo de ὕδωρ."},
        {"gr":"ἔχομεν πέντε ἄρτους","es":"tenemos cinco panes","prompt_es":"Di tenemos cinco panes."},
    ],
    "recon": [
        {"other_gr":"Ἔχεις ἄρτον;","other_voice":F,"prompt_es":"Te preguntan si tienes pan. Di que no tienes.","answer_gr":"Οὐκ ἔχω.","answer_voice":M},
        {"prompt_es":"Di que tienes necesidad de pan.","answer_gr":"Χρείαν ἔχω ἄρτου.","answer_voice":M},
        {"other_gr":"Ἰδού, λάβε τοῦτον.","other_voice":F,"prompt_es":"Te dan pan. Da gracias.","answer_gr":"Εὐχαριστῶ.","answer_voice":M},
        {"prompt_es":"Pregúntale si tiene agua.","answer_gr":"Ἔχεις ὕδωρ;","answer_voice":M},
        {"other_gr":"ναί, ἔχω.","other_voice":F,"prompt_es":"Di quiero agua.","answer_gr":"θέλω ὕδωρ.","answer_voice":M},
    ],
    "verse": {"gr":"Ὕπαγε, ὅσα ἔχεις πώλησον καὶ δὸς τοῖς πτωχοῖς.","voice":M,"ref_es":"En Marcos diez veintiuno, Jesús le dijo al joven rico:","explain_es":"Ve, vende todo lo que tienes y dalo a los pobres. Reconoces ἔχεις, tienes. καί, y. τοῖς πτωχοῖς significa a los pobres, en dativo."},
    "closing_es": "Felicidades. Has completado diez lecciones. Ya puedes saludar, presentarte, pedir comida, usar números, y hablar de lo que tienes y necesitas. Todo en el idioma del Nuevo Testamento. Εἰρήνη σοι.",
}
