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
