words = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(words):
	my_dict = {}
	for item in words:
		k = sorted(item)
		k = "".join(k)
		print(k)
		if k not in my_dict:
			my_dict[k] = [item]
		else:
			my_dict[k].append(item)
	return list(my_dict.values())

print(group_anagrams(words))
