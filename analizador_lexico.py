from tokens_palabras import tokens, palabras_reservadas, tipos_datos

def es_tab(char):
    if char == '\t':
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
    if char == '"' or char == "'":
        return True
    return False

def es_palabra_reservada(palabra):
    if palabra in palabras_reservadas:
        return True
    return False

def analizar_lexico(codigo):
    fila = 0  # Contador de filas (líneas de código)
    columna = 0  # Contador de columnas (posición en la línea)
    palabra = ''  # Variable de almacenamiento de palabra actual

    lineas = codigo.split('\n')  # Divide el código en líneas
    
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
                print(f"<tk_entero,{linea[inicio_numero-1:columna]},{fila},{inicio_numero}>")  # Imprime el token numérico
                continue
            
            #Validacion de identificador
            if es_identificador(char):
                inicio_numero = columna  # Guarda la posición inicial del identificador
                while columna < len(linea) and es_identificador(linea[columna]):  # Detectar todo el identificador
                    columna += 1     
                if linea[inicio_numero-1:columna] in palabras_reservadas:  # Imprimir palabra reservada
                    print(f"<{linea[inicio_numero-1:columna]},{fila},{inicio_numero}>")
                elif linea[inicio_numero-1:columna] in tipos_datos:  # Imprimir tipo de dato
                    print(f"<{linea[inicio_numero-1:columna]},{fila},{inicio_numero}>")
                else:
                    print(f"<id,{linea[inicio_numero-1:columna]},{fila},{inicio_numero}>")  # Imprime el token de identificador
                continue 
            
            #Validacion de Token
            if es_token(char):  # Si el carácter es un token válido
                check = False #Bandera para revisar si los dos tokens en conjunto indican otro token
                inicio_numero = columna
                while columna < len(linea) and columna < inicio_numero + 1 and es_token(linea[columna]):  # Detectar todo el identificador
                    columna += 1  
                for token, value in tokens.items():
                    if linea[inicio_numero-1:columna]== value:  # Si el token coincide
                        check = True
                        print(f"<{token}, {fila}, {columna-len(value)+1}>")  # Imprime el token
                        break
                if not check: #Si el token no coincide, se evalúan individualmente
                    i=0
                    for token, value in tokens.items():
                        for char in linea[inicio_numero-1:columna]: 
                            if char == value:
                              print(f"<{token}, {fila}, {columna-len(value)+i}>")  # Imprime el token
                              i+=1
                              break                 

            #Validacion de Cadena
            if es_cadena(char):  # Si estamos dentro de una cadena de texto
                while columna < len(linea) and not es_cadena(linea[columna]):
                    palabra += linea[columna]
                    columna += 1  
                print(f"<tkn_cadena,\"{palabra}\",{fila},{(columna-len(palabra))}>")  # Imprime el token de cadena
                columna+=1
                palabra = ''  # Resetea la palabra
                continue  # Continúa al siguiente carácter

            
            # Error Léxico por Caracter
            if not es_token(char) and not es_palabra_reservada(char) and not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')) and char != '_' and char !=' ' and char !='"':
                print(f">>> Error léxico(linea:{fila},posicion:{columna - len(palabra)})")
                return  # Finaliza la ejecución

            #Error Léxico por palabra desconocida
            if char == " " or char in tokens.values():  # Si el carácter es un espacio o un token
                if palabra:
                    if palabra in palabras_reservadas: # Si la palabra es una palabra reservada
                        print(f"<{palabra}, {fila}, {columna - len(palabra)}>")

                    elif palabra in tipos_datos: # Si la palabra es un tipo de dato
                        print(
                            f"<{palabra},{fila},{columna - len(palabra)}>")
                    elif es_identificador(palabra): # Si la palabra es un identificador
                        print(
                            f"<id, {palabra},{fila},{columna - len(palabra)}>")
                    else:
                        try:
                            # Intentar convertir en entero
                            numero_entero = int(palabra)
                            print(f"<numero_entero,{palabra},{fila},{columna - len(palabra)}>")
                        except ValueError:
                            print(f">>> Error léxico(linea:{fila},posicion:{columna - len(palabra)})")
                            return #Finaliza la ejecucion
                    palabra = ''  # Resetea la palabra
           
            else: # Ir guardando la palabra desconocida
                palabra += char

with open('codigo.py', 'r', encoding='utf-8') as file:  # Abre el archivo de código fuente
    input_text = file.read()  # Lee el contenido del archivo

analizar_lexico(input_text)  # Llama a la función de análisis léxico