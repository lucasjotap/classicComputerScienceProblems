from typing import Dict, Generator
from functools import lru_cache

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

	def fib_memoized(self, n: int) -> int:
		if n not in self.memo:
			self.memo[n] = self.fib_memoed(n-1) + self.fib_memoed(n-2)
		return self.memo[n]

	@lru_cache(maxsize=None)
	def fib_memoized_advanced(self, n: int) -> int:
		if n < 2: return n 
		return (self.fib_memoized_advanced(n-1) + self.fib_memoized_advanced(n-2))


	def fib_with_generator(self, n: int) -> Generator[int, None, None]:
		yield 0
		if n > 0: yield 1 
		last, next = 0, 1 
		for _ in range(1, n):
			last = next 
			next = last + next 
			yield next

if __name__ == "__main__":
	f = Fibbonaci()
	# fib_list = [f.fib_recursive(n) for n in range(0, 11)]
	# print(fib_list) 
	# print(f.fib_iterative(50)
	# print(f.fib_memoized_advanced(800))
	# print(f.fib_memoized_advanced(100))
	fib_list = list(f.fib_with_generator(10))
	fib_list = [i for i in f.fib_with_generator(200)]
	print(fib_list)