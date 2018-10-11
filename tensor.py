import numpy as np
from prettytable import PrettyTable
from .tools.tools import  float2front


#Tensor Class
class tensor(object):

	def __init__(self, data = None, shape = None):

		if shape == None:
			shape = data.shape

		self.data = np.array(data)
		self.shape = tuple(shape)
		self.dtype = data.dtype
		self.size = prod(self.shape)
		self.ndims = len(self.shape)
		self.information = self.information()
		self.order = list(range(self.ndims))

	def dimsize(self, index):
		return self.shape[index]

    # Print Tensor Information Via Table
	def information(self):
		print('\tTensor\tInformation')
		table = PrettyTable(['Order', 'Shape', 'Size'])
		table.add_row([self.ndims(), self.shape, self.size()])
		table.reversesort = False
		table.border = 1
		print(table)

	def copy(self):
		return tensor(self.data.copy(),self.shape)

	# Tensor Model-n Unfold
	def unfold(self, mode):
		order = float2front(self.order,mode)
		tensor_unfold = np.transpose(self.data, order).reshape(self.shape[mode], np.prod(self.shape) / self.shape[mode])
		return tensor_unfold

	def fold(self,mode):
		return None

	def full(self,state):
		self.data.fill(state)
		return self

	# Math
	def __add__(self, other):
		return tensor(self.data + other.data)
	def __sub__(self, other):
		return tensor(self.data - other.data)
