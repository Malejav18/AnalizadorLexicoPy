# Definir los tokens y palabras reservadas
# Cada token tiene asociado su representación en el lenguaje.
tokens = {
    'tk_ejecuta': '->', 
    'tk_potencia': '**', 
    'tk_mayor_igual': '>=', 
    'tk_menor_igual': '<=', 
    'tk_igual': '==', 
    'tk_distinto': '!=', 
    'tk_mas_asig': '+=', 
    'tk_menos_asig': '-=', 
    'tk_mult_asig': '*=', 
    'tk_div_asig': '/=', 
    'tk_div_entera': '//',
    'tk_mod_asig': '%=', 
    'tk_amper_asig': '&=', 
    'tk_bar_asig': '|=', 
    'tk_hat_asig': '^=', 
    'tk_menor_menor': '<<',
    'tk_mayor_mayor': '>>',
    'tk_punto_y_coma': ';', 
    'tk_coma': ',', 
    'tk_par_izq': '(', 
    'tk_par_der': ')', 
    'tk_corchete_izq': '[', 
    'tk_corchete_der': ']', 
    'tk_llave_izq': '{', 
    'tk_llave_der': '}', 
    'tk_dos_puntos': ':', 
    'tk_barra' : '|', 
    'tk_punto': '.', 
    'tk_asig': '=', 
    'tk_div': '/', 
    'tk_suma': '+', 
    'tk_resta': '-', 
    'tk_mult': '*', 
    'tk_modulo': '%', 
    'tk_mayor': '>', 
    'tk_menor': '<', 
    'tk_arroba': '@',
    'tk_arroba_asig': '@=',
    'tk_comentario': '#', 
    'tk_amper': '&', 
    'tk_interrogacion': '?', 
    'tk_tilde': '~', 
    'tk_barra_piso': '_', 
    'tk_exclamacion': '!', 
    'tk_comentario_multilinea': "'''", 
    'tk_hat': '^', 
    'tk_left_shift' : '<<', 
    'tk_right_shift' : '<<',
    'tk_colon_asig' : ':='

}


# Palabras reservadas en minúsculas
# Estas palabras tienen un significado especial en la sintaxis del lenguaje y no pueden usarse como identificadores
palabras_reservadas = {
    'range', 'object', 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'print', 'raise', 'return',
    'try', 'self', 'while', 'with', 'yield', '__init__'
}

# Tipos de datos básicos del lenguaje
# Cada tipo de dato se asocia con su palabra clave en el lenguaje
tipos_datos = {
    'int': 'int',
    'float': 'float',
    'str': 'str',
    'bool': 'bool',
    'list': 'list',
    'tuple': 'tuple',
    'dict': 'dict',
    'set': 'set'
}