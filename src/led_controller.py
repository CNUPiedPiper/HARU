from neopixel import *
import time

LED_COUNT   = 32
LED_PIN     = 18
LED_FREQ_HZ = 800000
LED_DMA     = 5
LED_INVERT  = False

class Led_controller:
    def __init__(self):
        self.strip = Adafruit_NeoPixel(
                LED_COUNT,
                LED_PIN,
                LED_FREQ_HZ,
                LED_DMA,
                LED_INVERT
        )
        self.strip.begin()

    def start(self):
        self.turn_on()
        self.turn_off()

    def turn_on(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(128, 0, 128))
            self.strip.show()
            time.sleep(0.01)

    def turn_off(self):
        time.sleep(2)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
            self.strip.show()
            time.sleep(0.01)

if __name__ == "__main__":
    led = Led_controller()
    led.turn_on()
    led.turn_off()
