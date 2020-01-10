{% if way == 'into' %}
{{scaler}} = StandardScaler()
{{lionFrame}}[{{columns}}] = {{scaler}}.fit_transform({{lionFrame}}[{{columns}}] )
{% elif way == 'using'%}
{{lionFrame}}[{{columns}}] = {{scaler}}.transform({{lionFrame}}[{{columns}}] )
{% endif %}
