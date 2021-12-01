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
    "func": "FUNCION",
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
    "Printf": "PRINTF",
    "bufio": "BUFIO",
    "NewWriter": "NEWWRITER",
    "os": "OS",
    "Stdout": "STDOUT",
    "Fprint": "FPRINT",
    "New": "NEW",
    "len": "LEN",
    "cap": "CAP",
    "append": "APPEND",
    "Sscanf": "SSCANF",
    "Scanf": "SCANF"
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
t_INTEGER = r'(\d+|^-\d+)'
t_STRING = r'("[^"]*"|\'[^\']*\')'


def t_FLOAT(t):
    r'(([1-9]\d*\.\d+)|0.0) | ((^-[1-9]\d*\.\d+)|0.0)'
    t.value = float(t.value)
    return t


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


def manejar_estado():
    manejar_estado.lexer = None
    manejar_estado.err_sintacticos = 0
    manejar_estado.descr_err_sintacticos = ''
    manejar_estado.err_lexicos = 0
    manejar_estado.descr_err_lexicos = ''
    manejar_estado.codigo = ''


def estados():
    estados.lexer = None
    estados.lex_error = ""
    estados.cont_lex_error = 0
    estados.syntax_error = ""
    estados.cont_syntax_error = ""
    estados.codigo = ''



def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    estados.lex_error = f"Caracter inválido {t.value[0]} en la línea {t.lineno}"
    estados.cont_lex_error += 1
    t.lexer.skip(1)


# states()
estados()


def build_lexer():
    estados.lexer = lex.lex()
    # states.lexer = lex.lex()


def lexanalysis(codigo):
    estados()
    build_lexer()
    estados.codigo = codigo
    lexer = estados.lexer
    lexer.input(codigo)
    while True:
        tok = lexer.token()
        if not tok:
            break
    return estados.lex_error


"""def lexical_analysis(code):
    states()
    build_lexer()
    lexico = states.lexer
    lexico.input(code)
    while True:
        tok = lexico.token()
        if not tok:
            break
    return states.lex_error
"""

# lexer = lex.lex()

# Test it out
data = '''
 func Binary(array []int, target int, lowIndex int, highIndex int) (int, error) {
	if highIndex < lowIndex || len(array) == 0 {
		return -1, ErrNotFound
	}
	mid := int(lowIndex + (highIndex-lowIndex)/2)
	if array[mid] > target {
		return Binary(array, target, lowIndex, mid-1)
	} else if array[mid] < target {
		return Binary(array, target, mid+1, highIndex)
	} else {
		return mid, nil
		~
	}
}
    '''
# Give the lexer some input
"""lexer.input(data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
"""


def p_initmap():
    '''initmap :  VARIABLE SHORTASSIGN MAKE BRACKETL createemptymap BRACKETR'''


def p_lenmap():
    ''' lenmap : len VARIABLE    '''


def p_deletemap():
    '''deletemap: DELETE BRACKETL VARIABLE COMA valor BRACKETR'''


def p_initmapvalue():
    '''initmapvalue: VARIABLE SHORTASSIGN createmap'''


def p_createemptymap():
    ''' createemptymap : MAP t_BRACEL valor t_BRACER valor '''


def p_createmap():
    ''' createmap : MAP t_BRACEL valor t_BRACED valor LOCKL LOCKR '''


def p_mapvalue():
    '''mapvalue : valor COLON valor '''


def p_mapvalues():
    ''' mapvalues : mapvalue
                 |  mapvalue COMA mapvalues
    '''
