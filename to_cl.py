class Tomato():
    """stages"""
    states= {1:"green", 2:"yellow", 3:"orange", 4:"red"}
    def __init__(self, index):
        self._index = index
        self._state = 0

    """plant growth"""
    def grow(self):
        self._state+=1

    """growth check"""
    def is_ripe(self):
        if self._state==4:
            return True
        else:
            return False