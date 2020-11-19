# Get the name of the file and open it
name = input('Introduce nombre del archivo')
handle = open(name, 'r')
text = handle.read()
words = text.split()

#count word frequency

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1

# Find the most common word

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# All done
print (bigword, bigword)