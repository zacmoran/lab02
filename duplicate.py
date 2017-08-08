words = {};
for word in reversed(input().split(' ')): words[word.lower()] = word;
print(' '.join(str(words[x]) for x in sorted(words.keys())));