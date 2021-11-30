import ply.yacc as yacc
from golanglexer import tokens

'''
01. Operaciones matemáticas                        100%

02. Condición. Operadores de comparación/lógicos   100%
03. Métodos de impresión de datos                  100%
04. Métodos de lectura de datos

05. Estructura de control (FOR)
07. Estructura de control (SWITCH)                 100%
06. Estructura de control (SELECT)


08. Estructura de datos (SLICES)
09. Estructura de datos (LISTAS)
10. Estructura de datos (MAPS)
11. Funciones
'''

########################################################################################################################
#ESTRUCTURAS DE CONTROL
########################################################################################################################
def p_main (p):
    '''main : ejecutable
            | ejecutable main
    '''

def p_ejecutable (p):
    '''ejecutable : estructuraControl
                  | impresion
                  | declaracion
                  | asignacion
    '''

def p_impresion (p):
    '''impresion : impresionSencilla
                  | impresionBufio
                  | impresionFormato
    '''

def p_declaracion_vartipo(p):
    '''declaracion : varAssign tipoDato
    '''
def p_asignacion(p):
    '''asignacion : varShortAssign asignable
                  | varAssign ASSIGN asignable
                  | VARIABLE ASSIGN asignable'''

def p_asignable(p):
    '''asignable : valor
                 | expresionMatematica
                 | condicion'''

def p_estructuraControl_switch(p):
    '''estructuraControl : SWITCH VARIABLE LOCKL cases LOCKR
    '''

def p_cases(p):
    '''cases : case
             | case cases
    '''

def p_case(p):
    '''case : CASE condicionCase COLON main
    '''

def p_impresionSencilla(p):
    '''impresionSencilla : tipoImpresion BRACKETL valores BRACKETR
     '''

def p_tipoImpresion(p):
    '''tipoImpresion : FMT DOT PRINT
                     | FMT DOT PRINTLN
    '''
def p_impresionBufio(p):
    '''impresionBufio : FMT DOT FPRINT BRACKETL VARIABLE COMA STRING BRACKETR '''

def p_impresionFormato(p):
    '''impresionFormato : FMT DOT PRINTF BRACKETL STRING COMA valores BRACKETR'''


def p_declaracion_newWriter(p):
    '''declaracion : varShortAssign BUFIO DOT NEWWRITER BRACKETL OS DOT STDOUT BRACKETR'''

def p_varShortAssign(p):
    '''
    varShortAssign : VARIABLE SHORTASSIGN 
    '''

def p_varAssign(p):
    '''
    varAssign : VAR VARIABLE
    '''
#VERIFICAR CONST

def p_condicionCase(p):
    '''condicionCase : INTEGER
                     | VARIABLE
                     | condicion
    '''

def p_condicion(p):
    '''condicion : valor operadorComparacion valor
                 | valor operadorLogico valor
    '''

def p_operadorComparacion(p):
    '''operadorComparacion : EQUAL
                           | UNEQUAL
                           | GREATERTHAN
                           | SMALLERTHAN
                           | GREATEROREQUALTHAN
                           | SMALLEROREQUALTHAN
    '''
def p_tipoDato(p):
    '''tipoDato : INTTYPE
                | FLOATTYPE
                | BOOLEANTYPE'''
def p_operadorLogico(p):
    ''' operadorLogico : AND
                       | OR
                       | NOT
    '''
#PREGUNTAR AL PROFESOR
def p_expresionMatematica(p):
    '''expresionMatematica : factor operadorMatematico factor
    '''

def p_operadorMatematico(p):
    '''operadorMatematico : PLUS
                          | MINUS
                          | TIMES
                          | DIVIDE
                          | MODULE
    '''

def p_valores(p):
    '''valores : valor
               | valor COMA valores
    '''

def p_valor(p):
    '''valor : STRING
             | factor
    '''

def p_factor(p):
    '''factor : VARIABLE
              | FLOAT
              | INTEGER
              
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