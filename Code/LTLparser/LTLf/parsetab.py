
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDWANDORWORIMPLIESDIMPLIESUNTILUUNTILLUNTILrightNEXTUNEXTLNEXTEVENTUALLYUEVENTUALLYLEVENTUALLYGLOBALLYUGLOBALLYLGLOBALLYrightNOTWNOTnonassocLPARRPARAND DIMPLIES EVENTUALLY FALSE GLOBALLY IMPLIES LEVENTUALLY LGLOBALLY LNEXT LPAR LUNTIL NEXT NOT OR RPAR TERM TRUE UEVENTUALLY UGLOBALLY UNEXT UNTIL UUNTIL WAND WNOT WOR\n        formula : formula AND formula\n                | formula WAND formula\n                | formula OR formula\n                | formula WOR formula\n                | formula IMPLIES formula\n                | formula DIMPLIES formula\n                | formula UNTIL formula\n                | formula LUNTIL formula\n                | formula UUNTIL formula\n                | NEXT formula\n                | LNEXT formula\n                | UNEXT formula\n                | EVENTUALLY formula\n                | LEVENTUALLY formula\n                | UEVENTUALLY formula\n                | GLOBALLY formula\n                | LGLOBALLY formula\n                | UGLOBALLY formula\n                | NOT formula\n                | WNOT formula\n                | TRUE\n                | FALSE\n                | TERM \n        \n        formula : LPAR formula RPAR\n        '
    
_lr_action_items = {'NEXT':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'LNEXT':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'UNEXT':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'EVENTUALLY':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'LEVENTUALLY':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'UEVENTUALLY':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'GLOBALLY':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'LGLOBALLY':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'UGLOBALLY':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'NOT':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'WNOT':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'TRUE':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'FALSE':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'TERM':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'LPAR':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'$end':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,],[0,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'AND':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[17,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,17,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'WAND':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[18,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,18,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'OR':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[19,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,19,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'WOR':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[20,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,20,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'IMPLIES':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[21,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,21,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'DIMPLIES':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[22,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,22,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'UNTIL':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[23,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,23,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'LUNTIL':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[24,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,24,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'UUNTIL':([1,13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[25,-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,25,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),'RPAR':([13,14,15,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-21,-22,-23,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,47,-1,-2,-3,-4,-5,-6,-7,-8,-9,-24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'formula':([0,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,],[1,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> formula","S'",1,None,None,None),
  ('formula -> formula AND formula','formula',3,'p_formula','Parser.py',46),
  ('formula -> formula WAND formula','formula',3,'p_formula','Parser.py',47),
  ('formula -> formula OR formula','formula',3,'p_formula','Parser.py',48),
  ('formula -> formula WOR formula','formula',3,'p_formula','Parser.py',49),
  ('formula -> formula IMPLIES formula','formula',3,'p_formula','Parser.py',50),
  ('formula -> formula DIMPLIES formula','formula',3,'p_formula','Parser.py',51),
  ('formula -> formula UNTIL formula','formula',3,'p_formula','Parser.py',52),
  ('formula -> formula LUNTIL formula','formula',3,'p_formula','Parser.py',53),
  ('formula -> formula UUNTIL formula','formula',3,'p_formula','Parser.py',54),
  ('formula -> NEXT formula','formula',2,'p_formula','Parser.py',55),
  ('formula -> LNEXT formula','formula',2,'p_formula','Parser.py',56),
  ('formula -> UNEXT formula','formula',2,'p_formula','Parser.py',57),
  ('formula -> EVENTUALLY formula','formula',2,'p_formula','Parser.py',58),
  ('formula -> LEVENTUALLY formula','formula',2,'p_formula','Parser.py',59),
  ('formula -> UEVENTUALLY formula','formula',2,'p_formula','Parser.py',60),
  ('formula -> GLOBALLY formula','formula',2,'p_formula','Parser.py',61),
  ('formula -> LGLOBALLY formula','formula',2,'p_formula','Parser.py',62),
  ('formula -> UGLOBALLY formula','formula',2,'p_formula','Parser.py',63),
  ('formula -> NOT formula','formula',2,'p_formula','Parser.py',64),
  ('formula -> WNOT formula','formula',2,'p_formula','Parser.py',65),
  ('formula -> TRUE','formula',1,'p_formula','Parser.py',66),
  ('formula -> FALSE','formula',1,'p_formula','Parser.py',67),
  ('formula -> TERM','formula',1,'p_formula','Parser.py',68),
  ('formula -> LPAR formula RPAR','formula',3,'p_expr_group','Parser.py',89),
]
