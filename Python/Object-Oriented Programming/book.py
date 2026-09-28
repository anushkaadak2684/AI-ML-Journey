class Book:
    def __init__(self, title, author, reviews):
        self.title = title
        self.author = author
        self.reviews = reviews

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        print(f"Total reviews: {len(self.reviews)}")

    def display_reviews(self):
        print("===Reviews===")
        for review in self.reviews:
            print(review)

b1 = Book("The Harry Potter", "J.K. Rowling", ["Amazing", "Nostalgia", "It's been always my favourite"])
b1.add_review("I love all the three children")
b1.count_reviews()
b1.display_reviews()