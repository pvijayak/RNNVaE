class EarlyStopping():

	def __init__(self, history = 5):
		super().__init__()

		self.history = history
		self.counter = 0
		self.best_val_loss = None

	def check(self, val_loss):
		result = False

		if(self.best_val_loss is None):
			self.best_val_loss = val_loss
		elif(val_loss > self.best_val_loss):
			self.counter += 1
			print("Early stopping: Counter = {}/{}, cur_val_loss = {}, best_val_loss = {}".format(self.counter, self.history, val_loss, self.best_val_loss))
		else:
			self.counter = 0
			self.best_val_loss = val_loss
		if(self.counter == self.history):
			self.counter = 0
			result = True

		return result