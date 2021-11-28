import ply.yacc as yacc
from golanglexer import tokens





# ISAAC
def p_declaracion_lista(p):
    '''
    declaracion : VARIABLE SHORTASSIGN LIST DOT NEW BRACKETL BRACKETR
    '''


# EMANUEL
def p_declaracion_var(p):
    '''
        declaracion : VARIABLE SHORTASSIGN
    '''


# EMANUEL
def p_declaracion_vartipo(p):
    '''declaracion : VAR VARIABLE FLOATTYPE
                   | VAR VARIABLE INTTYPE
                   | VAR VARIABLE BOOLEANTYPE
    '''


def p_declaracion_factor(p):
    '''
    declaracion : factor
    '''


# EMANUEL
def p_factor_booleano(p):
    ''' factor : TRUE
             | FALSE
    '''


# CLAUDIA
def p_factor_dato(p):
    ''' factor : STRING
             | INTEGER
             | FLOAT
    '''


def p_factor_variable(p):
    '''
    factor : VARIABLE
    '''


def p_factor_reservada(p):
    '''
    factor : reservada
    '''


def p_reservada_var(p):
    '''
    reservada : VAR
    '''


def p_reservada_simbolo(p):
    '''
    reservada : simbolo
    '''

# EMANUEL
def p_simbolo_comparacion(p):
    '''simbolo : EQUAL
               | UNEQUAL
               | GREATERTHAN
               | SMALLERTHAN
               | GREATEROREQUALTHAN
               | SMALLEROREQUALTHAN
    '''

def p_simbolo_bracketr(p):
    '''
    simbolo : BRACKETR
    '''


def p_simbolo_bracketl(p):
    '''
    simbolo : BRACKETL
    '''


def p_simbolo_dot(p):
    '''
    simbolo : DOT
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
