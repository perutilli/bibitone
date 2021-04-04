from kivy.config import Config
import json

config_file = "data/config.json"

pump_rate = 0
bic_size = 0
shot_size = 0
resolution = (0, 0)

with open(config_file) as data_file:
    data = json.load(data_file)
    pump_rate = data["pump_rate"]
    bic_size = data["bic_size"]
    shot_size = data["shot_size"]
    resolution = (data["resolution"][0], data["resolution"][1])


# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'fullscreen', 'fake')

# fix the width of the window
Config.set('graphics', 'width', resolution[0])

# fix the height of the window
Config.set('graphics', 'height', resolution[1])
