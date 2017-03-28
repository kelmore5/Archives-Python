main = [95,11,93,00,12,39,91,94,89]

def bubble(mainList):
	if(mainList == []):
		return []
	else:
		first = mainList[0]
		index = 0
		while(index < len(mainList)):
			if(mainList[index] > first):
				first = mainList[index]
			index += 1
		return [first] + bubble(mainList[1:])

print bubble(main)
