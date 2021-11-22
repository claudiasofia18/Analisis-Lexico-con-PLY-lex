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
    "Println": "PRINTLN",
    "Printf" : "PRINTF",
    "bufio" : "BUFIO",
    "NewWriter" : "NEWWRITER",
    "os" : "OS",
    "Stdout" : "STDOUT",
    "Fprint" : "FPRINT",
    "new" : "NEW",
    "len" : "LEN",
    "cap" : "CAP",
    "append" : "APPEND",
    


}

tokens = [
             # EMANUEL
             "CORCHETEI",
             "CORCHETED",
             "LLAVEI",
             "LLAVED",
             "PARENTESISI",
             "PARENTESISD",
             "PUNTOYCOMA",
             "DOSPUNTOS",
             "COMA",
             "PUNTO",
             # CLAUDIA
             'INIVAR',
             'DSHORTVAR',
             'PRINTD',
             'PRINTS',
             'PRINTF',
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
             'NOT'
         ] + list(reserved.values())

# EMANUEL
t_CORCHETEI = r"\["
t_CORCHETED = r"\]"
t_LLAVEI = r"\{"
t_LLAVED = r"\}"
t_PARENTESISI = r"\("
t_PARENTESISD = r"\)"
t_PUNTOYCOMA = r";"
t_DOSPUNTOS = r":"
t_COMA = r","
t_PUNTO = r"\."

"""
CLAUDIA
Tipos de datos,
asignacion,
formateo %s, %d,
error.
"""

# Claudia A.
t_INIVAR = r'='
t_DSHORTVAR = r':='
t_PRINTS = r'%s'
t_PRINTF = r'(%f | %\.[0-9]?f)'
t_INTEGER = r'(\d+|-\d+)'
t_FLOAT = r'\d+\.\d+'
t_STRING = r'("[^"]*"|\'[^\']*\')'


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


def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]{,9}'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Build the lexer
lexer = lex.lex()
'Si todo es correcto se construye!'

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
lexer.input(data)

'Lo que se quiere enviar '

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
