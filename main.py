def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

from stats import count_words

from stats import count_characters

def main():
	text = get_book_text("books/frankenstein.txt")
	word_count = count_words(text)
	characters = count_characters(text)
	print(f"{word_count} words found in the document")
	print(f"{characters}")
main()
