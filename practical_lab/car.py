class Car:
    def __init__(self):

        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print("The car is now running.")
        else:
            print("The car is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print("The car has stopped.")
        else:
            print("The car is not running.")

    def display_state(self):
        state = "running"
        if self.is_running:
            state = "running"
        else:
            state="stopped"
        print(f"The car is currently {state}.")
