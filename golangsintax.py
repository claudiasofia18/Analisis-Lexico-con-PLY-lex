import ply.yacc as yacc
from golanglexer import tokens

"""
1-3 : DIFICULTAD DE ACTIVIDADES

1. Operaciones matemáticas. 1
2. Condición. Operadores de comparación/lógicos. 1
3. Métodos de impresión de datos. 3
4. Métodos de lectura de datos. 3
5. Estructura de control (FOR) 1
6. Estructura de control (SELECT) 1
7. Estructura de control (SWITCH) 1
8. Estructura de datos (SLICES) 3
9. Estructura de datos (LISTAS) 3
10. Estructura de datos (MAPS) 3
11. Funciones. 1


CLAUDIA 
"""


# Métodos impresión de datos.
# fmt package

def p_impresionsencilla(p):
    '''impresionsencilla : tipoimpresion PARENTESISI expresion PARENTESISD
                            | tipoimpresion PARENTESISI expresiones PARENTESISD
     '''


def p_tipoimpresion(p):
    '''tipoimpresion : FMT PUNTO PRINT
                         | FMT PUNTO PRINTLN
    '''


def p_impresionformato(p):
    '''impresionformato : FMT PUNTO PRINTF PARENTESISI STRING COMA expresion PARENTESISD
                           | FMT PUNTO PRINTF PARENTESISI STRING COMA expresiones PARENTESISD
    '''


def p_expresion(p):
    '''expresion : tipodedato
    '''


def p_expresiones(p):
    '''expresiones : tipodedato COMA tipodedato
    '''


def p_tipodedato(p):
    '''tipodedato : STRING
                    | INTEGER
                    | FLOAT
                    | VARIABLE
    '''


# bufio package

def p_impressionbufio(p):
    '''impressionbufio : VARIABLE DSHORTVAR BUFIO PUNTO NEWWRITER PARENTESISI OS PUNTO STDOUT PARENTESISI NEWLINE impresion
    '''


def p_impresion(p):
    '''impresion : FMT PUNTO FPRINT PARENTESISI VARIABLE COMA tipodedato
    '''


# Estructura de datos (SLICES).

def p_slicevacio(p):
    '''slicevacio : VAR VARIABLE CORCHETEI CORCHETED dato
    '''


def p_declaracion_slice(p):
    '''declaracion_slice : VAR VARIABLE IGUAL CORCHETEI CORCHETED LLAVEI expresion LLAVED
                          | VAR VARIABLE IGUAL CORCHETEI CORCHETED LLAVEI expresiones LLAVED
                          | VAR VARIABLE IGUAL NEW PARENTESISI CORCHETEI INTEGER CORCHETED dato PARENTESISD CORCHETEI INTEGER DOSPUNTOS CORCHETED
                          | VARIABLE DSHORTVAR slice CORCHETEI DOSPUNTOS CORCHETED
                          | VARIABLE DSHORTVAR slice CORCHETEI INTEGER DOSPUNTOS CORCHETED
                          | VARIABLE DSHORTVAR slice CORCHETEI DOSPUNTOS INTEGER CORCHETED
                          | VARIABLE DSHORTVAR slice CORCHETEI INTEGER DOSPUNTOS INTEGER CORCHETED
    '''


def p_slice(p):
    '''slice : VARIABLE
    '''


def p_len_slice(p):
    '''len_slice : LEN CORCHETEI slice CORCHETED
    '''


def p_append_slice(p):
    '''append_slice : slice IGUAL APPEND PARENTESISI slice COMA expresion
                     | slice IGUAL APPEND PARENTESISI slice COMA expresiones
    '''


def p_cap_slice(p):
    '''cap_slice : CAP CORCHETEI slice CORCHETED
    '''


def p_dato(p):
    '''dato : INTTYPE
             | FLOATTYPE
             | BOOLEANTYPE
             | STRINGTYPE
    '''


# Estructura de control (SWITCH).

def p_switch(p):
    '''switch : SWITCH VARIABLE LLAVEI NEWLINE CASE valor DOSPUNTOS NEWLINE impresionsencilla cases LLAVED
    '''


def p_cases(p):
    '''cases : CASE valor DOSPUNTOS NEWLINE impresionsencilla
              | DEFAULT DOSPUNTOS NEWLINE impresionsencilla
    '''


def p_valor(p):
    '''valor : condicion
              | VARIABLE
              | TRUE
              | FALSE
    '''


"""
ISAAC
9
4
5
"""


#   Métodos de LECTURA de datos
def p_lecturaSscanf(p):
    '''
    lecturaSscanf : OR
    '''


def p_lecturaScanf(p):
    '''
    lecturaScanf : OR
    '''


#   Estructura de control FOR
def p_forCondicionParo(p):
    '''
    forCondicionParo : FOR condicion LLAVEI OR INCREMENT LLAVED
                     | FOR condicion LLAVEI OR DECREMENT LLAVED
    '''


def p_forEstandar(p):
    '''
    forEstandar : FOR asignacion PUNTOYCOMA condicion PUNTOYCOMA INCREMENT LLAVEI OR LLAVED
                | FOR asignacion PUNTOYCOMA condicion PUNTOYCOMA DECREMENT LLAVEI OR LLAVED
    '''


def p_forRango(p):
    '''
    forRango : FOR VARIABLE COMA VARIABLE DSHORTVAR RANGE VARIABLE LLAVEI OR LLAVED
             | FOR VARIABLE DSHORTVAR RANGE VARIABLE LLAVEI OR LLAVED
    '''


#   Estructura de datos LISTAS

def p_listaDeclaracion(p):
    '''
    listaDeclaracion : VARIABLE DSHORTVAR LIST PUNTO NEW PARENTESISI PARENTESISD
    '''


def p_listaPushBack(p):
    '''
    listaPushBack : VARIABLE PUNTO PUSHBACK PARENTESISI OR PARENTESISD
    '''


def p_listaFront(p):
    '''
    listaFront : VARIABLE PUNTO FRONT PARENTESISI  PARENTESISD
    '''


"""
EMANUEL

10
1
2
11
6


"""


def p_asignacion(p):
    ''' asignacion : declaracionEntero INIVAR expEntero
                    | declaracionFloat INIVAR expFloat
                    | declaracionBool INIVAR expBool
                    '''


def p_type(p):
    ''' type : INTTYPE
            |  FLOATTYPE
            |  BOOLEANTYPE
            |  STRINGTYPE
    '''


def p_signo(p):
    ''' signo : PLUS
              | MINUS
              | TIMES
              | DIVIDE
              | MODULE
    '''


def p_declaracionEntero(p):
    '''declaracionEntero : VAR VARIABLE INTTYPE
                        |  VARIABLE DSHORTVAR
                        |  VAR VARIABLE
    '''


def p_expEntero(p):
    ''' expEntero :  INTEGER
                    | INTEGER signo expEntero
                    | VARIABLE
    '''


def p_declaracionFloat(p):
    '''declaracionFloat :      VAR VARIABLE FLOATTYPE
                            |  VARIABLE DSHORTVAR
                            |  VAR VARIABLE
    '''


def p_expFloat(p):
    '''expFloat :    FLOAT
                   | VARIABLE
                   | FLOAT signo expFloat
                   | VARIABLE signo expFloat
    '''


# 2. Condición. Operadores de comparación/lógicos. 1
def p_declaracionBool(p):
    '''declaracionBool : VAR VARIABLE BOOLEANTYPE
                        |  VARIABLE DSHORTVAR
                        |  VAR VARIABLE
    '''


def p_expBool(p):
    ''' expBool : TRUE
                | FALSE

    '''


def p_comparacion(p):
    '''comparacion :  EQUAL
                    | UNEQUAL
                    | GREATERTHAN
                    | SMALLERTHAN
                    | GREATEROREQUALTHAN
                    | SMALLEROREQUALTHAN
    '''


def p_logical(p):
    ''' logical : AND
                | OR
                | NOT
    '''


def p_condicion(p):
    '''
        condicion : tipodedato comparacion tipodedato
                 |  tipodedato comparacion VARIABLE
                 |  VARIABLE comparacion VARIABLE
                 |  condicion logical condicion
    '''


# Funciones
def p_argument(p):
    ''' argument : VARIABLE TYPE    '''


def p_arguments(p):
    ''' arguments : argument COMA argument
                    | argument
    '''


def p_cabecerafunction(p):
    ''' function : FUNCION VARIABLE PARENTESISI arguments PARENTESISD  '''

def p_error(p):
    print("Error sintactico!")


parser = yacc.yacc()
while True:
    try:
        s = input('calc >')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
