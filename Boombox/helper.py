import json, ast, sounds as SD

whole_path = "Boombox\\"
dependencies_path = whole_path + "dependencies\\"
data_path = dependencies_path + "data\\"
images_path = dependencies_path + "images\\"
default_sounds_path = dependencies_path + "default_sounds\\"
properties_path = dependencies_path + "properties\\"

#parses the settings json
def get_settings():
    with open(properties_path + "settings.json", "r") as settings_file:
        settings = json.load(settings_file)

    return settings

#parses the theme json
def get_theme():
    settings = get_settings()

    chosen_theme = settings["theme"]

    with open(properties_path + "themes.json", "r") as themes_file:
        themes = json.load(themes_file)

    for i, theme in enumerate(themes):

        if theme["name"] == chosen_theme:
            
            #file path formatting for robustness
            theme_logo_temp = theme["logo"]
            theme["logo"] = images_path + theme_logo_temp

            #these are tuples, but json doesn't recognise them, this converts them appropriately
            standard_font = theme["standard_font"]
            theme["standard_font"] = ast.literal_eval(standard_font)

            version_font = theme["version_font"]
            theme["version_font"] = ast.literal_eval(version_font)

            title_font = theme["title_font"]
            theme["title_font"] = ast.literal_eval(title_font)

            return themes[i]

#retrieves the dimensions of the main screen
def get_dimensions():
    settings = get_settings()

    return settings["dimensions"]

#gets the version of boombox
def get_version():
    with open(properties_path + "version.txt", "r") as version_file:
        return version_file.read()

#generates a soundlist
def get_sound_list():
    with open(data_path + "sounds.json", "r") as sounds_file:
        sounds = json.load(sounds_file)
    
    sound_list = []

    for i, sound in enumerate(sounds):
        name = sounds[i]["name"]
        location = sounds[i]["location"]
        keybind = sounds[i]["keybind"]

        new_sound = SD.Sound(name, location, keybind)

        sound_list.append(new_sound)
    
    return sound_list

#turns the keybind code into a human-readable format
def get_keybind_string(keybind):
    #creating keybind string
    keybind_string =""
    for i, key in enumerate(keybind):

        if i == len(keybind) - 1:
            keybind_string = keybind_string + key
        else:
            keybind_string = keybind_string +  key + " + "
    
    return keybind_string

#used to format the volume sliders
def get_volume_slider_length():
    dimensions = get_dimensions()

    dimensions_array = dimensions.split("x")

    x = dimensions_array[0]

    #sets to 80% width
    return int(x) * 0.8

#returns y widths
def get_y_height():
    dimensions = get_dimensions()

    dimensions_array = dimensions.split("x")

    y = dimensions_array[1]

    #sets to 80% width
    return int(y)

#returns x widths
def get_x_width():

    dimensions = get_dimensions()

    dimensions_array = dimensions.split("x")

    x = dimensions_array[0]

    #sets to 80% width
    return int(x)

def get_IO_defaults():
    with open(data_path + "defaults.json", "r") as defaults_file:
        defaults = json.load(defaults_file)
    
    input_device = defaults["input"]
    output_device = defaults["output"]
    sample_rate = defaults["sample_rate"]
    host_api = defaults["host_api"]

    return input_device, output_device, sample_rate, host_api

def write_IO_defaults(data):
    with open(data_path + "defaults.json", "w") as defaults_file:
        json.dump(data, defaults_file)
