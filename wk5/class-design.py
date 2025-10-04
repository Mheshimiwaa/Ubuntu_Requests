# parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is powering on...")


# Child class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call parent constructor
        self.storage = storage
        self.battery = battery  # percent (0-100)

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")

    def charge_battery(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"Battery charged to {self.battery}%")


# Testing the Smartphone class
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Galaxy S24", 256, 80)

    phone.power_on()
    phone.make_call("+254712345678")
    phone.charge_battery(15)
