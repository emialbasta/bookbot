def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def count_words(text):
        words = text.split()
        return len(words)

def main():
	text = get_book_text("books/frankenstein.txt")
	word_count = count_words(text)
	print(f"{word_count} words found in the document")
main()
