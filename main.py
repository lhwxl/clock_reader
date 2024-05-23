import ssd1306py as screen
from machine import Pin, I2C


def init_screen():  #13,14引脚
	pass


def main():
	pass


if __name__ == "__main__":
	run_value = Pin(4, Pin.IN, Pin.PULL_UP)
	if run_value.value():
		_ = Pin(4, Pin.OUT)
		_.off()
		del _
		del run_value

		main()
