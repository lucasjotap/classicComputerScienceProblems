from stack import Stack
from typing import NoReturn
class Hanoi:
	
	def hanoi(		
				self, \
				begin: Stack[int], \
		   		end: Stack[int], \
		   		temp: Stack[int], \
				n: int
			) -> NoReturn:

		if (n == 1):
			end.push(begin.pop())
		else:
			self.hanoi(begin, temp, end, n-1)
			self.hanoi(begin, end, temp, 1)
			self.hanoi(temp, end, begin, n-1)