{% if way == 'into' %}
{{scaler}} = MinMaxScaler()
{{scaler}}.fit({{lionFrame}}[{{columns}}] )
{{lionFrame}}[{{columns}}] = {{scaler}}.transform({{lionFrame}}[{{columns}}] )
{% elif way == 'using'%}
{{lionFrame}}[{{columns}}] = {{scaler}}.transform({{lionFrame}}[{{columns}}] )
{% endif %}_
