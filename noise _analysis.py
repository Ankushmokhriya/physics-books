import librosa
import numpy as np
import matplotlib.pyplot as plt

file = "babylon.mp3"   # change to your file name

# Load audio: sr=None keeps the original sample rate, mono=True merges channels into one
y, sr = librosa.load(file, sr=None, mono=True)

# Time axis = sample number / sample rate
time = np.arange(len(y)) / sr

plt.plot(time, y)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (relative pressure)")
plt.title("Audio waveform")
plt.show()