from textx import metamodel_from_file
from processors import p1




mm = metamodel_from_file('LION_META_MODEL.tx')

# inject the processor into the meta-model : 
p1.inject_processor(mm)


m = mm.model_from_file('instance.lion')


print(m.rules[0].file_path)