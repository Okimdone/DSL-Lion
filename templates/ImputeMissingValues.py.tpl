{% for column in columns %}
imp = SimpleImputer(missing_values={{missing_value}}, strategy="{{strategy}}")
{{lionFrame}}["{{column}}"] = imr.fit({{lionFrame}}["{{column}}"]).transform({{lionFrame}}["{{column}}"]) 
{% endfor %}