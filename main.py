###FUNCION

#Funciones

def bienvenida():
    print("Bienvenido a Triviathon!")

def jugar_trivia():
    nombre = input("Ingresa tu nombre: ")
    categoria = seleccionar_categoria()
    preguntas_categoria = preguntas[categoria]
    puntuacion = 0
    
    for i in range(5):
        pregunta_actual = preguntas_categoria[i]
        print(f"Pregunta {i + 1}: {pregunta_actual['pregunta']}")
        
        for i, opcion in enumerate(pregunta_actual['opciones']):
            print(f"{i + 1}. {opcion}")
        
        respuesta = input("Selecciona la opción correcta (1-4): ")
        
        # Verificar si la respuesta es correcta
        respuesta_seleccionada = pregunta_actual['opciones'][int(respuesta) - 1]
        if respuesta_seleccionada.lower() == pregunta_actual['respuesta'].lower():
            puntuacion += 3
            print("¡Correcto! +3 puntos")
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta_actual['respuesta']}")
        
        print(f"Puntuación actual: {puntuacion}")
        print("")

    print(f"Juego terminado. Puntuación final: {puntuacion}")
    guardar_resultados(nombre, puntuacion)


def seleccionar_categoria():
    print("Selecciona una categoría:")
    print("1. Entretenimiento")
    print("2. Deporte")
    
    categoria = input("Ingrese el número de la categoría que desea jugar: ")
    if categoria == "1":
        return "entretenimiento"
    elif categoria == "2":
        return "deporte"
    else:
        print("Selección inválida. Por favor, elige 1 o 2.")
        return seleccionar_categoria()

#Diccionarios

preguntas = {
    "entretenimiento": [
        {"pregunta": "¿Quién dirigió la película 'Inception'?", 
        "opciones": ["Steven Spielberg", "Christopher Nolan", "James Cameron", "Quentin Tarantino"], 
        "respuesta": "Christopher Nolan"},
        {"pregunta": "¿En qué año se estrenó la primera temporada de 'Breaking Bad'?", 
        "opciones": ["2006", "2007", "2008", "2009"], 
        "respuesta": "2008"},
        # Agregar mas preguntas
    ],
    "deporte": [
        {"pregunta": "¿Quién ganó la Copa del Mundo de la FIFA en 2018?", 
        "opciones": ["Brasil", "Alemania", "Francia", "Argentina"], 
        "respuesta": "Francia"},
        {"pregunta": "¿Cuántos Grand Slam ha ganado Rafael Nadal?", 
        "opciones": ["20", "21", "22", "23"], 
        "respuesta": "22"},
        # Agregar mas preguntas
    ]
}


jugar_trivia()

###PROGRAMA
