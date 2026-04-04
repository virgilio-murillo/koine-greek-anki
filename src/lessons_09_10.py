"""Lessons 9-10: Numbers + Having/Not having"""
import sys; sys.path.insert(0, ".")
from lesson_engine import *

def get_speed(n):
    return 0.75 if n <= 7 else (0.85 if n <= 15 else 1.0)

def lesson_9():
    s = get_speed(9)
    S = []
    S += [es("Μάθημα ἐννέα. Lección nueve. Hoy aprenderás los números del uno al diez en griego koiné. Escucha."), P(800)]
    S += [gr("Πόσους ἄρτους ἔχετε;", voice=M, speed=s), P(400)]
    S += [gr("Πέντε ἄρτους καὶ δύο ἰχθύας.", voice=F, speed=s), P(1000)]
    # REVIEW
    S += [es("Repasemos. ¿Cómo dirías quiero pan?"), P(4000), gr("θέλω ἄρτον", speed=s), P(500)]
    S += [es("¿Cómo dirías como pan y bebo vino?"), P(5500), gr("ἐσθίω ἄρτον καὶ πίνω οἶνον", speed=s), P(800)]
    # NUMBERS 1-5
    S += [es("Los números. Uno: εἷς para masculino, μία para femenino, ἕν para neutro."), P(300)]
    S += [gr("εἷς", speed=s), P(2000), gr("μία", speed=s), P(2000), gr("ἕν", speed=s), P(2500)]
    S += [es("εἷς ἄρτος. Un pan."), P(300), gr("εἷς ἄρτος", speed=s), P(3000)]
    S += [es("Dos: δύο. No cambia con el género."), P(300)]
    S += [gr("δύο", speed=s), P(2500), gr("δύο", speed=s), P(500)]
    S += [es("Tres: τρεῖς."), P(300), gr("τρεῖς", speed=s), P(2500)]
    S += [es("Cuatro: τέσσαρες."), P(300), gr("τέσσαρες", speed=s), P(3000)]
    S += [es("Cinco: πέντε."), P(300), gr("πέντε", speed=s), P(2500)]
    S += [es("Repite los cinco. εἷς, δύο, τρεῖς, τέσσαρες, πέντε."), P(300)]
    S += [gr("εἷς", speed=s), P(2000), gr("δύο", speed=s), P(2000), gr("τρεῖς", speed=s), P(2000), gr("τέσσαρες", speed=s), P(2000), gr("πέντε", speed=s), P(3000)]
    # NUMBERS 6-10
    S += [es("Seis: ἕξ."), P(300), gr("ἕξ", speed=s), P(2500)]
    S += [es("Siete: ἑπτά. Un número muy importante en la Biblia."), P(300), gr("ἑπτά", speed=s), P(2500)]
    S += [es("Ocho: ὀκτώ."), P(300), gr("ὀκτώ", speed=s), P(2500)]
    S += [es("Nueve: ἐννέα."), P(300), gr("ἐννέα", speed=s), P(2500)]
    S += [es("Diez: δέκα."), P(300), gr("δέκα", speed=s), P(2500)]
    S += [es("Del seis al diez. ἕξ, ἑπτά, ὀκτώ, ἐννέα, δέκα."), P(300)]
    S += [gr("ἕξ", speed=s), P(2000), gr("ἑπτά", speed=s), P(2000), gr("ὀκτώ", speed=s), P(2000), gr("ἐννέα", speed=s), P(2000), gr("δέκα", speed=s), P(3000)]
    # GIR NUMBERS
    S += [es("¿Cómo dirías cinco?"), P(3000), gr("πέντε", speed=s), P(400)]
    S += [es("¿Cómo dirías tres?"), P(3000), gr("τρεῖς", speed=s), P(400)]
    S += [es("¿Cómo dirías siete?"), P(3000), gr("ἑπτά", speed=s), P(400)]
    S += [es("¿Cómo dirías uno?"), P(3000), gr("εἷς", speed=s), P(400)]
    S += [es("¿Cómo dirías diez?"), P(3000), gr("δέκα", speed=s), P(800)]
    # COMBINE WITH FOOD
    S += [es("Ahora combina números con lo que aprendiste. ¿Cómo dirías cinco panes?"), P(4500)]
    S += [gr("πέντε ἄρτοι", speed=s), P(500)]
    S += [es("Nota: cuando hay más de uno, ἄρτος cambia a ἄρτοι. Es el plural."), P(600)]
    S += [es("¿Cómo dirías dos peces?"), P(4000)]
    S += [gr("δύο ἰχθύες", speed=s), P(500)]
    S += [es("πέντε ἄρτοι καὶ δύο ἰχθύες. Cinco panes y dos peces. Exactamente lo que tenían los discípulos."), P(300)]
    S += [gr("πέντε ἄρτοι καὶ δύο ἰχθύες", speed=s), P(5000), gr("πέντε ἄρτοι καὶ δύο ἰχθύες", speed=s), P(800)]
    # GIR MIXED
    S += [es("¿Cómo dirías quiero agua?"), P(4000), gr("θέλω ὕδωρ", speed=s), P(500)]
    S += [es("¿Cómo dirías ocho?"), P(3000), gr("ὀκτώ", speed=s), P(500)]
    S += [es("¿Cómo dirías paz a ti?"), P(4000), gr("Εἰρήνη σοι", speed=s), P(500)]
    S += [es("¿Cómo dirías cuatro?"), P(3000), gr("τέσσαρες", speed=s), P(500)]
    S += [es("¿Cómo dirías voy al templo?"), P(5000), gr("πορεύομαι εἰς τὸ ἱερόν", speed=s), P(800)]
    # VERSE
    S += [es("Escucha. En el evangelio de Mateo, capítulo catorce, versículo diecisiete, los discípulos le dijeron a Jesús:"), P(500)]
    S += [gr("Οὐκ ἔχομεν ὧδε εἰ μὴ πέντε ἄρτους καὶ δύο ἰχθύας.", voice=M, speed=s), P(600)]
    S += [es("No tenemos aquí sino cinco panes y dos peces. Reconoces οὐκ, no. ὧδε, aquí. πέντε, cinco. ἄρτους, panes. δύο, dos. ἰχθύας, peces."), P(800)]
    S += [es("En la siguiente lección aprenderás el verbo tener y a decir que no tienes algo. Εἰρήνη σοι."), P(500)]
    return S

def lesson_10():
    s = get_speed(10)
    S = []
    S += [es("Μάθημα δέκα. Lección diez. Hoy aprenderás a decir tengo, no tengo, y a hablar de necesidades. Escucha."), P(800)]
    S += [gr("Ἔχεις ἄρτον;", voice=F, speed=s), P(400)]
    S += [gr("Οὐκ ἔχω. Χρείαν ἔχω ἄρτου.", voice=M, speed=s), P(400)]
    S += [gr("Ἰδού, λάβε τοῦτον.", voice=F, speed=s), P(1000)]
    # REVIEW
    S += [es("Repasemos. ¿Cómo dirías cinco panes y dos peces?"), P(5500), gr("πέντε ἄρτοι καὶ δύο ἰχθύες", speed=s), P(500)]
    S += [es("¿Cómo dirías siete?"), P(3000), gr("ἑπτά", speed=s), P(500)]
    S += [es("¿Cómo dirías quiero vino?"), P(4000), gr("θέλω οἶνον", speed=s), P(800)]
    # TEACH ἔχω
    S += [es("ἔχω significa tengo. Es uno de los verbos más frecuentes del Nuevo Testamento, aparece más de setecientas veces."), P(300)]
    S += [gr("ἔχω", speed=s), P(3000), gr("ἔχω", speed=s), P(500)]
    S += [es("ἔχεις significa tienes. ἔχει significa tiene."), P(300)]
    S += [gr("ἔχεις", speed=s), P(2500), gr("ἔχει", speed=s), P(2500)]
    S += [es("ἔχομεν significa tenemos."), P(300)]
    S += [gr("ἔχομεν", speed=s), P(3000), gr("ἔχομεν", speed=s), P(800)]
    # TEACH οὐκ ἔχω
    S += [es("Para decir no tengo: οὐκ ἔχω."), P(300)]
    S += [gr("οὐκ ἔχω", speed=s), P(3500), gr("οὐκ ἔχω", speed=s), P(600)]
    S += [es("οὐκ ἔχομεν. No tenemos."), P(300)]
    S += [gr("οὐκ ἔχομεν", speed=s), P(3500), gr("οὐκ ἔχομεν", speed=s), P(800)]
    # TEACH πολύς / ὀλίγος
    S += [es("πολύς significa mucho. ὀλίγος significa poco."), P(300)]
    S += [gr("πολύς", speed=s), P(2500), es("mucho"), P(300)]
    S += [gr("ὀλίγος", speed=s), P(2500), es("poco"), P(500)]
    S += [es("ἔχω πολλά. Tengo mucho. πολλά es la forma neutra plural de πολύς."), P(300)]
    S += [gr("ἔχω πολλά", speed=s), P(3500), gr("ἔχω πολλά", speed=s), P(600)]
    S += [es("ἔχω ὀλίγον. Tengo poco."), P(300)]
    S += [gr("ἔχω ὀλίγον", speed=s), P(3500), gr("ἔχω ὀλίγον", speed=s), P(800)]
    # TEACH χρεία
    S += [es("χρείαν ἔχω significa tengo necesidad. χρεία es necesidad."), P(300)]
    S += [gr("χρείαν ἔχω", speed=s), P(3500), gr("χρείαν ἔχω", speed=s), P(600)]
    S += [es("χρείαν ἔχω ἄρτου. Tengo necesidad de pan. Nota: ἄρτου con ου al final indica de pan. Es el genitivo."), P(300)]
    S += [gr("χρείαν ἔχω ἄρτου", speed=s), P(4500), gr("χρείαν ἔχω ἄρτου", speed=s), P(800)]
    # TEACH οὐδείς
    S += [es("οὐδείς significa nadie o nada. οὐδὲν es la forma neutra: nada."), P(300)]
    S += [gr("οὐδείς", speed=s), P(3000), gr("οὐδέν", speed=s), P(3000)]
    S += [es("οὐκ ἔχω οὐδέν. No tengo nada."), P(300)]
    S += [gr("οὐκ ἔχω οὐδέν", speed=s), P(4000), gr("οὐκ ἔχω οὐδέν", speed=s), P(800)]
    # GIR
    S += [es("¿Cómo dirías tengo?"), P(3000), gr("ἔχω", speed=s), P(500)]
    S += [es("¿Cómo dirías no tengo?"), P(3500), gr("οὐκ ἔχω", speed=s), P(500)]
    S += [es("¿Cómo dirías tienes pan?"), P(4000), gr("ἔχεις ἄρτον;", speed=s), P(500)]
    S += [es("¿Cómo dirías tengo mucho?"), P(4000), gr("ἔχω πολλά", speed=s), P(500)]
    S += [es("¿Cómo dirías tengo necesidad de agua?"), P(5000), gr("χρείαν ἔχω ὕδατος", speed=s), P(500)]
    S += [es("¿Cómo dirías no tengo nada?"), P(4500), gr("οὐκ ἔχω οὐδέν", speed=s), P(500)]
    S += [es("¿Cómo dirías hola?"), P(3000), gr("Χαῖρε", speed=s), P(500)]
    S += [es("¿Cómo dirías tres?"), P(3000), gr("τρεῖς", speed=s), P(800)]
    # DIALOGUE
    S += [es("Estás en el mercado. Alguien te pregunta si tienes pan. No tienes. Dile que necesitas pan."), P(500)]
    S += [gr("Ἔχεις ἄρτον;", voice=F, speed=s), P(500)]
    S += [es("Dile que no tienes."), P(4500)]
    S += [gr("Οὐκ ἔχω.", voice=M, speed=s), P(500)]
    S += [es("Dile que tienes necesidad de pan."), P(5000)]
    S += [gr("Χρείαν ἔχω ἄρτου.", voice=M, speed=s), P(500)]
    S += [gr("Ἰδού, λάβε τοῦτον.", voice=F, speed=s), P(500)]
    S += [es("Ella te dice mira, toma este. τοῦτον significa este, en acusativo."), P(800)]
    # FINAL GIR
    S += [es("Repaso de las diez lecciones. Paz a ti."), P(4000), gr("Εἰρήνη σοι", speed=s), P(400)]
    S += [es("¿Cuál es tu nombre?"), P(4500), gr("Τί ὄνομά σοι;", speed=s), P(400)]
    S += [es("¿De dónde eres?"), P(4000), gr("Πόθεν εἶ;", speed=s), P(400)]
    S += [es("Yo sé."), P(3000), gr("γινώσκω", speed=s), P(400)]
    S += [es("Voy a la casa."), P(4000), gr("πορεύομαι εἰς τὸν οἶκον", speed=s), P(400)]
    S += [es("Quiero pan y agua."), P(4500), gr("θέλω ἄρτον καὶ ὕδωρ", speed=s), P(400)]
    S += [es("No tengo nada."), P(4000), gr("οὐκ ἔχω οὐδέν", speed=s), P(400)]
    S += [es("Cinco panes."), P(3500), gr("πέντε ἄρτοι", speed=s), P(800)]
    # VERSE
    S += [es("Escucha. En el evangelio de Marcos, capítulo diez, versículo veintiuno, Jesús le dijo al joven rico:"), P(500)]
    S += [gr("Ὕπαγε, ὅσα ἔχεις πώλησον καὶ δὸς τοῖς πτωχοῖς.", voice=M, speed=s), P(600)]
    S += [es("Ve, vende todo lo que tienes y dalo a los pobres. Reconoces ἔχεις, tienes. καί, y."), P(800)]
    S += [es("Felicidades. Has completado diez lecciones. Ya puedes saludar, presentarte, pedir comida, usar números, y hablar de lo que tienes y necesitas. Todo en el idioma del Nuevo Testamento. Εἰρήνη σοι."), P(500)]
    return S

if __name__ == "__main__":
    print("Generating lessons 9-10...")
    build_lesson(lesson_9(), 9)
    build_lesson(lesson_10(), 10)
