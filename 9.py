hf = open('file.txt')

for line in hf:
	line = line.rstrip()
	wds = line.split()

	if len(wds) < 3 or wds[0] != 'From':
		continue
	print(wds[2])