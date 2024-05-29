QUEUE = 1
STACK = 2


class Message:
	def __init__(self, mode: int=QUEUE):
		self.messages = []
		self.list_mode = mode

	def put(self, msg):
		self.messages.append(msg)

	def get(self):
		if self.list_mode == QUEUE:
			return self.messages.pop(0)

		elif self.list_mode == STACK:
			return self.messages.pop()

		else:
			raise TypeError("Unknown mode")

	def get_all(self):
		if self.list_mode == QUEUE:
			messages = self.messages
			self.messages = []
			return messages

		elif self.list_mode == STACK:
			messages = self.messages.reverse()
			self.messages = []
			return messages

		else:
			raise TypeError("Unknown mode")


class Signal:
	def __init__(self):
		self.signals = dict()

	def set(self, name, value):
		self.signals[name] = value

	def get(self, name):
		return self.signals.get(name)
