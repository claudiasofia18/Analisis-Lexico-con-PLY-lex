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


# ISAAC
def p_cuerpo(p):
    '''
    cuerpo : asignacion
            | impresionsencilla
            | impresionformato
            | impressionbufio
            | impresion
            | valor
            | switch
            | cases
            | cap_slice
            | declaracion_slice
            | dato
            | len_slice
            | forCondicionParo
            | forEstandar
            | forRango
            | listaPushBack
            | cabecerafunction
            | arguments
            | listaFront
            | append_slice
            | slicevacio
            | lecturaScanf
            | lecturaSscanf

    '''


# EMANUEL
def p_asignacion(p):
    ''' asignacion : declaracionEntero INIVAR expEntero
                    | declaracionFloat INIVAR expFloat
                    | declaracionBool INIVAR expBool
    '''


# CLAUDIA
def p_impresionsencilla(p):
    '''impresionsencilla : tipoimpresion PARENTESISI expresion PARENTESISD
                            | tipoimpresion PARENTESISI expresiones PARENTESISD
     '''





# CLAUDIA
def p_impresionformato(p):
    '''impresionformato : FMT PUNTO PRINTF PARENTESISI STRING COMA expresion PARENTESISD
                           | FMT PUNTO PRINTF PARENTESISI STRING COMA expresiones PARENTESISD
    '''








# CLAUDIA
def p_impressionbufio(p):
    '''impressionbufio : VARIABLE DSHORTVAR BUFIO PUNTO NEWWRITER PARENTESISI OS PUNTO STDOUT PARENTESISI NEWLINE impresion
    '''


# CLAUDIA
def p_impresion(p):
    '''impresion : FMT PUNTO FPRINT PARENTESISI VARIABLE COMA tipodedato
    '''


# CLAUDIA
def p_declaracion_slice(p):
    '''declaracion_slice : VAR VARIABLE INIVAR CORCHETEI CORCHETED LLAVEI expresion LLAVED
                          | VAR VARIABLE INIVAR CORCHETEI CORCHETED LLAVEI expresiones LLAVED
                          | VAR VARIABLE INIVAR NEW PARENTESISI CORCHETEI INTEGER CORCHETED dato PARENTESISD CORCHETEI INTEGER DOSPUNTOS CORCHETED
                          | VARIABLE DSHORTVAR slice CORCHETEI DOSPUNTOS CORCHETED
                          | VARIABLE DSHORTVAR slice CORCHETEI INTEGER DOSPUNTOS CORCHETED
                          | VARIABLE DSHORTVAR slice CORCHETEI DOSPUNTOS INTEGER CORCHETED
                          | VARIABLE DSHORTVAR slice CORCHETEI INTEGER DOSPUNTOS INTEGER CORCHETED
    '''


# CLAUDIA
def p_len_slice(p):
    '''len_slice : LEN CORCHETEI slice CORCHETED
    '''


# CLAUDIA
def p_append_slice(p):
    '''append_slice : slice INIVAR APPEND PARENTESISI slice COMA expresion
                     | slice INIVAR APPEND PARENTESISI slice COMA expresiones
    '''


# CLAUDIA
def p_cap_slice(p):
    '''cap_slice : CAP CORCHETEI slice CORCHETED
    '''




# CLAUDIA
def p_switch(p):
    '''switch : SWITCH VARIABLE LLAVEI NEWLINE CASE valor DOSPUNTOS NEWLINE impresionsencilla cases LLAVED
    '''










# ISAAC
def p_forCondicionParo(p):
    '''
    forCondicionParo : FOR condicion LLAVEI asignacion INCREMENT LLAVED
                     | FOR condicion LLAVEI asignacion DECREMENT LLAVED
    '''


# ISAAC
def p_forEstandar(p):
    '''
    forEstandar : FOR asignacion PUNTOYCOMA condicion PUNTOYCOMA INCREMENT LLAVEI asignacion LLAVED
                | FOR asignacion PUNTOYCOMA condicion PUNTOYCOMA DECREMENT LLAVEI asignacion LLAVED
    '''


# ISAAC
def p_forRango(p):
    '''
    forRango : FOR VARIABLE COMA VARIABLE DSHORTVAR RANGE VARIABLE LLAVEI asignacion LLAVED
             | FOR VARIABLE DSHORTVAR RANGE VARIABLE LLAVEI asignacion LLAVED
    '''


################################################################################################################################################

################################################################################################################################################

# CLAUDIA
def p_expresion(p):
    '''expresion : tipodedato
    '''


# CLAUDIA
def p_expresiones(p):
    '''expresiones : tipodedato COMA tipodedato
    '''

# ISAAC
def p_PushBack(p):
    '''
    listaPushBack : VARIABLE PUNTO PUSHBACK PARENTESISI tipodedato PARENTESISD
    '''


# CLAUDIA
def p_cases(p):
    '''cases : CASE valor DOSPUNTOS NEWLINE impresionsencilla
              | DEFAULT DOSPUNTOS NEWLINE impresionsencilla
    '''

# CLAUDIA
def p_valor(p):
    '''valor : condicion
              | VARIABLE
              | TRUE
              | FALSE
    '''

# EMANUEL
def p_condicion(p):
    '''
        condicion : tipodedato comparacion tipodedato
                 |  tipodedato comparacion VARIABLE
                 |  VARIABLE comparacion VARIABLE
                 |  condicion logical condicion
    '''


# EMANUEL
def p_expFloat(p):
    '''expFloat :    FLOAT
                   | VARIABLE
                   | FLOAT signo expFloat
                   | VARIABLE signo expFloat
    '''


# EMANUEL
def p_cabecerafunction(p):
    ''' cabecerafunction : FUNCION VARIABLE PARENTESISI arguments PARENTESISD  '''


# EMANUEL
def p_arguments(p):
    ''' arguments : argument COMA argument
                    | argument
    '''

# EMANUEL
def p_argument(p):
    ''' argument : VARIABLE dato '''

# CLAUDIA
def p_slicevacio(p):
    '''slicevacio : VAR VARIABLE CORCHETEI CORCHETED dato
    '''


# CLAUDIA
def p_dato(p):
    '''dato : INTTYPE
             | FLOATTYPE
             | BOOLEANTYPE
             | STRINGTYPE
    '''

# EMANUEL
def p_expEntero(p):
    ''' expEntero :  INTEGER
                    | INTEGER signo expEntero
                    | VARIABLE
    '''


# EMANUEL
def p_signo(p):
    '''signo : PLUS
             | MINUS
             | TIMES
             | DIVIDE
             | MODULE
    '''


# EMANUEL
def p_logical(p):
    ''' logical : AND
                | OR
                | NOT
    '''


# CLAUDIA
def p_slice(p):
    '''slice : VARIABLE
    '''


# EMANUEL
def p_comparacion(p):
    '''comparacion :  EQUAL
                    | UNEQUAL
                    | GREATERTHAN
                    | SMALLERTHAN
                    | GREATEROREQUALTHAN
                    | SMALLEROREQUALTHAN
    '''

# EMANUEL
def p_declaracionBool(p):
    '''declaracionBool : VAR VARIABLE BOOLEANTYPE
                        |  VARIABLE DSHORTVAR
                        |  VAR VARIABLE
    '''

# EMANUEL
def p_expBool(p):
    ''' expBool : TRUE
                | FALSE
    '''

# EMANUEL
def p_declaracionFloat(p):
    '''declaracionFloat :      VAR VARIABLE FLOATTYPE
                            |  VARIABLE DSHORTVAR
                            |  VAR VARIABLE
    '''

# EMANUEL
def p_declaracionEntero(p):
    '''declaracionEntero : VAR VARIABLE INTTYPE
                        |  VARIABLE DSHORTVAR
                        |  VAR VARIABLE
    '''



# ISAAC
def p_listaFront(p):
    '''
    listaFront : VARIABLE PUNTO FRONT PARENTESISI  PARENTESISD
    '''


# CLAUDIA
def p_tipodedato(p):
    '''tipodedato : STRING
                    | INTEGER
                    | FLOAT
                    | VARIABLE
    '''

# ISAAC
def p_lecturaSscanf(p):
    '''
    lecturaSscanf : FMT PUNTO SSCANF PARENTESISI STRING COMA STRING COMA AMPERSON VARIABLE PARENTESISD
    '''

# CLAUDIA
def p_tipoimpresion(p):
    '''tipoimpresion : FMT PUNTO PRINT
                         | FMT PUNTO PRINTLN
    '''


# ISAAC
def p_lecturaScanf(p):
    '''
    lecturaScanf : FMT PUNTO SCANF PARENTESISI STRING COMA AMPERSON VARIABLE PARENTESISD
    '''

# ISAAC
def p_listaDeclaracion(p):
    '''
    listaDeclaracion : VARIABLE DSHORTVAR LIST PUNTO NEW PARENTESISI PARENTESISD
    '''


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
