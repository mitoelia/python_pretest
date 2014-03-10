def find_longest_word(list):
	max = list[0]
	for word in list:
		if len(word) > len(max):
			max = word
	return max

def filter_long_words(list, n):
	words_longer = []
	for word in list:
		if len(word) > n:
			words_longer.append(word)
	return words_longer



if __name__ == '__main__':		# se ci fosse import in un altro fai non entrerebbe nell if
	print find_longest_word(['ciao', 'hey', 'brother', 'audi', 'bmw', 'jesoloBeach', 'avicii'])
	print '\n'
	list_longer = filter_long_words(['ciao', 'hey', 'brother', 'audi', 'bmw', 'jesoloBeach', 'avicii'], 5)
	for word in list_longer:
		print word+'\n'
