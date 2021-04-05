class Liquid:

    # attributes
    # name -> string
    # position -> list
    # shot -> boolean (is shottable)

    def __init__(self, name, position, shot):
        self.name = name
        self.position = position
        self.shot = shot

    def __str__(self):
        return self.name
