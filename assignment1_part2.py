class book:
	author = ''
	title = ''
	def __init__(self, author, title):
		self.author = author
		self.title = title

	def display():
		print "{}, written by {}".format(title, author)

if __name__ == '__main__':
	book1 = book("Of Mice and Men","JJohn Steinbeck")
	book2 = book("To Kill a Mockingbird","Harper Lee")
	book1.display()
	book2.display()
