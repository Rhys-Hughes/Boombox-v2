import audioManager

class Sound:
    def __init__(self, name, location, keybind, volume):
        self.name = name
        self.location = location
        self.keybind = keybind
        self.volume = volume
    
    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location

    def get_keybind(self):
        return self.keybind

    #calls to the audio manager to play the desired sound
    def play(self):
        
        audioManager.play(self.location, self.volume)
    
    #adds the sound to the sounds file
    def add(self):
        pass