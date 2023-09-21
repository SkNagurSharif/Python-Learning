from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, title, author_artist, item_id, copies=1):
        self.title = title
        self.author_artist = author_artist
        self.item_id = item_id
        self.on_loan = False
        self.copies = copies
        self.borrow_history = []

    # Track how many days an item has been borrowed
    def days_borrowed(self):
        if self.on_loan:
            start_date = self.borrow_history[-1][1]
            return (datetime.now() - start_date).days
        return 0

    def calculate_fine(self):
        days = self.days_borrowed() - 14  # Assuming a 2-week borrowing period
        if days > 0:
            return days * 0.5  # 50 cents per day late
        return 0
    
    def add_feedback(self, user, rating, comment):
        if user in self.borrow_history:
            self.feedback.append((user, rating, comment))

    def average_rating(self):
        if not self.feedback:
            return None
        total = sum([rating for _, rating, _ in self.feedback])
        return total / len(self.feedback)
