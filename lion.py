#!ENV/bin/python

from textx import metamodel_from_file, get_children_of_type
import pandas as pd

mm = metamodel_from_file('LION_META_MODEL.tx')
m = mm.model_from_file('instance.lion')

import templateTesting
x = templateTesting.genCode(m)
print(x)