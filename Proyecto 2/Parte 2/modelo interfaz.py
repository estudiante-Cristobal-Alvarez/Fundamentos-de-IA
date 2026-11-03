import janus_swi as janus
import unicodedata
from pathlib import Path


# Ubicacion de la base de conocimiento.
CARPETA = Path(__file__).resolve().parent
BASE_CONOCIMIENTO = CARPETA / "Area de conocimiento automoviles.pl"

# Verificar que existe el archivo.
if not BASE_CONOCIMIENTO.is_file():
    raise FileNotFoundError(
        f"No se encontro la base de conocimiento: {BASE_CONOCIMIENTO}"
    )

# Cargar la KB en SWI-Prolog.
ruta_prolog = BASE_CONOCIMIENTO.as_posix()
janus.query_once("consult(Ruta)", {"Ruta": ruta_prolog})

print("Base de conocimiento cargada correctamente.")

# Consultar una regla de la KB.
print("\nAutomoviles ecologicos:")

with janus.query("vehiculo_ecologico(X)") as resultados:
    for resultado in resultados:
        print("-", resultado["X"])

# Consultar un hecho de la KB.
resultado = janus.query_once("cantidad_puertas(hatchback, X)")

print("\nPuertas del hatchback:", resultado["X"])


# Consultas del chatbot desde Python.


def consultar_automoviles(tipo_consulta):
    consultas = {
        "tipo_sedan": (
            "tipo_automovil(sedan)",
            "El sedan es un tipo de automovil"
        ),
        "puertas_sedan": (
            "cantidad_puertas(sedan, X)",
            "Cantidad de puertas del sedan"
        ),
        "asientos_suv": (
            "cantidad_asientos(suv, X)",
            "Cantidad de asientos del SUV"
        ),
        "espacio_carga_alto": (
            "espacio_carga(X, alto)",
            "Automoviles con espacio de carga alto"
        ),
        "uso_pickup": (
            "uso_principal(pickup, X)",
            "Uso principal de una pickup"
        ),
        "aptos_familia": (
            "apto_familia(X, si)",
            "Automoviles aptos para familia"
        ),
        "consumo_alto": (
            "consumo_combustible(X, alto)",
            "Automoviles con consumo alto"
        ),
        "conduccion_comoda": (
            "comodidad_conduccion(X, alta)",
            "Automoviles con comodidad de conduccion alta"
        ),
        "familiares": (
            "automovil_familiar(X)",
            "Automoviles familiares"
        ),
        "carga": (
            "apto_para_carga(X)",
            "Automoviles aptos para transportar carga"
        ),
        "offroad": (
            "apto_offroad(X)",
            "Automoviles aptos para uso off-road"
        ),
        "urbanos": (
            "vehiculo_urbano(X)",
            "Automoviles de uso urbano"
        ),
        "grandes": (
            "vehiculo_grande(X)",
            "Automoviles grandes"
        ),
        "bajo_consumo": (
            "vehiculo_bajo_consumo(X)",
            "Automoviles de bajo consumo"
        ),
        "comodos_familia": (
            "comodo_para_familia(X)",
            "Automoviles comodos para familia"
        ),
        "trabajo": (
            "apto_para_trabajo(X)",
            "Automoviles aptos para trabajo"
        ),
        "pasajeros": (
            "buena_capacidad_pasajeros(X)",
            "Automoviles con buena capacidad de pasajeros"
        ),
        "urbano_bajo_consumo": (
            "urbano_bajo_consumo(X)",
            "Automoviles urbanos y de bajo consumo"
        ),
        "deportivo_familia": (
            "apto_familia(deportivo, si)",
            "El deportivo es apto para familia"
        ),
        "interior_alta": (
            "comodidad_interior(X, alta)",
            "Automoviles con comodidad interior alta"
        ),
        "espaciosos": (
            "vehiculo_espacioso(X)",
            "Automoviles espaciosos"
        ),
        "interior_comodo": (
            "interior_comodo(X)",
            "Automoviles con interior comodo"
        ),
        "ecologicos": (
            "vehiculo_ecologico(X)",
            "Automoviles ecologicos"
        ),
        "trabajo_pesado": (
            "vehiculo_trabajo_pesado(X)",
            "Automoviles de trabajo pesado"
        ),
        "aventura": (
            "vehiculo_familiar_aventura(X)",
            "Automoviles familiares para aventuras"
        )
    }

    if tipo_consulta not in consultas:
        return "No reconozco esa consulta."

    consulta_prolog, descripcion = consultas[tipo_consulta]

    # Consultas que responden verdadero o falso.
    if tipo_consulta in ("tipo_sedan", "deportivo_familia"):
        resultado = janus.query_once(consulta_prolog)

    if tipo_consulta == "tipo_sedan":
        if resultado["truth"]:
            return "Si, el sedan es un tipo de automovil."
        return "No, el sedan no es un tipo de automovil."

    if tipo_consulta == "deportivo_familia":
        if resultado["truth"]:
            return "Si, el deportivo es apto para una familia."
        return "No, el deportivo no es apto para una familia."

    resultados = []

    with janus.query(consulta_prolog) as soluciones:
        for solucion in soluciones:
            resultados.append(str(solucion["X"]))

    if not resultados:
        return f"{descripcion}: no se encontraron resultados."

    return f"{descripcion}: {', '.join(resultados)}."

def normalizar_texto(texto):
    texto = texto.lower().strip()

    # Eliminar tildes.
    texto = "".join(
        caracter for caracter in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caracter) != "Mn"
    )

    # Eliminar signos de puntuacion.
    for signo in "¿?¡!.,;:":
        texto = texto.replace(signo, "")

    return " ".join(texto.split())



def reconocer_pregunta(pregunta):
    preguntas = {
        "el sedan es un tipo de automovil": "tipo_sedan",
        "cuantas puertas tiene un sedan": "puertas_sedan",
        "cuantos asientos tiene un suv": "asientos_suv",
        "que automoviles tienen espacio de carga alto": "espacio_carga_alto",
        "cual es el uso principal de una pickup": "uso_pickup",
        "que automoviles son aptos para familia": "aptos_familia",
        "que automoviles tienen consumo alto": "consumo_alto",
        "que automoviles tienen comodidad de conduccion alta": "conduccion_comoda",
        "que automoviles son familiares segun las reglas": "familiares",
        "que automoviles son aptos para carga": "carga",
        "que automoviles son aptos para off-road": "offroad",
        "que automoviles son urbanos": "urbanos",
        "que automoviles son grandes": "grandes",
        "que automoviles tienen bajo consumo": "bajo_consumo",
        "que automoviles son comodos para familia": "comodos_familia",
        "que automoviles son aptos para trabajo": "trabajo",
        "que automoviles tienen buena capacidad de pasajeros": "pasajeros",
        "que automoviles son urbanos y de bajo consumo": "urbano_bajo_consumo",
        "el deportivo es apto para familia": "deportivo_familia",
        "que automoviles tienen comodidad interior alta": "interior_alta",
        "que automoviles son espaciosos": "espaciosos",
        "que automoviles poseen interior comodo": "interior_comodo",
        "que automoviles son ecologicos": "ecologicos",
        "que automoviles son de trabajo pesado": "trabajo_pesado",
        "que automoviles familiares sirven para aventuras": "aventura"
    }

    texto = normalizar_texto(pregunta)
    return preguntas.get(texto)



def iniciar_chatbot():
    print("\n=================================")
    print(" CHATBOT DE AUTOMOVILES - PYTHON")
    print("=================================")
    print("Escribe una pregunta sobre automoviles.")
    print("Escribe 'ayuda' para ver las preguntas disponibles.")
    print("Escribe 'salir' para finalizar.\n")

    while True:
        pregunta = input("Usuario: ").strip()
        texto = normalizar_texto(pregunta)

        if texto == "salir":
            print("Chatbot: Gracias por utilizar el chatbot.")
            break

        if texto == "ayuda":
            mostrar_ayuda()
            continue

        tipo_consulta = reconocer_pregunta(pregunta)

        if tipo_consulta is None:
            print("Chatbot: No reconozco esa pregunta.")
            print("Escribe 'ayuda' para consultar las preguntas disponibles.")
        else:
            respuesta = consultar_automoviles(tipo_consulta)
            print("Chatbot:", respuesta)

        print()


def mostrar_ayuda():
    preguntas = [
        "El sedan es un tipo de automovil?",
        "Cuantas puertas tiene un sedan?",
        "Cuantos asientos tiene un SUV?",
        "Que automoviles tienen espacio de carga alto?",
        "Cual es el uso principal de una pickup?",
        "Que automoviles son aptos para familia?",
        "Que automoviles tienen consumo alto?",
        "Que automoviles tienen comodidad de conduccion alta?",
        "Que automoviles son familiares segun las reglas?",
        "Que automoviles son aptos para carga?",
        "Que automoviles son aptos para off-road?",
        "Que automoviles son urbanos?",
        "Que automoviles son grandes?",
        "Que automoviles tienen bajo consumo?",
        "Que automoviles son comodos para familia?",
        "Que automoviles son aptos para trabajo?",
        "Que automoviles tienen buena capacidad de pasajeros?",
        "Que automoviles son urbanos y de bajo consumo?",
        "El deportivo es apto para familia?",
        "Que automoviles tienen comodidad interior alta?",
        "Que automoviles son espaciosos?",
        "Que automoviles poseen interior comodo?",
        "Que automoviles son ecologicos?",
        "Que automoviles son de trabajo pesado?",
        "Que automoviles familiares sirven para aventuras?"
    ]

    print("\n========== PREGUNTAS DISPONIBLES ==========")

    for numero, pregunta in enumerate(preguntas, start=1):
        print(f"{numero}. {pregunta}")

    print("==========================================\n")


if __name__ == "__main__":
    iniciar_chatbot()