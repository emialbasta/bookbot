def count_words(text):
        words = text.split()
        return len(words)

def count_characters(text):
	character_count = {}
	lower_case_text = text.lower()
	for character in lower_case_text:
		if character in character_count:
			character_count[character] += 1
		else:
			character_count[character] = 1
	return character_count

def sort_chars_by_count(chars_dict):
	char_list = []
	for char, count in chars_dict.items():
		char_dict = {"char": char, "num": count}
		char_list.append(char_dict)

	def sort_on(dict):
		return dict["num"]

	char_list.sort(reverse=True, key=sort_on)

	return char_list
