#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment1_Part2 working with classes """

class Book(object):
    """ Book class - each book has a title, author """
    author = ''
    title = ''
    def __init__(self, title, author):
        self.author = author
        self.title = title

    def setAuthor(self, author):
        """Author setter"""
        self.author = author

    def setTitle(self, title):
        """Title setter"""
        self.title = title

    def display(self):
        """ display function to display a book's title, author """
        print '"{}, written by {}"'.format(self.title, self.author)

if __name__ == '__main__':
    BOOK1 = Book("Of Mice and Men", "John Steinbeck")
    BOOK2 = Book("To Kill a Mockingbird", "Harper Lee")
    BOOK1.display()
    BOOK2.display()
