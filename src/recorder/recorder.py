import pyaudio
import wave
from array import array
from speech_recognition.transcribe_streaming import transcribe_streaming

class Recorder:
	def __init__(self):
		self.THRESHOLD = 500
		self.FORMAT = pyaudio.paInt16
		self.CHANNELS = 1
		self.RATE = 44100
		self.CHUNK = 8192#int(RATE / 10)
		self.MINIMUM_RECORD_SECONDS = 3 #seconds (approximate)
		self.f = None

	def record_audio(self):
		def is_silent(data):
			#wheh it's silent, max(data) tend to be 100~200
			return max(data) < self.THRESHOLD
	
		p = pyaudio.PyAudio()
	
		stream = p.open(format=self.FORMAT,
   	             channels=self.CHANNELS,
   	             rate=self.RATE,
   	             input=True,
   	             frames_per_buffer=self.CHUNK,
					input_device_index=2)

		print "* Recording audio..."

		frames = array('h')
		minimum = 0
		silent_counter = 0
		while True:
			data = array('h', stream.read(self.CHUNK))
			#record sounds while at least 3 seconds
			if minimum < int(self.RATE / self.CHUNK * self.MINIMUM_RECORD_SECONDS):
				frames.extend(data)
				minimum = minimum + 1
			#after 3 seconds
			else:
				silent = is_silent(data)
				#if it is noisy
				if not silent:
					frames.extend(data)
					silent_counter = 0;
				#if it is silent, wait a second more
				elif silent and silent_counter < 5: #1 second (approximate)
					frames.extend(data)
					silent_counter = silent_counter + 1
				#after a second, finish the recording
				else:
					break

		print "* done\n" 

		stream.stop_stream()
		stream.close()
		p.terminate()

		self.f = open("sound.raw", "w+")
		frames.tofile(f)
		self.f.write('\0')
		self.f.seek(0)
		return self.f
	
	def close_buf(self):
		self.f.seek(0)
		self.f.turncate()
		self.f.close()

if __name__ == "__main__":
	r = Recorder()
	f = r.record_audio()
	transcribe_streaming(f)
	r.close_buf()
