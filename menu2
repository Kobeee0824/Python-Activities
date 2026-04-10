class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False
        self.guest_name = None


class Hotel:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_number, room_type, price):
        if room_number in self.rooms:
            print("Room already exists.")
        else:
            self.rooms[room_number] = Room(room_number, room_type, price)
            print("Room added successfully.")

    def check_in(self, room_number, guest_name):
        room = self.rooms.get(room_number)
        if not room:
            print("Room does not exist.")
        elif room.is_booked:
            print("Room already booked.")
        else:
            room.is_booked = True
            room.guest_name = guest_name
            print(f"{guest_name} checked into room {room_number}.")

    def check_out(self, room_number):
        room = self.rooms.get(room_number)
        if not room or not room.is_booked:
            print("Room is not currently booked.")
        else:
            print(f"{room.guest_name} checked out.")
            room.is_booked = False
            room.guest_name = None

    def view_rooms(self):
        if not self.rooms:
            print("No rooms available.")
            return

        for room in self.rooms.values():
            status = "Booked" if room.is_booked else "Available"
            print(f"Room {room.room_number} | {room.room_type} | ${room.price} | {status}")


def main():
    hotel = Hotel()

    while True:
        print("\n--- Hotel Management System ---")
        print("1. Add Room")
        print("2. Check In")
        print("3. Check Out")
        print("4. View Rooms")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            num = input("Room number: ")
            rtype = input("Room type: ")
            price = float(input("Price per night: "))
            hotel.add_room(num, rtype, price)

        elif choice == "2":
            num = input("Room number: ")
            name = input("Guest name: ")
            hotel.check_in(num, name)

        elif choice == "3":
            num = input("Room number: ")
            hotel.check_out(num)

        elif choice == "4":
            hotel.view_rooms()

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
