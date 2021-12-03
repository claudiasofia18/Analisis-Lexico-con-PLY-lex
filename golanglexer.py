import ply.lex as lex

"""
EMANUEL
Palabras reservadas, 
Caracteres ()
"""

# EMANUEL
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
    "func": "FUNC",
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
    "var": "VAR",
    "true": "TRUE",
    "false": "FALSE",
    "error": "ERROR",
    "string": "STRINGTYPE",
    "int": "INTTYPE",
    "float": "FLOATTYPE",
    "boolean": "BOOLEANTYPE",
    "fmt": "FMT",
    "Print": "PRINT",
    "list": "LIST",
    "PushBack": "PUSHBACK",
    "Front": "FRONT",
    "Println": "PRINTLN",
    "Printf" : "PRINTF",
    "bufio" : "BUFIO",
    "NewWriter" : "NEWWRITER",
    "NewReader" : "NEWREADER",
    "os" : "OS",
    "Stdout" : "STDOUT",
    "Stdin" : "STDIN",
    "ReadString" : "READSTRING",
    "Fprint" : "FPRINT",
    "New" : "NEW",
    "len" : "LEN",
    "cap" : "CAP",
    "append" : "APPEND",
    "Sscanf" : "SSCANF",
    "Scanf" : "SCANF",
    'delete':'DELETE',
    'make' : "MAKE"
}

tokens = [
             # EMANUEL
             "BRACEL",
             "BRACER",
             "LOCKL",
             "LOCKR",
             "BRACKETL",
             "BRACKETR",
             "SEMICOLON",
             "COLON",
             "COMA",
             "DOT",
             # CLAUDIA
             'ASSIGN',
             'SHORTASSIGN',
             'FLOAT',
             'INTEGER',
             'STRING',
             # Isaac Ponce [ispovala]
             'VARIABLE',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'MODULE',
             'INCREMENT',
             'DECREMENT',
             'EQUAL',
             'UNEQUAL',
             'GREATERTHAN',
             'SMALLERTHAN',
             'GREATEROREQUALTHAN',
             'SMALLEROREQUALTHAN',
             'AND',
             'OR',
             'NOT',
             'AMPERSON'
         ] + list(reserved.values())

# EMANUEL
t_BRACEL = r"\["
t_BRACER = r"\]"
t_LOCKL = r"\{"
t_LOCKR = r"\}"
t_BRACKETL = r"\("
t_BRACKETR = r"\)"
t_SEMICOLON = r";"
t_COLON = r":"
t_COMA = r","
t_DOT = r"\."

"""
CLAUDIA
Tipos de datos,
asignacion,
formateo %s, %d,
error.
"""

# Claudia A.
t_ASSIGN = r'='
t_SHORTASSIGN = r':='
t_STRING = r'("[^"]*"|\'[^\']*\')'

def t_FLOAT(t):
    r'(([1-9]\d*\.\d+)|0.0) | ((^-[1-9]\d*\.\d+)|0.0)'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'(\d+|^-\d+)'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


"""
ISAAC
Definir variables, 
Operadores,
Salto de linea.

"""

# Isaac Ponce [ispovala]

t_AMPERSON = r'&'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULE = r'%'
t_INCREMENT = r'\+{2}'
t_DECREMENT = r'--'
t_EQUAL = r'=='
t_UNEQUAL = r'!='
t_GREATERTHAN = r'>'
t_SMALLERTHAN = r'<'
t_GREATEROREQUALTHAN = r'>='
t_SMALLEROREQUALTHAN = r'<='
t_AND = r'&&'
t_OR = r'\|{2}'
t_NOT = r'!'
t_ignore = ' \t'
t_ignore_comments = r'\/\/.+|\/\*.+\*\/'

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]{,9}'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
 5.5
    '''
lexer.input(data)
while True:
    #data = input(">")
    # Give the lexer some input
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
