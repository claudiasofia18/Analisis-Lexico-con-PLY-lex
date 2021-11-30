import ply.yacc as yacc
from golanglexer import tokens

'''
01. Operaciones matemáticas
02. Condición. Operadores de comparación/lógicos   100%
03. Métodos de impresión de datos                   50%
04. Métodos de lectura de datos
05. Estructura de control (FOR)
06. Estructura de control (SELECT)
07. Estructura de control (SWITCH)                 100%
08. Estructura de datos (SLICES)
09. Estructura de datos (LISTAS)
10. Estructura de datos (MAPS)
11. Funciones
'''

########################################################################################################################
#ESTRUCTURAS DE CONTROL
########################################################################################################################

# Estructura de control (SWITCH).
def p_ejecutable (p):
    '''ejecutable : estructuraControl
                  | impresionSencilla
    '''

def p_estructuraControl_switch(p):
    '''estructuraControl : SWITCH VARIABLE LOCKL cases LOCKR
    '''

def p_cases(p):
    '''cases : case
             | case cases
    '''

def p_case(p):
    '''case : CASE condicionCase COLON ejecutable
    '''

def p_impresionSencilla(p):
    '''impresionSencilla : tipoImpresion BRACKETL valores BRACKETR
     '''

def p_tipoImpresion(p):
    '''tipoImpresion : FMT DOT PRINT
                     | FMT DOT PRINTLN
    '''

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

def p_operadorLogico(p):
    ''' operadorLogico : AND
                       | OR
                       | NOT
    '''

def p_valores(p):
    '''valores : valor
               | valor COMA valores
    '''

def p_valor(p):
    '''valor : STRING
             | INTEGER
             | FLOAT
             | VARIABLE
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
