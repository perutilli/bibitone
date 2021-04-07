class Drink:

    # attributes
    # name
    # dict(?) liquid, qt
    # img source -> string

    def __init__(self, name, quantities, img_source):
        self.name = name
        self.quantities = quantities
        self.img_source = img_source

    def __str__(self):
        return self.name
