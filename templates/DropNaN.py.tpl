{{ lionFrame }}.dropna(axis={{ axis | default(0, true)}} {% if subset != [] %}, subset={{ subset }}{% endif %} {% if how != '' %}, how='{{ how }}' {% elif thresh > 0 %}, thresh={{ thresh }} {% endif %}, inplace=True) 

