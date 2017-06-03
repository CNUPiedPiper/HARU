import snowboydecoder
import sys
import signal
import os.path

class hotword:
    def __init__(self):
        self.interrupted = False
        self.model = ''.join([os.path.dirname(__file__), '/HARU.pmdl'])

    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    def start_detection(self, callback_func):
        signal.signal(signal.SIGINT, self.signal_handler)
        self.detector = snowboydecoder.HotwordDetector(self.model, sensitivity=0.5)
        self.detector.start(detected_callback=callback_func, interrupt_check=self.interrupt_callback, sleep_time=1)

    def terminate_detection(self):
        self.detector.terminate()
