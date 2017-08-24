import pyaudio

p = pyaudio.PyAudio()

# Get audio device information
for i in range(p.get_device_count()):
	dev = p.get_device_info_by_index(i)
	print((i, dev["name"], dev["maxInputChannels"]))
