import re
# text = "fox The quick brown fox base() jumps over the lazy dog user()"



# # Define a pattern to search for words containing 'o'
# pattern = r'\b\w*o\w*\b'  # This regex pattern looks for words containing the letter 'o'
# mat = re.match(pattern, text)

# if mat:
# 	print(mat)
# 	print("yes")
# else:
# 	print(mat)
# 	print("No")

# exit()
# pattern2 = r'\b[a-zA-Z]+\(\)'
# # Use re.findall() to find all matches for the pattern in the text
# matches = re.findall(pattern, text)
# matches2 = re.findall(pattern2, text)

# # s = re.match(re'',"")

# print(matches)
# print(matches2)


text = 'User.show("7f2951e0-e941-4830-a444-2d66ac5261db")'

if re.match(r'\b[a-zA-Z]+\.show\(.+\)', text):
	print("yes!")
	l = text.split("(")
	clsss = l[0].replace(".show", "")
	id_ = l[1][:-1]
	id_ = id_.replace("'", "")
	id_ = id_.replace("\"", "")
	print(f"{clsss} {id_}")

