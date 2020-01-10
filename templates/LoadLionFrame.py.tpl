{% if only == True %}
{{ lionFrame }} = pd.read_csv('{{file_path}}', usecols={{ features }}, dtype={{ dtype }}{% if sep != '' %}, sep='{{sep}}'{% endif %})
{% else %}
{{ lionFrame }} = pd.read_csv('{{file_path}}'{% if sep != '' %}, sep='{{sep}}'{% endif %})
features = {{ features }}
dtype = {{dtype}}
for feature, type in zip(features, dtype):
    {{ lionFrame }}[feature] = {{ lionFrame }}[feature].astype(type)
{% endif %}
