class Mood:
    def __init__(self, feeling:str, intensity:int):
        self.feeling = feeling  # Description of the mood
        self.intensity = intensity  # Intensity of the mood on a scale from 1 to 10

    def display_mood(self):
        return f'Mood: {self.feeling}, Intensity: {self.intensity}'

