class CompressedGene(object):
	"""
	Class works with data compression for string.
	"""
	def __init__(self, gene: str):
		self._compress(gene)

	def _compress(self, gene: str) -> None:
		"""
		Method compresses the data in the incoming string.
		"""
		self.bit_string: int = 1 # sentinel
		for nucleotide in gene.upper():
			self.bit_string <<= 2
			try:
				match nucleotide:
					case "A":
						self.bit_string |= 0b00
					case"C": # change last two bits to 01
						self.bit_string |= 0b01
					case "G": # change last two bits to 10
						self.bit_string |= 0b10
					case "T": # change last two bits to 11
						self.bit_string |= 0b11
			except nucleotide not in ['A', 'B', 'C', 'D']:			
				raise ValueError("Invalid Nucleotide:{}".format(nucleotide))


	def decompress(self) -> str:
		"""
		Method decompresses the data in the incoming string.
		"""
		gene: str = ""
		for i in range(0, self.bit_string.bit_length() -1, 2): # -1 to exclude sentinel
			bits: int = self.bit_string >> i & 0b11
			if bits == 0b00:
				gene += "A"
			elif bits == 0b01:
				gene += "C"
			elif bits == 0b10:
				gene += "G"
			elif bits == 0b11:
				gene += "T"
			else:
				raise ValueError("Invalid bits: {}".format(bits))
		return gene[::-1]

	def __str__(self) -> str:
		return self.decompress()

if __name__ == "__main__":
	from sys import getsizeof
	original: str ="TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
	print("original is {} bytes".format(getsizeof(original)))
	compressed: CompressedGene = CompressedGene(original)
	print("compressed is {}".format(getsizeof(compressed.bit_string)))
	print(compressed)
	print("original and decompressed are the same: {}".format(original ==
	compressed.decompress()))

