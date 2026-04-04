"""Lessons 5-6: Articles/Demonstratives + Review Dialogue"""
import sys; sys.path.insert(0, ".")
from lesson_engine import *

def get_speed(n):
    return 0.75 if n <= 7 else (0.85 if n <= 15 else 1.0)

def lesson_5():
    s = get_speed(5)
    S = []
    S += [es("Μάθημα πέντε. Lección cinco. Hoy aprenderás a decir el, la, lo, y a señalar personas y cosas. Escucha."), P(800)]
    S += [gr("Βλέπεις τὸν ἄνθρωπον ἐκεῖνον;", voice=F, speed=s), P(400)]
    S += [gr("ναί. Τίς ἐστιν;", voice=M, speed=s), P(400)]
    S += [gr("Οὗτός ἐστιν ὁ διδάσκαλος.", voice=F, speed=s), P(1000)]
    # REVIEW
    S += [es("Repasemos. ¿Cómo dirías no oigo, di otra vez?"), P(5000), gr("Οὐκ ἀκούω. Λέγε πάλιν.", speed=s), P(500)]
    S += [es("¿Cómo dirías yo sé?"), P(3500), gr("γινώσκω", speed=s), P(800)]
    # TEACH ὁ ἡ τό
    S += [es("En griego, el artículo cambia según el género. ὁ es el, para masculino. ἡ es la, para femenino. τό es lo, para neutro."), P(300)]
    S += [gr("ὁ", speed=s), P(2000), es("el"), P(300)]
    S += [gr("ἡ", speed=s), P(2000), es("la"), P(300)]
    S += [gr("τό", speed=s), P(2000), es("lo"), P(600)]
    S += [es("ὁ ἄνθρωπος. El hombre. ἄνθρωπος significa persona o hombre."), P(300)]
    S += [gr("ὁ ἄνθρωπος", speed=s), P(3500), gr("ὁ ἄνθρωπος", speed=s), P(600)]
    S += [es("ἡ γυνή. La mujer."), P(300)]
    S += [gr("ἡ γυνή", speed=s), P(3000), gr("ἡ γυνή", speed=s), P(600)]
    S += [es("τὸ τέκνον. El niño. τέκνον es neutro."), P(300)]
    S += [gr("τὸ τέκνον", speed=s), P(3000), gr("τὸ τέκνον", speed=s), P(800)]
    # TEACH οὗτος / ἐκεῖνος
    S += [es("Para decir este se dice οὗτος. Para decir aquel se dice ἐκεῖνος."), P(300)]
    S += [gr("οὗτος", speed=s), P(3000), es("este"), P(300)]
    S += [gr("ἐκεῖνος", speed=s), P(3000), es("aquel"), P(600)]
    S += [es("οὗτος ὁ ἄνθρωπος. Este hombre."), P(300)]
    S += [gr("οὗτος ὁ ἄνθρωπος", speed=s), P(4000), gr("οὗτος ὁ ἄνθρωπος", speed=s), P(800)]
    # TEACH ὅτι
    S += [es("ὅτι es una palabra muy importante. Significa que o porque. Aparece más de mil veces en el Nuevo Testamento."), P(300)]
    S += [gr("ὅτι", speed=s), P(2500)]
    S += [es("γινώσκω ὅτι. Sé que."), P(300)]
    S += [gr("γινώσκω ὅτι", speed=s), P(3500), gr("γινώσκω ὅτι", speed=s), P(800)]
    # TEACH οὖν
    S += [es("οὖν significa entonces o por lo tanto. Como δέ, nunca va al principio. Siempre en segundo lugar."), P(300)]
    S += [gr("οὖν", speed=s), P(2500), gr("οὖν", speed=s), P(800)]
    # GIR
    S += [es("¿Cómo dirías el hombre?"), P(3500), gr("ὁ ἄνθρωπος", speed=s), P(500)]
    S += [es("¿Cómo dirías la mujer?"), P(3500), gr("ἡ γυνή", speed=s), P(500)]
    S += [es("¿Cómo dirías este hombre?"), P(4000), gr("οὗτος ὁ ἄνθρωπος", speed=s), P(500)]
    S += [es("¿Cómo dirías sé que?"), P(4000), gr("γινώσκω ὅτι", speed=s), P(500)]
    S += [es("¿Cómo dirías te digo que?"), P(4500), gr("λέγω σοι ὅτι", speed=s), P(500)]
    S += [es("¿Cómo dirías de dónde eres?"), P(4500), gr("Πόθεν εἶ;", speed=s), P(800)]
    # TEACH ἰδού
    S += [es("Una palabra muy expresiva: ἰδού. Significa ¡mira! o ¡he aquí! Aparece doscientas veces en el Nuevo Testamento."), P(300)]
    S += [gr("ἰδού", speed=s), P(3000), gr("ἰδού", speed=s), P(600)]
    S += [es("ἰδοὺ ὁ ἄνθρωπος. He aquí el hombre. Pilato dijo esto señalando a Jesús."), P(300)]
    S += [gr("ἰδοὺ ὁ ἄνθρωπος", speed=s), P(4000), gr("ἰδοὺ ὁ ἄνθρωπος", speed=s), P(800)]
    # FINAL GIR
    S += [es("Repaso. El."), P(2500), gr("ὁ", speed=s), P(300)]
    S += [es("La."), P(2500), gr("ἡ", speed=s), P(300)]
    S += [es("Este."), P(3000), gr("οὗτος", speed=s), P(300)]
    S += [es("Aquel."), P(3000), gr("ἐκεῖνος", speed=s), P(300)]
    S += [es("Que o porque."), P(3000), gr("ὅτι", speed=s), P(300)]
    S += [es("Entonces."), P(3000), gr("οὖν", speed=s), P(300)]
    S += [es("¡Mira!"), P(3000), gr("ἰδού", speed=s), P(800)]
    # VERSE
    S += [es("Escucha. En el evangelio de Juan, capítulo diecinueve, versículo cinco, Pilato presentó a Jesús ante la multitud y dijo:"), P(500)]
    S += [gr("Ἰδοὺ ὁ ἄνθρωπος.", voice=M, speed=s), P(600)]
    S += [es("He aquí el hombre. Tres palabras que ya conoces perfectamente."), P(800)]
    S += [es("En la siguiente lección haremos un repaso completo con un diálogo largo. Εἰρήνη σοι."), P(500)]
    return S

def lesson_6():
    s = get_speed(6)
    S = []
    S += [es("Μάθημα ἕξ. Lección seis. Hoy repasaremos todo lo que has aprendido con un diálogo completo. También aprenderás tres palabras nuevas. Escucha la conversación."), P(800)]
    # FULL DIALOGUE
    S += [gr("Χαῖρε!", voice=M, speed=s), P(300)]
    S += [gr("Εἰρήνη σοι. Τί ὄνομά σοι;", voice=F, speed=s), P(300)]
    S += [gr("Τὸ ὄνομά μου Σίμων. Καὶ σοί;", voice=M, speed=s), P(300)]
    S += [gr("Μαρία. Πόθεν εἶ;", voice=F, speed=s), P(300)]
    S += [gr("ἀπὸ Ἰερουσαλήμ. Καὶ σύ;", voice=M, speed=s), P(300)]
    S += [gr("ἀπὸ Γαλιλαίας.", voice=F, speed=s), P(300)]
    S += [gr("Γινώσκεις τὸν ἄνθρωπον ἐκεῖνον;", voice=M, speed=s), P(300)]
    S += [gr("ναί, γινώσκω αὐτόν. Αὐτός ἐστιν ὁ διδάσκαλος.", voice=F, speed=s), P(1000)]
    S += [es("¿Cuánto entendiste? Vamos a reconstruirlo paso a paso."), P(800)]
    # TEACH ποῦ / ὧδε / ἐκεῖ
    S += [es("Primero, tres palabras nuevas de lugar. ποῦ significa dónde."), P(300)]
    S += [gr("ποῦ", speed=s), P(3000), gr("ποῦ", speed=s), P(500)]
    S += [es("ὧδε significa aquí."), P(300)]
    S += [gr("ὧδε", speed=s), P(3000), gr("ὧδε", speed=s), P(500)]
    S += [es("ἐκεῖ significa allí."), P(300)]
    S += [gr("ἐκεῖ", speed=s), P(3000), gr("ἐκεῖ", speed=s), P(800)]
    S += [es("ποῦ ἐστιν; ¿Dónde está?"), P(300)]
    S += [gr("ποῦ ἐστιν;", speed=s), P(4000), gr("ποῦ ἐστιν;", speed=s), P(600)]
    S += [es("ὧδε ἐστιν. Está aquí."), P(300)]
    S += [gr("ὧδε ἐστιν", speed=s), P(3500), gr("ὧδε ἐστιν", speed=s), P(800)]
    # RECONSTRUCTION — student plays Simón
    S += [es("Ahora tú eres Simón. María te saluda. Responde."), P(800)]
    S += [gr("Χαῖρε!", voice=F, speed=s), P(500)]
    S += [es("Dile paz a ti y pregunta su nombre."), P(5500)]
    S += [gr("Εἰρήνη σοι. Τί ὄνομά σοι;", voice=M, speed=s), P(500)]
    S += [gr("Μαρία. Καὶ σοί;", voice=F, speed=s), P(500)]
    S += [es("Di tu nombre."), P(4500)]
    S += [gr("Τὸ ὄνομά μου Σίμων.", voice=M, speed=s), P(500)]
    S += [gr("Πόθεν εἶ;", voice=F, speed=s), P(500)]
    S += [es("Dile que eres de Jerusalén y pregúntale a ella."), P(5500)]
    S += [gr("ἀπὸ Ἰερουσαλήμ. Καὶ σύ;", voice=M, speed=s), P(400)]
    S += [gr("ἀπὸ Γαλιλαίας.", voice=F, speed=s), P(500)]
    S += [es("Pregúntale si conoce a aquel hombre."), P(5500)]
    S += [gr("Γινώσκεις τὸν ἄνθρωπον ἐκεῖνον;", voice=M, speed=s), P(400)]
    S += [gr("ναί, γινώσκω αὐτόν.", voice=F, speed=s), P(800)]
    # COMPREHENSIVE GIR — everything from L1-6
    S += [es("Repaso completo de las seis lecciones."), P(500)]
    S += [es("Hola."), P(3500), gr("Χαῖρε", speed=s), P(400)]
    S += [es("Paz a ti."), P(3500), gr("Εἰρήνη σοι", speed=s), P(400)]
    S += [es("¿Cuál es tu nombre?"), P(4500), gr("Τί ὄνομά σοι;", speed=s), P(400)]
    S += [es("Mi nombre es."), P(4000), gr("Τὸ ὄνομά μου", speed=s), P(400)]
    S += [es("¿De dónde eres?"), P(4000), gr("Πόθεν εἶ;", speed=s), P(400)]
    S += [es("Yo soy de Galilea."), P(4500), gr("ἐγώ εἰμι ἀπὸ Γαλιλαίας", speed=s), P(400)]
    S += [es("Él es."), P(3000), gr("αὐτός ἐστιν", speed=s), P(400)]
    S += [es("Yo sé."), P(3000), gr("γινώσκω", speed=s), P(400)]
    S += [es("Te digo."), P(3500), gr("λέγω σοι", speed=s), P(400)]
    S += [es("No oigo."), P(3500), gr("οὐκ ἀκούω", speed=s), P(400)]
    S += [es("Di otra vez."), P(3500), gr("λέγε πάλιν", speed=s), P(400)]
    S += [es("El hombre."), P(3000), gr("ὁ ἄνθρωπος", speed=s), P(400)]
    S += [es("La mujer."), P(3000), gr("ἡ γυνή", speed=s), P(400)]
    S += [es("¿Dónde está?"), P(3500), gr("ποῦ ἐστιν;", speed=s), P(400)]
    S += [es("Aquí."), P(2500), gr("ὧδε", speed=s), P(400)]
    S += [es("¡Mira!"), P(2500), gr("ἰδού", speed=s), P(800)]
    # VERSE
    S += [es("Escucha. En el evangelio de Mateo, capítulo veintiocho, versículo seis, el ángel dijo a las mujeres en la tumba vacía:"), P(500)]
    S += [gr("Οὐκ ἔστιν ὧδε· ἠγέρθη.", voice=M, speed=s), P(600)]
    S += [es("No está aquí. Ha resucitado. Reconoces οὐκ, no. ἔστιν, está. ὧδε, aquí."), P(800)]
    S += [es("Felicidades. Has completado las primeras seis lecciones. Ya puedes saludar, presentarte, decir de dónde eres, y tener una conversación básica en el idioma del Nuevo Testamento. En la siguiente lección aprenderás verbos de movimiento: ir, venir, caminar. Εἰρήνη σοι."), P(500)]
    return S

if __name__ == "__main__":
    print("Generating lessons 5-6...")
    build_lesson(lesson_5(), 5)
    build_lesson(lesson_6(), 6)
