from dataclasses import dataclass

@dataclass
class PieCalculator:

	@staticmethod
	def calculate_pi(n_terms: int) -> float:
		numerator: float = 4.0
		denominator: float = 1.0
		operation: float = 1.0
		pi: float = 0.0

		for _ in range(n_terms):
			pi = pi + operation * (numerator / denominator)
			denominator = denominator + 2.0
			operation = operation * -1.0
		return pi

if __name__ == "__main__":
	print(PieCalculator.calculate_pi(1000000000000000000))