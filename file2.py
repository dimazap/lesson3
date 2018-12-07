import codecs
import sys
sys.stdout=open("referat2.txt","w")

with open('referat.txt', 'r', encoding='utf-8') as f:
	contents = codecs.open('referat.txt', encoding='utf-8').read()
	content = f.read()
	length = len(content)
	words = content.split()
	num_words = len(words)
print(f"Length of content is: {length}")
print(num_words)
print(contents.replace('.', '!'))
sys.stdout.close()