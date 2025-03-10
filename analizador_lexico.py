import sys
from tokens_palabras import tokens, palabras_reservadas, tipos_datos

def es_tab(char):
    if char == '\t':
        return True
    return False

def es_espacio(char):
    if char == ' ':
        return True
    return False

def es_comentario(char):
    if char == "#":
        return True

def es_digito(char):
    if ('0' <= char <= '9'):
        return True
    return False

def es_identificador(cadena):
    if not cadena:
        return False  # Cadena vacía
    for char in cadena:
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')) and char != '_':
            return False  # Solo se permiten letras minusculas y mayusculas , números y guion bajo
    return True

def es_token(char):
    if char in tokens.values():
        return True
    return False

def es_cadena(char):
    if char == "'" or char == '"':
        return True
    return False


def es_palabra_reservada(palabra):
    if palabra in palabras_reservadas:
        return True
    return False

def analizar_lexico(codigo, salida):
    fila = 0  # Contador de filas (líneas de código)
    columna = 0  # Contador de columnas (posición en la línea)
    palabra = ''  # Variable de almacenamiento de palabra actual

    lineas = codigo.split('\n')  # Divide el código en líneas
    
    # Abre el archivo de salida para escribir los resultados
    with open(salida, 'w', encoding='utf-8') as output_file:
        for linea in lineas: 
            # Reinicio de contadores y variables
            fila += 1  
            columna = 0  
            palabra = ''  

            while columna < len(linea):
                char = linea[columna]

                #Validacion de Tabulacion
                if es_tab(char):
                    columna += 4 # Tabulacion equivalente a 4 espacios
                if es_espacio(char):
                    columna += 1
                else:
                    columna += 1

                # Validacion de comentario
                if es_comentario(char):
                    break  # Ignorar el resto de la línea
                
                # Validacion de Digito
                if es_digito(char):  
                    inicio_numero = columna  # Guarda la posición inicial del número
                    while columna < len(linea) and (es_digito(linea[columna])):  # Detectar todo el número
                        columna += 1
                    if (columna+1) < len(linea) and (('a' <= linea[columna+1] <= 'z') or ('A' <= linea[columna+1] <= 'Z') or (linea[columna + 1] == '_')): #Un identificador no puede comenzar con un número
                        output_file.write(f">>> Error léxico(linea:{fila},posicion:{columna})\n")
                        return  # Finaliza la ejecución
                    output_file.write(f"<tk_entero,{linea[inicio_numero-1:columna]},{fila},{inicio_numero}>\n")  # Escribe el token numérico en el archivo
                    continue
                
                #Validacion de identificador
                if es_identificador(char):
                    inicio_numero = columna  # Guarda la posición inicial del identificador
                    while columna < len(linea) and es_identificador(linea[columna]):  # Detectar todo el identificador
                        columna += 1     
                    if linea[inicio_numero-1:columna] in palabras_reservadas:  # Imprimir palabra reservada
                        output_file.write(f"<{linea[inicio_numero-1:columna]},{fila},{inicio_numero}>\n")
                    elif linea[inicio_numero-1:columna] in tipos_datos:  # Imprimir tipo de dato
                        output_file.write(f"<{linea[inicio_numero-1:columna]},{fila},{inicio_numero}>\n")
                    else:
                        output_file.write(f"<id,{linea[inicio_numero-1:columna]},{fila},{inicio_numero}>\n")  # Imprime el token de identificador
                    continue

                
                #Validacion de Token
                if es_token(char):  # Si el carácter es un token válido
                    check = False #Bandera para revisar si los dos tokens en conjunto indican otro token
                    inicio_numero = columna
                    while columna < len(linea) and es_token(linea[columna]):  # Detectar todo el identificador
                        columna += 1  
                    for token, value in tokens.items():
                        if linea[inicio_numero-1:columna] == value:  # Si el token coincide
                            check = True
                            output_file.write(f"<{token}, {fila}, {columna - len(value) + 1}>\n")  # Escribe el token en el archivo
                            break
                    if not check:  # Si el token no coincide, se evalúan individualmente
                        i = 0
                        for token, value in tokens.items():
                            for char in linea[inicio_numero-1:columna]: 
                                if char == value:
                                    output_file.write(f"<{token}, {fila}, {columna - len(value) + i}>\n")  # Escribe el token en el archivo
                                    i += 1
                                    break                 

                #Validacion de Cadena
                if es_cadena(char):  # Si dentro de una cadena de texto
                    comillas = char
                    while columna < len(linea) and not es_cadena(linea[columna]):
                        palabra += linea[columna]
                        columna += 1  
                    if columna >= len(linea): # Comillas sin cerrar
                        output_file.write(f">>> Error léxico(linea:{fila},posicion:{columna})\n")
                        return  # Finaliza la ejecución
                    output_file.write(f"<tkn_cadena,\"{palabra}\",{fila},{(columna - len(palabra))}>\n")  # Escribe el token de cadena
                    columna += 1
                    palabra = ''  # Resetea la palabra
                    continue  # Continúa al siguiente carácter


                # Error Léxico por Caracter
                if not es_token(char) and not es_palabra_reservada(char) and not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')) and char != '_' and char !=' ' and char !='"':
                    output_file.write(f">>> Error léxico(linea:{fila},posicion:{columna - len(palabra)})\n")
                    return  # Finaliza la ejecución

                #Error Léxico por palabra desconocida
                if char == " " or char in tokens.values():  # Si el carácter es un espacio o un token
                    if palabra:
                        if palabra in palabras_reservadas: # Si la palabra es una palabra reservada
                            output_file.write(f"<{palabra}, {fila}, {columna - len(palabra)}>\n")

                        elif palabra in tipos_datos: # Si la palabra es un tipo de dato
                            output_file.write(f"<{palabra},{fila},{columna - len(palabra)}>\n")
                        elif es_identificador(palabra): # Si la palabra es un identificador
                            output_file.write(f"<id, {palabra},{fila},{columna - len(palabra)}>\n")
                        else:
                            try:
                                # Intentar convertir en entero
                                numero_entero = int(palabra)
                                output_file.write(f"<numero_entero,{palabra},{fila},{columna - len(palabra)}>\n")
                            except ValueError:
                                output_file.write(f">>> Error léxico(linea:{fila},posicion:{columna - len(palabra)})\n")
                                return # Finaliza la ejecución
                        palabra = ''  # Resetea la palabra
               
                else:  # Ir guardando la palabra desconocida
                    palabra += char

if len(sys.argv) != 2:
    print("Modo de Uso: python analizador_lexico.py codigo.py")
else:
    archivo_entrada = sys.argv[1]
    salida = "resultado_lexico.txt"

    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:  # Abre el archivo de código fuente
            input_text = file.read() 

        analizar_lexico(input_text, salida) 

        #print(f"Análisis léxico completado. Resultados guardados en '{salida}'.")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
