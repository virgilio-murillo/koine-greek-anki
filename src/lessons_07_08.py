"""Lessons 7-8: Movement verbs + Market/Food"""
import sys; sys.path.insert(0, ".")
from lesson_engine import *

def get_speed(n):
    return 0.75 if n <= 7 else (0.85 if n <= 15 else 1.0)

def lesson_7():
    s = get_speed(7)  # last lesson at 75%
    S = []
    S += [es("Μάθημα ἑπτά. Lección siete. Hoy aprenderás a decir ir, venir, y caminar. Escucha."), P(800)]
    S += [gr("Ποῦ πορεύῃ;", voice=F, speed=s), P(400)]
    S += [gr("Πορεύομαι εἰς τὸ ἱερόν.", voice=M, speed=s), P(400)]
    S += [gr("Ἔρχου μετ᾽ ἐμοῦ.", voice=F, speed=s), P(400)]
    S += [gr("ναί, ἔρχομαι.", voice=M, speed=s), P(1000)]
    # REVIEW
    S += [es("Repasemos. ¿Cómo dirías he aquí el hombre?"), P(5000), gr("ἰδοὺ ὁ ἄνθρωπος", speed=s), P(500)]
    S += [es("¿Cómo dirías dónde está?"), P(4000), gr("ποῦ ἐστιν;", speed=s), P(800)]
    # TEACH ἔρχομαι
    S += [es("ἔρχομαι significa venir o ir. Es un verbo deponente. Tiene forma pasiva pero significado activo. No te preocupes por eso ahora, solo aprende la palabra."), P(300)]
    S += [gr("ἔρχομαι", speed=s), P(3500), gr("ἔρχομαι", speed=s), P(600)]
    S += [es("Para decir ven, como una orden, se dice ἔρχου."), P(300)]
    S += [gr("ἔρχου", speed=s), P(3000), gr("ἔρχου", speed=s), P(600)]
    S += [es("Jesús dijo a Felipe: ἔρχου. Ven. Y Felipe lo siguió."), P(800)]
    # TEACH πορεύομαι
    S += [es("πορεύομαι significa ir o caminar. También es deponente."), P(300)]
    S += [gr("πορεύομαι", speed=s), P(3500), gr("πορεύομαι", speed=s), P(600)]
    S += [es("πορεύομαι εἰς τὸ ἱερόν. Voy al templo. εἰς significa hacia o a."), P(300)]
    S += [gr("πορεύομαι εἰς τὸ ἱερόν", speed=s), P(4500), gr("πορεύομαι εἰς τὸ ἱερόν", speed=s), P(800)]
    # TEACH εἰς / ἐν
    S += [es("Recuerda: εἰς significa hacia, movimiento. ἐν significa en, ubicación. Voy hacia el templo: εἰς. Estoy en el templo: ἐν."), P(300)]
    S += [gr("εἰς τὸ ἱερόν", speed=s), P(3000), es("hacia el templo"), P(300)]
    S += [gr("ἐν τῷ ἱερῷ", speed=s), P(3000), es("en el templo"), P(800)]
    # TEACH οἶκος / ὁδός
    S += [es("οἶκος significa casa."), P(300)]
    S += [gr("οἶκος", speed=s), P(3000), gr("οἶκος", speed=s), P(500)]
    S += [es("ὁδός significa camino."), P(300)]
    S += [gr("ὁδός", speed=s), P(3000), gr("ὁδός", speed=s), P(500)]
    S += [es("ἐν τῇ ὁδῷ. En el camino."), P(300)]
    S += [gr("ἐν τῇ ὁδῷ", speed=s), P(3500), gr("ἐν τῇ ὁδῷ", speed=s), P(800)]
    # TEACH δεῦτε
    S += [es("δεῦτε significa vengan. Es una invitación plural. Jesús dijo a los pescadores:"), P(300)]
    S += [gr("Δεῦτε ὀπίσω μου.", voice=M, speed=s), P(4000)]
    S += [es("Vengan tras de mí. ὀπίσω significa detrás o tras."), P(300)]
    S += [gr("Δεῦτε ὀπίσω μου", speed=s), P(4500), gr("Δεῦτε ὀπίσω μου", speed=s), P(800)]
    # GIR
    S += [es("¿Cómo dirías yo voy?"), P(3500), gr("πορεύομαι", speed=s), P(500)]
    S += [es("¿Cómo dirías ven?"), P(3500), gr("ἔρχου", speed=s), P(500)]
    S += [es("¿Cómo dirías voy al templo?"), P(5000), gr("πορεύομαι εἰς τὸ ἱερόν", speed=s), P(500)]
    S += [es("¿Cómo dirías en el camino?"), P(4000), gr("ἐν τῇ ὁδῷ", speed=s), P(500)]
    S += [es("¿Cómo dirías vengan tras de mí?"), P(5000), gr("Δεῦτε ὀπίσω μου", speed=s), P(500)]
    S += [es("¿Cómo dirías cuál es tu nombre?"), P(5000), gr("Τί ὄνομά σοι;", speed=s), P(500)]
    S += [es("¿Cómo dirías no oigo?"), P(4000), gr("οὐκ ἀκούω", speed=s), P(800)]
    # DIALOGUE
    S += [es("Practica. Alguien te pregunta a dónde vas. Dile que vas al templo e invítalo a venir contigo."), P(500)]
    S += [gr("Ποῦ πορεύῃ;", voice=F, speed=s), P(500)]
    S += [es("Dile que vas al templo."), P(5000)]
    S += [gr("Πορεύομαι εἰς τὸ ἱερόν.", voice=M, speed=s), P(500)]
    S += [es("Dile ven conmigo. μετ᾽ ἐμοῦ significa conmigo."), P(5000)]
    S += [gr("Ἔρχου μετ᾽ ἐμοῦ.", voice=M, speed=s), P(800)]
    # VERSE
    S += [es("Escucha. En el evangelio de Mateo, capítulo cuatro, versículo diecinueve, Jesús vio a Simón y Andrés pescando y les dijo:"), P(500)]
    S += [gr("Δεῦτε ὀπίσω μου, καὶ ποιήσω ὑμᾶς ἁλιεῖς ἀνθρώπων.", voice=M, speed=s), P(600)]
    S += [es("Vengan tras de mí, y los haré pescadores de hombres. Reconoces δεῦτε, vengan. ὀπίσω μου, tras de mí. καί, y. ἀνθρώπων, de hombres."), P(800)]
    S += [es("En la siguiente lección aprenderás a comprar en el mercado: pan, agua, vino. Y la velocidad del griego aumentará un poco. Εἰρήνη σοι."), P(500)]
    return S

def lesson_8():
    s = get_speed(8)  # 85% speed starts
    S = []
    S += [es("Μάθημα ὀκτώ. Lección ocho. Hoy aprenderás vocabulario del mercado: pan, agua, vino, y a decir quiero y como. Nota que el griego ahora suena un poco más rápido. Escucha."), P(800)]
    S += [gr("Θέλεις ἄρτον;", voice=F, speed=s), P(400)]
    S += [gr("ναί, θέλω ἄρτον καὶ ὕδωρ.", voice=M, speed=s), P(400)]
    S += [gr("Ἰδού. Λάβε.", voice=F, speed=s), P(400)]
    S += [gr("Εὐχαριστῶ.", voice=M, speed=s), P(1000)]
    # REVIEW
    S += [es("Repasemos. ¿Cómo dirías voy al templo?"), P(5000), gr("πορεύομαι εἰς τὸ ἱερόν", speed=s), P(500)]
    S += [es("¿Cómo dirías ven?"), P(3500), gr("ἔρχου", speed=s), P(800)]
    # TEACH θέλω
    S += [es("θέλω significa quiero. Es uno de los verbos más útiles."), P(300)]
    S += [gr("θέλω", speed=s), P(3000), gr("θέλω", speed=s), P(500)]
    S += [es("θέλεις significa quieres. θέλει significa quiere."), P(300)]
    S += [gr("θέλεις", speed=s), P(2500), gr("θέλει", speed=s), P(2500)]
    # TEACH ἄρτος
    S += [es("ἄρτος significa pan. Es la palabra que Jesús usa en la última cena."), P(300)]
    S += [gr("ἄρτος", speed=s), P(3000), gr("ἄρτος", speed=s), P(500)]
    S += [es("θέλω ἄρτον. Quiero pan. Nota que ἄρτον termina en ον. Eso indica que es objeto directo."), P(300)]
    S += [gr("θέλω ἄρτον", speed=s), P(3500), gr("θέλω ἄρτον", speed=s), P(800)]
    # TEACH ὕδωρ
    S += [es("ὕδωρ significa agua. Nunca uses la palabra moderna νερό. En koiné siempre es ὕδωρ."), P(300)]
    S += [gr("ὕδωρ", speed=s), P(3000), gr("ὕδωρ", speed=s), P(600)]
    S += [es("θέλω ὕδωρ. Quiero agua."), P(300)]
    S += [gr("θέλω ὕδωρ", speed=s), P(3500), gr("θέλω ὕδωρ", speed=s), P(800)]
    # TEACH οἶνος
    S += [es("οἶνος significa vino."), P(300)]
    S += [gr("οἶνος", speed=s), P(3000), gr("οἶνος", speed=s), P(500)]
    S += [gr("θέλω οἶνον", speed=s), P(3500), gr("θέλω οἶνον", speed=s), P(800)]
    # TEACH ἐσθίω / πίνω
    S += [es("ἐσθίω significa comer."), P(300)]
    S += [gr("ἐσθίω", speed=s), P(3000), gr("ἐσθίω", speed=s), P(500)]
    S += [es("πίνω significa beber."), P(300)]
    S += [gr("πίνω", speed=s), P(3000), gr("πίνω", speed=s), P(500)]
    S += [es("ἐσθίω ἄρτον καὶ πίνω οἶνον. Como pan y bebo vino."), P(300)]
    S += [gr("ἐσθίω ἄρτον καὶ πίνω οἶνον", speed=s), P(5000), gr("ἐσθίω ἄρτον καὶ πίνω οἶνον", speed=s), P(800)]
    # TEACH ἰχθύς
    S += [es("ἰχθύς significa pez. Los primeros cristianos usaban el pez como símbolo."), P(300)]
    S += [gr("ἰχθύς", speed=s), P(3000), gr("ἰχθύς", speed=s), P(800)]
    # GIR
    S += [es("¿Cómo dirías quiero pan?"), P(4000), gr("θέλω ἄρτον", speed=s), P(500)]
    S += [es("¿Cómo dirías quiero agua?"), P(4000), gr("θέλω ὕδωρ", speed=s), P(500)]
    S += [es("¿Cómo dirías como pan y bebo vino?"), P(5500), gr("ἐσθίω ἄρτον καὶ πίνω οἶνον", speed=s), P(500)]
    S += [es("¿Cómo dirías ven?"), P(3500), gr("ἔρχου", speed=s), P(500)]
    S += [es("¿Cómo dirías en el camino?"), P(4000), gr("ἐν τῇ ὁδῷ", speed=s), P(500)]
    S += [es("¿Cómo dirías quieres pan?"), P(4000), gr("θέλεις ἄρτον;", speed=s), P(800)]
    # DIALOGUE
    S += [es("Estás en el mercado de Jerusalén. Una vendedora te ofrece pan."), P(500)]
    S += [gr("Θέλεις ἄρτον;", voice=F, speed=s), P(500)]
    S += [es("Dile que sí, quieres pan y agua."), P(5000)]
    S += [gr("ναί, θέλω ἄρτον καὶ ὕδωρ.", voice=M, speed=s), P(500)]
    S += [gr("Ἰδού. Λάβε.", voice=F, speed=s), P(500)]
    S += [es("Ella te dice mira, toma. Λάβε significa toma. Responde con gracias. En koiné, dar gracias se dice εὐχαριστῶ. Pero recuerda, en koiné esta palabra es formal, es dar gracias a Dios. No es el gracias casual del griego moderno."), P(300)]
    S += [gr("εὐχαριστῶ", speed=s), P(3500), gr("εὐχαριστῶ", speed=s), P(800)]
    # FINAL GIR
    S += [es("Pan."), P(3000), gr("ἄρτος", speed=s), P(400)]
    S += [es("Agua."), P(3000), gr("ὕδωρ", speed=s), P(400)]
    S += [es("Vino."), P(3000), gr("οἶνος", speed=s), P(400)]
    S += [es("Pez."), P(3000), gr("ἰχθύς", speed=s), P(400)]
    S += [es("Quiero."), P(3000), gr("θέλω", speed=s), P(400)]
    S += [es("Comer."), P(3000), gr("ἐσθίω", speed=s), P(400)]
    S += [es("Beber."), P(3000), gr("πίνω", speed=s), P(400)]
    S += [es("Toma."), P(3000), gr("λάβε", speed=s), P(800)]
    # VERSE
    S += [es("Escucha. En el evangelio de Juan, capítulo seis, versículo cinco, Jesús vio una gran multitud y le preguntó a Felipe:"), P(500)]
    S += [gr("Πόθεν ἀγοράσωμεν ἄρτους ἵνα φάγωσιν οὗτοι;", voice=M, speed=s), P(600)]
    S += [es("¿De dónde compraremos panes para que estos coman? Reconoces πόθεν, de dónde. ἄρτους, panes. οὗτοι, estos."), P(800)]
    S += [es("En la siguiente lección aprenderás los números del uno al diez. Εἰρήνη σοι."), P(500)]
    return S

if __name__ == "__main__":
    print("Generating lessons 7-8...")
    build_lesson(lesson_7(), 7)
    build_lesson(lesson_8(), 8)
