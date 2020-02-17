#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import textx as tx

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
env.globals.update(zip=zip)

def cname(o):
    return o.__class__.__name__

def genDependenciesCode():
    return env.get_template('main.py.tpl').render()

def genCode(rule):
    code = ""
    if cname(rule) == 'Load':
        # Loading RULE :
        loadFrame = env.get_template('LoadLionFrame.py.tpl')
        code += loadFrame.render(lionFrame=rule.lionFrame.name, file_path=rule.file_path.name, features=[f.v_name for f in rule.features], dtype=[f.dtype for f in rule.features], sep=rule.sep, only=rule.only)
        
    elif cname(rule) == 'Save':
        # Saving a RULE :
        saveFrame = env.get_template('SaveLionFrame.py.tpl')
        code += saveFrame.render(lionFrame=rule.lionFrame.name, file_path=rule.file_path.name)

    elif cname(rule) == 'Drop':
        if rule.nan == False:
            # Dropping a column from a dataframe :
            DropColumn = env.get_template('DropColumn.py.tpl')
            code += DropColumn.render(lionFrame=rule.lionFrame.name, features=rule.features)
            #print(code)
        else :
            # Dropping a column from a dataframe :
            DropNan = env.get_template('DropNaN.py.tpl')
            axis, subset = (0, rule.features) if rule.axis == 'ROW' else (1,[int(f) for f in rule.features])
            code += DropNan.render(lionFrame=rule.lionFrame.name, axis=axis, subset=subset, how=rule.how.lower(), thresh=rule.thresh)
            #print(code)
    elif cname(rule) == 'Modify':
        # Changing the type a column from a dataframe :
        ChangeColumnType = env.get_template('ChangeColumnType.py.tpl')
        code += ChangeColumnType.render(lionFrame=rule.lionFrame.name, columnToType={c.v_name: c.type for c in rule.columns})

    elif cname(rule) == 'Rename':
        # Renaming a column from a dataframe :
        ChangeColumnName = env.get_template('ChangeColumnName.py.tpl')
        code += ChangeColumnName.render(lionFrame=rule.lionFrame.name, columnNewNames={c.old_feature:c.new_feature for c in rule.columnNewNames})

# Updating the of columns Where a condition is verified:
#UpdateColumnValues = env.get_template('UpdateColumnValues.py.tpl')
#TODO Define the code for the conditions of the where and put them as a string into the whereCode variable
#UCV = UpdateColumnValues.render(lionFrame='feaf', assigns={"col1":1, "col6":6 }, whereCode="1 >= 2")
#print(UCV)

    elif cname(rule) == 'Impute':
        # Imputing missing values in a column of a dataframe :
        ImputedColumn = env.get_template('ImputeMissingValues.py.tpl')
        code += ImputedColumn.render(
            lionFrame=rule.lionFrame.name, 
            columns=[assign.feature for assign in rule.assigns],
            missing_values=[assign.val for assign in rule.assigns], strategy=rule.strategy.lower())

    elif cname(rule) == 'Map':
        # Mapping a ordinal categorical Feature of a dataframe :
        MapFeature = env.get_template('MapCategoricalFeature.py.tpl')
        columns = [c.feature for c in rule.mapcolumns]
        mappinglist = [ {c.category:c.val  for c in mc.categories} for mc in rule.mapcolumns]
        code += MapFeature.render(lionFrame=rule.lionFrame.name, columns=columns, mappings=mappinglist )

    elif cname(rule) == 'Encode':
        # Encoding a categorical Feature of a dataframe Using one-hot encoding :
        EncodeFeature = env.get_template('EncodeCategoricalFeature.py.tpl')
        code += EncodeFeature.render(lionFrame=rule.lionFrame.name, columns=rule.features)

    elif cname(rule) == 'Partition':
        # Splitting the data into training set and testing set
        PartitionFrame = env.get_template('PartitionFrame.py.tpl')
        train_percentage =  rule.train_size if rule.train_size else rule.train_size
        code += PartitionFrame.render(lionFrame=rule.lionFrame.name, trainFrameName=rule.lf_train, testFrameName=rule.lf_test, trainPercentage=train_percentage)

    elif cname(rule) == 'Normalize':
        # Normalizing the data into training set and testing set
        NormalizeFeature = env.get_template('NormalizeFeatures.py.tpl')
        code += NormalizeFeature.render(lionFrame=rule.lionFrame.name, columns=rule.features, way=rule.way.lower(), scaler=rule.scaler)

    elif cname(rule) == 'Standardize':
        # Normalizing the data into training set and testing set
        StandardizeFeature = env.get_template('StandardizeFeature.py.tpl')
        code += StandardizeFeature.render(lionFrame=rule.lionFrame.name, columns=rule.features, way=rule.way.lower(), scaler=rule.scaler)
    elif cname(rule) == 'Select':
        # Select the best features subset from the lionframe
        SelectFeatures = env.get_template('SelectFeatures.py.tpl')
        code += SelectFeatures.render(lionframe=rule.oldlionFrame.name, best_lionframe=rule.lionFrame.name, filter=rule.filter.lower(), k=rule.k, target=rule.target)
    elif cname(rule) ==  'Print':
        return f"\nprint({rule.lionFrame.name})\n"

    return code


if __name__ == "__main__":
    mm = tx.metamodel_from_file('LION_META_MODEL.tx')
    m = mm.model_from_file('testModels/instance2.lion')
    print(genCode(m))