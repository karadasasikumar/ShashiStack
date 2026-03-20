# Create a HotelRoom class that:
# •	Keeps a base price per night (shared).
# •	Each room has room_number, nights_booked, and guest_name.
# •	Has a method to calculate total bill.
# •	Allows updating the base price across all rooms.
# •	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
# Demonstrate:
# 1.	Creating rooms and bookings.
# 2.	Changing base price.
# 3.	Checking bill updates and validation.


class HotelRoom:
    base_price=1500
    def __init__(self,name,room_no,nights_booked):
        self.name=name
        self.room_no=room_no
        self.nights_booked=nights_booked
    def total_bill(self):
        total=self.nights_booked*HotelRoom.base_price
    @classmethod
    def update(cls,new):
        cls.base_price=new
    @staticmethod
    def valid(n):
        return n>0

r1=HotelRoom("Sashi",105,2)

print(HotelRoom.valid(2))
r1.total_bill()
HotelRoom.update(2000)
r1.total_bill()

