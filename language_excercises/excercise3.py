# per aprire file: f = open('words.txt', 'rb')
# s = f.read()

in_f = open('words.txt', 'rb')
out_f = open('words_out.txt', 'wb')
i = 0
first = 1
for s in in_f.read():
	if first == 1:
		out_f.write(str(i)+'. ')
		first = 0
	out_f.write(s)
	if s == '\n':
		i += 1
		first = 1
