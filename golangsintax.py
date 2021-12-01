import ply.yacc as yacc
from golanglexer import tokens

'''
01. Operaciones matemáticas                        100%

02. Condición. Operadores de comparación/lógicos   100%
03. Métodos de impresión de datos                  100%
04. Métodos de lectura de datos                    100%

05. Estructura de control (FOR)                    100%
07. Estructura de control (SWITCH)                 100%
06. Estructura de control (SELECT)                 100%

11. Funciones                                      100%
08. Estructura de datos (SLICES)                   100%
09. Estructura de datos (LISTAS)                   100%
10. Estructura de datos (MAPS)                     100%

'''

def p_main (p):
    '''main : ejecutable
            | funcion
            | ejecutable main
    '''

def p_ejecutable (p):
    '''ejecutable : estructuraControl
                  | estructuraDatos
                  | impresion
                  | declaracion
                  | asignacion
                  | lectura
                  | metodos
                  | expresionMatematica
                  | map
                  | condicion
    '''


def p_impresion(p):
    '''impresion : impresionSencilla
                  | impresionBufio
                  | impresionFormato
    '''


# NUEVO
def p_lectura(p):
    '''lectura : lecturaReader
               | lecturaScanf
               | lecturaSscanf'''

def p_metodos_slice(p):
    '''metodos : lenSlice
               | appendSlice
               | capSlice'''


def p_metodos_lista(p):
    '''metodos : listaPushBack
               | listaFront'''

def p_asignacion(p):
    '''asignacion : varShortAssign asignable
                  | varAssign ASSIGN asignable
                  | VARIABLE ASSIGN asignable
                  | varAssign tipoDato ASSIGN asignable
    '''

def p_declaracion_vartipo(p):
    '''declaracion : varAssign tipoDato
    '''

def p_asignable(p):
    '''asignable : valor
                 | expresionMatematica
                 | condicion'''


#FUNCION
def p_funcion(p):
    '''funcion : FUNC VARIABLE BRACKETL VARIABLE tipoDato BRACKETR tipoDato LOCKL cuerpos LOCKR'''

def p_cuerpos(p):
    '''cuerpos : cuerpo
               | cuerpo cuerpos'''

def p_cuerpo(p):
    '''cuerpo : ejecutable
              | RETURN VARIABLE'''

########################################################################################################################
#ESTRUCTURAS DE CONTROL
########################################################################################################################
def p_estructuraControl_switch(p):
    '''estructuraControl : SWITCH VARIABLE LOCKL cases LOCKR
    '''

def p_estructuraControl_forCondicion(p):
    '''estructuraControl : FOR condicion LOCKL main LOCKR
    '''

def p_estructuraControl_forEstandar(p):
    '''estructuraControl : FOR asignacion SEMICOLON condicion SEMICOLON iterador LOCKL main LOCKR
    '''

def p_estructuraControl_forRange(p):
    '''estructuraControl : FOR VARIABLE COMA varShortAssign RANGE VARIABLE LOCKL main LOCKR
                         | FOR varShortAssign RANGE VARIABLE LOCKL main LOCKR
    '''
#SELECT
def p_estructuraControl_select(p):
    '''estructuraControl : SELECT LOCKL casesSelect LOCKR
    '''

def p_casesSelect(p):
    '''casesSelect : caseSelect
                   | caseSelect casesSelect'''

def p_caseSelect(p):
    '''caseSelect : CASE varShortAssign SMALLERTHAN MINUS COLON main '''

def p_cases(p):
    '''cases : case
             | case cases
    '''

def p_case(p):
    '''case : CASE condicionCase COLON main
    '''

########################################################################################################################
#ESTRUCTURAS DE DATOS
########################################################################################################################

def p_estructuraDatos_slice(p):
    '''estructuraDatos : varShortAssign BRACEL INTEGER BRACER tipoDato LOCKL valores LOCKR
                       | varShortAssign BRACEL BRACER tipoDato LOCKL valores LOCKR
                       | varShortAssign VARIABLE BRACEL COLON BRACER
                       | varShortAssign VARIABLE BRACEL INTEGER COLON BRACER
                       | varShortAssign VARIABLE BRACEL COLON INTEGER BRACER
                       | varShortAssign VARIABLE BRACEL INTEGER COLON INTEGER BRACER
    '''

def p_lenSlice(p):
    '''lenSlice : LEN BRACKETL VARIABLE BRACKETR
    '''

def p_appendSlice(p):
    '''appendSlice : APPEND BRACKETL VARIABLE valores BRACKETR
                   | VARIABLE ASSIGN APPEND BRACKETL VARIABLE valores BRACKETR
    '''

def p_capSlice(p):
    '''capSlice : CAP BRACKETL VARIABLE BRACKETR
    '''

def p_estructuraDatos_lista(p):
    '''estructuraDatos : varShortAssign LIST DOT NEW BRACKETL BRACKETR'''

def p_listaPushBack(p):
    '''
    listaPushBack : VARIABLE DOT PUSHBACK BRACKETL tipoDato BRACKETR
    '''

def p_listaFront(p):
    '''
    listaFront : VARIABLE DOT FRONT BRACKETL BRACKETR
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

#REVISADO ADJUNTAR AL ALGORITMO
def p_lecturaReader(p):
    '''lecturaReader : varShortAssign VARIABLE DOT READSTRING BRACKETL STRING BRACKETR '''

def p_lecturaScanf(p):
    '''lecturaScanf : FMT DOT SCANF BRACKETL STRING opcionLectura BRACKETR '''

def p_opcionLectura(p):
    '''opcionLectura : COMA opciones
                     | COMA opciones opcionLectura  
    '''
    
def p_ampersand(p):
    '''ampersand : AMPERSON VARIABLE'''

def p_lecturaSscanf(p):
    '''lecturaSscanf : FMT DOT SSCANF BRACKETL opcionesLectura BRACKETR'''

def p_opcionesLectura(p):
    '''opcionesLectura : opciones 
                       | opciones COMA opcionesLectura '''

def p_opciones(p):
    '''opciones : STRING
                | ampersand'''

def p_declaracion_newReader(p):
    '''declaracion : varShortAssign BUFIO DOT NEWREADER BRACKETL OS DOT STDIN BRACKETR'''
###############################################################################################
def p_declaracion_newWriter(p):
    '''declaracion : varShortAssign BUFIO DOT NEWWRITER BRACKETL OS DOT STDOUT BRACKETR'''

def p_varShortAssign(p):
    '''
    varShortAssign : VARIABLE SHORTASSIGN 
    '''

#VERIFICAR CONST
def p_varAssign(p):
    '''
    varAssign : VAR VARIABLE
    '''

def p_condicionCase(p):
    '''condicionCase : INTEGER
                     | VARIABLE
                     | condicion
    '''

def p_condicion(p):
    '''condicion : valor operadorComparacion valor
                 | valor operadorLogico valor
                 | comparaciones
    '''

def p_comparaciones_igual(p):
    '''comparaciones : INTEGER EQUAL INTEGER
    '''
    print(p[1]==p[3])

def p_comparaciones_noigual(p):
    '''comparaciones : INTEGER UNEQUAL INTEGER
    '''
    print(p[1]!=p[3])

def p_comparaciones_mayorque(p):
    '''comparaciones : INTEGER GREATERTHAN INTEGER
    '''
    print(p[1]>p[3])

def p_comparaciones_menorque(p):
    '''comparaciones : INTEGER SMALLERTHAN INTEGER
    '''
    print(p[1]<p[3])

def p_comparaciones_mayoroigual(p):
    '''comparaciones : INTEGER GREATEROREQUALTHAN INTEGER
    '''
    print(p[1]>=p[3])

def p_comparaciones_menoroigual(p):
    '''comparaciones : INTEGER SMALLEROREQUALTHAN INTEGER
    '''
    print(p[1]<=p[3])


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

def p_map(p):
    ''' map : initmapvalue
            | initmap
    '''
def p_lenmap(p):
    ''' lenmap : LEN VARIABLE    '''
def p_deletemap(p):
    '''deletemap : DELETE BRACKETL VARIABLE COMA valor BRACKETR'''

def p_initmapvalue(p):
        '''initmapvalue : VARIABLE SHORTASSIGN createmap'''

def p_initmap(p):
    '''initmap :  VARIABLE SHORTASSIGN MAKE BRACKETL createemptymap BRACKETR'''

def p_createemptymap(p):
    ''' createemptymap : MAP BRACEL tipoDato BRACER tipoDato '''


def p_createmap(p):
    '''createmap : MAP BRACEL tipoDato BRACER tipoDato LOCKL mapvalues LOCKR '''


def p_mapvalues(p):
    ''' mapvalues : mapvalue
                  | mapvalue COMA mapvalues
    '''


def p_mapvalue(p):
    '''mapvalue : valor COLON valor
    '''


def p_tipoDato(p):
    '''tipoDato : INTTYPE
                | FLOATTYPE
                | BOOLEANTYPE
                | STRINGTYPE
                '''


def p_operadorLogico(p):
    ''' operadorLogico : AND
                       | OR
                       | NOT
    '''


# PREGUNTAR AL PROFESOR
def p_expresionMatematica(p):
    '''expresionMatematica : expresionSuma
                           | expresionResta
                           | expresionMultiplicacion
                           | expresionDivision
                           | expresionModulo
                           | factor operadorMatematico factor
    '''

def p_expresionSuma(p):
    'expresionSuma : INTEGER PLUS INTEGER'
    p[0] = p[1] + p[3]
    print(p[0])

def p_expresionResta(p):
    'expresionResta : INTEGER MINUS INTEGER'
    p[0] = p[1] - p[3]
    print(p[0])


def p_expresionMultiplicacion(p):
    'expresionMultiplicacion : INTEGER TIMES INTEGER'
    p[0] = p[1] * p[3]
    print(p[0])

def p_expresionDivision(p):
    'expresionDivision : INTEGER DIVIDE INTEGER'
    p[0] = p[1] / p[3]
    print(p[0])

def p_expresionModulo(p):
    'expresionModulo : INTEGER MODULE INTEGER'
    p[0] = p[1] % p[3]
    print(p[0])


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
    return p

def p_factor(p):
    '''factor : VARIABLE
              | numero
    '''

def p_numero(p):
    '''numero : FLOAT
              | INTEGER
    '''
    return p



def p_iterador(p):
    '''iterador : VARIABLE INCREMENT
                | VARIABLE DECREMENT
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