{% for column, mapping in zip(columns, mappings) %}
# {{lionFrame}}['{{column}}'] => {{mapping}}
{{lionFrame}}['{{column}}'] = {{lionFrame}}['{{column}}'].map({{mapping}}) {% endfor %}