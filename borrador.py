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

# CLAUDIA
def p_declaracion_slice(p):
    '''declaracion_slice : VAR VARIABLE ASSIGN BRACEL BRACER LLAVEI expresion LLAVED
                          | VAR VARIABLE ASSIGN BRACEL BRACER LLAVEI expresiones LLAVED
                          | VAR VARIABLE ASSIGN NEW BRACKETL BRACEL INTEGER BRACER dato BRACKETR BRACEL INTEGER COLON BRACER
                          | VARIABLE SHORTASSIGN slice BRACEL COLON BRACER
                          | VARIABLE SHORTASSIGN slice BRACEL INTEGER COLON BRACER
                          | VARIABLE SHORTASSIGN slice BRACEL COLON INTEGER BRACER
                          | VARIABLE SHORTASSIGN slice BRACEL INTEGER COLON INTEGER BRACER
    '''
# CLAUDIA
def p_len_slice(p):
    '''len_slice : LEN BRACKETL slice BRACKETR
    '''
# CLAUDIA
def p_append_slice(p):
    '''append_slice : slice ASSIGN APPEND BRACKETL slice COMA expresion
                     | slice ASSIGN APPEND BRACKETL slice COMA expresiones
    '''
# CLAUDIA
def p_cap_slice(p):
    '''cap_slice : CAP BRACKETL slice BRACKETR
    '''

# CLAUDIA
def p_switch(p):
    '''switch : SWITCH VARIABLE LLAVEI NEWLINE CASE valor COLON NEWLINE impresionsencilla cases LLAVED
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
# ISAAC
def p_PushBack(p):
    '''
    listaPushBack : VARIABLE DOT PUSHBACK BRACKETL tipodedato BRACKETR
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
def p_listaFront(p):
    '''
    listaFront : variable dot FRONT bracketl bracketr
    '''

# ISAAC
def p_lecturaSscanf(p):
    '''
    lecturaSscanf : FMT DOT SSCANF BRACKETL STRING COMA STRING COMA AMPERSON VARIABLE BRACKETR
    '''

# CLAUDIA
def p_tipoimpresion(p):
    '''tipoimpresion : FMT DOT PRINT
                         | FMT DOT PRINTLN
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