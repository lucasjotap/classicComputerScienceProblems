from secrets import token_bytes
from typing import Tuple

class RandomKeyGenerator:

	def __init__(self, length: int):
		self.token_bytes_key = self.random_key(length)

	def random_key(self, length: int) -> int:
		return int.from_bytes(token_bytes(length), "big")

if __name__ == '__main__':
	rkg = RandomKeyGenerator(10)
	rkg_key = rkg.token_bytes_key
	print(rkg_key)