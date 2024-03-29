from secrets import token_bytes
from typing import Tuple

class RandomKeyGenerator:

	def __init__(self, length: int):
		self.token_bytes_key = self.random_key(length)

	def random_key(self, length: int) -> int:
		return int.from_bytes(token_bytes(length), "big")	

	def encrypt(self, original: str) -> Tuple[int, int]:
		original_bytes: bytes = original.encode()
		dummy: int = self.random_key(len(original_bytes))
		original_key: int = int.from_bytes(original_bytes, "big")
		encrypted: int = original_key ^ dummy #XOR
		return dummy, encrypted

	def decrypt(self, key1: int, key2: int) -> str:
		decrypted: int = key1 ^ key2 # XOR
		temp: bytes = decrypted.to_bytes((decrypted.bit_length()+ 7) // 8, "big")
		return temp.decode()

if __name__ == '__main__':
	rkg = RandomKeyGenerator(10)
	key1, key2 = rkg.encrypt("One Time Pad!")
	result: str = rkg.decrypt(key1, key2)
	print(result)
