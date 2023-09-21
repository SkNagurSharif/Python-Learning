from items.User import User


class Student(User):
    def __init__(self, user_id, name, grade_level, major, advisor):
        super().__init__(user_id, name)
        self.grade_level = grade_level
        self.major = major
        self.advisor = advisor
        self.study_period = False

    def can_borrow(self):
        limit = 5 if self.study_period else 3
        return len(self.borrowed_items) < limit

    def start_study_period(self):
        self.study_period = True

    def end_study_period(self):
        self.study_period = False

    def display_advisor(self):
        print(f"{self.name}'s advisor is {self.advisor}.")

        """
        For students, we can consider attributes like grade level, major, and an academic advisor. 
        Moreover, students might have a study period during which they can borrow more books than usual.
        """

