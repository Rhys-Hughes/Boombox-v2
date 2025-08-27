import json, ast

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

            print(theme["title_font"])

            return themes[i]
        


def get_dimensions():
    settings = get_settings()

    return settings["dimensions"]

def get_version():
    with open(properties_path+"version.txt", "r") as version_file:
        return version_file.read()