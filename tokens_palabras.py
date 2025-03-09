# Definir los tokens y palabras reservadas
# Cada token tiene asociado su representación en el lenguaje.
tokens = {
    'tkn_ejecuta': '->',
    'tkn_potencia': '**',
    'tkn_mayor_igual': '>=',
    'tkn_menor_igual': '<=',
    'tkn_igual': '==',
    'tkn_distinto': '!=',
    'tkn_and': 'and',
    'tkn_or': 'or',
    'tkn_not': 'not',
    'tkn_mas_asig': '+=',
    'tkn_menos_asig': '-=',
    'tkn_mult_asig': '*=',
    'tkn_div_asig': '/=',
    'tkn_div_entera': '//',
    'tkn_mod_asig': '%=',
    'tkn_menor_menor': '<<',
    'tkn_mayor_mayor': '>>',
    'tkn_punto_y_coma': ';',
    'tkn_coma': ',',
    'tkn_par_izq': '(',
    'tkn_par_der': ')',
    'tkn_corchete_izq': '[',
    'tkn_corchete_der': ']',
    'tkn_llave_izq': '{',
    'tkn_llave_der': '}',
    'tkn_dos_puntos': ':',
    'tkn_punto': '.',
    'tkn_asig': '=',
    'tkn_div': '/',
    'tkn_suma': '+',
    'tkn_resta': '-',
    'tkn_mult': '*',
    'tkn_modulo': '%',
    'tkn_mayor': '>',
    'tkn_menor': '<',
    'tkn_arroba': '@',
    'tkn_comentario': '#',
    'tkn_ampersand': '&',
    'tkn_interrogacion': '?',
    'tkn_tilde': '~',
    'tkn_barra_piso': '_',
    'tkn_exclamacion': '!'
}


# Palabras reservadas en minúsculas
# Estas palabras tienen un significado especial en la sintaxis del lenguaje y no pueden usarse como identificadores
palabras_reservadas = {
    'range', 'object', 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'print', 'raise', 'return',
    'try', 'self', 'while', 'with', 'yield', 'init'
}

# Tipos de datos básicos del lenguaje
# Cada tipo de dato se asocia con su palabra clave en el lenguaje
tipos_datos = {
    'int': 'int',
    'float': 'float',
    'str': 'str',
    'bool': 'bool'
}
