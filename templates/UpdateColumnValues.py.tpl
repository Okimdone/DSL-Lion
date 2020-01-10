{% if whereCode is defined %}mask = {{whereCode}} {% endif %}
{% for feature, val in assigns.items() %}
{{ lionFrame }}["{{feature}}"]{% if whereCode is defined %}[mask]{% endif %} = {{val}}   
{% endfor %}
