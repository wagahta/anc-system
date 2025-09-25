import numpy as np

class ANCDataLoader:
    def __init__(self, sample_rate=16000, duration=4.0):
        self.sample_rate = sample_rate
        self.duration = duration
        self.audio_length = int(sample_rate * duration)
    
    def generate_test_signals(self):
        t = np.linspace(0, self.duration, self.audio_length)
        clean_audio = 0.5 * np.sin(2 * np.pi * 300 * t)
        return clean_audio / np.max(np.abs(clean_audio))
