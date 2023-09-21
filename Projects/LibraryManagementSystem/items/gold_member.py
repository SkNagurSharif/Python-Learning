from datetime import datetime

from items.User import User


class GoldMember(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.membership_start_date = datetime.now()
        self.loyalty_points = 0

    def can_borrow(self):
        return len(self.borrowed_items) < 7

    def add_loyalty_points(self, points):
        self.loyalty_points += points

    def use_loyalty_points(self, points):
        if self.loyalty_points >= points:
            self.loyalty_points -= points
            print(f"Used {points} loyalty points. Remaining: {self.loyalty_points}")
        else:
            print("Not enough loyalty points.")

    def request_acquisition(self, title):
        # In a real-world application, this would likely notify library acquisition staff or save to a database
        print(f"Gold Member {self.name} has requested a new acquisition: {title}.")

        """
        These enriched derived classes provide more depth to our library management system:

The Student class has a study period mode, enabling students to borrow more books during intense study times.
The Staff class has an override capability for exceptional borrowing situations, reflecting the trust and responsibility given to staff members.
The GoldMember class incorporates a loyalty program, which not only makes the system more engaging for users but also encourages more borrowing and returning of items, keeping the library's circulation healthy.
        """