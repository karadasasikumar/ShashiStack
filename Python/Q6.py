# Design a LibraryMember class that:
# •	Tracks total active members.
# •	Each member has a name and books_borrowed count.
# •	Has a function to borrow books, with borrowing limit common to all.
# •	Allows updating borrowing limit globally.
# •	Has a static function to check if book title is valid (non-empty string, reasonable length).
# Demonstrate:
# 1.	Borrowing books for multiple users.
# 2.	Changing borrowing limits.
# 3.	Validating book titles before borrowing.


class LibraryMember:
    total_members=0
    limit=2
    def __init__(self,name,book):
        self.name=name
        self.book=book
        LibraryMember.total_members+=1
        

