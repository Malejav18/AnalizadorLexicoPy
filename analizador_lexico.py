
from tokens_palabras import tokens, palabras_reservadas, tipos_datos

def es_identificador(cadena):
    if not cadena:
        return False  # Retorna falso si la cadena está vacía
    if cadena[0].isdigit():
        return False  # Un identificador no puede empezar con un número
    for char in cadena:
        if not char.isalnum() and char != '_':
            return False  # Solo se permiten letras, números y guion bajo
    return True  # Si pasa todas las validaciones, es un identificador válido

def analizar_lexico(codigo):
    fila = 0  # Inicializa el contador de filas (líneas de código)
    columna = 0  # Inicializa el contador de columnas (posición en la línea)
    palabra = ''  # Variable para almacenar la palabra actual en análisis
    comentario = False  # Bandera para ignorar caracteres dentro de comentarios
    dentro_cadena = False  # Bandera para manejar cadenas de texto

    lineas = codigo.split('\n')  # Divide el código en líneas
    
    for linea in lineas:  # Itera sobre cada línea del código
        fila += 1  # Incrementa el número de fila
        columna = 0  # Reinicia el contador de columnas
        comentario = False  # Reinicia la bandera de comentario en cada nueva línea
        palabra = ''  # Reinicia la palabra analizada en cada nueva línea
        while columna < len(linea):
            char = linea[columna]
            if char == '\t':
                columna += 4 # Incrementa la columna en 4 espacios
            else:
                columna += 1

            if comentario:  # Si ya estamos en un comentario, ignoramos el resto de la línea
                continue
            if dentro_cadena:  # Si estamos dentro de una cadena de texto
                palabra += char  # Agrega el carácter actual a la palabra en análisis
                if char == '"' or char == "'":  # Si se encuentra el cierre de la cadena
                    print(f"<tkn_cadena, {palabra}, {fila}, {(columna-len(palabra))+1}>")  # Imprime el token de cadena
                    palabra = ''  # Resetea la palabra
                    dentro_cadena = False  # Sale del modo cadena
                continue  # Continúa al siguiente carácter

            if char == '#':  # Detecta el inicio de un comentario en línea
                comentario = True  # Activa la bandera de comentario
                continue  # Ignora el resto de la línea

            if char not in tokens.values() and char not in palabras_reservadas and not char.isalnum() and char != '_' and char!=' ' and char!='"':
                print(f">>>Error léxico: Símbolo no definido '{char}' en la fila {fila}, columna {columna}")  # Reporta error léxico
                return  # Finaliza la ejecución
                continue

            if char.isdigit():  # Si el carácter es un número
                inicio_numero = columna - 1  # Guarda la posición inicial del número
                while columna < len(linea) and (linea[columna].isdigit()):  # Mientras sea un número
                    columna += 1  # Avanza la columna
                print(f"<tk_entero, {linea[inicio_numero:columna]}, {fila}, {inicio_numero + 1}>")  # Imprime el token numérico
                palabra = ''  # Resetea la palabra
                continue  # Pasa al siguiente carácter

            if es_identificador(char):  # Si el carácter es el inicio de un identificador
                inicio_numero = columna - 1  # Guarda la posición inicial del identificador
                while columna < len(linea) and es_identificador(linea[columna]):  # Mientras sea parte del identificador
                    columna += 1  # Avanza la columna
                
                if linea[inicio_numero:columna] in palabras_reservadas:  # Si es una palabra reservada
                    print(f"<{linea[inicio_numero:columna]}, {fila}, {inicio_numero + 1}>")  # Imprime el token de palabra reservada
                elif linea[inicio_numero:columna] in tipos_datos:  # Si es un tipo de dato
                    print(f"<tipo_dato, {linea[inicio_numero:columna]}, {fila}, {inicio_numero + 1}>")  # Imprime el token de tipo de dato
                else:
                    print(f"<id, {linea[inicio_numero:columna]}, {fila}, {inicio_numero + 1}>")  # Imprime el token de identificador
                continue  # Pasa al siguiente carácter

            
                
                

            if char.isspace() or char in tokens.values():  # Si el carácter es un espacio o un token
                if palabra:
                    if palabra in palabras_reservadas: # Si la palabra es una palabra reservada
                        print(f"<{palabra}, {fila}, {columna - len(palabra)}>")

                    elif palabra in tipos_datos: # Si la palabra es un tipo de dato
                        print(
                            f"<tipo_dato, {palabra}, {fila}, {columna - len(palabra)}>")
                    elif es_identificador(palabra): # Si la palabra es un identificador
                        print(
                            f"<id, {palabra}, {fila}, {columna - len(palabra)}>")
                    else:
                        try:
                            # Intentamos convertir la palabra en un número entero
                            numero_entero = int(palabra)
                            print(f"<numero_entero, {palabra}, {fila}, {columna - len(palabra)}>")
                        except ValueError:
                            print(
                                f">>>Error léxico(Fila:{fila},Columna:{columna - len(palabra)})")
                            return
                    palabra = ''

                if char in tokens.values():  # Si el carácter es un token válido
                    for token, value in tokens.items():  # Recorre los tokens definidos
                        if columna >= len(value) and linea[columna-len(value):columna] == value:  # Si el token coincide
                            print(f"<{token}, {fila}, {columna-len(value)+1}>")  # Imprime el token
                            palabra = ''  # Resetea la palabra
                            break  # Sale del bucle de tokens

            elif char == '"' or char == "'":
                palabra += char
                dentro_cadena = True

            else:
                palabra += char

with open('codigo.py', 'r', encoding='utf-8') as file:  # Abre el archivo de código fuente
    input_text = file.read()  # Lee el contenido del archivo

analizar_lexico(input_text)  # Llama a la función de análisis léxico