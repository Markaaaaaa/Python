Inheritance allows classes to reuse code from a base class, making it easier to organize, extend, and maintain code. 
The base class defines common functionality that can be reused by derived classes, reducing redundancy.
It enables a logical structure, making it clear which classes share common features.
Also, Changes in the base class can automatically propagate to derived classes.
class Appliance:
    def use(self):
        print("Using the appliance")

class WashingMachine(Appliance):
    def use(self):
        print("Washing clothes")

class Refrigerator(Appliance):
    def use(self):
        print("Cooling food")

appliances = [WashingMachine(), Refrigerator()]
for appliance in appliances:
    appliance.use()
