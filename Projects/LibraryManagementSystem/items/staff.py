from items.User import User

"""
For staff members, consider attributes like job title, department, and an option to override
    borrowing limits for special circumstances.
"""
class Staff(User):
    def __init__(self, user_id, name, job_title, department):
        super().__init__(user_id, name)
        self.job_title = job_title
        self.department = department
        self.override_limit = False

    def can_borrow(self):
        if self.override_limit:
            return True
        return len(self.borrowed_items) < 10

    def enable_override(self):
        self.override_limit = True

    def disable_override(self):
        self.override_limit = False

    def display_department(self):
        print(f"{self.name} works in the {self.department} department as a {self.job_title}.")
