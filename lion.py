#!ENV/bin/python

from textx import metamodel_from_file
import pandas as pd

mm = metamodel_from_file('LION_META_MODEL.tx')
m = mm.model_from_file('instance.lion')

