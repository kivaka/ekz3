from to_cl import Tomato

class TomatoBush():
    """creating a bush"""
    def __init__(self, quantity):
        self.quantity=0
        list1 = []
        key = 0
        while quantity != key:
            q = "tom"+str(key)
            q = Tomato(1)
            key += 1
            list1.append(q)
        self.tomatoes=list1

    """bush growth"""
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    """checking ripeness"""
    def all_are_ripe(self):
        for i in self.tomatoes:
            i.is_ripe()
            if i.is_ripe()==True:
                return True
            else:
                return False
                break

    """harvesting"""
    def give_away_all(self):
        self.tomatoes =[]
