import ply.lex as lex

"""

EMANUEL
Tokens,
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
             "COMA"
         ] + list(reserved.values())

"""
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







"""
CLAUDIA
Tipos de datos,
asignacion,
formateo %s, %d,

ISSAC
Definir variables, 
Operadores,
salto de  linea,



errores,


"""
