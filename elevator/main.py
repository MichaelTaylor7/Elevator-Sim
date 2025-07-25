import time

class Elevator:
    def __init__(self, bottom=0, top=9):
        self.current_floor = 0
        self.requests = []
        self.min_floor = bottom
        self.max_floor = top
        self.direction = None

    def request_floor(self, floor):
        if self.min_floor <= floor <= self.max_floor:
            print(f"Heading to {floor} floor!")
            self.requests.append(floor)
        else:
            print("Not sure how you pressed that number...")

    def move(self):
        while self.requests:
            destination = self.requests.pop(0)
            self._move_to(destination)

    def _move_to(self, destination):
        print(f"Moving from floor {self.current_floor} to {destination}")
        # stretch goal: "going up!" and "going down!" conditions
        while self.current_floor != destination:
            if self.current_floor < destination:
                self.current_floor +=1
            else:
                self.current_floor -= 1
            time.sleep(0.5)
        print(f"Arrive at floor {destination}")

def run_sim():
    elevator = Elevator()
    requests = [4,4,4,4,4]
    for floor in requests:
        elevator.request_floor(floor)
    elevator.move()

run_sim()


