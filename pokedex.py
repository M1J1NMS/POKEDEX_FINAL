from InquirerPy import inquirer as inqui
import random

def random_poke():
    results = random.choices(opciones, k=6)
    print("Tu equipo sera:")
    print(f"{results[0]} | {results[1]} | {results[2]}\n{results[3]} | {results[4]} | {results[5]} ")
    reafirmacion = ["Si", "salir"]
    behind = inqui.select(message=f"otra vez o prefieres salir?", choices=reafirmacion,).execute()
    while behind == reafirmacion[0]:
        results = random.choices(opciones, k=6)
        print("Tu equipo sera:")
        print(f"{results[0]} | {results[1]} | {results[2]}\n{results[3]} | {results[4]} | {results[5]} ")
        reafirmacion = ["Si", "salir"]
        behind = inqui.select(message=f"otra vez o prefieres salir?", choices=reafirmacion,).execute()

    if behind == reafirmacion[1]:
        inicio()
  
    

class pokemon:
    def __init__(self, num, nom_p, tipo, descrip, altura, peso, habilidad, sexo, ps, atk, defs, atk_e, def_e, vel, debilidad, evo):
        self.numero = num
        self.nom = str(nom_p)
        self.tipo = list(tipo)
        self.descripcion = str(descrip)
        self.altura = altura
        self.peso = peso
        self.habilidad = str(habilidad)
        self.sexo = list(sexo)
        self.ps = ps
        self.ataque = atk
        self.defensa = defs
        self.ataque_e = atk_e
        self.def_e = def_e
        self.vel = vel
        self.debilidad = list(debilidad)
        self.evo = evo
    def info(self):
        print(f"#{self.numero}\nNombre: {self.nom}\nTipo:{self.tipo}\nDescripcion:{self.descripcion}\nAltura:{self.altura}Cm\nPeso:{self.peso}Kg\nHabilidad:{self.habilidad}\nSexo:{self.sexo}\nPs    {self.ps}\nAtk   {self.ataque}\ndef   {self.defensa}\nAtk-e {self.ataque_e}\nDef_e {self.def_e}\nVel   {self.vel}\nDebilidad:{self.debilidad}\nEvolucion:{self.evo} ")
    def name(self):
        print(f"Nombre: {self.nom}")
    def statics(self):
        print(f"Ps    {self.ps}\nAtk   {self.ataque}\ndef   {self.defensa}\nAtk-e {self.ataque_e}\nDef_e {self.def_e}\nVel   {self.vel}")
    def evolucion(self):
        print(f"Evolucion:{self.evo}")
    
    def adios(self):
        acierto = ["SI", "NO"] 
        res = inqui.select(message=f"Escojiste al pokemon: {self.nom}", choices=acierto,).execute()
        if res == acierto[1]:
            poke_dex()
            quit()
        elif res == acierto[0]:
            informacion = ["Todo", "Estadisticas", "Evolucion"]
            answer = inqui.select(message=f"Que deseas saber sobre el pokemon {self.nom}:", choices=informacion,).execute()
            if answer == informacion[0]:
                self.info()
            if answer == informacion[1]:
                print(f"Las estadisticas del pokemon{self.nom}son:")
                self.statics()
            if answer == informacion[2]:
                print(f"La evolucion del pokemon{self.nom}es:")
                self.evolucion()
            reafirmacion = ["Si", "No"]
            behind = inqui.select(message=f"Quieres ver otro pokemon:", choices=reafirmacion,).execute()
            if behind == reafirmacion[0]:
                poke_dex()
                quit()
            if behind == reafirmacion[1]:
                quit()




bulbasaur = pokemon(1, "Bulbasaur", ["planta", "veneno"], "Tras nacer, crece alimentándose durante un tiempo de los nutrientes que contiene el bulbo de su lomo.", 70, 6.9, "Espesura", ["macho", "hembra"], 45, 49, 49, 65, 65, 45, ["fuego", "hielo", "volador", "psíquico"], "Ivysaur")

ivysaur = pokemon(2, "Ivysaur", ["planta", "veneno"], "Cuanta más luz solar recibe, más aumenta su fuerza y más se desarrolla el capullo que tiene en el lomo.", 100, 13, "Espesura", ["macho", "hembra"], 60, 62, 63, 80, 80, 60, ["fuego", "hielo", "volador", "psíquico"], "Venusaur")

venusaur = pokemon(3, "Venusaur", ["planta", "veneno"], "Puede convertir la luz del sol en energía. Por esa razón, es más poderoso en verano.", 200, 100, "Espesura", ["macho", "hembra"], 80, 82, 83, 100, 100, 80, ["fuego", "hielo", "volador", "psíquico"], "0")

charmander = pokemon(4, "Charmander", ["fuego"], "Prefiere las cosas calientes. Dicen que cuando llueve, le sale vapor de la punta de la cola.", 60, 8.5, "mar llamas", ["macho", "hembra"], 39, 52, 43, 60, 50, 65, ["agua", "tierra", "roca"], "Charmeleon")

charmeleon = pokemon(5, "Charmeleon", ["fuego"], "Evoluciona de Charmander. Es feroz y orgulloso, y su cola emite llamas ardientes.", 110, 19, "mar llamas", ["macho", "hembra"], 58, 64, 58, 80, 65, 80, ["agua", "tierra", "roca"], "Charizard")

charizard = pokemon(6, "Charizard", ["fuego", "volador"], "Es conocido por su aliento ardiente, que puede derretir rocas.", 170, 90.5, "mar llamas", ["macho", "hembra"], 78, 84, 78, 109, 85, 100, ["agua", "eléctrico", "roca"], "0")

squirtle = pokemon(7, "Squirtle", ["agua"], "Su caparazón no solo lo protege, sino que también le ayuda a nadar a gran velocidad.", 50, 9, "torrent", ["macho", "hembra"], 44, 48, 65, 50, 64, 43, ["eléctrico", "planta"], "Wartortle")

wartortle = pokemon(8, "Wartortle", ["agua"], "Evoluciona de Squirtle. Su caparazón se cubre de algas a medida que envejece.", 100, 22.5, "torrent", ["macho", "hembra"], 59, 63, 80, 65, 80, 58, ["eléctrico", "planta"], "Blastoise")

blastoise = pokemon(9, "Blastoise", ["agua"], "Lanza chorros de agua con gran precisión y potencia desde sus cañones.", 160, 85.5, "torrent", ["macho", "hembra"], 79, 83, 100, 85, 105, 78, ["eléctrico", "planta"], "0")

caterpie = pokemon(10, "Caterpie", ["bicho"], "Para protegerse, despide un hedor terrible por las antenas de su cabeza para ahuyentar a los enemigos.", 30, 2.9, "polvo escudo", ["macho", "hembra"],  45, 30, 35, 20, 20, 45,  ["fuego", "volador", "roca"], "Metapod")

metapod = pokemon(11, "Metapod", ["bicho"], "Su dura coraza le protege mientras evoluciona. Sin embargo, es completamente indefenso durante esta etapa.", 70, 9.9, "mudar",  ["macho", "hembra"], 50, 20, 55, 25, 25, 30, ["fuego", "volador", "roca"], "Butterfree")

butterfree = pokemon(12, "Butterfree", ["bicho", "volador"], "Sus alas tienen un polvo muy fino que puede causar una parálisis en sus enemigos.", 110, 32, "efecto espora", ["macho", "hembra"], 60, 45, 50, 80, 80, 70, ["fuego", "eléctrico", "roca"], "0") 

weedle = pokemon(13, "Weedle", ["bicho", "veneno"], "Su aguijón puede inyectar un veneno doloroso. Es muy temido por los demás Pokémon.", 30, 3.2, "escudo polvoso", ["macho", "hembra"], 40, 35, 30, 20, 20, 50, ["fuego", "volador", "psíquico"], "Kakuna") 

kakuna = pokemon(14, "Kakuna", ["bicho", "veneno"], "Su dura coraza protege el capullo mientras evoluciona. Es totalmente inmóvil en esta etapa.", 60, 10, "mudar", ["macho", "hembra"], 45, 25, 50, 25, 25, 35, ["fuego", "volador", "psíquico"], "Beedrill") 

beedrill = pokemon(15, "Beedrill", ["bicho", "veneno"], "Sus aguijones son muy afilados y venenosos. Puede atacar con gran rapidez.", 100, 29.5, "escudo polvoso", ["macho", "hembra"], 65, 90, 40, 45, 80, 75, ["fuego", "volador", "psíquico"], "0") 

pidgey = pokemon(16, "Pidgey", ["normal", "volador"], "Es un Pokémon común que habita en casi todas partes. Su vuelo es muy rápido y ágil.", 30, 1.8, "enfermo", ["macho", "hembra"], 40, 45, 40, 35, 35, 56, ["eléctrico", "roca"], "Pidgeotto") 

pidgeotto = pokemon(17, "Pidgeotto", ["normal", "volador"], "Vuela rápidamente para buscar comida. Si encuentra algo que le gusta, no deja de perseguirlo.", 110, 30, "enfermo", ["macho", "hembra"], 63, 60, 55, 50, 50, 71, ["eléctrico", "roca"], "Pidgeot") 

pidgeot = pokemon(18, "Pidgeot", ["normal", "volador"], "Tiene un vuelo muy rápido y puede alcanzar una gran velocidad. Su precisión es excelente.", 170, 39.5, "enfermo", ["macho", "hembra"], 83, 80, 75, 70, 70, 101, ["eléctrico", "roca"], "0") 

rattata = pokemon(19, "Rattata", ["normal"], "Es conocido por su agilidad y rapidez. Su vida es corta, pero se reproduce en grandes cantidades.", 30, 3.5, "fuga", ["macho", "hembra"], 30, 56, 35, 25, 35, 72, ["lucha", "roca"], "Raticate") 

raticate = pokemon(20, "Raticate", ["normal"], "Su cola es muy fuerte y puede romperse cuando se agarra. Es muy rápido y peligroso.", 70, 18.5, "fuga", ["macho", "hembra"], 55, 81, 60, 50, 70, 97, ["lucha", "roca"], "0") 
spearow = pokemon(21, "Spearow", ["normal", "volador"], "Spearow tiene un temperamento irritable. Ataca a sus enemigos con sus afiladas garras y su pico.", 20, 2.0, "carrera", ["macho", "hembra"], 40, 60, 30, 31, 31, 70, ["eléctrico", "hielo"], "Fearow")

fearow = pokemon(22, "Fearow", ["normal", "volador"], "Fearow es conocido por su velocidad en el aire y su agresividad. Puede atacar a sus presas desde el aire sin piedad.", 120, 38.0, "carrera", ["macho", "hembra"], 65, 90, 65, 61, 61, 100, ["eléctrico", "hielo"], "0")

ekans = pokemon(23, "Ekans", ["veneno"], "Ekans es un Pokémon que se enrolla alrededor de sus presas para asfixiarlas. Su cuerpo es flexible y serpenteante.", 20, 6.9, "intimidación", ["macho", "hembra"], 35, 60, 44, 40, 54, 55, ["psíquico", "tierra"], "Arbok")

arbok = pokemon(24, "Arbok", ["veneno"], "Arbok extiende su capucha cuando está enojado para hacer más intimidante su apariencia y atacar a sus enemigos.", 35, 65.0, "intimidación", ["macho", "hembra"], 60, 85, 69, 65, 79, 80, ["psíquico", "tierra"], "0")

pikachu = pokemon(25, "Pikachu", ["eléctrico"], "Pikachu puede generar electricidad en sus mejillas y liberarla a través de descargas eléctricas.", 40, 6.0, "estática", ["macho", "hembra"], 35, 55, 40, 50, 50, 90, ["tierra"], "Raichu")

raichu = pokemon(26, "Raichu", ["eléctrico"], "Raichu puede acumular electricidad y liberarla en potentes ataques eléctricos. Su velocidad le permite moverse rápidamente.", 80, 30.0, "estática", ["macho", "hembra"], 60, 90, 55, 90, 80, 110, ["tierra"], "0")

sandshrew = pokemon(27, "Sandshrew", ["tierra"], "Sandshrew puede excavar rápidamente túneles subterráneos y protegerse de ataques con su cuerpo recubierto de espinas.", 60, 12.0, "escudo arena", ["macho", "hembra"], 50, 75, 85, 20, 30, 40, ["agua", "hielo", "planta"], "Sandslash")

sandslash = pokemon(28, "Sandslash", ["tierra"], "Sandslash usa sus afiladas espinas para defenderse y atacar a sus enemigos. Puede excavar rápidamente en la tierra.", 100, 29.5, "escudo arena", ["macho", "hembra"], 50, 100, 110, 45, 55, 65, ["agua", "hielo", "planta"], "0")

nidoran_femenino = pokemon(29, "Nidoran♀", ["veneno"], "Nidoran♀ tiene un sentido agudo del olfato y libera toxinas cuando se siente amenazada.", 70, 7.5, "punto tóxico", ["hembra"], 55, 47, 52, 40, 40, 41, ["psíquico", "tierra"], "Nidorina")

nidorina = pokemon(30, "Nidorina", ["veneno"], "Nidorina tiene un cuerpo más fuerte y robusto que el de Nidoran♀. Es muy protectora con sus crías.", 120, 20.0, "punto tóxico", ["hembra"], 70, 62, 67, 55, 55, 56, ["psíquico", "tierra"], "Nidoqueen")

nidoqueen = pokemon(31, "Nidoqueen", ["veneno", "tierra"], "Nidoqueen usa su cuerpo resistente y blindado para proteger a sus crías de cualquier peligro.", 130, 60.0, "punto tóxico", ["hembra"], 90, 92, 87, 75, 85, 76, ["agua", "hielo", "psíquico", "tierra"], "0")

nidoran_m = pokemon(32, "Nidoran♂", ["veneno"], "Tiene unas orejas grandes y se le ve más agresivo que su contraparte hembra. Su cuerno contiene veneno.", 50, 9, "Punto tóxico", ["macho"], 46, 57, 40, 40, 40, 50, ["psíquico", "tierra"], "Nidorino")

nidorino = pokemon(33, "Nidorino", ["veneno"], "Es muy agresivo y el cuerno que tiene en la frente es más duro que un diamante. Si detecta peligro, lanza un ataque con todas sus fuerzas.",90, 19.5, "Punto tóxico", ["macho"], 61, 72, 57, 55, 55, 65, ["psíquico", "tierra"], "Nidoking")

nidoking = pokemon(34, "Nidoking", ["veneno", "tierra"], "Nidoking tiene una gran fuerza y una cola que usa como arma destructiva en batalla.", 140, 62.0, "punto tóxico", ["macho"], 81, 102, 77, 85, 75, 85, ["agua", "hielo", "psíquico", "tierra"], "0")

clefairy = pokemon(35, "Clefairy", ["hada"], "Clefairy es un Pokémon de aspecto tierno que tiene una conexión especial con la luna.", 60, 7.5, "gran encanto", ["hembra", "macho"], 70, 45, 48, 60, 65, 35, ["acero", "veneno"], "Clefable")

clefable = pokemon(36, "Clefable", ["hada"], "Clefable camina tan suavemente que no deja huella. Su oído es tan agudo que puede escuchar una aguja caer a 1 km.", 130, 40.0, "gran encanto", ["hembra", "macho"], 95, 70, 73, 95, 90, 60, ["acero", "veneno"], "0")

vulpix = pokemon(37, "Vulpix", ["fuego"], "Vulpix tiene seis colas que emiten un calor suave. A medida que crece, sus colas se multiplican.", 60, 9.9, "cuerpo llama", ["hembra", "macho"], 38, 41, 40, 50, 65, 65, ["agua", "roca", "tierra"], "Ninetales")

ninetales = pokemon(38, "Ninetales", ["fuego"], "Ninetales tiene un pelaje resplandeciente y se dice que vive mil años. Se cree que tiene poderes místicos.", 110, 19.9, "sequía", ["hembra", "macho"], 73, 76, 75, 81, 100, 100, ["agua", "roca", "tierra"], "0")

jigglypuff = pokemon(39, "Jigglypuff", ["normal", "hada"], "Canta una canción de cuna que hace que cualquiera que la escuche se quede dormido.", 50, 5.5, "cuerpo sedoso", ["macho", "hembra"], 115, 45, 50, 45, 50, 20, ["acero", "veneno"], "Wigglytuff")

wigglytuff = pokemon(40, "Wigglytuff", ["normal", "hada"], "Su cuerpo es blando y flexible. Si lo golpeas, rebotará sin problema.", 100, 12.0, "cuerpo sedoso", ["macho", "hembra"], 140, 70, 45, 85, 50, 45, ["acero", "veneno"], "0")

zubat = pokemon(41, "Zubat", ["veneno", "volador"], "Le gusta esconderse en lugares oscuros y húmedos durante el día. Absorbe sangre de otros Pokémon.", 80, 7.5, "foco interno", ["macho", "hembra"], 40, 45, 35, 30, 40, 55, ["eléctrico", "hielo", "psíquico", "roca"], "Golbat")

golbat = pokemon(42, "Golbat", ["veneno", "volador"], "Usa sus afilados colmillos para succionar la sangre de su presa.", 160, 55.0, "foco interno", ["macho", "hembra"], 75, 80, 70, 65, 75, 90, ["eléctrico", "hielo", "psíquico", "roca"], "Crobat")

oddish = pokemon(43, "Oddish", ["planta", "veneno"], "Durante el día, se entierra en la tierra para absorber nutrientes. De noche, vaga en busca de un lugar para plantar sus raíces.", 50, 5.4, "clorofila", ["macho", "hembra"], 45, 50, 55, 75, 65, 30, ["fuego", "volador", "hielo", "psíquico"], "Gloom")

gloom = pokemon(44, "Gloom", ["planta", "veneno"], "Expulsa un hedor tan fuerte que puede provocar desmayos. Si se siente amenazado, el olor empeora.", 80, 8.6, "clorofila", ["macho", "hembra"], 60, 65, 70, 85, 75, 40, ["fuego", "volador", "hielo", "psíquico"], "Vileplume")

vileplume = pokemon(45, "Vileplume", ["planta", "veneno"], "Sus pétalos liberan esporas tóxicas. A menudo se usa en la medicina natural.", 120, 18.6, "clorofila", ["macho", "hembra"], 75, 80, 85, 110, 90, 50, ["fuego", "volador", "hielo", "psíquico"], "0")

paras = pokemon(46, "Paras", ["bicho", "planta"], "Los hongos en su espalda se apoderan de su cuerpo. Se usa en pociones medicinales.", 30, 5.4, "efecto espora", ["macho", "hembra"], 35, 70, 55, 45, 55, 25, ["fuego", "volador", "veneno", "roca", "hielo"], "Parasect")

parasect = pokemon(47, "Parasect", ["bicho", "planta"], "El hongo ha crecido tanto que controla todo su cuerpo. Se alimenta de árboles y plantas.", 100, 29.5, "efecto espora", ["macho", "hembra"], 60, 95, 80, 60, 80, 30, ["fuego", "volador", "veneno", "roca", "hielo"], "0")

venonat = pokemon(48, "Venonat", ["bicho", "veneno"], "Sus grandes ojos actúan como radares en la oscuridad. Se siente atraído por la luz.", 100, 30.0, "ojo compuesto", ["macho", "hembra"], 60, 55, 50, 40, 55, 45, ["fuego", "volador", "psíquico", "roca"], "Venomoth")

venomoth = pokemon(49, "Venomoth", ["bicho", "veneno"], "Sus alas están cubiertas de polvo venenoso que puede causar parálisis y debilitar a sus enemigos.", 150, 12.5, "ojo compuesto", ["macho", "hembra"], 70, 65, 60, 90, 75, 90, ["fuego", "volador", "psíquico", "roca"], "0")

diglett = pokemon(50, "Diglett", ["tierra"], "Vive bajo tierra y solo sale a la superficie cuando siente que está seguro. Su cuerpo es pequeño y rápido.", 20, 0.8, "velo arena", ["macho", "hembra"], 10, 55, 25, 35, 45, 95, ["agua", "planta", "hielo"], "Dugtrio")

dugtrio = pokemon(51, "Dugtrio", ["tierra"], "Es un trío de Diglett que trabajan en conjunto para cavar más rápido. Son muy veloces y difíciles de atrapar.", 70, 33.3, "velo arena", ["macho", "hembra"], 35, 100, 50, 50, 70, 120, ["agua", "planta", "hielo"], "0")

meowth = pokemon(52, "Meowth", ["normal"], "Es un Pokémon nocturno que usa sus garras afiladas para cazar. Tiene un gusto particular por las monedas brillantes.", 40, 4.2, "recogida", ["macho", "hembra"], 40, 45, 35, 40, 40, 90, ["lucha"], "Persian")

persian = pokemon(53, "Persian", ["normal"], "Tiene una elegancia natural. Suele vivir en ciudades, donde caza pequeños Pokémon para alimentarse.", 100, 32.0, "flexibilidad", ["macho", "hembra"], 65, 70, 60, 65, 65, 115, ["lucha"], "0")

psyduck = pokemon(54, "Psyduck", ["agua"], "Sufre de dolores de cabeza constantes, que le otorgan misteriosos poderes psíquicos. Es algo torpe.", 80, 19.6, "humedad", ["macho", "hembra"], 50, 52, 48, 65, 50, 55, ["eléctrico", "planta"], "Golduck")

golduck = pokemon(55, "Golduck", ["agua"], "Es rápido y muy ágil en el agua. Se cree que tiene grandes poderes psíquicos.", 170, 76.6, "humedad", ["macho", "hembra"], 80, 82, 78, 95, 80, 85, ["eléctrico", "planta"], "0")

mankey = pokemon(56, "Mankey", ["lucha"], "Es muy temperamental. Sus ataques son rápidos y poderosos, pero no tiene control sobre su temperamento.", 50, 28.0, "espíritu vital", ["macho", "hembra"], 40, 80, 35, 35, 45, 70, ["psíquico", "volador", "hada"], "Primeape")

primeape = pokemon(57, "Primeape", ["lucha"], "Siempre está furioso. Su ira es tan grande que no se detiene hasta derrotar a su oponente.", 100, 32.0, "espíritu vital", ["macho", "hembra"], 65, 105, 60, 60, 70, 95, ["psíquico", "volador", "hada"], "0")

growlithe = pokemon(58, "Growlithe", ["fuego"], "Es muy leal y protegerá a su entrenador a toda costa. Su olfato es extremadamente agudo.", 70, 19.0, "intimidación", ["macho", "hembra"], 55, 70, 45, 70, 50, 60, ["agua", "tierra", "roca"], "Arcanine")

arcanine = pokemon(59, "Arcanine", ["fuego"], "Es un Pokémon majestuoso conocido por su velocidad y su lealtad. Su rugido puede ser escuchado a kilómetros.", 190, 155.0, "intimidación", ["macho", "hembra"], 90, 110, 80, 100, 80, 95, ["agua", "tierra", "roca"], "0")

poliwag = pokemon(60, "Poliwag", ["agua"], "Aunque tiene patas, prefiere nadar en el agua. Su piel es tan delgada que se puede ver su interior.", 60, 12.4, "absorbe agua", ["macho", "hembra"], 40, 50, 40, 40, 40, 90, ["eléctrico", "planta"], "Poliwhirl")

poliwhirl = pokemon(61, "Poliwhirl", ["agua"], "Es conocido por su agilidad bajo el agua. Sus espirales hipnóticas pueden confundir a sus enemigos.", 100, 20.0, "absorbe agua", ["macho", "hembra"], 65, 65, 65, 50, 50, 90, ["eléctrico", "planta"], "Poliwrath")

poliwrath = pokemon(62, "Poliwrath", ["agua", "lucha"], "Sus músculos bien desarrollados le permiten nadar durante días sin cansarse.", 130, 54.0, "absorb. agua", ["macho", "hembra"], 90, 95, 95, 70, 90, 70, ["eléctrico", "planta", "psíquico", "volador"], "0")

abra = pokemon(63, "Abra", ["psíquico"], "Abra duerme 18 horas al día. Incluso mientras duerme, usa sus poderes psíquicos para defenderse.", 90, 19.5, "sincronía", ["macho", "hembra"], 25, 20, 15, 105, 55, 90, ["bicho", "fantasma", "siniestro"], "Kadabra")

kadabra = pokemon(64, "Kadabra", ["psíquico"], "Se dice que Kadabra apareció cuando un niño que tenía habilidades psíquicas despertó su poder.", 130, 56.5, "sincronía", ["macho", "hembra"], 40, 35, 30, 120, 70, 105, ["bicho", "fantasma", "siniestro"], "Alakazam")

alakazam = pokemon(65, "Alakazam", ["psíquico"], "Tiene un cerebro increíblemente desarrollado. Se dice que su memoria es infinita.", 150, 48.0, "sincronía", ["macho", "hembra"], 55, 50, 45, 135, 95, 120, ["bicho", "fantasma", "siniestro"], "0")

machop = pokemon(66, "Machop", ["lucha"], "Le encanta entrenar sus músculos. Puede levantar objetos que son muchas veces su propio peso.", 80, 19.5, "agallas", ["macho", "hembra"], 70, 80, 50, 35, 35, 35, ["psíquico", "volador", "hada"], "Machoke")

machoke = pokemon(67, "Machoke", ["lucha"], "Es tan fuerte que tiene que controlar su poder para no causar daño a otros Pokémon.", 150, 70.5, "agallas", ["macho", "hembra"], 80, 100, 70, 50, 60, 45, ["psíquico", "volador", "hada"], "Machamp")

machamp = pokemon(68, "Machamp", ["lucha"], "Tiene cuatro brazos increíblemente fuertes. Puede realizar un sinfín de tareas a la vez.", 160, 130.0, "agallas", ["macho", "hembra"], 90, 130, 80, 65, 85, 55, ["psíquico", "volador", "hada"], "0")

bellsprout = pokemon(69, "Bellsprout", ["planta", "veneno"], "Su cuerpo flexible le permite moverse en cualquier dirección para atrapar insectos.", 70, 4.0, "clorofila", ["macho", "hembra"], 50, 75, 35, 70, 30, 40, ["fuego", "volador", "hielo", "psíquico"], "Weepinbell")

weepinbell = pokemon(70, "Weepinbell", ["planta", "veneno"], "Segrega una sustancia ácida para disolver a su presa. Se cuelga de las ramas para dormir.", 100, 6.4, "clorofila", ["macho", "hembra"], 65, 90, 50, 85, 45, 55, ["fuego", "volador", "hielo", "psíquico"], "Victreebel")

victreebel = pokemon(71, "Victreebel", ["planta", "veneno"], "La planta en su cuerpo puede digerir cualquier cosa, incluso objetos metálicos.", 170, 15.5, "clorofila", ["macho", "hembra"], 80, 105, 65, 100, 60, 70, ["fuego", "volador", "hielo", "psíquico"], "0")

tentacool = pokemon(72, "Tentacool", ["agua", "veneno"], "Flota en el agua y usa sus tentáculos para atrapar presas. Sus ataques pueden envenenar fácilmente.", 90, 45.5, "cura lluvia", ["macho", "hembra"], 40, 40, 35, 50, 100, 70, ["eléctrico", "psíquico", "tierra"], "Tentacruel")

tentacruel = pokemon(73, "Tentacruel", ["agua", "veneno"], "Sus tentáculos liberan toxinas peligrosas que pueden inmovilizar a su presa. Es un nadador veloz.", 160, 55.0, "cura lluvia", ["macho", "hembra"], 80, 70, 65, 80, 120, 100, ["eléctrico", "psíquico", "tierra"], "0")

geodude = pokemon(74, "Geodude", ["roca", "tierra"], "Se parece tanto a una roca que a menudo es pisado accidentalmente. Es muy resistente.", 40, 20.0, "cabeza roca", ["macho", "hembra"], 40, 80, 100, 30, 30, 20, ["agua", "planta", "hielo", "lucha", "tierra", "acero"], "Graveler")

graveler = pokemon(75, "Graveler", ["roca", "tierra"], "Rueda por las laderas de las montañas y aplasta todo a su paso. Su cuerpo es extremadamente duro.", 100, 105.0, "cabeza roca", ["macho", "hembra"], 55, 95, 115, 45, 45, 35, ["agua", "planta", "hielo", "lucha", "tierra", "acero"], "Golem")

golem = pokemon(76, "Golem", ["roca", "tierra"], "Su cuerpo es tan duro como el granito. Puede rodar por terrenos accidentados a gran velocidad.", 140, 300.0, "cabeza roca", ["macho", "hembra"], 80, 120, 130, 55, 65, 45, ["agua", "planta", "hielo", "lucha", "tierra", "acero"], "0")

ponyta = pokemon(77, "Ponyta", ["fuego"], "Corre a gran velocidad, impulsado por sus patas fuertes y resistentes. Su melena ardiente quema a quien se acerque demasiado.", 100, 30.0, "fuga", ["macho", "hembra"], 50, 85, 55, 65, 65, 90, ["agua", "roca", "tierra"], "Rapidash")

rapidash = pokemon(78, "Rapidash", ["fuego"], "Es conocido por su increíble velocidad. Se dice que puede alcanzar los 240 km/h.", 170, 95.0, "fuga", ["macho", "hembra"], 65, 100, 70, 80, 80, 105, ["agua", "roca", "tierra"], "0")

slowpoke = pokemon(79, "Slowpoke", ["agua", "psíquico"], "Es extremadamente lento y no se da cuenta de lo que sucede a su alrededor. Si pierde su cola, le crecerá otra.", 120, 36.0, "ritmo propio", ["macho", "hembra"], 90, 65, 65, 40, 40, 15, ["eléctrico", "bicho", "siniestro", "fantasma"], "Slowbro")

slowbro = pokemon(80, "Slowbro", ["agua", "psíquico"], "Cuando la cola de Slowpoke es mordida por un Shellder, se transforma en Slowbro. No es consciente del dolor.", 160, 78.5, "ritmo propio", ["macho", "hembra"], 95, 75, 110, 100, 80, 30, ["eléctrico", "bicho", "siniestro", "fantasma"], "0")

magnemite = pokemon(81, "Magnemite", ["eléctrico", "acero"], "Es un Pokémon que flota en el aire gracias al magnetismo. Su cuerpo emite potentes ondas magnéticas.", 30, 6.0, "imán", ["ninguno"], 25, 35, 70, 95, 55, 45, ["fuego", "tierra", "lucha"], "Magneton")

magneton = pokemon(82, "Magneton", ["eléctrico", "acero"], "Está formado por tres Magnemite unidos por campos magnéticos. Puede causar apagones eléctricos.", 100, 60.0, "imán", ["ninguno"], 50, 60, 95, 120, 70, 70, ["fuego", "tierra", "lucha"], "0")

farfetchd = pokemon(83, "Farfetch'd", ["normal", "volador"], "Farfetch'd siempre lleva un puerro, que usa como arma en combate. Es muy territorial.", 80, 15.0, "impasible", ["macho", "hembra"], 52, 90, 55, 58, 62, 60, ["eléctrico", "hielo", "roca"], "0")

doduo = pokemon(84, "Doduo", ["normal", "volador"], "Tiene dos cabezas que piensan independientemente. Si una duerme, la otra permanece alerta.", 140, 39.2, "fuga", ["macho", "hembra"], 35, 85, 45, 35, 35, 75, ["eléctrico", "hielo", "roca"], "Dodrio")

dodrio = pokemon(85, "Dodrio", ["normal", "volador"], "Sus tres cabezas pueden compartir pensamientos entre ellas. Puede correr a gran velocidad.", 180, 85.2, "fuga", ["macho", "hembra"], 60, 110, 70, 60, 60, 100, ["eléctrico", "hielo", "roca"], "0")

seel = pokemon(86, "Seel", ["agua"], "Le gusta nadar en aguas frías. Usa su cuerno afilado para romper el hielo cuando necesita aire.", 110, 90.0, "hidración", ["macho", "hembra"], 65, 45, 55, 45, 70, 45, ["eléctrico", "planta"], "Dewgong")

dewgong = pokemon(87, "Dewgong", ["agua", "hielo"], "Dewgong nada grácilmente en aguas heladas. Su piel gruesa lo protege del frío extremo.", 170, 120.0, "hidración", ["macho", "hembra"], 90, 70, 80, 70, 95, 70, ["eléctrico", "planta", "lucha", "roca"], "0")

grimer = pokemon(88, "Grimer", ["veneno"], "Está formado por barro tóxico y residuos industriales. Deja un rastro de suciedad a su paso.", 90, 30.0, "hedor", ["macho", "hembra"], 80, 80, 50, 40, 50, 25, ["psíquico", "tierra"], "Muk")

muk = pokemon(89, "Muk", ["veneno"], "Muk está compuesto de residuos altamente tóxicos. Su olor es lo suficientemente fuerte como para enfermar a otros Pokémon.", 160, 30.0, "hedor", ["macho", "hembra"], 105, 105, 75, 65, 100, 50, ["psíquico", "tierra"], "0")

shellder = pokemon(90, "Shellder", ["agua"], "Vive adherido a las rocas del fondo del mar. Su caparazón es extremadamente duro y lo protege de los depredadores.", 30, 4.0, "caparazón", ["macho", "hembra"], 30, 65, 100, 45, 25, 40, ["eléctrico", "planta"], "Cloyster")

cloyster = pokemon(91, "Cloyster", ["agua", "hielo"], "Su caparazón es tan duro como el diamante. Cloyster se cierra completamente para resistir cualquier ataque.", 150, 132.5, "caparazón", ["macho", "hembra"], 50, 95, 180, 85, 45, 70, ["eléctrico", "planta", "lucha", "roca"], "0")

gastly = pokemon(92, "Gastly", ["fantasma", "veneno"], "Este Pokémon está compuesto casi completamente de gas. Puede atravesar objetos sólidos.", 130, 0.1, "levitación", ["ninguno"], 30, 35, 30, 100, 35, 80, ["psíquico", "fantasma", "siniestro"], "Haunter")

haunter = pokemon(93, "Haunter", ["fantasma", "veneno"], "Haunter se esconde en la oscuridad y acecha a sus presas. Sus manos gaseosas pueden provocar pesadillas.", 160, 0.1, "levitación", ["ninguno"], 45, 50, 45, 115, 55, 95, ["psíquico", "fantasma", "siniestro"], "Gengar")

gengar = pokemon(94, "Gengar", ["fantasma", "veneno"], "Gengar se deleita causando miedo en las personas y Pokémon. Su risa malévola se escucha en la oscuridad.", 150, 40.5, "levitación", ["ninguno"], 60, 65, 60, 130, 75, 110, ["psíquico", "fantasma", "siniestro"], "0")

onix = pokemon(95, "Onix", ["roca", "tierra"], "Onix excava túneles a gran velocidad. Su cuerpo rocoso es increíblemente duro.", 880, 210.0, "cabeza roca", ["macho", "hembra"], 35, 45, 160, 30, 45, 70, ["agua", "planta", "hielo", "lucha", "acero"], "Steelix")

drowzee = pokemon(96, "Drowzee", ["psíquico"], "Es capaz de comerse los sueños de las personas. Cuanto más dulce es el sueño, mejor sabe para Drowzee.", 100, 32.4, "insomnio", ["macho", "hembra"], 60, 48, 45, 43, 90, 42, ["bicho", "fantasma", "siniestro"], "Hypno")

hypno = pokemon(97, "Hypno", ["psíquico"], "Hypno usa su péndulo para hipnotizar a sus enemigos. Puede causar sueños o pesadillas.", 160, 75.6, "insomnio", ["macho", "hembra"], 85, 73, 70, 73, 115, 67, ["bicho", "fantasma", "siniestro"], "0")

krabby = pokemon(98, "Krabby", ["agua"], "Krabby usa sus grandes pinzas para atrapar a sus presas. Puede moverse lateralmente a gran velocidad.", 40, 6.5, "caparazón", ["macho", "hembra"], 30, 105, 90, 25, 25, 50, ["eléctrico", "planta"], "Kingler")

kingler = pokemon(99, "Kingler", ["agua"], "Kingler tiene una pinza enorme que usa para triturar a sus enemigos. Aunque es muy pesada, es increíblemente poderosa.", 130, 60.0, "caparazón", ["macho", "hembra"], 55, 130, 115, 50, 50, 75, ["eléctrico", "planta"], "0")

voltorb = pokemon(100, "Voltorb", ["eléctrico"], "Este Pokémon es una esfera misteriosa que puede explotar de repente. Se dice que nació de una Poké Ball.", 50, 10.4, "levitación", ["ninguno"], 40, 30, 50, 55, 55, 100, ["tierra"], "Electrode")

electrode = pokemon(101, "Electrode", ["eléctrico"], "Es un Pokémon que siempre parece estar al borde de explotar. Es conocido por su velocidad y su naturaleza impredecible.", 120, 66.6, "levitación", ["ninguno"], 60, 50, 70, 80, 80, 150, ["tierra"], "0")

exeggcute = pokemon(102, "Exeggcute", ["planta", "psíquico"], "Exeggcute parece un grupo de huevos, pero es una especie de semillas que se agrupan.", 40, 2.5, "cosecha", ["macho", "hembra"], 60, 40, 80, 60, 45, 40, ["bicho", "fuego", "hielo", "veneno", "volador", "fantasma", "siniestro"], "Exeggutor")

exeggutor = pokemon(103, "Exeggutor", ["planta", "psíquico"], "Conocido como el Pokémon árbol, Exeggutor puede atacar desde diferentes direcciones gracias a sus cabezas múltiples.", 200, 120.0, "cosecha", ["macho", "hembra"], 95, 95, 85, 125, 75, 55, ["bicho", "fuego", "hielo", "veneno", "volador", "fantasma", "siniestro"], "0")

cubone = pokemon(104, "Cubone", ["tierra"], "Cubone es un Pokémon que lleva el cráneo de su madre como casco. Llora su pérdida a menudo por las noches.", 40, 6.5, "cabeza roca", ["macho", "hembra"], 50, 50, 95, 40, 50, 35, ["agua", "hielo", "planta"], "Marowak")

marowak = pokemon(105, "Marowak", ["tierra"], "Marowak ha superado la tristeza por la muerte de su madre y se ha vuelto fuerte y resistente. Es un luchador feroz.", 100, 45.0, "cabeza roca", ["macho", "hembra"], 60, 80, 110, 50, 80, 45, ["agua", "hielo", "planta"], "0")

hitmonlee = pokemon(106, "Hitmonlee", ["lucha"], "Hitmonlee tiene piernas flexibles que se estiran y retraen a voluntad, lo que le permite lanzar patadas desde cualquier ángulo.", 150, 49.8, "flexibilidad", ["macho"], 50, 120, 53, 35, 110, 87, ["psíquico", "volador", "hada"], "0")

hitmonchan = pokemon(107, "Hitmonchan", ["lucha"], "Hitmonchan posee la capacidad de lanzar puñetazos increíblemente rápidos, como si tuviera guantes de boxeo.", 140, 50.2, "puño férreo", ["macho"], 50, 105, 79, 35, 110, 76, ["psíquico", "volador", "hada"], "0")

lickitung = pokemon(108, "Lickitung", ["normal"], "Lickitung usa su larga lengua para capturar presas y lamer todo lo que encuentre. Su saliva tiene propiedades únicas.", 120, 65.5, "despiste", ["macho", "hembra"], 90, 55, 75, 60, 75, 30, ["lucha"], "0")

koffing = pokemon(109, "Koffing", ["veneno"], "Koffing flota en el aire gracias a los gases venenosos en su cuerpo. Puede liberar explosiones de gas cuando está en peligro.", 60, 1.0, "levitación", ["macho", "hembra"], 40, 65, 95, 60, 45, 35, ["psíquico", "tierra"], "Weezing")

weezing = pokemon(110, "Weezing", ["veneno"], "Weezing es una combinación de dos Koffing que se han fusionado. Produce gases tóxicos aún más potentes.", 120, 9.5, "levitación", ["macho", "hembra"], 65, 90, 120, 85, 70, 60, ["psíquico", "tierra"], "0")

rhyhorn = pokemon(111, "Rhyhorn", ["tierra", "roca"], "Rhyhorn tiene una piel extremadamente dura y un cuerno afilado. Puede derribar edificios con su carga.", 100, 115.0, "cabeza roca", ["macho", "hembra"], 80, 85, 95, 30, 30, 25, ["agua", "hielo", "planta", "acero", "tierra", "lucha"], "Rhydon")

rhydon = pokemon(112, "Rhydon", ["tierra", "roca"], "Rhydon usa su gruesa piel y fuerza para luchar contra sus enemigos. Puede resistir temperaturas extremas.", 190, 120.0, "cabeza roca", ["macho", "hembra"], 105, 130, 120, 45, 45, 40, ["agua", "hielo", "planta", "acero", "tierra", "lucha"], "0")

chansey = pokemon(113, "Chansey", ["normal"], "Chansey es extremadamente amable y comparte sus nutritivos huevos con los enfermos y heridos.", 110, 34.6, "cura natural", ["hembra"], 250, 5, 5, 35, 105, 50, ["lucha"], "Blissey")

tangela = pokemon(114, "Tangela", ["planta"], "Tangela está cubierto de enredaderas azules que lo protegen de los ataques. Si se pierden, rápidamente vuelven a crecer.", 100, 35.0, "clorofila", ["macho", "hembra"], 65, 55, 115, 100, 40, 60, ["fuego", "hielo", "volador", "veneno", "bicho"], "0")

kangaskhan = pokemon(115, "Kangaskhan", ["normal"], "Kangaskhan cuida celosamente a su cría en su bolsa. Ataca ferozmente para proteger a sus pequeños.", 220, 80.0, "fuerza bruta", ["hembra"], 105, 95, 80, 40, 80, 90, ["lucha"], "0")

horsea = pokemon(116, "Horsea", ["agua"], "Horsea expulsa agua a alta presión para defenderse y cazar. Se mueve rápidamente en el agua para escapar de los depredadores.", 40, 8.0, "nado rápido", ["macho", "hembra"], 30, 40, 70, 70, 25, 60, ["eléctrico", "planta"], "Seadra")

seadra = pokemon(117, "Seadra", ["agua"], "Seadra es un nadador rápido que puede disparar agua a alta velocidad. Sus escamas son resistentes a los ataques.", 120, 25.0, "nado rápido", ["macho", "hembra"], 55, 65, 95, 95, 45, 85, ["eléctrico", "planta"], "Kingdra")

goldeen = pokemon(118, "Goldeen", ["agua"], "Goldeen nada grácilmente en ríos y lagos. Su cuerno puntiagudo puede perforar rocas y otros objetos duros.", 60, 15.0, "nado rápido", ["macho", "hembra"], 45, 67, 60, 35, 50, 63, ["eléctrico", "planta"], "Seaking")

seaking = pokemon(119, "Seaking", ["agua"], "Seaking es conocido por perforar rocas con su cuerno afilado. Es un nadador fuerte y territorial.", 130, 39.0, "nado rápido", ["macho", "hembra"], 80, 92, 65, 65, 80, 68, ["eléctrico", "planta"], "0")

staryu = pokemon(120, "Staryu", ["agua"], "Staryu tiene la capacidad de regenerarse si se le cortan las extremidades. Su núcleo central brilla con intensidad.", 80, 34.5, "cura natural", ["ninguno"], 30, 45, 55, 70, 55, 85, ["eléctrico", "planta"], "Starmie")

starmie = pokemon(121, "Starmie", ["agua", "psíquico"], "Starmie emite una extraña luz desde su núcleo en forma de joya. Es conocido por su capacidad telepática.", 110, 80.0, "cura natural", ["ninguno"], 60, 75, 85, 100, 85, 115, ["eléctrico", "planta", "bicho", "fantasma", "siniestro"], "0")

mr_mime = pokemon(122, "Mr. Mime", ["psíquico", "hada"], "Mr. Mime es experto en crear barreras invisibles con sus habilidades de mimo, lo que le permite defenderse de ataques.", 130, 54.5, "filtro", ["macho", "hembra"], 40, 45, 65, 100, 120, 90, ["acero", "veneno", "fantasma"], "0")

scyther = pokemon(123, "Scyther", ["bicho", "volador"], "Scyther corta el aire a gran velocidad con sus afiladas cuchillas. Es extremadamente rápido y mortal en combate.", 150, 56.0, "experto", ["macho", "hembra"], 70, 110, 80, 55, 80, 105, ["fuego", "eléctrico", "volador", "roca"], "Scizor")

jynx = pokemon(124, "Jynx", ["hielo", "psíquico"], "Jynx baila para comunicarse, y su estilo hipnotizante de movimiento puede confundir y encantar a sus oponentes.", 140, 40.6, "seco velo", ["hembra"], 65, 50, 35, 115, 95, 95, ["acero", "bicho", "roca", "fuego", "fantasma", "siniestro"], "0")

electabuzz = pokemon(125, "Electabuzz", ["eléctrico"], "Electabuzz se rodea de electricidad estática, lo que le permite paralizar a sus oponentes con solo tocarlos.", 110, 30.0, "electricidad estática", ["macho", "hembra"], 65, 83, 57, 95, 85, 105, ["tierra"], "Electivire")

magmar = pokemon(126, "Magmar", ["fuego"], "Magmar emite un calor tan intenso que su cuerpo brilla como una llama viva. Es capaz de derretir cualquier cosa a su alrededor.", 130, 44.5, "cuerpo llama", ["macho", "hembra"], 65, 95, 57, 100, 85, 93, ["agua", "roca", "tierra"], "Magmortar")

pinsir = pokemon(127, "Pinsir", ["bicho"], "Pinsir es capaz de atrapar a sus presas con sus afiladas pinzas y levantarlas del suelo con facilidad.", 150, 55.0, "experto", ["macho", "hembra"], 65, 125, 100, 55, 70, 85, ["fuego", "volador", "roca"], "0")

tauros = pokemon(128, "Tauros", ["normal"], "Tauros es un Pokémon extremadamente agresivo que embiste a sus enemigos con una fuerza arrolladora.", 140, 88.4, "intimidación", ["macho"], 75, 100, 95, 40, 70, 110, ["lucha"], "0")

magikarp = pokemon(129, "Magikarp", ["agua"], "Magikarp es un Pokémon débil y torpe, conocido por su incapacidad para hacer mucho más que salpicar agua.", 90, 10.0, "nado rápido", ["macho", "hembra"], 20, 10, 55, 15, 20, 80, ["eléctrico", "planta"], "Gyarados")

gyarados = pokemon(130, "Gyarados", ["agua", "volador"], "Gyarados es temido por su naturaleza destructiva. Es capaz de destruir ciudades enteras con su furia.", 650, 235.0, "intimidación", ["macho", "hembra"], 95, 125, 79, 60, 100, 81, ["eléctrico", "roca"], "0")

lapras = pokemon(131, "Lapras", ["agua", "hielo"], "Lapras es conocido por su amabilidad y por ayudar a los humanos a cruzar grandes extensiones de agua.", 250, 220.0, "absorbe agua", ["macho", "hembra"], 130, 85, 80, 85, 95, 60, ["eléctrico", "lucha", "planta", "roca"], "0")

ditto = pokemon(132, "Ditto", ["normal"], "Ditto tiene la capacidad de transformarse en cualquier otro Pokémon, copiando incluso sus movimientos.", 30, 4.0, "flexibilidad", ["ninguno"], 48, 48, 48, 48, 48, 48, ["lucha"], "0")

eevee = pokemon(133, "Eevee", ["normal"], "Eevee tiene un ADN inestable, lo que le permite evolucionar en múltiples formas diferentes dependiendo de su entorno.", 30, 6.5, "fuga", ["macho", "hembra"], 55, 55, 50, 45, 65, 55, ["lucha"], ["Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon", "Leafeon", "Glaceon", "Sylveon"])

vaporeon = pokemon(134, "Vaporeon", ["agua"], "Vaporeon tiene la capacidad de disolver su cuerpo en agua, lo que le permite camuflarse bajo la superficie.", 100, 29.0, "absorbe agua", ["macho", "hembra"], 130, 65, 60, 110, 95, 65, ["eléctrico", "planta"], "0")

jolteon = pokemon(135, "Jolteon", ["eléctrico"], "Jolteon tiene celdas en su cuerpo que generan electricidad estática, lo que lo convierte en un Pokémon muy rápido.", 100, 24.5, "absorbe electricidad", ["macho", "hembra"], 65, 65, 60, 110, 95, 130, ["tierra"], "0")

flareon = pokemon(136, "Flareon", ["fuego"], "Flareon tiene una temperatura corporal extremadamente alta y puede exhalar aire ardiente que alcanza los 1,600 grados.", 90, 25.0, "absorbe fuego", ["macho", "hembra"], 65, 130, 60, 95, 110, 65, ["agua", "roca", "tierra"], "0")

porygon = pokemon(137, "Porygon", ["normal"], "Porygon es un Pokémon artificial que puede entrar en sistemas informáticos y modificar datos.", 80, 36.5, "descarga", ["ninguno"], 65, 60, 70, 85, 75, 40, ["lucha"], "Porygon2")

omanyte = pokemon(138, "Omanyte", ["roca", "agua"], "Omanyte es un antiguo Pokémon fósil que vivió en el mar hace millones de años. Sus tentáculos le permiten nadar.", 40, 7.5, "nado rápido", ["macho", "hembra"], 35, 40, 100, 90, 55, 35, ["eléctrico", "planta", "lucha", "tierra"], "Omastar")

omastar = pokemon(139, "Omastar", ["roca", "agua"], "Omastar es conocido por su fuerte mandíbula que puede romper rocas y sus tentáculos que capturan a sus presas.", 110, 35.0, "nado rápido", ["macho", "hembra"], 70, 60, 125, 115, 70, 55, ["eléctrico", "planta", "lucha", "tierra"], "0")

kabuto = pokemon(140, "Kabuto", ["roca", "agua"], "Kabuto es un Pokémon fósil que ha permanecido sin cambios durante 300 millones de años.", 50, 11.5, "armadura batalla", ["macho", "hembra"], 30, 80, 90, 55, 45, 55, ["eléctrico", "planta", "lucha", "tierra"], "Kabutops")

kabutops = pokemon(141, "Kabutops", ["roca", "agua"], "Kabutops utiliza sus afiladas guadañas para cortar a sus presas antes de succionarles los fluidos.", 130, 40.5, "armadura batalla", ["macho", "hembra"], 60, 115, 105, 65, 70, 80, ["eléctrico", "planta", "lucha", "tierra"], "0")

aerodactyl = pokemon(142, "Aerodactyl", ["roca", "volador"], "Aerodactyl era el rey de los cielos en la era prehistórica, conocido por su agresividad y poder destructivo.", 180, 59.0, "presión", ["macho", "hembra"], 80, 105, 65, 60, 75, 130, ["eléctrico", "hielo", "agua", "roca", "acero"], "0")

snorlax = pokemon(143, "Snorlax", ["normal"], "Snorlax pasa la mayor parte del tiempo durmiendo y solo se despierta para comer. Es capaz de consumir grandes cantidades de comida.", 210, 460.0, "inmunidad", ["macho", "hembra"], 160, 110, 65, 65, 110, 30, ["lucha"], "0")

articuno = pokemon(144, "Articuno", ["hielo", "volador"], "Articuno es un legendario Pokémon conocido por su capacidad de controlar el hielo. Es raro verlo en la naturaleza.", 170, 55.4, "presión", ["ninguno"], 90, 85, 100, 95, 125, 85, ["fuego", "eléctrico", "roca", "acero"], "0")

zapdos = pokemon(145, "Zapdos", ["eléctrico", "volador"], "Zapdos es un legendario que controla los rayos y tormentas eléctricas. Es conocido por ser extremadamente poderoso.", 160, 52.6, "presión", ["ninguno"], 90, 90, 85, 125, 90, 100, ["hielo", "roca"], "0")

moltres = pokemon(146, "Moltres", ["fuego", "volador"], "Moltres es un legendario que controla el fuego. Sus alas brillan con intensidad cuando está en combate.", 200, 60.0, "presión", ["ninguno"], 90, 100, 90, 125, 85, 90, ["agua", "eléctrico", "roca"], "0")

dratini = pokemon(147, "Dratini", ["dragón"], "Dratini vive en cuerpos de agua profundos y se dice que su piel desprende una energía mística.", 180, 3.3, "mudar", ["macho", "hembra"], 41, 64, 45, 50, 50, 50, ["hielo", "hada", "dragón"], "Dragonair")

dragonair = pokemon(148, "Dragonair", ["dragón"], "Dragonair puede controlar el clima con la energía que acumula en su cuerpo serpenteante.", 400, 16.5, "mudar", ["macho", "hembra"], 61, 84, 65, 70, 70, 70, ["hielo", "hada", "dragón"], "Dragonite")

dragonite = pokemon(149, "Dragonite", ["dragón", "volador"], "Dragonite es conocido por su gran tamaño y su increíble velocidad a pesar de su apariencia robusta.", 220, 210.0, "foco interno", ["macho", "hembra"], 91, 134, 95, 100, 100, 80, ["hielo", "roca", "hada", "dragón"], "0")

mewtwo = pokemon(150, "Mewtwo", ["psíquico"], "Mewtwo es un Pokémon creado por manipulación genética. Es extremadamente poderoso y tiene una actitud feroz.", 200, 122.0, "presión", ["ninguno"], 106, 110, 90, 154, 90, 130, ["bicho", "fantasma", "siniestro"], "0")

mew = pokemon(151, "Mew", ["psíquico"], "Mew es un Pokémon extremadamente raro y tiene la capacidad de aprender cualquier ataque de los demás Pokémon.", 40, 4.0, "sincronía", ["ninguno"], 100, 100, 100, 100, 100, 100, ["bicho", "fantasma", "siniestro"], "0")

opciones = [
    "SALIR", "1) Bulbasaur", "2) Ivysaur", "3) Venusaur", "4) Charmander", "5) Charmeleon", "6) Charizard",
    "7) Squirtle", "8) Wartortle", "9) Blastoise", "10) Caterpie", "11) Metapod", "12) Butterfree",
    "13) Weedle", "14) Kakuna", "15) Beedrill", "16) Pidgey", "17) Pidgeotto", "18) Pidgeot",
    "19) Rattata", "20) Raticate", "21) Spearow", "22) Fearow", "23) Ekans", "24) Arbok",
    "25) Pikachu", "26) Raichu", "27) Sandshrew", "28) Sandslash", "29) Nidoran♀", "30) Nidorina",
    "31) Nidoqueen", "32) Nidoran♂", "33) Nidorino", "34) Nidoking", "35) Clefairy", "36) Clefable",
    "37) Vulpix", "38) Ninetales", "39) Jigglypuff", "40) Wigglytuff", "41) Zubat", "42) Golbat",
    "43) Oddish", "44) Gloom", "45) Vileplume", "46) Paras", "47) Parasect", "48) Venonat",
    "49) Venomoth", "50) Diglett", "51) Dugtrio", "52) Meowth", "53) Persian", "54) Psyduck",
    "55) Golduck", "56) Mankey", "57) Primeape", "58) Growlithe", "59) Arcanine", "60) Poliwag",
    "61) Poliwhirl", "62) Poliwrath", "63) Abra", "64) Kadabra", "65) Alakazam", "66) Machop",
    "67) Machoke", "68) Machamp", "69) Bellsprout", "70) Weepinbell", "71) Victreebel", "72) Tentacool",
    "73) Tentacruel", "74) Geodude", "75) Graveler", "76) Golem", "77) Ponyta", "78) Rapidash",
    "79) Slowpoke", "80) Slowbro", "81) Magnemite", "82) Magneton", "83) Farfetch'd", "84) Doduo",
    "85) Dodrio", "86) Seel", "87) Dewgong", "88) Grimer", "89) Muk", "90) Shellder", "91) Cloyster",
    "92) Gastly", "93) Haunter", "94) Gengar", "95) Onix", "96) Drowzee", "97) Hypno", "98) Krabby",
    "99) Kingler", "100) Voltorb", "101) Electrode", "102) Exeggcute", "103) Exeggutor", "104) Cubone",
    "105) Marowak", "106) Hitmonlee", "107) Hitmonchan", "108) Lickitung", "109) Koffing", "110) Weezing",
    "111) Rhyhorn", "112) Rhydon", "113) Chansey", "114) Tangela", "115) Kangaskhan", "116) Horsea",
    "117) Seadra", "118) Goldeen", "119) Seaking", "120) Staryu", "121) Starmie", "122) Mr. Mime",
    "123) Scyther", "124) Jynx", "125) Electabuzz", "126) Magmar", "127) Pinsir", "128) Tauros",
    "129) Magikarp", "130) Gyarados", "131) Lapras", "132) Ditto", "133) Eevee", "134) Vaporeon",
    "135) Jolteon", "136) Flareon", "137) Porygon", "138) Omanyte", "139) Omastar", "140) Kabuto",
    "141) Kabutops", "142) Aerodactyl", "143) Snorlax", "144) Articuno", "145) Zapdos", "146) Moltres",
    "147) Dratini", "148) Dragonair", "149) Dragonite", "150) Mewtwo", "151) Mew"
]

def poke_dex():
    print("#########-POKEDEX-###########\n##-NACIONAL--DE--KANTO-######")
    respuesta = inqui.select(message="De que pokemon quieres saber su informacion?", choices=opciones,).execute()

    print(f"has seleccionado: {respuesta}")
    if respuesta == opciones[0]:
        inicio()
    if respuesta == opciones[1]:
        bulbasaur.adios()
    if respuesta == opciones[2]:
        ivysaur.adios()
    if respuesta == opciones[3]:
        venusaur.adios()
    if respuesta == opciones[4]:
        charmander.adios()
    if respuesta == opciones[5]:
        charmeleon.adios()
    if respuesta == opciones[6]:
        charizard.adios()
    if respuesta == opciones[7]:
        squirtle.adios()
    if respuesta == opciones[8]:
        wartortle.adios()
    if respuesta == opciones[9]:  
        blastoise.adios()
    if respuesta == opciones[10]: 
        caterpie.adios()
    if respuesta == opciones[11]:
        metapod.adios()
    if respuesta == opciones[12]:
        butterfree.adios()
    if respuesta == opciones[13]:
        weedle.adios()
    if respuesta == opciones[14]:
        kakuna.adios()
    if respuesta == opciones[15]:
        beedrill.adios()
    if respuesta == opciones[16]:
        pidgey.adios()
    if respuesta == opciones[17]:
        pidgeot.adios()
    if respuesta == opciones[18]:
        pidgeotto.adios()
    if respuesta == opciones[19]:
        rattata.adios()
    if respuesta == opciones[20]:
        raticate.adios()
    if respuesta == opciones[21]:
        spearow.adios()
    if respuesta == opciones[22]:
        fearow.adios()
    if respuesta == opciones[23]:
        ekans.adios()
    if respuesta == opciones[24]:
        arbok.adios()
    if respuesta == opciones[25]:
        pikachu.adios()
    if respuesta == opciones[26]:
        raichu.adios()
    if respuesta == opciones[27]:
        sandshrew.adios()
    if respuesta == opciones[28]:
        sandslash.adios()
    if respuesta == opciones[29]:
        nidoran_femenino.adios()
    if respuesta == opciones[30]:
        nidorina.adios()
    if respuesta == opciones[31]:
        nidoqueen.adios()
    if respuesta == opciones[32]:
        nidoran_m.adios()
    if respuesta == opciones[33]:
        nidorino.adios()
    if respuesta == opciones[34]:
        nidoking.adios()
    if respuesta == opciones[35]:
        clefairy.adios()
    if respuesta == opciones[36]:
        clefable.adios()
    if respuesta == opciones[37]:
        vulpix.adios()
    if respuesta == opciones[38]:
        ninetales.adios()
    if respuesta == opciones[39]:
        jigglypuff.adios()
    if respuesta == opciones[40]:
        wigglytuff.adios()
    if respuesta == opciones[41]:
        zubat.adios()
    if respuesta == opciones[42]:
        golbat.adios()
    if respuesta == opciones[43]:
        oddish.adios()
    if respuesta == opciones[44]:
        gloom.adios()
    if respuesta == opciones[45]:
        vileplume.adios()
    if respuesta == opciones[46]:
        paras.adios()
    if respuesta == opciones[47]:
        parasect.adios()
    if respuesta == opciones[48]:
        venonat.adios()
    if respuesta == opciones[49]:
        venomoth.adios()
    if respuesta == opciones[50]:
        diglett.adios()
    if respuesta == opciones[51]:
        dugtrio.adios()
    if respuesta == opciones[52]:
        meowth.adios()
    if respuesta == opciones[53]:
        persian.adios()
    if respuesta == opciones[54]:
        psyduck.adios()
    if respuesta == opciones[55]:
        golduck.adios()
    if respuesta == opciones[56]:
        mankey.adios()
    if respuesta == opciones[57]:
        primeape.adios()
    if respuesta == opciones[58]:
        growlithe.adios()
    if respuesta == opciones[59]:
        arcanine.adios()
    if respuesta == opciones[60]:
        poliwag.adios()
    if respuesta == opciones[61]:
        poliwhirl.adios()
    if respuesta == opciones[62]:
        poliwrath.adios()
    if respuesta == opciones[63]:
        abra.adios()
    if respuesta == opciones[64]:
        kadabra.adios()
    if respuesta == opciones[65]:
        alakazam.adios()
    if respuesta == opciones[66]:
        machop.adios()
    if respuesta == opciones[67]:
        machoke.adios()
    if respuesta == opciones[68]:
        machamp.adios()
    if respuesta == opciones[69]:
        bellsprout.adios()
    if respuesta == opciones[70]:
        weepinbell.adios()
    if respuesta == opciones[71]:
        victreebel.adios()
    if respuesta == opciones[72]:
        tentacool.adios()
    if respuesta == opciones[73]:
        tentacruel.adios()
    if respuesta == opciones[74]:
        geodude.adios()
    if respuesta == opciones[75]:
        graveler.adios()
    if respuesta == opciones[76]:
        golem.adios()
    if respuesta == opciones[77]:
        ponyta.adios()
    if respuesta == opciones[78]:
        rapidash.adios()
    if respuesta == opciones[79]:
        slowpoke.adios()
    if respuesta == opciones[80]:
        slowbro.adios()
    if respuesta == opciones[81]:
        magnemite.adios()
    if respuesta == opciones[82]:
        magneton.adios()
    if respuesta == opciones[83]:
        farfetchd.adios()
    if respuesta == opciones[84]:
        doduo.adios()
    if respuesta == opciones[85]:
        dodrio.adios()
    if respuesta == opciones[86]:
        seel.adios()
    if respuesta == opciones[87]:
        dewgong.adios()
    if respuesta == opciones[88]:
        grimer.adios()
    if respuesta == opciones[89]:
        muk.adios()
    if respuesta == opciones[90]:
        shellder.adios()
    if respuesta == opciones[91]:
        cloyster.adios()
    if respuesta == opciones[92]:
        gastly.adios()
    if respuesta == opciones[93]:
        haunter.adios()
    if respuesta == opciones[94]:
        gengar.adios()
    if respuesta == opciones[95]:
        onix.adios()
    if respuesta == opciones[96]:
        drowzee.adios()
    if respuesta == opciones[97]:
        hypno.adios()
    if respuesta == opciones[98]:
        krabby.adios()
    if respuesta == opciones[99]:
        kingler.adios()
    if respuesta == opciones[100]:
        voltorb.adios()
    if respuesta == opciones[101]:
        electrode.adios()
    if respuesta == opciones[102]:
        exeggcute.adios()
    if respuesta == opciones[103]:
        exeggutor.adios()
    if respuesta == opciones[104]:
        cubone.adios()
    if respuesta == opciones[105]:
        marowak.adios()
    if respuesta == opciones[106]:
        hitmonlee.adios()
    if respuesta == opciones[107]:
        hitmonchan.adios()
    if respuesta == opciones[108]:
        lickitung.adios()
    if respuesta == opciones[109]:
        koffing.adios()
    if respuesta == opciones[110]:
        weezing.adios()
    if respuesta == opciones[111]:
        rhyhorn.adios()
    if respuesta == opciones[112]:
        rhydon.adios()
    if respuesta == opciones[113]:
        chansey.adios()
    if respuesta == opciones[114]:
        tangela.adios()
    if respuesta == opciones[115]:
        kangaskhan.adios()
    if respuesta == opciones[116]:
        horsea.adios()
    if respuesta == opciones[117]:
        seadra.adios()
    if respuesta == opciones[118]:
        goldeen.adios()
    if respuesta == opciones[119]:
        seaking.adios()
    if respuesta == opciones[120]:
        staryu.adios()
    if respuesta == opciones[121]:
        starmie.adios()
    if respuesta == opciones[122]:
        mr_mime.adios()
    if respuesta == opciones[123]:
        scyther.adios()
    if respuesta == opciones[124]:
        jynx.adios()
    if respuesta == opciones[125]:
        electabuzz.adios()
    if respuesta == opciones[126]:
        magmar.adios()
    if respuesta == opciones[127]:
        pinsir.adios()
    if respuesta == opciones[128]:
        tauros.adios()
    if respuesta == opciones[129]:
        magikarp.adios()
    if respuesta == opciones[130]:
        gyarados.adios()
    if respuesta == opciones[131]:
        lapras.adios()
    if respuesta == opciones[132]:
        ditto.adios()
    if respuesta == opciones[133]:
        eevee.adios()
    if respuesta == opciones[134]:
        vaporeon.adios()
    if respuesta == opciones[135]:
        jolteon.adios()
    if respuesta == opciones[136]:
        flareon.adios()
    if respuesta == opciones[137]:
        porygon.adios()
    if respuesta == opciones[138]:
        omanyte.adios()
    if respuesta == opciones[139]:
        omastar.adios()
    if respuesta == opciones[140]:
        kabuto.adios()
    if respuesta == opciones[141]:
        kabutops.adios()
    if respuesta == opciones[142]:
        aerodactyl.adios()
    if respuesta == opciones[143]:
        snorlax.adios()
    if respuesta == opciones[144]:
        articuno.adios()
    if respuesta == opciones[145]:
        zapdos.adios()
    if respuesta == opciones[146]:
        moltres.adios()
    if respuesta == opciones[147]:
        dratini.adios()
    if respuesta == opciones[148]:
        dragonair.adios()
    if respuesta == opciones[149]:
        dragonite.adios()
    if respuesta == opciones[150]:
        mewtwo.adios()
    if respuesta == opciones[151]:
        mew.adios()



def inicio():
    print("#######################################\n##############--INICIO--###############\n#######################################")
    elegir = ["Equipo Random", "Pokedex"]
    respuesta = inqui.select(message="Elige una opcion:", choices=elegir,).execute()
    if respuesta == elegir[0]:
        random_poke()
    if respuesta == elegir[1]:
        poke_dex()

inicio()
