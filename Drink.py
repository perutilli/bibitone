class Drink:

    # attributes
    # name
    # dict(?) liquid, qt

    def __init__(self, name, quantities):
        self.name = name
        self.quantities = quantities

    def __str__(self):
        return self.name + ": " + str(self.quantities)
