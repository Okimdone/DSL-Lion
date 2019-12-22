from textx.exceptions import *
from textx import model


def lionframe_unique_declaration(loads, err):
    lloads = len(loads)

    for i in range(lloads-1):
        for j in range(i+1, lloads):
            if loads[i].lionFrame == loads[j].lionFrame:
                raise TextXSemanticError(err % loads[i].lionFrame)
    

def column_unique_declaration(cols, err):
    lcols = len(cols)

    for i in range(lcols-1):
        for j in range(i+1, lcols):
            if cols[i].v_name == cols[j].v_name:
                raise TextXSemanticError(err % cols[i].v_name)



# OBJ PROCESSORS : 

def main_obj_processor(main_rule):
    loads = model.get_children_of_type('LoadRule', main_rule) 
    lionframe_unique_declaration(loads,'lionFrame variable name ("%s") is already used!')    
    

def load_obj_processor(load):
    column_unique_declaration(load.columns,'column name ("%s") is already used in ("{}")'.format(load.lionFrame)) 
    
# def column_obj_processor(column):
#     if column._tx_attrs['type'].cls.__name__ != "Dtype":
#         raise TextXSemanticError("data type {} doesn't exist!".format(column.type))
    


def inject_processor(mm):
    obj_processors = {
        'MainRule': main_obj_processor,
        'LoadRule': load_obj_processor
        # 'ColumnRule':column_obj_processor
    }

    mm.register_obj_processors(obj_processors)
