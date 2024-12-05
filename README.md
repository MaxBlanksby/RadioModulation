# Radio Modulation

A Python project for audio signal modulation and demodulation, demonstrating amplitude modulation (AM) techniques for radio communication.

## Overview

This project implements amplitude modulation to encode audio signals onto carrier waves, simulating radio transmission and reception. It includes real-time audio waveform visualization and signal processing capabilities.

## Features

- **Audio Recording**: Capture audio input through your microphone
- **Signal Upsampling**: High-quality interpolation for precise modulation
- **Amplitude Modulation**: Encode audio signals onto carrier waves
- **Signal Demodulation**: Recover original audio from modulated signals
- **Waveform Visualization**: Real-time and static waveform displays
- **Data Export**: Save waveform data to text files

## Files

- `Modulate.py` - Main modulation script demonstrating the full AM process
- `ModulationFunctions.py` - Core signal processing functions (recording, upsampling, downsampling, carrier generation)
- `Client Final.py` - Complete client implementation with all modulation functions
- `LiveWaveform.py` - Real-time audio waveform visualization tool

## Requirements

- Python 3.x
- numpy
- sounddevice
- matplotlib
- scipy

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MaxBlanksby/RadioModulation.git
cd RadioModulation
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Modulation

Run the main modulation script:
```bash
python Modulate.py
```

This will:
1. Record 5 seconds of audio
2. Display the original waveform
3. Upsample the signal
4. Generate a carrier wave
5. Modulate the audio onto the carrier
6. Demodulate to recover the original signal

### Live Waveform Visualization

To view real-time audio input:
```bash
python LiveWaveform.py
```

## Configuration

Key parameters in `Modulate.py`:

- `duration` - Recording duration in seconds (default: 5)
- `audioSampleRate` - Audio sampling rate in Hz (default: 20000)
- `amUpSampleFactor` - Initial upsampling factor (default: 10)
- `simUpSampleFactor` - Simulation resolution factor (default: 10)
- `modulationIndex` - Modulation depth (default: 1)

## How It Works

1. **Recording**: Audio is captured at a specified sample rate
2. **Upsampling**: Signal is interpolated to a higher sample rate for accurate modulation
3. **Carrier Generation**: A high-frequency sine wave carrier is generated
4. **Modulation**: The audio signal modulates the amplitude of the carrier wave
5. **Transmission**: (Simulated) Modulated signal represents transmitted data
6. **Demodulation**: Original signal is recovered by dividing by the carrier and downsampling

## License

MIT License

## Author

Max Blanksby
