import sys
from .image import AntImage

def main(argv: list[str]) -> int:
	if len(argv) == 1:
		print("usage: python -m ant file")
		return 1
	for fp in argv[1:]:
		print(AntImage.open(fp))
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
