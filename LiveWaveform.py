import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
SAMPLE_RATE = 44100  # Hz
DURATION = 5  # seconds
WINDOW_SIZE = 1024  # Number of samples per frame

# Initialize the plot
fig, ax = plt.subplots()
x = np.arange(0, WINDOW_SIZE) / SAMPLE_RATE
y = np.zeros(WINDOW_SIZE)
line, = ax.plot(x, y)
ax.set_xlim(0, WINDOW_SIZE / SAMPLE_RATE)
ax.set_ylim(-1, 1)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Real-Time Audio Waveform")

# Callback function to update the waveform
def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    # Update the line data
    line.set_ydata(indata[:, 0])

# Animation update function
def update(frame):
    return line,

# Start recording
stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, blocksize=WINDOW_SIZE, callback=audio_callback)
ani = FuncAnimation(fig, update, blit=True, interval=50)

with stream:
    print("Recording... Close the window to stop.")
    plt.show()
print("Recording complete!")
