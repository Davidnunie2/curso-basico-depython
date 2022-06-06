# la condicional es: si se cumple "esto" "haz esto"

calificacion = input("introduce la calificación del examen: ")

calificacion = int(calificacion)

    #preguntamos si la calificacion en menor a 700
if calificacion < 700 :
    print("veeees, por no estudiar")#si if es menor a 700 muestra esto
elif calificacion > 1000 :
    print("MIENTES!!!")
else :#si no se cumple el if anterior, pasa a esta linea
    print("¡felicidades cerebrito!")# se ejecuta si ninguno de los if se cumple

#verificador de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 115 :
    print("Bienvenid@ al mamitas")
elif edad > 100 :
    print("si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("ni que fueras viajero del tiempo")
else :
    print("no puedes llevarte esos cigarros")