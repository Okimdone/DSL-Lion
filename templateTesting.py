#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import textx as tx

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
env.globals.update(zip=zip)

def cname(o):
    return o.__class__.__name__

def genCode(mainRule):
    #main_tpl = env.get_template('main.py.tpl')
    
    # Loading RULE :
    #loadFrame = env.get_template('LoadLionFrame.py.tpl')
    #LF = loadFrame.render(lionFrame="lionFrame", file_path="file_path", features=["columns", "daed"], dtype=[1,3], sep='t', only="f")
    #print(LF)

    # Saving a RULE :
    #saveFrame = env.get_template('SaveLionFrame.py.tpl')
    #SF = saveFrame.render(lionFrame='feaf', file_path='feafeaf')
    #print(SF)

    # Dropping a column from a dataframe :
    #DropColumn = env.get_template('DropColumn.py.tpl')
    #DC = DropColumn.render(lionFrame='feaf', features=repr(['feafeaf']))
    #print(DC)

    # Dropping a column from a dataframe :
    #DropNan = env.get_template('DropNaN.py.tpl')
    #DNaN = DropNan.render(lionFrame='feaf', axis=1, subset=repr(['feafeaf']), how=repr("any"), tresh=3)
    #print(DNaN)

    # Changing the type a column from a dataframe :
    #ChangeColumnType = env.get_template('ChangeColumnType.py.tpl')
    #CCType = ChangeColumnType.render(lionFrame='feaf', columnToType={'col1':'int64'})
    #print(CCType)

    # Renaming a column from a dataframe :
    #ChangeColumnName = env.get_template('ChangeColumnName.py.tpl')
    #CCName = ChangeColumnName.render(lionFrame='feaf', columnNewNames={'col1':'col66'})
    #print(CCName)

    # Updating the of columns Where a condition is verified:
    #UpdateColumnValues = env.get_template('UpdateColumnValues.py.tpl')
    #TODO Define the code for the conditions of the where and put them as a string into the whereCode variable
    #UCV = UpdateColumnValues.render(lionFrame='feaf', assigns={"col1":1, "col6":6 }, whereCode="1 >= 2")
    #print(UCV)

    # Imputing missing values in a column of a dataframe :
    #ImputedColumn = env.get_template('ImputeMissingValues.py.tpl')
    #IC = ImputedColumn.render(lionFrame='feaf', columns=['col1','col66'], missing_value="np.nan", strategy='mean/median/most_frequant')
    #print(IC)

    # Mapping a ordinal categorical Feature of a dataframe :
    #MapFeature = env.get_template('MapCategoricalFeature.py.tpl')
    #MF = MapFeature.render(lionFrame='feaf', columns=['col1','col66'], mappings=[{"A":1, "B":2}, {"C":4, "D":6}])
    #print(MF)

    # Encoding a categorical Feature of a dataframe Using one-hot encoding :
    #EncodeFeature = env.get_template('EncodeCategoricalFeature.py.tpl')
    #EF = EncodeFeature.render(lionFrame='feaf', columns=['col1','col66'])
    #print(EF)

    # Splitting the data into training set and testing set
    #PartitionFrame = env.get_template('PartitionFrame.py.tpl')
    #PF = PartitionFrame.render(lionFrame='feaf',trainFrameName='dsl_train', testFrameName='dsl_test' , columns=['col1','col66'], trainPercentage=0.7)
    #print(PF)

    # Normalizing the data into training set and testing set
    #NormalizeFeature = env.get_template('NormalizeFeatures.py.tpl')
    #NF = NormalizeFeature.render(lionFrame='feaf', columns=['col1','col66'], way='using'.lower(), scaler='SCALER_NAME')
    #print(NF)

    # Normalizing the data into training set and testing set
    #StandardizeFeature = env.get_template('StandardizeFeature.py.tpl')
    #SF = StandardizeFeature.render(lionFrame='feaf', columns=['col1','col66'], way='into'.lower(), scaler='SCALER_NAME')
    #print(SF)


    loadrules = tx.get_children_of_type('LoadRule',mainRule)


    # Generating the load code for every LoadRule
    #loadedFramesCode = []
    #for loadrule in loadrules:
    #    file_path = loadrule.file_path
    #    lionFrame = loadrule.lionFrame
    #    columns = []
    #    dtypes = dict()
    #    for column in loadrule.columns:
    #        columns.append(column.v_name)
    #        dtypes[column.v_name] = column.type
    #    
    #    LF = loadFrame.render(lionFrame=lionFrame, file_path=file_path, columns=columns, dtype=dtypes)
    #    loadedFramesCode.append(LF)
    #        
    #return loadedFramesCode


if __name__ == "__main__":
    pass
    genCode(2)