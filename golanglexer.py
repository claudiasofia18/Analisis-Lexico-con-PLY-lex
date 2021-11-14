import ply.lex as lex

"""

EMANUEL
Palabras reservadas, 
Caracteres (),"""

reserved = {
    "break": "BREAK",
    "case": "CASE",
    "chan": "CHAN",
    "const": "CONST",
    "default": "DEFAULT",
    "defer": "DEFER",
    "else": "ELSE",
    "fallthrough": "FALLTHROUGH",
    "for": "FOR",
    "funct": "FUNCION",
    "go": "GO",
    "goto": "GOTO",
    "if": "IF",
    "import": "IMPORT",
    "interface": "INTERFACE",
    "map": "MAP",
    "package": "PACKAGE",
    "range": "RANGE",
    "return": "RETURN",
    "select": "SELECT",
    "struct": "STRUCT",
    "switch": "SWITCH",
    "type": "TYPE",
    "var": "VAR"
}

tokens = [
    #EMANUEL
             "VARIABLE",
             "ENTERO",
             "DOUBLE",
             "STRING",
             "BOOLEAN",

             "SUMA",
             "RESTA",
             "MULTIPLICACION",
             "DIVISION",
             "MODULO",
             "INCREMENTO",
             "DECREMENTO"


             "IGUAL",
             "DIFERENTE",
             "MAYOR",
             "MENOR",
             "MAYORIGUAL",
             "MENORIGUAL",

             "AND",
             "OR"
             "NOT",

             "CORCHETEI",
             "CORCHETED",
             "LLAVEI",
             "LLAVED",
             "PARENTESISI",
             "PARENTESISD",
             "PUNTOYCOMA",
             "DOSPUNTOS",
             "COMA",
             #CLAUDIA
             'INIVAR',
             'D_SHORTVAR',
             'PRINT_D',
             'PRINT_S',
             'PRINT_F',
             'BOOLEAN',
             'FLOAT',
             'INTEGER',
             'STRING',
             #CLAUDIA

        #EMANUEL
         ] + list(reserved.values())



t_CORCHETEI = r"\["
t_CORCHETED = r"\]"
t_LLAVEI = r"\{"
t_LLAVED = r"\}"
t_PARENTESISI = r"\("
t_PARENTESISD = r"\)"
t_PUNTOYCOMA = r";"
t_DOSPUNTOS = r":"
t_COMA = r","





"""
CLAUDIA
Tipos de datos,
asignacion,
formateo %s, %d,
error.

"""
#Claudia A.
t_INIVAR = r'=',
t_D_SHORTVAR = r':=',
t_PRINT_S = r'%s',
t_PRINT_F = r'(%f' | r'%\.[0-9]?f)'
t_PRINT_D = r'(%d'| r'%[0-9]?\s?d)'

def t_BOOLEAN(t):
    r'(true|false)'

def t_INTEGER(t):
    r'(\d+)|(-\d+)'

def t_FlOAT(t):
    r'\d+\.\d+'

def t_STRING(t):
    r'("[^"]*"|\'[^\']*\')'


def t_ERROR(t):
    print("No se reconoce '%s", t.value[0])
    t.lexer.skip(1)
#Claudia A.


"""
ISSAC
Definir variables, 
Operadores,
salto de  linea,

"""

lexer = lex.lex()




