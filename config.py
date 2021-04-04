import json

config_file = "data/config.json"

pump_rate = 0
bic_size = 0
shot_size = 0

with open(config_file) as data_file:
    data = json.load(data_file)
    pump_rate = data["pump_rate"]
    bic_size = data["bic_size"]
    shot_size = data["shot_size"]
