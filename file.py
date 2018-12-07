with open('referat.txt', 'r', encoding='utf-8') as f:
	content = f.read()
	length = len(content)
	words = content.split()
	num_words = len(words)
print(f"Length of content is: {length}")
print(num_words)