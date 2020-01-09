{% if only is defined %}
{{ lionFrame }} = pd.read_csv('{{file_path}}', usecols={{ features }}, dtype={{ dtype }}{% if sep is defined %}, sep='{{sep}}'{% endif %})
{% else %}
{{ lionFrame }} = pd.read_csv('{{file_path}}'{% if sep is defined %}, sep='{{sep}}'{% endif %})
features = {{ features }}
dtype = {{dtype}}
for feature, type in zip(features, dtype):
    {{ lionFrame }}[feature] = {{ lionFrame }}[feature].astype(type)
{% endif %}