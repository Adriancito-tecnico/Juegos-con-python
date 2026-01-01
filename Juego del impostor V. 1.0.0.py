import random
import time 

print ("Bienbenido al juego del Impostor")
print ("Escriba #Normas para ver las normas del juego, o scriba #Comandos para ver los comandos disponibles")

while True:

    command = input ("Escriba un comando: ")

# Comandos informativos

    if command == "#Normas":
        print ("---Normas del Juego \"El impostor\"---")
        print ("1. Minimo de 3 jugadores (recomendación: De 5 a 10 jugadores).")
        print ("2. 1 impostor por partida.")
        print ("3. Se eligirá una palabra por ronda que sabran todos menos el impostor (seran palabras sencillas).")
        print ("4. El impostor debera adivinar la palabra correcta para ganar.") 
        print ("5. Al jugador que le toque el turno debera decir una palabra relacionada con la palabra, sin que sea la misma e intentando que el impostor no la adivine y qeu no le boten a el.")
        print ("6. el impostor tiene que por el contexto de las palabras intentar adivinar la palabra y decir palabras para que no le pillen")
        print ("7. Cada ronda se hara una botacion para intentar eliminar al impostor.")
        print ("8. A cada jugador se le asignará un número único para identificarse durante el juego. Contando el 0 como jugador.")

        print (" ")

        print ("Escriba #Comandos para ver los comandos disponibles.")

    if command == "#Comandos":
        print ("---Comandos disponibles---")

        print ("Comandos informativos:")
        print ("#Normas - Muestra las normas del juego.")
        print ("#Comandos - Muestra los comandos disponibles.")

        print (" ")

        print ("Comandos de juego:")
        print ("!Iniciar - Inicia el juego.")
        print ("!Finalizar - Finaliza el juego.")
        print ("!Palabra - Muestra tu rol.")
        print ("!Listo - Tras colocar el comando \"!Palabra\" oculta tu palabra para el siguiente jugador.")
        print ("!Turno - Indica de quien es el turno actual y el sentido de preguntas.")
        print ("!votacion - Inicia la votación para eliminar a un jugador.")

#Comandos de juego

    if command == "!Iniciar":
        command = input ("Numero de jugadores: ")
    
        if command < "3":
            print ("Numero de jugadores insuficiente para iniciar el juego, se necesitan minimo 3 jugadores. Comience de nuevo.")
            continue

        print ("Cada jugador tiene que tener un numero del 1 al" , command + "(todos deven ser diferntes).")

        jugadores = int (command)
        impostor = random.randint (0, jugadores -1)

        palabras = ["gato", "perro", "casa", "coche", "arbol", "libro", "ciudad", "playa", "montaña", "río", "gato", "perro", "casa", "coche", "arbol", "libro", "ciudad", "playa", "montaña", "rio", "mesa", "silla", "cama", "puerta", "ventana", "llave", "reloj", "espejo", "sofa", "lampara", "vaso", "plato", "tenedor", "cuchara", "cuchillo", "sarten", "nevera", "horno", "toalla", "jabon", "cepillo", "maleta", "bolso", "cartera", "moneda", "papel", "lapiz", "pluma", "cuaderno", "tijeras", "martillo", "clavo", "escoba", "cuadro", "alfombra", "cortina", "almohada", "manta", "sabana", "botella", "bosque", "selva", "desierto", "valle", "lago", "mar", "oceano", "nube", "lluvia", "nieve", "viento", "fuego", "tierra", "piedra", "arena", "hierba", "flor", "jardin", "parque", "cielo", "sol", "luna", "estrella", "planeta", "rayo", "trueno", "isla", "costa", "volcan", "cueva", "caballo", "vaca", "oveja", "cerdo", "pollo", "pajaro", "pez", "leon", "tigre", "elefante", "jirafa", "mono", "oso", "lobo", "zorro", "conejo", "raton", "serpiente", "rana", "tortuga", "araña", "abeja", "mosca", "mariposa", "delfin", "tiburon", "ballena", "aguila", "buho", "pato", "cabeza", "cara", "ojo", "nariz", "boca", "oreja", "cuello", "hombro", "brazo", "codo", "mano", "dedo", "pecho", "espalda", "barriga", "pierna", "rodilla", "pie", "sangre", "hueso", "corazon", "pulmon", "cerebro", "piel", "pelo", "diente", "lengua", "uña", "salud", "medico", "pan", "agua", "leche", "cafe", "te", "jugo", "vino", "cerveza", "arroz", "pasta", "carne", "pescado", "huevo", "queso", "fruta", "manzana", "platano", "naranja", "uva", "limon", "fresa", "tomate", "patata", "cebolla", "ajo", "zanahoria", "ensalada", "sopa", "azucar", "sal", "aceite", "miel", "chocolate", "helado", "tiempo", "dia", "noche", "tarde", "mañana", "semana", "mes", "año", "siglo", "calendario", "trabajo", "escuela", "universidad", "calle", "avenida", "puente", "edificio", "tienda", "mercado", "banco", "hospital", "cine", "teatro", "museo", "musica", "arte", "deporte", "futbol", "viaje", "avion", "tren", "barco", "bicicleta", "camino", "pueblo", "gobierno", "familia", "amigo", "persona"]
        palabra_secreta = random.choice (palabras)

        time . sleep (2)
        print ("---El impostor y la palabra han sido elegidos---")
        time . sleep (0.5)

        for i in range(jugadores):
            command = input ("Escriba \"!Palabra\" para ver su palabra o si eres impostor: ")

            if command == "!Palabra":
                player_number = int (input ("Escriba su numero de jugador: "))
                if player_number > jugadores -1 or player_number < 0:
                    print ("Numero de jugador invalido. Reinicie el juego.")
                    break
                if player_number == impostor:
                    print ("Eres el impostor. Tu objetivo el abivinar la palabra correcta antes de que te eliminen.")
                    print (" ")
                    command = input ("Escriba \"!Listo\" para ocultar su rol: ")
                    if command == "!Listo":
                        for i in range(50):
                            print (" ")
                        print ("El rol esta oculto. Pase el dispositivo al siguiente jugador.")
                else:
                    print ("Tu palabra es: " , palabra_secreta)
                    print ("Recuerda no decir la palabra exacta durante el juego.")
                    print (" ")
                    
                    command = input ("Escriba \"!Listo\" para ocultar su rol: ")
                    if command == "!Listo":
                        for i in range(50):
                            print (" ")
                        print ("La palabra esta oculta. Pase el dispositivo al siguiente jugador.")

        command = input ("Escriba \"!Turno\" para ver de quien es el turno o \"!Votación\" para iniciar la votación: ")
        
        if command == "!Turno":
            turno = random.randint (1, jugadores )
            sentido = random.choice (["Sumando", "Restando"])
            print ("Es el turno del jugador" , turno , sentido)
        
    for i in range(jugadores -2):

        command = input ("Escriba \"!Votación\" para iniciar la votación: ")

        if command == "!Votación":

            resultado = {}

            for i in range(jugadores):
                resultado[i] = 0

            print ("---Iniciando la votación de el impostor---")
            for i in range(jugadores):
                eleccion = int(input(f"Jugador {i}, escriba el número de jugador al que vota: "))
                
                if eleccion in resultado:
                    resultado[eleccion] += 1
                    print(f"Voto registrado contra el jugador {eleccion}.")
                else:
                    print("Ese jugador no existe. Voto nulo.")
                
                time.sleep(1)

            print ("--- VOTACION FINALIZADA ---")

            time . sleep (0.5)
            print ("Contando votos...")
            time . sleep (5)

            eliminado = max(resultado, key=resultado.get)
            votos_recibidos = resultado[eliminado]

            print(f"El jugador eliminado fue el jugador {eliminado} con {votos_recibidos} votos.")

            if eliminado == impostor:
                print ("¡Felicidades! El impostor ha sido eliminado.")
                time . sleep (2)
                for i in range(25):
                    print (" ")
                print ("---La partida ha terminado---")
                print ("Han ganado los jugadores. El jugador ", impostor , "era el impostor.")
                for i in range(25):
                    print (" ")
                break
                
            else:
                print ("El jugador no era el impostor, el impostor sigue libre.")
    
    if 0 >= jugadores -2:
        for i in range(25):
            print (" ")
        print ("---La partida ha terminado---")
        print ("El impostor ha logrado sobrevivir.")
        for i in range(25):
            print (" ")
        break

    else:
        print ("Comando desconocido.")

    command = input ("Escriba \"!Finalizar\" para finalizar la partida o \"!Iniciar\" para reiniciar: ")

    if command == "!Finalizar":
        for i in range(25):
            print (" ")
        print ("---La partida ha sido finalizada---")
        for i in range(25):
            print (" ")
        break
