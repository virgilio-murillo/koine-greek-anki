"""Lessons 1-2: Greetings + Names"""
import sys; sys.path.insert(0, ".")
from lesson_engine import *

def get_speed(lesson_num):
    return 0.75 if lesson_num <= 7 else (0.85 if lesson_num <= 15 else 1.0)

def lesson_1():
    s = get_speed(1)
    S = []  # segments
    # INTRO
    S += [es("Μάθημα ἕν. Lección uno de griego koiné. Imagina que caminas por un sendero polvoriento hacia Jerusalén. Es el siglo primero. Te encuentras con dos personas que se saludan. Escucha."), P(800)]
    # DIALOGUE
    S += [gr("Χαῖρε!", voice=M, speed=s), P(400)]
    S += [gr("Εἰρήνη σοι.", voice=F, speed=s), P(400)]
    S += [gr("Εἰρήνη σοι. Πόθεν εἶ;", voice=M, speed=s), P(400)]
    S += [gr("ἐγώ εἰμι ἀπὸ Γαλιλαίας.", voice=F, speed=s), P(1000)]
    S += [es("No te preocupes si no entendiste todo. Al final de esta lección podrás saludar y responder en griego koiné."), P(800)]
    # TEACH χαῖρε
    S += [es("El hombre dijo χαῖρε. Significa alégrate, o simplemente, hola. Es el saludo más común en el Nuevo Testamento. Escucha y repite."), P(300)]
    S += [gr("Χαῖρε", speed=s), P(3500), gr("Χαῖρε", speed=s), P(800)]
    # TEACH εἰρήνη σοι
    S += [es("La mujer respondió εἰρήνη σοι. Significa paz a ti. Escucha la primera palabra. Εἰρήνη. Paz."), P(300)]
    S += [gr("Εἰρήνη", speed=s), P(3500), gr("Εἰρήνη", speed=s), P(600)]
    S += [es("σοι significa a ti. Ahora la frase completa. Εἰρήνη σοι. Paz a ti."), P(300)]
    S += [gr("Εἰρήνη σοι", speed=s), P(4000), gr("Εἰρήνη σοι", speed=s), P(800)]
    # TEACH ναί / οὐ
    S += [es("Aprende a decir sí y no. Sí en griego es ναί."), P(300)]
    S += [gr("ναί", speed=s), P(3000), gr("ναί", speed=s), P(600)]
    S += [es("No en griego es οὐ. Antes de vocal se dice οὐκ."), P(300)]
    S += [gr("οὐ", speed=s), P(3000), gr("οὐ", speed=s), P(600)]
    # GIR 1
    S += [es("¿Cómo dirías hola?"), P(4000), gr("Χαῖρε", speed=s), P(500)]
    S += [es("¿Cómo dirías paz a ti?"), P(4000), gr("Εἰρήνη σοι", speed=s), P(500)]
    S += [es("¿Cómo dirías sí?"), P(3000), gr("ναί", speed=s), P(500)]
    S += [es("¿Cómo dirías no?"), P(3000), gr("οὐ", speed=s), P(800)]
    # TEACH ἐγώ εἰμι
    S += [es("Ahora aprende a decir yo soy. Escucha."), P(300)]
    S += [gr("ἐγώ εἰμι", speed=s), P(3500)]
    S += [es("ἐγώ significa yo. εἰμι significa soy. ἐγώ εἰμι. Yo soy. Repite."), P(300)]
    S += [gr("ἐγώ εἰμι", speed=s), P(4000), gr("ἐγώ εἰμι", speed=s), P(800)]
    # TEACH σύ εἶ
    S += [es("Para decir tú eres, se dice σὺ εἶ. σύ es tú. εἶ es eres."), P(300)]
    S += [gr("σὺ εἶ", speed=s), P(3500), gr("σὺ εἶ", speed=s), P(800)]
    # GIR 2
    S += [es("¿Cómo dirías yo soy?"), P(4000), gr("ἐγώ εἰμι", speed=s), P(500)]
    S += [es("¿Cómo dirías tú eres?"), P(4000), gr("σὺ εἶ", speed=s), P(500)]
    S += [es("¿Cómo dirías paz a ti?"), P(4000), gr("Εἰρήνη σοι", speed=s), P(500)]
    S += [es("¿Cómo dirías hola?"), P(3500), gr("Χαῖρε", speed=s), P(800)]
    # MINI DIALOGUE
    S += [es("Alguien te saluda en el camino. Respóndele."), P(500)]
    S += [gr("Χαῖρε!", voice=M, speed=s), P(500)]
    S += [es("Dile paz a ti."), P(4000), gr("Εἰρήνη σοι", speed=s), P(800)]
    # VERSE
    S += [es("Escucha este versículo. En el evangelio de Lucas, capítulo veinticuatro, versículo treinta y seis, Jesús se apareció a sus discípulos y les dijo:"), P(500)]
    S += [gr("Εἰρήνη ὑμῖν.", voice=M, speed=s), P(600)]
    S += [es("Paz a ustedes. Ya conoces εἰρήνη, paz. ὑμῖν significa a ustedes. σοι es a ti, ὑμῖν es a ustedes."), P(800)]
    # FINAL GIR
    S += [es("Repaso final. Hola."), P(3500), gr("Χαῖρε", speed=s), P(400)]
    S += [es("Paz a ti."), P(3500), gr("Εἰρήνη σοι", speed=s), P(400)]
    S += [es("Yo soy."), P(3500), gr("ἐγώ εἰμι", speed=s), P(400)]
    S += [es("Tú eres."), P(3500), gr("σὺ εἶ", speed=s), P(400)]
    S += [es("Sí."), P(2500), gr("ναί", speed=s), P(400)]
    S += [es("No."), P(2500), gr("οὐ", speed=s), P(800)]
    # CLOSE
    S += [es("Excelente. Aprendiste seis expresiones en griego koiné. En la siguiente lección aprenderás a preguntar y decir tu nombre. Εἰρήνη σοι."), P(500)]
    return S

def lesson_2():
    s = get_speed(2)
    S = []
    # INTRO
    S += [es("Μάθημα δύο. Lección dos. Sigues caminando hacia Jerusalén. Un hombre te pregunta tu nombre. Escucha."), P(800)]
    S += [gr("Χαῖρε! Τί ὄνομά σοι;", voice=M, speed=s), P(400)]
    S += [gr("Τὸ ὄνομά μου Μαρία. Καὶ σοί;", voice=F, speed=s), P(400)]
    S += [gr("Σίμων.", voice=M, speed=s), P(1000)]
    # REVIEW from L1
    S += [es("Antes de aprender palabras nuevas, repasemos. ¿Cómo dirías paz a ti?"), P(4000), gr("Εἰρήνη σοι", speed=s), P(500)]
    S += [es("¿Cómo dirías yo soy?"), P(4000), gr("ἐγώ εἰμι", speed=s), P(800)]
    # TEACH τί ὄνομά σοι
    S += [es("El hombre preguntó τί ὄνομά σοι. Significa ¿cuál es tu nombre? Literalmente: ¿qué nombre a ti? Escucha parte por parte."), P(500)]
    S += [es("τί significa qué o cuál."), P(300), gr("τί", speed=s), P(3000), gr("τί", speed=s), P(600)]
    S += [es("ὄνομα significa nombre."), P(300), gr("ὄνομα", speed=s), P(3000), gr("ὄνομα", speed=s), P(600)]
    S += [es("σοι ya lo conoces. Significa a ti. Ahora la pregunta completa."), P(300)]
    S += [gr("Τί ὄνομά σοι;", speed=s), P(4500), gr("Τί ὄνομά σοι;", speed=s), P(800)]
    # TEACH τὸ ὄνομά μου
    S += [es("La mujer respondió τὸ ὄνομά μου Μαρία. Mi nombre es María. μου significa mi o de mí."), P(300)]
    S += [gr("μου", speed=s), P(2500), gr("μου", speed=s), P(500)]
    S += [es("τὸ ὄνομά μου. Mi nombre. Repite."), P(300)]
    S += [gr("τὸ ὄνομά μου", speed=s), P(4000), gr("τὸ ὄνομά μου", speed=s), P(800)]
    # TEACH καί
    S += [es("La mujer también dijo καὶ σοί, que significa y a ti, o sea, ¿y tú? καί significa y. Es la palabra más común del Nuevo Testamento."), P(300)]
    S += [gr("καί", speed=s), P(2500), gr("καί", speed=s), P(500)]
    S += [gr("καὶ σοί;", speed=s), P(3500), gr("καὶ σοί;", speed=s), P(800)]
    # TEACH σου vs σοι
    S += [es("Nota importante. σοι significa a ti. σου significa de ti o tu. Son diferentes. σοι con iota es a ti. σου con ípsilon es tu."), P(300)]
    S += [gr("σοι", speed=s), P(2000), es("a ti"), P(300)]
    S += [gr("σου", speed=s), P(2000), es("de ti, tu"), P(800)]
    # GIR 1
    S += [es("¿Cómo preguntarías cuál es tu nombre?"), P(5000), gr("Τί ὄνομά σοι;", speed=s), P(500)]
    S += [es("¿Cómo dirías mi nombre es Simón?"), P(5000), gr("Τὸ ὄνομά μου Σίμων", speed=s), P(500)]
    S += [es("¿Cómo dirías hola?"), P(3500), gr("Χαῖρε", speed=s), P(500)]
    S += [es("¿Cómo dirías y tú?"), P(3500), gr("καὶ σοί;", speed=s), P(800)]
    # PRACTICE DIALOGUE
    S += [es("Practica. Alguien te pregunta tu nombre. Responde con tu nombre y pregúntale el suyo."), P(500)]
    S += [gr("Χαῖρε! Τί ὄνομά σοι;", voice=M, speed=s), P(500)]
    S += [es("Di tu nombre. Mi nombre es..."), P(5000)]
    S += [gr("Τὸ ὄνομά μου Μαρία.", voice=F, speed=s), P(500)]
    S += [es("Ahora pregúntale su nombre."), P(5000)]
    S += [gr("Τί ὄνομά σοι;", voice=F, speed=s), P(400)]
    S += [gr("Σίμων.", voice=M, speed=s), P(800)]
    # GIR 2 (longer intervals)
    S += [es("¿Cómo dirías yo soy?"), P(4000), gr("ἐγώ εἰμι", speed=s), P(500)]
    S += [es("¿Cómo dirías paz a ti?"), P(4000), gr("Εἰρήνη σοι", speed=s), P(500)]
    S += [es("¿Cómo preguntarías cuál es tu nombre?"), P(5000), gr("Τί ὄνομά σοι;", speed=s), P(500)]
    S += [es("¿Cómo dirías y?"), P(3000), gr("καί", speed=s), P(800)]
    # VERSE
    S += [es("En el evangelio de Marcos, capítulo cinco, versículo nueve, Jesús le preguntó al endemoniado:"), P(500)]
    S += [gr("Τί ὄνομά σοι;", voice=M, speed=s), P(500)]
    S += [es("¿Cuál es tu nombre? Y él respondió:"), P(400)]
    S += [gr("Λεγιὼν ὄνομά μοι, ὅτι πολλοί ἐσμεν.", voice=M, speed=s), P(500)]
    S += [es("Legión es mi nombre, porque somos muchos. Reconoces ὄνομα, nombre, y μοι, que es otra forma de decir a mí."), P(800)]
    # CLOSE
    S += [es("En esta lección aprendiste a preguntar y decir tu nombre. Τί ὄνομά σοι, cuál es tu nombre. Τὸ ὄνομά μου, mi nombre es. Y la palabra καί, y. En la siguiente lección aprenderás a decir de dónde eres. Εἰρήνη σοι."), P(500)]
    return S

if __name__ == "__main__":
    print("Generating lessons 1-2...")
    build_lesson(lesson_1(), 1)
    build_lesson(lesson_2(), 2)
