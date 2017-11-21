import pyaudio
import wave
from array import array
import os
import sys
from speech_recognition import transcribe_streaming

# Set device number with get_dev_index.py.
DEVICE_NUMBER = 1

class Recorder:
	def __init__(self):
		self.THRESHOLD = 500
		self.FORMAT = pyaudio.paInt16
		self.CHANNELS = 1
		self.RATE = 44100
		self.CHUNK = 8192 # int(RATE / 10)
		self.MINIMUM_RECORD_SECONDS = 3 # seconds (approximate)
		self.f = None

	def record_audio(self):
		def is_silent(data):
			# When it's silent, max(data) tend to be 100~200
			result = max(data) < self.THRESHOLD
            self.THRESHOLD = self.THRESHOLD + 0.3 * (max(data) - self.THRESHOLD)
            #print("THRESHOLD : " + str(self.THRESHOLD))
            return result
	
		p = pyaudio.PyAudio()
	
		stream = p.open(
			format=self.FORMAT,
			channels=self.CHANNELS,
			rate=self.RATE,
			input=True,
			frames_per_buffer=self.CHUNK,
			input_device_index=DEVICE_NUMBER
		)

		print("[HARU] Recording audio...")

		frames = array('h')
		minimum = 0
		silent_counter = 0
        MAX_FRAME_LENGTH = 230000
		
		while True:
			data = array('h', stream.read(self.CHUNK))

			# Record sounds while at least 3 seconds
			if minimum < int(self.RATE / self.CHUNK * self.MINIMUM_RECORD_SECONDS):
				frames.extend(data)
				minimum = minimum + 1

			# After 3 seconds
			else:
                #print("SILENT COUNTER : " + str(silent_counter))
                #print("FRAME LENGTH : " + str(len(frames)))
				silent = is_silent(data)

				# If it is noisy
				if not silent:
					frames.extend(data)
					silent_counter = 0

				# If it is silent, wait a second more
				elif silent and silent_counter < 5: # 1 second (approximate)
					frames.extend(data)
					silent_counter = silent_counter + 1

				# After a second, finish the recording
				else:
                    if len(frames) > MAX_FRAME_LENGTH: 
                        frames = frames[:MAX_FRAME_LENGTH]
					break

		print("[HARU] Recording is done")

		stream.stop_stream()
		stream.close()
		#p.terminate()

		self.f = open(".sound.raw", "w+")
		frames.tofile(self.f)
		self.f.write('\0')
		self.f.seek(0)
		return self.f
	
	def close_buf(self):
		self.f.seek(0)
		self.f.truncate()
		self.f.close()

if __name__ == "__main__":
	r = Recorder()
	f = r.record_audio()
	sen = transcribe_streaming(f)
        print(sen)
	r.close_buf()
