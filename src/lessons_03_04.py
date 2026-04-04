"""Lessons 3-4: Origin + Understanding"""
import sys; sys.path.insert(0, ".")
from lesson_engine import *

def get_speed(n):
    return 0.75 if n <= 7 else (0.85 if n <= 15 else 1.0)

def lesson_3():
    s = get_speed(3)
    S = []
    S += [es("Μάθημα τρία. Lección tres. Hoy aprenderás a decir de dónde eres y a preguntar a otros. Escucha esta conversación."), P(800)]
    S += [gr("Χαῖρε! Πόθεν εἶ σύ;", voice=M, speed=s), P(400)]
    S += [gr("ἐγώ εἰμι ἀπὸ Γαλιλαίας. Καὶ σύ;", voice=F, speed=s), P(400)]
    S += [gr("ἀπὸ Ἰερουσαλήμ.", voice=M, speed=s), P(1000)]
    # REVIEW
    S += [es("Repasemos. ¿Cómo preguntarías cuál es tu nombre?"), P(5000), gr("Τί ὄνομά σοι;", speed=s), P(500)]
    S += [es("¿Cómo dirías mi nombre es María?"), P(5000), gr("Τὸ ὄνομά μου Μαρία", speed=s), P(800)]
    # TEACH πόθεν εἶ
    S += [es("El hombre preguntó πόθεν εἶ σύ. Significa ¿de dónde eres tú? Esta misma pregunta aparece en el evangelio de Juan, cuando Pilato le pregunta a Jesús. Escucha."), P(300)]
    S += [gr("πόθεν", speed=s), P(3000)]
    S += [es("πόθεν significa de dónde."), P(300), gr("πόθεν", speed=s), P(3000)]
    S += [es("εἶ ya lo conoces. Significa eres. πόθεν εἶ. ¿De dónde eres?"), P(300)]
    S += [gr("Πόθεν εἶ;", speed=s), P(4000), gr("Πόθεν εἶ;", speed=s), P(800)]
    # TEACH ἀπό
    S += [es("Para responder, usas ἀπό, que significa de o desde. ἀπὸ Γαλιλαίας. De Galilea."), P(300)]
    S += [gr("ἀπό", speed=s), P(2500), gr("ἀπό", speed=s), P(500)]
    S += [gr("ἀπὸ Γαλιλαίας", speed=s), P(3500), gr("ἀπὸ Γαλιλαίας", speed=s), P(600)]
    S += [gr("ἀπὸ Ἰερουσαλήμ", speed=s), P(3500), gr("ἀπὸ Ἰερουσαλήμ", speed=s), P(800)]
    # TEACH αὐτός ἐστιν
    S += [es("Para decir él es, se dice αὐτός ἐστιν. αὐτός significa él. ἐστιν significa es."), P(300)]
    S += [gr("αὐτός ἐστιν", speed=s), P(3500), gr("αὐτός ἐστιν", speed=s), P(600)]
    S += [es("Para decir ella es, se dice αὐτή ἐστιν."), P(300)]
    S += [gr("αὐτή ἐστιν", speed=s), P(3500), gr("αὐτή ἐστιν", speed=s), P(800)]
    # TEACH ἐκ
    S += [es("Hay otra palabra para decir de. ἐκ significa de dentro de, o de un grupo. ἀπό es para lugares. ἐκ es para grupos o familias."), P(300)]
    S += [gr("ἐκ", speed=s), P(2500)]
    S += [es("Por ejemplo, ἐκ τοῦ οὐρανοῦ significa del cielo. Pero ἀπὸ Ἰερουσαλήμ, de Jerusalén."), P(800)]
    # GIR
    S += [es("¿Cómo preguntarías de dónde eres?"), P(4500), gr("Πόθεν εἶ;", speed=s), P(500)]
    S += [es("¿Cómo dirías de Galilea?"), P(4000), gr("ἀπὸ Γαλιλαίας", speed=s), P(500)]
    S += [es("¿Cómo dirías él es?"), P(3500), gr("αὐτός ἐστιν", speed=s), P(500)]
    S += [es("¿Cómo dirías yo soy de Jerusalén?"), P(5000), gr("ἐγώ εἰμι ἀπὸ Ἰερουσαλήμ", speed=s), P(500)]
    S += [es("¿Cómo dirías hola?"), P(3500), gr("Χαῖρε", speed=s), P(500)]
    S += [es("¿Cómo dirías paz a ti?"), P(4000), gr("Εἰρήνη σοι", speed=s), P(800)]
    # DIALOGUE PRACTICE
    S += [es("Practica. Alguien te pregunta de dónde eres. Responde que eres de Galilea."), P(500)]
    S += [gr("Χαῖρε! Πόθεν εἶ;", voice=M, speed=s), P(500)]
    S += [es("Responde."), P(5000), gr("ἐγώ εἰμι ἀπὸ Γαλιλαίας", voice=F, speed=s), P(500)]
    S += [es("Ahora pregúntale de dónde es él."), P(5000), gr("Καὶ σύ; Πόθεν εἶ;", voice=F, speed=s), P(400)]
    S += [gr("ἀπὸ Ἰερουσαλήμ.", voice=M, speed=s), P(800)]
    # GIR 2
    S += [es("¿Cómo dirías ella es de Galilea?"), P(5000), gr("αὐτή ἐστιν ἀπὸ Γαλιλαίας", speed=s), P(500)]
    S += [es("¿Cómo preguntarías cuál es tu nombre?"), P(5000), gr("Τί ὄνομά σοι;", speed=s), P(500)]
    S += [es("¿Cómo dirías de dónde eres?"), P(4500), gr("Πόθεν εἶ;", speed=s), P(800)]
    # VERSE
    S += [es("Escucha. En el evangelio de Juan, capítulo diecinueve, versículo nueve, Pilato le pregunta a Jesús:"), P(500)]
    S += [gr("Πόθεν εἶ σύ;", voice=M, speed=s), P(600)]
    S += [es("¿De dónde eres tú? Jesús no le respondió. Ya conoces cada palabra de esta pregunta."), P(800)]
    S += [es("En la siguiente lección aprenderás a decir que entiendes o no entiendes algo. Εἰρήνη σοι."), P(500)]
    return S

def lesson_4():
    s = get_speed(4)
    S = []
    S += [es("Μάθημα τέσσαρα. Lección cuatro. Hoy aprenderás a decir que entiendes, que no entiendes, y a pedir que alguien repita. Escucha."), P(800)]
    S += [gr("Γινώσκεις ἑλληνιστί;", voice=F, speed=s), P(400)]
    S += [gr("ναί, γινώσκω ὀλίγον.", voice=M, speed=s), P(400)]
    S += [gr("Λέγω σοι ὅτι...", voice=F, speed=s), P(400)]
    S += [gr("Οὐκ ἀκούω. Λέγε πάλιν.", voice=M, speed=s), P(1000)]
    # REVIEW
    S += [es("Repasemos. ¿Cómo dirías de dónde eres?"), P(4500), gr("Πόθεν εἶ;", speed=s), P(500)]
    S += [es("¿Cómo dirías yo soy de Jerusalén?"), P(5000), gr("ἐγώ εἰμι ἀπὸ Ἰερουσαλήμ", speed=s), P(500)]
    S += [es("¿Cómo dirías mi nombre es Simón?"), P(5000), gr("Τὸ ὄνομά μου Σίμων", speed=s), P(800)]
    # TEACH γινώσκω
    S += [es("La mujer preguntó γινώσκεις ἑλληνιστί. Significa ¿sabes griego? γινώσκω significa saber o conocer. Escucha."), P(300)]
    S += [gr("γινώσκω", speed=s), P(3500), gr("γινώσκω", speed=s), P(600)]
    S += [es("γινώσκεις es la forma para tú. ¿Sabes? ¿Conoces?"), P(300)]
    S += [gr("γινώσκεις", speed=s), P(3500), gr("γινώσκεις", speed=s), P(800)]
    # TEACH ἀκούω
    S += [es("El hombre dijo οὐκ ἀκούω. No oigo. ἀκούω significa oír o escuchar."), P(300)]
    S += [gr("ἀκούω", speed=s), P(3500), gr("ἀκούω", speed=s), P(600)]
    S += [es("οὐκ ἀκούω. No oigo. Recuerda, οὐ es no. Antes de vocal se dice οὐκ."), P(300)]
    S += [gr("οὐκ ἀκούω", speed=s), P(3500), gr("οὐκ ἀκούω", speed=s), P(800)]
    # TEACH λέγω
    S += [es("λέγω significa decir o hablar. Es una de las palabras más frecuentes del Nuevo Testamento."), P(300)]
    S += [gr("λέγω", speed=s), P(3000), gr("λέγω", speed=s), P(500)]
    S += [es("λέγω σοι significa te digo. Jesús usa esta frase constantemente."), P(300)]
    S += [gr("λέγω σοι", speed=s), P(3500), gr("λέγω σοι", speed=s), P(800)]
    # TEACH πάλιν
    S += [es("El hombre pidió λέγε πάλιν. Significa di otra vez. πάλιν significa otra vez o de nuevo."), P(300)]
    S += [gr("πάλιν", speed=s), P(3000), gr("πάλιν", speed=s), P(500)]
    S += [gr("λέγε πάλιν", speed=s), P(3500), gr("λέγε πάλιν", speed=s), P(800)]
    # TEACH λόγος
    S += [es("λόγος significa palabra. Es una de las palabras más importantes del Nuevo Testamento. En el principio era el λόγος."), P(300)]
    S += [gr("λόγος", speed=s), P(3000), gr("λόγος", speed=s), P(800)]
    # TEACH δέ
    S += [es("Aprende la palabra δέ. Significa pero o y. Es especial porque nunca va al principio de la frase. Siempre va en segundo lugar. Por ejemplo: ἐγὼ δέ, pero yo."), P(300)]
    S += [gr("δέ", speed=s), P(2500)]
    S += [gr("ἐγὼ δὲ λέγω ὑμῖν", speed=s), P(4000)]
    S += [es("Pero yo les digo. Jesús dice esto muchas veces en el Sermón del Monte."), P(800)]
    # TEACH ἀλλά
    S += [es("Otra palabra para pero es ἀλλά. Esta sí va al principio. ἀλλά es un pero más fuerte, como sino."), P(300)]
    S += [gr("ἀλλά", speed=s), P(3000), gr("ἀλλά", speed=s), P(800)]
    # GIR
    S += [es("¿Cómo dirías yo sé o yo conozco?"), P(4000), gr("γινώσκω", speed=s), P(500)]
    S += [es("¿Cómo dirías no oigo?"), P(4000), gr("οὐκ ἀκούω", speed=s), P(500)]
    S += [es("¿Cómo dirías di otra vez?"), P(4000), gr("λέγε πάλιν", speed=s), P(500)]
    S += [es("¿Cómo dirías te digo?"), P(4000), gr("λέγω σοι", speed=s), P(500)]
    S += [es("¿Cómo dirías paz a ti?"), P(4000), gr("Εἰρήνη σοι", speed=s), P(500)]
    S += [es("¿Cómo dirías de dónde eres?"), P(4500), gr("Πόθεν εἶ;", speed=s), P(800)]
    # DIALOGUE
    S += [es("Practica. Alguien te habla muy rápido. Dile que no oíste y que repita."), P(500)]
    S += [gr("Λέγω σοι ὅτι ὁ κύριος ἔρχεται σήμερον.", voice=F, speed=s), P(500)]
    S += [es("Dile que no oíste. Di otra vez."), P(5000)]
    S += [gr("Οὐκ ἀκούω. Λέγε πάλιν.", voice=M, speed=s), P(800)]
    # FINAL GIR
    S += [es("¿Cómo dirías palabra?"), P(3500), gr("λόγος", speed=s), P(400)]
    S += [es("¿Cómo dirías pero, la forma que va en segundo lugar?"), P(4000), gr("δέ", speed=s), P(400)]
    S += [es("¿Cómo dirías pero, la forma fuerte?"), P(4000), gr("ἀλλά", speed=s), P(400)]
    S += [es("¿Cómo dirías yo sé?"), P(3500), gr("γινώσκω", speed=s), P(400)]
    S += [es("¿Cómo dirías cuál es tu nombre?"), P(5000), gr("Τί ὄνομά σοι;", speed=s), P(800)]
    # VERSE
    S += [es("Escucha. En el evangelio de Mateo, capítulo cinco, versículo treinta y siete, Jesús dice:"), P(500)]
    S += [gr("Ἔστω δὲ ὁ λόγος ὑμῶν ναὶ ναί, οὐ οὔ.", voice=M, speed=s), P(600)]
    S += [es("Que su palabra sea sí sí, no no. Reconoces λόγος, palabra. δέ, pero. ναί, sí. οὐ, no."), P(800)]
    S += [es("En la siguiente lección aprenderás el artículo y a señalar cosas. Εἰρήνη σοι."), P(500)]
    return S

if __name__ == "__main__":
    print("Generating lessons 3-4...")
    build_lesson(lesson_3(), 3)
    build_lesson(lesson_4(), 4)
