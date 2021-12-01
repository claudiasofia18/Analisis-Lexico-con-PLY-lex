import ply.yacc as yacc
from golanglexer import tokens

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
    ''' asignacion : declaracionEntero ASSIGN expEntero
                    | declaracionFloat ASSIGN expFloat
                    | declaracionBool ASSIGN expBool
    '''




def p_forEstandar(p):
    '''
    forEstandar : FOR asignacion SEMICOLON condicion SEMICOLON INCREMENT LLAVEI asignacion LLAVED
                | FOR asignacion SEMICOLON condicion SEMICOLON DECREMENT LLAVEI asignacion LLAVED
    '''
# ISAAC
def p_forRango(p):
    '''
    forRango : FOR VARIABLE COMA VARIABLE SHORTASSIGN RANGE VARIABLE LLAVEI asignacion LLAVED
             | FOR VARIABLE SHORTASSIGN RANGE VARIABLE LLAVEI asignacion LLAVED
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


# CLAUDIA
def p_cases(p):
    '''cases : CASE valor COLON NEWLINE impresionsencilla
              | DEFAULT COLON NEWLINE impresionsencilla
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
    ''' cabecerafunction : FUNCION VARIABLE BRACKETL arguments BRACKETR  '''

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
    '''slicevacio : VAR VARIABLE BRACEL BRACER dato
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



# ISAAC
def p_lecturaSscanf(p):
    '''
    lecturaSscanf : FMT DOT SSCANF BRACKETL STRING COMA STRING COMA AMPERSON VARIABLE BRACKETR
    '''
# ISAAC
def p_lecturaScanf(p):
    '''
    lecturaScanf : FMT DOT SCANF BRACKETL STRING COMA AMPERSON VARIABLE BRACKETR
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