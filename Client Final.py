from random import sample
from typing import final

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import math


waveformData = []
duration = 5 #seconds
audioSampleRate = 20000 #20000 is common
amUpSampleFactor = 10 # first upsample
amCarrierFreq = audioSampleRate*amUpSampleFactor # is the freq that the data is modulated on
simUpSampleFactor = 10 # is the digital simulation resolution
modulationIndex = 1
simSampleFreq = amCarrierFreq*simUpSampleFactor # the frequency of the digital sample frequency
totalUpSample = amUpSampleFactor*simUpSampleFactor



def Record(duration=duration, samplerate=audioSampleRate):
    """
    Records audio for a specified duration and stores the waveform data.
    Args:
        duration (int): The duration of the recording in seconds.
        samplerate (int): The sampling rate for the recording.
    """
    global waveformData
    print("Recording...")
    waveformData = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float64')
    sd.wait()  # Wait for the recording to finish
    print("Recording finished!")

def upscaleData(data, factor):
    """
    Upscales the waveform data by repeating the data points.
    Args:
        data (list or np.ndarray): The original waveform data.
        factor (int): The factor by which to upscale the data.
    Returns:
        np.ndarray: The upscaled waveform data.
    """
    return np.repeat(data, factor, axis=0)

def upsample(data, factor):
    """
    Upsamples the waveform data using linear interpolation.
    Args:
        data (list or np.ndarray): The original waveform data.
        factor (int): The factor by which to upsample the data.
    Returns:
        np.ndarray: The upsampled waveform data.
    """
    original_indices = np.arange(len(data))
    upsampled_indices = np.linspace(0, len(data) - 1, len(data) * factor)

    # Create a linear interpolator
    interpolator = interp1d(original_indices, data.flatten(), kind='linear')

    # Interpolate to create upsampled data
    upsampled_data = interpolator(upsampled_indices)
    return upsampled_data.reshape(-1, 1)  # Reshape to match original data shape


def writeTextfile(data, filename="waveform.txt"):
    """
    Writes the waveform data to a text file.
    Args:
        filename (str): The name of the text file to write.
    """
    if len(data) == 0:
        print("No waveform data to write!")
        return
    np.savetxt(filename, data, fmt='%.6f')
    print(f"Waveform data written to {filename}")

def showWaveform(data, samplerate):
    """
    Displays the waveform data as a graph.
    Args:
        data (list or np.ndarray): The waveform data to display.
        samplerate (int): The sampling rate of the audio data.
    """
    if len(data) == 0:
        print("No waveform data to display!")
        return

    # Calculate time points based on the sampling rate
    time = np.linspace(0, len(data) / samplerate, num=len(data))
    sampleIndex = np.arange(0,len(data),1)

    plt.figure(figsize=(10, 5))
    #plt.plot(time, data, color='blue')
    plt.plot(sampleIndex, data, color='blue')
    plt.title("Waveform")
    #plt.xlabel("Time (s)")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()


def playWaveform(data, samplerate=audioSampleRate):
    """
    Plays the waveform data as audio.
    Args:
        data (list or np.ndarray): The waveform data to play.
        samplerate (int): The sampling rate of the audio data.
    """
    if len(data) == 0:
        print("No waveform data to play!")
        return

    # Ensure the data is in the correct format for playback
    data = np.array(data, dtype='float64')

    print("Playing audio...")
    sd.play(data, samplerate=samplerate)
    sd.wait()  # Wait for the playback to finish
    print("Playback finished!")

def generateCarrier(freq, sampleSize):
    y = np.zeros(sampleSize)
    angfreq = 2*math.pi*freq
    for i in range(sampleSize):
        y[i] = math.cos(angfreq*i/sampleSize)
    return y


def downSample(data, factor):
    """
    Downsamples the waveform data by selecting every nth sample.
    Args:
        data (list or np.ndarray): The waveform data to downsample.
        factor (int): The factor by which to downsample the data.
    Returns:
        np.ndarray: The downsampled waveform data.
    """
    if factor <= 0:
        raise ValueError("Downsampling factor must be greater than 0.")
    if len(data) == 0:
        print("No data to downsample!")
        return data

    # Select every nth sample based on the factor
    downsampled_data = data[::factor]
    return downsampled_data


Record(duration=5)  # Record audio for 5 seconds
initialWaveData = waveformData # get the data from the recording
showWaveform(waveformData,audioSampleRate)# prints the original waveform data in a graph

upSampledData = upsample(waveformData, factor= totalUpSample)# take more peices of the same data changing the density by a factor we provide see picture

writeTextfile(waveformData)
#showWaveform(upSampledData)


#playWaveform(waveformData)
#playWaveform(upSampledData)



numSamples = upSampledData.size

carrierSamples = generateCarrier(amCarrierFreq,numSamples)

showWaveform(carrierSamples,totalUpSample)

modulatedSamples = np.zeros(numSamples)

for i in range (numSamples):
    modulatedSamples[i] = (1 + modulationIndex*upSampledData[i])*carrierSamples[i]
showWaveform(modulatedSamples,totalUpSample)


#now we need to send modulated data

# this would be reciver side
receivedUpSample = modulatedSamples / carrierSamples
finalMessage = downSample(receivedUpSample,totalUpSample)
#playWaveform(finalMessage)






