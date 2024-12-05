import numpy as np
from ModulationFunctions import Record, showWaveform, upsample, writeTextfile, generateCarrier, downSample


duration = 5 #seconds
audioSampleRate = 20000 #20000 is common
amUpSampleFactor = 10 # first upsample
amCarrierFreq = audioSampleRate*amUpSampleFactor # is the freq that the data is modulated on
simUpSampleFactor = 10 # is the digital simulation resolution
modulationIndex = 1
simSampleFreq = amCarrierFreq*simUpSampleFactor # the frequency of the digital sample frequency
totalUpSample = amUpSampleFactor*simUpSampleFactor





initialWaveData = Record(duration=5,samplerate=audioSampleRate,) # gather auio data
showWaveform(initialWaveData)#show the data

writeTextfile(initialWaveData) # write to a text file

upSampledData = upsample(initialWaveData,totalUpSample) # upsample data

showWaveform(upSampledData) # show the upsampled data


numSamples = upSampledData.size


carrierSamples = generateCarrier(amCarrierFreq, numSamples)

showWaveform(carrierSamples)

modulatedSamples = np.zeros(numSamples)


for i in range (numSamples):
    modulatedSamples[i] = (1 + modulationIndex*upSampledData[i])*carrierSamples[i]
showWaveform(modulatedSamples)


# this is where we would send the data


receivedUpSample = modulatedSamples / carrierSamples
finalMessage = downSample(receivedUpSample, totalUpSample)



