import requests
import json
from collections import namedtuple

REQUEST_PARAMETERS = {'api_key' : 'u70702-2831728b7a23c82f750e3f5e', 'format' : 'json'}
URL = "https://api.uptimerobot.com/v2/getMonitors"

data = requests.post(URL, data=REQUEST_PARAMETERS)

data_obj = json.loads(data.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

for monitor in data_obj.monitors:
    filename = monitor.friendly_name.lower().replace(" ", "_") + ".txt"
    file = open(filename, "w")
    if monitor.status == 8 or monitor.status == 9:
        file.write("1")
    else:
        file.write("0")

    file.close()

    


