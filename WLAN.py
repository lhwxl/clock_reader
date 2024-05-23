import network
import time


class WLAN:
	def __init__(self):
		self.ap = network.WLAN(network.AP_IF)
		self.wifi = network.WLAN(network.STA_IF)

	def ap_active(self, active: bool) -> None:
		self.ap.active(active)

	def wifi_active(self, active: bool) -> None:
		self.wifi.active(active)


	def set_ap_config(self, essid: str=None, password: str=None, hidden: int=0) -> None:
		self.ap.config(essid=essid, password=password, hidden=hidden)

	def ap_ifconfig(self, config: tuple=None):
		if config:
			self.ap.ifconfig(config)
			return True

		else:
			return self.ap.ifconfig()


	def scan_wifi(self):
		ap_names = []

		for aps in self.wifi.scan():
			ap_names.append(aps[0])

		return ap_names

	def connect_wifi(self, ssid: str, password: str):
		self.disconnect_wifi()

		start_time = time.time()

		self.wifi.connect(ssid, password)
		while not self.wifi.isconnected():
			if self.wifi.status() == network.WLAN.STAT_CONNECTING:
				pass

			else:
				return False

			if time.time - start_time > 5:
				return False

			time.sleep_ms(100)

		return True

	def disconnect_wifi(self):
		self.wifi.disconnect()

	def wifi_status(self):
		return self.wifi.status()

	def wifi_ifconfig(self, config: tuple=None):
		if config:
			self.ap.ifconfig(config)
			return True

		else:
			return self.wifi.ifconfig()
