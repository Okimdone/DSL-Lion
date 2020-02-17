kbest = SelectKBest({{filter}}, k={{k}}).fit({{lionframe}}.loc[:, {{lionframe}}.columns != '{{target}}'], {{lionframe}}['{{target}}'])
selected_cols = kbest.get_support(indices=True)
{{best_lionframe}} = {{lionframe}}.iloc[:,selected_cols]

kbest = None
selected_cols = None
