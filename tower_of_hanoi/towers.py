from stack import Stack

class Tower(Stack):

	def __init__(self, num_discs: int):
		self.num_discs: int = num_discs
		self.tower_a: Stack[int] = Stack()
		self.tower_b: Stack[int] = Stack()
		self.tower_c: Stack[int] = Stack()

		for i in range(1, self.num_discs + 1):
			self.tower_a.push(i)

