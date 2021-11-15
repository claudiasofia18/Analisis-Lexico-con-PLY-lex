import ply.lex as lex

"""
EMANUEL
Palabras reservadas, 
Caracteres ()
"""

#EMANUEL
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
    #Isaac Ponce [ispovala]
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULE',
    'INCREMENTE',
    'DECREMENT',
    'EQUAL',
    'UNEQUAL',
    'GREATERTHAN',
    'SMALLERTHAN',
    'GREATEROREQUALTHAN',
    'SMALLEROREQUALTHAN',
    'AND',
    'OR',
    'NOT'
 ] + list(reserved.values())

#EMANUEL
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
t_PRINT_F = r'((%f' | r'%\.[0-9]?f)'
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


"""
ISAAC
Definir variables, 
Operadores,
Salto de linea.

"""

#Isaac Ponce [ispovala]


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULE = r'%'
t_INCREMENT = r'\+{2}'
t_DECREMENT = r'--'
t_EQUAL= r'=='
t_UNEQUAL= r'!='
t_GREATERTHAN = r'>'
t_SMALLERTHAN = r'<'
t_GREATEROREQUALTHAN = r'>='
t_SMALLEROREQUALTHAN = r'<='
t_AND = r'&&'
t_OR = r'\|{2}'
t_NOT = r'!'

def t_VARIABLE(t):
  r'^[a-zA-Z_][a-zA-Z_0-9]{,9}$'
  t.type = reserved.get(t.value,'VARIABLE')
  return t

def t_NEWLINE(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

lexer = lex.lex()

# Test it out
data = '''for i in range(4): 
  if 4>5 && 5<4:
    return true
    '''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)




