from datetime import datetime

class Reservation:
    def __init__(self, user, item):
        self.user = user
        self.item = item
        self.reservation_date = datetime.now()
        self.is_fulfilled = False

    def days_since_reserved(self):
        return (datetime.now() - self.reservation_date).days

    def has_expired(self):
        # Assuming a reservation expires after 7 days
        return self.days_since_reserved() > 7

    def notify_availability(self):
        # A simple print statement for this example. In a real-world application, 
        # this might send an email or a system notification.
        print(f"Hello, {self.user.name}! The item '{self.item.title}' you reserved is now available!")

    def fulfill(self, library):
        if not self.item.on_loan and not self.is_fulfilled:
            self.notify_availability()
            # Optionally: Automatically check out the item for the user.
            # self.user.borrow_item(self.item)
            self.is_fulfilled = True
            library.reservations.remove(self)
        elif self.has_expired():
            print(f"Reservation for {self.user.name} for {self.item.title} has expired.")
            library.reservations.remove(self)
        else:
            print(f"{self.item.title} is still on loan by another user.")
            
    def fulfill_reservations(self):
    # It's common to create a copy of the list you're iterating over if you're going to modify it during iteration.
        for reservation in self.reservations.copy():
            reservation.fulfill(self)

        """
           Certainly! The `Reservation` class is crucial for managing the temporary allocation or booking of library items that are currently unavailable. Let's make it more comprehensive and realistic.

### Reservation Class:

#### Features:

1. **Expiration**: If a reservation isn't fulfilled within a set number of days, it expires.
2. **Notification**: The class can notify the user when the item they reserved becomes available.
3. **Priority Queue**: If multiple users reserve the same item, they are served on a first-come, first-serve basis.

#### Implementation:

In the `Library` class, the `fulfill_reservations` method can be adjusted to handle these extended reservation features:

```

### Summary:

With this more detailed `Reservation` class:

1. **Expiry of Reservations** is introduced, so reservations don't remain indefinitely if not fulfilled.
2. **Notification** allows users to be informed as soon as their reserved item becomes available.
3. **Priority Management** ensures that if multiple users reserve the same item, the first person to reserve gets it first. This is implicitly managed by the order of the `reservations` list in the `Library` class; earlier reservations appear earlier in the list.

This enhanced reservation system provides a more user-friendly and efficient method of managing reserved items, making the library system more robust and realistic. 
        """
