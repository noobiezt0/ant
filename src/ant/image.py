from os import PathLike
import sys
from typing import Optional

class AntImage:
	def __init__(self: AntImage, size: tuple[int, int], data: Optional[bytes]) -> None:
		self._width, self._height = size
		self._length: int = self._width * self._height
		self._data: bytearray = bytearray(self._length)
		if data is not None:
			self._data = bytearray(data)
			if len(self._data) != self._length:
				message = "{} bytes expected, {} found".format(self._length, len(self._data))
				raise IndexError(message)

	@classmethod
	def open(cls: type[AntImage], fp: str | PathLike[str]) -> AntImage:
		with open(fp, 'rb') as f:
			if f.read(1) != b'a':
				message = "'{}' is not an ant file".format(fp)
				raise SyntaxError(message)
			width, height = f.read(2)
			if not width or not height:
				message = "couldn't define image dimensions."
				raise EOFError(message)
			data = f.read()
			return cls((width + 1, height + 1), data)

	def save(self: AntImage, fp: str | PathLike[str]) -> None:
		with open(fp, 'wb') as f:
			f.write(b'a')
			f.write(bytes([self._width - 1, self._height - 1]))
			f.write(self._data)

	def __str__(self: AntImage):
		data: list = [self._data[i:i + self._width] for i in range(0, len(self._data), self._width)]
		image: list
		if sys.platform == "win32":
			image = [''.join(['{} '.format(hex(y)) for y in x]) for x in data]
			return "{}x{}\n".format(self._width, self._height) + '\n'.join(image)
		image = [''.join(['\033[48;5;{}m  \033[0m'.format(y) for y in x]) for x in data]
		return "{}x{}\n".format(self._width, self._height) + '\n'.join(image)

	def __repr__(self: AntImage):
		return "AntImage(size=({}, {}), len(data)={})".format(self._width, self._height, len(self._data))
