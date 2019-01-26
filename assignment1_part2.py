class book:
	author = ''
	title = ''
	def __init__(self, title, author):
		self.author = author
		self.title = title

def display(book):
	print '"{}, written by {}"'.format(book.title, book.author)

if __name__ == '__main__':
	Book1 = book("Of Mice and Men","John Steinbeck")
	Book2 = book("To Kill a Mockingbird","Harper Lee")
	display(Book1)
	display(Book2)
