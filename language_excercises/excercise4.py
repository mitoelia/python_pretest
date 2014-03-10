#coding:utf-8
def translate(text):
	d = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
	text_out = []
	for a in text:
		if a in d.keys():
			text_out.append(d[a])
		else:
			text_out.append(a)
	return text_out


if __name__ == '__main__':
	result = translate(['christmas', 'and', 'merry', 'year'])
	for word in result:
		print word
