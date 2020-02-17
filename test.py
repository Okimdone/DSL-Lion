import textx as tx   
from textx.model import get_children


mm = tx.metamodel_from_file('LION_META_MODEL.tx')
m = mm.model_from_str('FROM "data.csv" LOAD AS ds;')
print(mm)
print(m.rules)
