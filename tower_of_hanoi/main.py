from hanoi import Hanoi
from towers import Tower

if __name__ == "__main__":
	t = Tower(num_discs=4)
	h = Hanoi()

	h.hanoi(t.tower_a, t.tower_c, t.tower_b, t.num_discs)
	print(t.tower_a)
	print(t.tower_b)
	print(t.tower_c)