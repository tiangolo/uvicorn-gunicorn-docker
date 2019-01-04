import json

# Gunicorn config variables
loglevel = "warning"
workers = 3
bind = "0.0.0.0:8000"
errorlog = "-"

# For debugging and testing
log_data = {"loglevel": loglevel, "workers": workers, "bind": bind}
print(json.dumps(log_data))
