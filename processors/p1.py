from textx.exceptions import *


def general_obj_processor(general):

    lloads = len(general.rules)

    

    for i in range(lloads-1):
        for j in range(i+1, lloads):
            if general.rules[i].lionFrame == general.rules[j].lionFrame:
                raise TextXSemanticError('lionFrame variable name ("%s") is already used!' % general.loadrules[i].lionFrame)

    pass


def load_obj_processor(load):
    # l = len(load.columns)

    # for i in range(l-1):
    #     for j in range(i+1, l):
    #         if general.loadrules[i].lionFrame == general.loadrules[j].lionFrame:
    #             raise TextXSemanticError('lionFrame variable name ("%s") is already used!' % general.loadrules[i].lionFrame)

    pass




def inject_processor(mm):
    obj_processors = {
        'GeneralRule': general_obj_processor
        # 'LoadRule': load_obj_processor
    }

    mm.register_obj_processors(obj_processors)

    pass