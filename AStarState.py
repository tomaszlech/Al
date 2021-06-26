
class AStarState:
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position
    def show(self):
        return str("{("+str(self.position[0])+", "+str(self.position[1])+") "+str(self.g)+"}")