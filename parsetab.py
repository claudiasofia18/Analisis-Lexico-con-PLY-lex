
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSON AND APPEND ASSIGN BOOLEANTYPE BRACEL BRACER BRACKETL BRACKETR BREAK BUFIO CAP CASE CHAN COLON COMA CONST DECREMENT DEFAULT DEFER DIVIDE DOT ELSE EQUAL ERROR FALLTHROUGH FALSE FLOAT FLOATTYPE FMT FOR FPRINT FRONT FUNCION GO GOTO GREATEROREQUALTHAN GREATERTHAN IF IMPORT INCREMENT INTEGER INTERFACE INTTYPE LEN LIST LOCKL LOCKR MAP MINUS MODULE NEW NEWWRITER NOT OR OS PACKAGE PLUS PRINT PRINTF PRINTLN PUSHBACK RANGE RETURN SCANF SELECT SEMICOLON SHORTASSIGN SMALLEROREQUALTHAN SMALLERTHAN SSCANF STDOUT STRING STRINGTYPE STRUCT SWITCH TIMES TRUE TYPE UNEQUAL VAR VARIABLEmain : ejecutable\n            | ejecutable main\n    ejecutable : estructuraControl\n                  | impresion\n                  | declaracion\n                  | asignacion\n    impresion : impresionSencilla\n                  | impresionBufio\n                  | impresionFormato\n    asignacion : varShortAssign asignable\n                  | varAssign ASSIGN asignable\n                  | VARIABLE ASSIGN asignable\n                  | varAssign tipoDato ASSIGN asignable\n    declaracion : varAssign tipoDato\n    asignable : valor\n                 | expresionMatematica\n                 | condicionestructuraControl : SWITCH VARIABLE LOCKL cases LOCKR\n    estructuraControl : FOR condicion LOCKL main LOCKR\n    estructuraControl : FOR asignacion SEMICOLON condicion SEMICOLON iterador LOCKL main LOCKR\n    estructuraControl : FOR VARIABLE COMA varShortAssign RANGE VARIABLE LOCKL main LOCKR\n                         | FOR varShortAssign RANGE VARIABLE LOCKL main LOCKR\n    cases : case\n             | case cases\n    case : CASE condicionCase COLON main\n    impresionSencilla : tipoImpresion BRACKETL valores BRACKETR\n     tipoImpresion : FMT DOT PRINT\n                     | FMT DOT PRINTLN\n    impresionBufio : FMT DOT FPRINT BRACKETL VARIABLE COMA STRING BRACKETR impresionFormato : FMT DOT PRINTF BRACKETL STRING COMA valores BRACKETRdeclaracion : varShortAssign BUFIO DOT NEWWRITER BRACKETL OS DOT STDOUT BRACKETR\n    varShortAssign : VARIABLE SHORTASSIGN \n    \n    varAssign : VAR VARIABLE\n    condicionCase : INTEGER\n                     | VARIABLE\n                     | condicion\n    condicion : valor operadorComparacion valor\n                 | valor operadorLogico valor\n    operadorComparacion : EQUAL\n                           | UNEQUAL\n                           | GREATERTHAN\n                           | SMALLERTHAN\n                           | GREATEROREQUALTHAN\n                           | SMALLEROREQUALTHAN\n    tipoDato : INTTYPE\n                | FLOATTYPE\n                | BOOLEANTYPE operadorLogico : AND\n                       | OR\n                       | NOT\n    expresionMatematica : factor operadorMatematico factor\n    operadorMatematico : PLUS\n                          | MINUS\n                          | TIMES\n                          | DIVIDE\n                          | MODULE\n    valores : valor\n               | valor COMA valores\n    valor : STRING\n             | factor\n    factor : VARIABLE\n              | FLOAT\n              | INTEGER\n              \n    iterador : VARIABLE INCREMENT\n                | VARIABLE DECREMENT\n    '
    
_lr_action_items = {'SWITCH':([0,2,3,4,5,6,11,12,13,28,29,30,31,33,34,35,36,37,38,39,41,42,43,48,49,73,88,89,91,92,93,97,103,106,111,120,123,124,131,132,133,134,135,],[7,7,-3,-4,-5,-6,-7,-8,-9,-59,-60,-62,-63,-10,-15,-16,-17,-60,-61,-14,-45,-46,-47,-12,7,-11,-37,-38,-51,-13,-26,-18,-19,7,7,7,7,-22,-29,-30,-20,-21,-31,]),'FOR':([0,2,3,4,5,6,11,12,13,28,29,30,31,33,34,35,36,37,38,39,41,42,43,48,49,73,88,89,91,92,93,97,103,106,111,120,123,124,131,132,133,134,135,],[9,9,-3,-4,-5,-6,-7,-8,-9,-59,-60,-62,-63,-10,-15,-16,-17,-60,-61,-14,-45,-46,-47,-12,9,-11,-37,-38,-51,-13,-26,-18,-19,9,9,9,9,-22,-29,-30,-20,-21,-31,]),'VARIABLE':([0,2,3,4,5,6,7,9,10,11,12,13,17,20,21,25,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,73,82,88,89,91,92,93,94,95,97,103,104,105,106,111,118,120,123,124,131,132,133,134,135,],[8,8,-3,-4,-5,-6,19,24,38,-7,-8,-9,46,38,-32,38,-59,-60,-62,-63,-10,-15,-16,-17,-60,-61,-14,38,-45,-46,-47,38,-12,8,38,85,87,38,38,-39,-40,-41,-42,-43,-44,-48,-49,-50,38,-52,-53,-54,-55,-56,38,-11,101,-37,-38,-51,-13,-26,38,109,-18,-19,113,114,8,8,38,8,8,-22,-29,-30,-20,-21,-31,]),'FMT':([0,2,3,4,5,6,11,12,13,28,29,30,31,33,34,35,36,37,38,39,41,42,43,48,49,73,88,89,91,92,93,97,103,106,111,120,123,124,131,132,133,134,135,],[16,16,-3,-4,-5,-6,-7,-8,-9,-59,-60,-62,-63,-10,-15,-16,-17,-60,-61,-14,-45,-46,-47,-12,16,-11,-37,-38,-51,-13,-26,-18,-19,16,16,16,16,-22,-29,-30,-20,-21,-31,]),'VAR':([0,2,3,4,5,6,9,11,12,13,28,29,30,31,33,34,35,36,37,38,39,41,42,43,48,49,73,88,89,91,92,93,97,103,106,111,120,123,124,131,132,133,134,135,],[17,17,-3,-4,-5,-6,17,-7,-8,-9,-59,-60,-62,-63,-10,-15,-16,-17,-60,-61,-14,-45,-46,-47,-12,17,-11,-37,-38,-51,-13,-26,-18,-19,17,17,17,17,-22,-29,-30,-20,-21,-31,]),'$end':([1,2,3,4,5,6,11,12,13,18,28,29,30,31,33,34,35,36,37,38,39,41,42,43,48,73,88,89,91,92,93,97,103,124,131,132,133,134,135,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-2,-59,-60,-62,-63,-10,-15,-16,-17,-60,-61,-14,-45,-46,-47,-12,-11,-37,-38,-51,-13,-26,-18,-19,-22,-29,-30,-20,-21,-31,]),'LOCKR':([2,3,4,5,6,11,12,13,18,28,29,30,31,33,34,35,36,37,38,39,41,42,43,48,73,80,81,83,88,89,91,92,93,97,98,103,115,119,124,128,129,131,132,133,134,135,],[-1,-3,-4,-5,-6,-7,-8,-9,-2,-59,-60,-62,-63,-10,-15,-16,-17,-60,-61,-14,-45,-46,-47,-12,-11,97,-23,103,-37,-38,-51,-13,-26,-18,-24,-19,124,-25,-22,133,134,-29,-30,-20,-21,-31,]),'CASE':([2,3,4,5,6,11,12,13,18,28,29,30,31,33,34,35,36,37,38,39,41,42,43,47,48,73,81,88,89,91,92,93,97,103,119,124,131,132,133,134,135,],[-1,-3,-4,-5,-6,-7,-8,-9,-2,-59,-60,-62,-63,-10,-15,-16,-17,-60,-61,-14,-45,-46,-47,82,-12,-11,82,-37,-38,-51,-13,-26,-18,-19,-25,-22,-29,-30,-20,-21,-31,]),'ASSIGN':([8,14,24,27,39,41,42,43,46,64,],[20,40,20,40,72,-45,-46,-47,-33,72,]),'SHORTASSIGN':([8,24,85,],[21,21,21,]),'STRING':([9,10,20,21,25,40,44,50,53,54,55,56,57,58,59,60,61,62,63,72,82,94,96,117,118,],[28,28,28,-32,28,28,28,28,28,28,-39,-40,-41,-42,-43,-44,-48,-49,-50,28,28,28,110,126,28,]),'FLOAT':([9,10,20,21,25,40,44,50,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,82,94,118,],[30,30,30,-32,30,30,30,30,30,30,-39,-40,-41,-42,-43,-44,-48,-49,-50,30,-52,-53,-54,-55,-56,30,30,30,30,]),'INTEGER':([9,10,20,21,25,40,44,50,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,82,94,118,],[31,31,31,-32,31,31,31,31,31,31,-39,-40,-41,-42,-43,-44,-48,-49,-50,31,-52,-53,-54,-55,-56,31,100,31,31,]),'BUFIO':([10,21,],[32,-32,]),'INTTYPE':([14,27,46,],[41,41,-33,]),'FLOATTYPE':([14,27,46,],[42,42,-33,]),'BOOLEANTYPE':([14,27,46,],[43,43,-33,]),'BRACKETL':([15,76,77,78,79,90,],[44,95,96,-27,-28,107,]),'DOT':([16,32,116,],[45,65,125,]),'LOCKL':([19,22,28,29,30,31,38,87,88,89,112,114,121,122,],[47,49,-59,-60,-62,-63,-61,106,-37,-38,120,123,-64,-65,]),'RANGE':([21,25,86,],[-32,52,105,]),'SEMICOLON':([23,28,29,30,31,33,34,35,36,37,38,48,73,84,88,89,91,92,],[50,-59,-60,-62,-63,-10,-15,-16,-17,-60,-61,-12,-11,104,-37,-38,-51,-13,]),'COMA':([24,28,29,30,31,38,75,109,110,],[51,-59,-60,-62,-63,-61,94,117,118,]),'EQUAL':([24,26,28,29,30,31,34,37,38,100,101,],[-61,55,-59,-60,-62,-63,55,-60,-61,-63,-61,]),'UNEQUAL':([24,26,28,29,30,31,34,37,38,100,101,],[-61,56,-59,-60,-62,-63,56,-60,-61,-63,-61,]),'GREATERTHAN':([24,26,28,29,30,31,34,37,38,100,101,],[-61,57,-59,-60,-62,-63,57,-60,-61,-63,-61,]),'SMALLERTHAN':([24,26,28,29,30,31,34,37,38,100,101,],[-61,58,-59,-60,-62,-63,58,-60,-61,-63,-61,]),'GREATEROREQUALTHAN':([24,26,28,29,30,31,34,37,38,100,101,],[-61,59,-59,-60,-62,-63,59,-60,-61,-63,-61,]),'SMALLEROREQUALTHAN':([24,26,28,29,30,31,34,37,38,100,101,],[-61,60,-59,-60,-62,-63,60,-60,-61,-63,-61,]),'AND':([24,26,28,29,30,31,34,37,38,100,101,],[-61,61,-59,-60,-62,-63,61,-60,-61,-63,-61,]),'OR':([24,26,28,29,30,31,34,37,38,100,101,],[-61,62,-59,-60,-62,-63,62,-60,-61,-63,-61,]),'NOT':([24,26,28,29,30,31,34,37,38,100,101,],[-61,63,-59,-60,-62,-63,63,-60,-61,-63,-61,]),'BRACKETR':([28,29,30,31,38,74,75,108,126,127,130,],[-59,-60,-62,-63,-61,93,-57,-58,131,132,135,]),'COLON':([28,29,30,31,38,88,89,99,100,101,102,],[-59,-60,-62,-63,-61,-37,-38,111,-34,-35,-36,]),'PLUS':([30,31,37,38,],[-62,-63,67,-61,]),'MINUS':([30,31,37,38,],[-62,-63,68,-61,]),'TIMES':([30,31,37,38,],[-62,-63,69,-61,]),'DIVIDE':([30,31,37,38,],[-62,-63,70,-61,]),'MODULE':([30,31,37,38,],[-62,-63,71,-61,]),'FPRINT':([45,],[76,]),'PRINTF':([45,],[77,]),'PRINT':([45,],[78,]),'PRINTLN':([45,],[79,]),'NEWWRITER':([65,],[90,]),'OS':([107,],[116,]),'INCREMENT':([113,],[121,]),'DECREMENT':([113,],[122,]),'STDOUT':([125,],[130,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,2,49,106,111,120,123,],[1,18,83,115,119,128,129,]),'ejecutable':([0,2,49,106,111,120,123,],[2,2,2,2,2,2,2,]),'estructuraControl':([0,2,49,106,111,120,123,],[3,3,3,3,3,3,3,]),'impresion':([0,2,49,106,111,120,123,],[4,4,4,4,4,4,4,]),'declaracion':([0,2,49,106,111,120,123,],[5,5,5,5,5,5,5,]),'asignacion':([0,2,9,49,106,111,120,123,],[6,6,23,6,6,6,6,6,]),'varShortAssign':([0,2,9,49,51,106,111,120,123,],[10,10,25,10,86,10,10,10,10,]),'impresionSencilla':([0,2,49,106,111,120,123,],[11,11,11,11,11,11,11,]),'impresionBufio':([0,2,49,106,111,120,123,],[12,12,12,12,12,12,12,]),'impresionFormato':([0,2,49,106,111,120,123,],[13,13,13,13,13,13,13,]),'varAssign':([0,2,9,49,106,111,120,123,],[14,14,27,14,14,14,14,14,]),'tipoImpresion':([0,2,49,106,111,120,123,],[15,15,15,15,15,15,15,]),'condicion':([9,10,20,25,40,50,72,82,],[22,36,36,36,36,84,36,102,]),'valor':([9,10,20,25,40,44,50,53,54,72,82,94,118,],[26,34,34,34,34,75,26,88,89,34,26,75,75,]),'factor':([9,10,20,25,40,44,50,53,54,66,72,82,94,118,],[29,37,37,37,37,29,29,29,29,91,37,29,29,29,]),'asignable':([10,20,25,40,72,],[33,48,33,73,92,]),'expresionMatematica':([10,20,25,40,72,],[35,35,35,35,35,]),'tipoDato':([14,27,],[39,64,]),'operadorComparacion':([26,34,],[53,53,]),'operadorLogico':([26,34,],[54,54,]),'operadorMatematico':([37,],[66,]),'valores':([44,94,118,],[74,108,127,]),'cases':([47,81,],[80,98,]),'case':([47,81,],[81,81,]),'condicionCase':([82,],[99,]),'iterador':([104,],[112,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> ejecutable','main',1,'p_main','golangsintax.py',26),
  ('main -> ejecutable main','main',2,'p_main','golangsintax.py',27),
  ('ejecutable -> estructuraControl','ejecutable',1,'p_ejecutable','golangsintax.py',31),
  ('ejecutable -> impresion','ejecutable',1,'p_ejecutable','golangsintax.py',32),
  ('ejecutable -> declaracion','ejecutable',1,'p_ejecutable','golangsintax.py',33),
  ('ejecutable -> asignacion','ejecutable',1,'p_ejecutable','golangsintax.py',34),
  ('impresion -> impresionSencilla','impresion',1,'p_impresion','golangsintax.py',38),
  ('impresion -> impresionBufio','impresion',1,'p_impresion','golangsintax.py',39),
  ('impresion -> impresionFormato','impresion',1,'p_impresion','golangsintax.py',40),
  ('asignacion -> varShortAssign asignable','asignacion',2,'p_asignacion','golangsintax.py',44),
  ('asignacion -> varAssign ASSIGN asignable','asignacion',3,'p_asignacion','golangsintax.py',45),
  ('asignacion -> VARIABLE ASSIGN asignable','asignacion',3,'p_asignacion','golangsintax.py',46),
  ('asignacion -> varAssign tipoDato ASSIGN asignable','asignacion',4,'p_asignacion','golangsintax.py',47),
  ('declaracion -> varAssign tipoDato','declaracion',2,'p_declaracion_vartipo','golangsintax.py',51),
  ('asignable -> valor','asignable',1,'p_asignable','golangsintax.py',55),
  ('asignable -> expresionMatematica','asignable',1,'p_asignable','golangsintax.py',56),
  ('asignable -> condicion','asignable',1,'p_asignable','golangsintax.py',57),
  ('estructuraControl -> SWITCH VARIABLE LOCKL cases LOCKR','estructuraControl',5,'p_estructuraControl_switch','golangsintax.py',60),
  ('estructuraControl -> FOR condicion LOCKL main LOCKR','estructuraControl',5,'p_estructuraControl_forCondicion','golangsintax.py',64),
  ('estructuraControl -> FOR asignacion SEMICOLON condicion SEMICOLON iterador LOCKL main LOCKR','estructuraControl',9,'p_estructuraControl_forEstandar','golangsintax.py',68),
  ('estructuraControl -> FOR VARIABLE COMA varShortAssign RANGE VARIABLE LOCKL main LOCKR','estructuraControl',9,'p_estructuraControl_forRange','golangsintax.py',72),
  ('estructuraControl -> FOR varShortAssign RANGE VARIABLE LOCKL main LOCKR','estructuraControl',7,'p_estructuraControl_forRange','golangsintax.py',73),
  ('cases -> case','cases',1,'p_cases','golangsintax.py',77),
  ('cases -> case cases','cases',2,'p_cases','golangsintax.py',78),
  ('case -> CASE condicionCase COLON main','case',4,'p_case','golangsintax.py',82),
  ('impresionSencilla -> tipoImpresion BRACKETL valores BRACKETR','impresionSencilla',4,'p_impresionSencilla','golangsintax.py',86),
  ('tipoImpresion -> FMT DOT PRINT','tipoImpresion',3,'p_tipoImpresion','golangsintax.py',90),
  ('tipoImpresion -> FMT DOT PRINTLN','tipoImpresion',3,'p_tipoImpresion','golangsintax.py',91),
  ('impresionBufio -> FMT DOT FPRINT BRACKETL VARIABLE COMA STRING BRACKETR','impresionBufio',8,'p_impresionBufio','golangsintax.py',94),
  ('impresionFormato -> FMT DOT PRINTF BRACKETL STRING COMA valores BRACKETR','impresionFormato',8,'p_impresionFormato','golangsintax.py',97),
  ('declaracion -> varShortAssign BUFIO DOT NEWWRITER BRACKETL OS DOT STDOUT BRACKETR','declaracion',9,'p_declaracion_newWriter','golangsintax.py',101),
  ('varShortAssign -> VARIABLE SHORTASSIGN','varShortAssign',2,'p_varShortAssign','golangsintax.py',105),
  ('varAssign -> VAR VARIABLE','varAssign',2,'p_varAssign','golangsintax.py',111),
  ('condicionCase -> INTEGER','condicionCase',1,'p_condicionCase','golangsintax.py',115),
  ('condicionCase -> VARIABLE','condicionCase',1,'p_condicionCase','golangsintax.py',116),
  ('condicionCase -> condicion','condicionCase',1,'p_condicionCase','golangsintax.py',117),
  ('condicion -> valor operadorComparacion valor','condicion',3,'p_condicion','golangsintax.py',121),
  ('condicion -> valor operadorLogico valor','condicion',3,'p_condicion','golangsintax.py',122),
  ('operadorComparacion -> EQUAL','operadorComparacion',1,'p_operadorComparacion','golangsintax.py',126),
  ('operadorComparacion -> UNEQUAL','operadorComparacion',1,'p_operadorComparacion','golangsintax.py',127),
  ('operadorComparacion -> GREATERTHAN','operadorComparacion',1,'p_operadorComparacion','golangsintax.py',128),
  ('operadorComparacion -> SMALLERTHAN','operadorComparacion',1,'p_operadorComparacion','golangsintax.py',129),
  ('operadorComparacion -> GREATEROREQUALTHAN','operadorComparacion',1,'p_operadorComparacion','golangsintax.py',130),
  ('operadorComparacion -> SMALLEROREQUALTHAN','operadorComparacion',1,'p_operadorComparacion','golangsintax.py',131),
  ('tipoDato -> INTTYPE','tipoDato',1,'p_tipoDato','golangsintax.py',134),
  ('tipoDato -> FLOATTYPE','tipoDato',1,'p_tipoDato','golangsintax.py',135),
  ('tipoDato -> BOOLEANTYPE','tipoDato',1,'p_tipoDato','golangsintax.py',136),
  ('operadorLogico -> AND','operadorLogico',1,'p_operadorLogico','golangsintax.py',138),
  ('operadorLogico -> OR','operadorLogico',1,'p_operadorLogico','golangsintax.py',139),
  ('operadorLogico -> NOT','operadorLogico',1,'p_operadorLogico','golangsintax.py',140),
  ('expresionMatematica -> factor operadorMatematico factor','expresionMatematica',3,'p_expresionMatematica','golangsintax.py',144),
  ('operadorMatematico -> PLUS','operadorMatematico',1,'p_operadorMatematico','golangsintax.py',148),
  ('operadorMatematico -> MINUS','operadorMatematico',1,'p_operadorMatematico','golangsintax.py',149),
  ('operadorMatematico -> TIMES','operadorMatematico',1,'p_operadorMatematico','golangsintax.py',150),
  ('operadorMatematico -> DIVIDE','operadorMatematico',1,'p_operadorMatematico','golangsintax.py',151),
  ('operadorMatematico -> MODULE','operadorMatematico',1,'p_operadorMatematico','golangsintax.py',152),
  ('valores -> valor','valores',1,'p_valores','golangsintax.py',156),
  ('valores -> valor COMA valores','valores',3,'p_valores','golangsintax.py',157),
  ('valor -> STRING','valor',1,'p_valor','golangsintax.py',161),
  ('valor -> factor','valor',1,'p_valor','golangsintax.py',162),
  ('factor -> VARIABLE','factor',1,'p_factor','golangsintax.py',166),
  ('factor -> FLOAT','factor',1,'p_factor','golangsintax.py',167),
  ('factor -> INTEGER','factor',1,'p_factor','golangsintax.py',168),
  ('iterador -> VARIABLE INCREMENT','iterador',2,'p_iterador','golangsintax.py',173),
  ('iterador -> VARIABLE DECREMENT','iterador',2,'p_iterador','golangsintax.py',174),
]
