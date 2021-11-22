import ply.yacc as yacc
from .golanglexer import tokens

"""
1-3 : DIFICULTAD DE ACTIVIDADES

1. Operaciones matemáticas. 1
2. Condición. Operadores de comparación/lógicos. 1
3. Métodos de impresión de datos. 3
4. Métodos de lectura de datos. 3
5. Estructura de control (FOR) 1
6. Estructura de control (SELECT) 1
7. Estructura de control (SWITCH) 1
8. Estructura de datos (SLICES) 3
9. Estructura de datos (LISTAS) 3
10. Estructura de datos (MAPS) 3
11. Funciones. 1


CLAUDIA 
""" 
#Métodos impresión de datos.
#fmt package

def p_impresionsencilla(p):
   '''impresionsencilla : tipoimpresion PARENTESISI expresion PARENTESISD
                           | tipoimpresion PARENTESISI expresiones PARENTESISD
    '''
def p_tipoimpresion(p):
  '''tipoimpresion : "fmt" PUNTO "Print"
                       | "fmt" PUNTO "Println"
  '''     
def p_impresionformato(p): 
  '''impresionformato: "fmt" PUNTO "Printf" PARENTESISI STRING COMA expresion PARENTESISD
                         | "fmt" PUNTO "Printf" PARENTESISI STRING COMA expresiones PARENTESISD
  '''
def p_expresion(p):
  '''expresion : tipodedato
  '''
def p_expresiones(p):
  '''expresiones : tipodedato COMA tipodedato
  '''

def p_tipodedato(p):
  '''tipodedato : STRING
                  | INTEGER
                  | FLOAT
                  | VARIABLE 
  '''
#bufio package

def p_impressionbufio(p):
  '''impressionbufio : VARIABLE DSHORTVAR "bufio.NewWriter" PARENTESISI "os.Stdout" PARENTESISI NEWLINE impresion
  '''
def p_impresion(p):
  '''impresion: "fmt.Fprint" PARENTESISI VARIABLE COMA tipodedato
  '''
  
#Estructura de datos (SLICES).


#Estructura de control (SWITCH).

def p_switch(p):
  '''switch : SWITCH VARIABLE LLAVEI NEWLINE CASE valor DOSPUNTOS NEWLINE impresionsencilla cases
  '''
def p_cases(p):
  '''cases: CASE valor DOSPUNTOS NEWLINE impresionsencilla
            | DEFAULT DOSPUNTOS NEWLINE impresionsencilla
  '''

def p_valor(p):
  '''valor: condicion
            | VARIABLE  
            | TRUE
            | FALSE
  '''



"""
ISAAC

9
4
5

EMANUEL

10
1
2
11
6


"""


# 1. Operaciones matemáticas. 1

def p_signo(p):
    '''signo : PLUS
             | MINUS
             | TIMES
             | DIVIDE
             | MODULE
    '''


def p_declaracionEntero(p):
    '''declaracionEntero : VAR VARIABLE INTTYPE
                        |  VARIABLE DSHORTVAR
                        |  VAR VARIABLE

    '''


def p_expEntero(p):
    ''' expEntero :  INTEGER
                    | INTEGER signo expEntero
                    | VARIABLE
    '''


def p_declaracionFloat(p):
    '''declaracionFloat :      VAR VARIABLE FLOATTYPE
                            |  VARIABLE DSHORTVAR
                            |  VAR VARIABLE
    '''


def p_expFloat(p):
    '''expFloat :    FLOAT
                   | INTEGER
                   | VARIABLE
                   | FLOAT signo expFloat
                   | INTEGER signo expFloat
                   | VARIABLE signo expFloat
    '''
