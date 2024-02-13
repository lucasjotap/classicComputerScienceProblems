from typing import Dict

class Fibbonaci(object):
	"""
	Class implements many variations of writing the fibbonaci algorithm.
	"""
	memo: Dict[int, int] = {0: 0, 1: 1} 

	def fib_recursive(self, n: int) -> int:
		"""
		Fibbonaci recursive
		"""
		if n < 2: return n

		return (self.fib_recursive(n-1) + self.fib_recursive(n-2))

	def fib_iterative(self, n: int) -> int:
		"""
		Fibonnaci iterative
		"""
		if n == 0: return n

		last: int = 0
		next: int = 1

		for _ in range(1, n):
			last = next
			next = last + next 
		return next

	def fib_memoed(self, n: int) -> int:
		if n not in self.memo:
			self.memo[n] = self.fib_memoed(n-1) + self.fib_memoed(n-2)
		return self.memo[n]

if __name__ == "__main__":
	f = Fibbonaci()
	# fib_list = [f.fib_recursive(n) for n in range(0, 11)]
	# print(fib_list) 
	# print(f.fib_iterative(50)
	print(f.fib_memoed(800))