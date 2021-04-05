class Liquid:

    # attributes
    # name -> string
    # position -> list

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return self.name
