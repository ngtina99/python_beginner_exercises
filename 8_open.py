fh = open('file.txt')
print(fh)

for lx in fh:
	ly = lx.lstrip()
	print(ly.upper())