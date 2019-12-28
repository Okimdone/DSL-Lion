from textx import metamodel_from_file, model, metamodel
from processors import p1
# from generator import genCode

from textx import metamodel_from_file, get_children_of_type
import pandas as pd

mm = metamodel_from_file('LION_META_MODEL.tx')

import templateTesting
x = templateTesting.genCode(m)
print(x)
# inject the processor into the meta-model : 
p1.inject_processor(mm)

m = mm.model_from_file('testModels/instance.lion')
# print(model.get_children_of_type('LoadRule', m))
# generated_file_path = getCode(m)

# print(dir(mm.rootcls._tx_attrs['rules'].cls))
# print(dir(metamodel))
# print(dir(mm.namespaces['LION_META_MODEL']))
