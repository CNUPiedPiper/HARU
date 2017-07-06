import snowboydecoder
import sys
import signal
import os.path
import wiringpi

class hotword:
    def __init__(self):
        self.PUSH_BUTTON = 14
        self.interrupted = False
        self.model = ''.join([os.path.dirname(__file__), '/HARU.pmdl'])
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.PUSH_BUTTON, wiringpi.GPIO.INPUT)
        wiringpi.pullUpDnControl(self.PUSH_BUTTON, wiringpi.GPIO.PUD_UP)

    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return wiringpi.digitalRead(self.PUSH_BUTTON) == 0

    def start_detection(self, callback_func):
        signal.signal(signal.SIGINT, self.signal_handler)
        self.detector = snowboydecoder.HotwordDetector(self.model, sensitivity=0.5)
        self.detector.start(detected_callback=callback_func, interrupt_check=self.interrupt_callback, sleep_time=0.5)

    def terminate_detection(self):
        self.detector.terminate()
