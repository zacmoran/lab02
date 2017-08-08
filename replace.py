text, find, replace = input(), input(), input();
final = "";
for txt in text.split(" "):
	if(txt == find):
		final += replace + " ";
	else:
		final += txt + " ";

print(final);