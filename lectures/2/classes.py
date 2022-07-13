


'''class point():
    def __init__(self,x,y):
        self.x = x
        self.y =y

p = point(2,5)
print(p.x)
print(p.y)
'''
class Flight():
    # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add a passenger to the flight:
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(2)
people = ["Nigga","Cunt","Faggot","Pussy"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
