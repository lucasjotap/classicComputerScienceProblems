from typing import TypeVar, Generic, List, NoReturn
T = TypeVar('T')

class Stack(Generic[T]):

	def __init__(self) -> None:
		self._container: List[T] = []

	def push(self, item: T) -> None:
		self._container.append(item)

	def pop(self) -> T:
		return self._container.pop()

	def __repr__(self) -> str:
		return repr(self._container)
