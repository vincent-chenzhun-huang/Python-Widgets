import numpy as np
import wave
import struct
import matplotlib.pyplot as plt



frequency = 1000
noisy_freq = 50
num_samples = 48000

sampling_rate = 48000.0

sine_wave = [np.sin(2 * np.pi * frequency * x1 / sampling_rate) for x1 in range(num_samples)]
sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/ sampling_rate) for x1 in range(num_samples)]

sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)

# Add them to create a noisy signal

combined_signal = sine_wave + sine_noise



#get the fft of the data
data_fft = np.fft.fft(combined_signal)
freq = (np.abs(data_fft[:len(data_fft)]))


index = 0
filtered_freq = []
for f in freq:
    
    if index > 950 and index < 1050:
        
        if f>1:
            filtered_freq.append(f)
            
            
        else:
            filtered_freq.append(0)
    else:
        filtered_freq.append(0)
    index +=1


recovered_signal = np.fft.ifft(filtered_freq)

plt.subplot(3,3,1)
plt.title("Original sine wave")
plt.subplots_adjust(hspace = 1.0)
plt.plot(sine_wave[:500])
plt.subplot(3,1,2)
plt.title("Noisy wave")
plt.plot(combined_signal[:4000])
plt.subplot(3,1,3)
plt.title("Sine wave after clean up")
plt.plot((recovered_signal[:500]))
plt.show()