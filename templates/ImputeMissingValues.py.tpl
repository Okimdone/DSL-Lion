{% for column, missing_value in zip(columns,missing_values) %}
imp = SimpleImputer(missing_values={% if missing_value.lower() == 'nan'%}np.nan{%else%}{{missing_value}}{% endif %}, strategy="{{strategy}}")
{{lionFrame}}["{{column}}"] = imr.fit({{lionFrame}}["{{column}}"]).transform({{lionFrame}}["{{column}}"]) 
{% endfor %}
