#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import textx as tx

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

def genCode(mainRule):
    main_tpl = env.get_template('main.py.tpl')
    loadFrame = env.get_template('LoadLionFrame.py.tpl')

    loadrules = tx.get_children_of_type('LoadRule',mainRule)


    # Generating the load code for every LoadRule
    loadedFramesCode = []
    for loadrule in loadrules:
        file_path = loadrule.file_path
        lionFrame = loadrule.lionFrame
        columns = []
        dtypes = dict()
        for column in loadrule.columns:
            columns.append(column.v_name)
            dtypes[column.v_name] = column.type
        
        LF = loadFrame.render(lionFrame=lionFrame, file_path=file_path, columns=columns, dtype=dtypes)
        loadedFramesCode.append(LF)
            
    return loadedFramesCode


if __name__ == "__main__":
    pass
    #genCode()