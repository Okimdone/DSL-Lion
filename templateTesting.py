#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

main_tpl = env.get_template('main.py.tpl')
loadFrame = env.get_template('LoadLionFrame.py.tpl')

# This must contain a dtypes as a dict of keyworld ( names of columns and their types )
dtypes={"salam":"salamd", "hi":"hid"}
LF1  =  loadFrame.render(lionFrameName='FrameName', fileName="filename.csv", columns=str(list(dtypes.keys())), dtypes=dtypes)
LF2  =  loadFrame.render(lionFrameName='FrameName2', fileName="filename2.csv", columns=str(list(dtypes.keys())), dtypes=dtypes)
print(main_tpl.render(loadFrames=[LF1, LF2]))