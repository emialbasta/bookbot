import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

from stats import count_words

from stats import count_characters

from stats import sort_chars_by_count

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path_to_book = sys.argv[1]
	text = get_book_text(path_to_book)
	word_count = count_words(text)
	characters = count_characters(text)
	word_list = sort_chars_by_count(characters)
	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at {path_to_book}")
	print ("----------- Word Count ----------")
	print (f"Found {word_count} total words")
	print ("--------- Character Count -------")
	for char_dict in word_list:
		char = char_dict["char"]
		count = char_dict["num"]

		if char.isalpha():
			print(f"{char}: {count}")
	print ("============= END ===============")
main()
