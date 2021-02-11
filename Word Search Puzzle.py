def leftright(wordsearch,word,pos):
	## left section
	found = 0
	if pos[1] - len(word) >= -1:
		s = wordsearch[pos[0]][pos[1]+1-len(word):pos[1]+1]
		if s[::-1] == word:
			found += 1

	## right section
	if pos[1] + len(word) <= len(wordsearch[pos[0]]):
		if wordsearch[pos[0]][pos[1]:pos[1] + len(word)] == word:
			found += 1
	return found

def updown(wordsearch,word,pos):
	found = 0
	## down section
	if pos[0] + len(word) <= len(wordsearch):
		s = "".join([wordsearch[pos[0]+i][pos[1]]for i in range(len(word))])
		if s == word:
			found += 1
	## up section
	if pos[0] - len(word) >= -1:
		s = "".join([wordsearch[pos[0]-i][pos[1]]for i in range(len(word))])
		if s == word:
			found += 1
	return found

def diagonal(wordsearch,word,pos):
	found = 0
	## diagonal down right
	if pos[0] + len(word) <= len(wordsearch) and pos[1] + len(word) <= len(wordsearch[pos[0]]):
		s = "".join([wordsearch[pos[0]+i][pos[1]+i] for i in range(len(word))])
		if s == word:
			found += 1
	## diagonal down left
	if pos[0] + len(word) <= len(wordsearch) and pos[1] - len(word) >= -1:
		s = "".join([wordsearch[pos[0]+i][pos[1]-i] for i in range(len(word))])
		if s == word:
			found += 1
	## diagonal up right
	if pos[0] - len(word) >= -1 and pos[1] + len(word) <= len(wordsearch[pos[0]]):
		s = "".join([wordsearch[pos[0]-i][pos[1]+i] for i in range(len(word))])
		if s == word:
			found += 1
	## diagonal up left
	if pos[0] - len(word) >= -1 and pos[1] - len(word) >= -1:
		s = "".join([wordsearch[pos[0]-i][pos[1]-i] for i in range(len(word))])
		if s == word:
			found += 1

	return found


def find_word(wordsearch,word):
	fst_ltr = word[0]
	fst_pos = [[i,j] for i in range(len(wordsearch)) for j in range(len(wordsearch[i])) if wordsearch[i][j] == fst_ltr]
	found_word = 0
	for a in fst_pos:
		found_word += leftright(wordsearch,word,a)
		found_word += updown(wordsearch, word, a)
		found_word += diagonal(wordsearch, word, a)
	return found_word

T = int(input())
i = 0
while T>0:
	row = int(input())
	column = int(input())
	arr = [input() for i in range(row)]
	W = input()
	found = find_word(arr,W)
	print("Case {0}: {1}".format(i+1,found))
	i += 1
	T -= 1