class Employee:
    def work(self):
        print("Working on general tasks")

class Engineer(Employee):
    def work(self):
        print("Engineering specific tasks")

employee = Employee()
engineer = Engineer()
employee.work()
engineer.work()
