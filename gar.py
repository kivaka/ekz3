class Gardener():

    """creating a gardener"""
    def __init__(self, name, plant):
        self.name=name
        self._plant=plant

    """the function of the gardener's work"""
    def work(self):
        print("the gardener is working")
        self._plant.grow_all()

    """checking ripeness and harvesting"""
    def harvest(self):
        self._plant.all_are_ripe()
        if self._plant.all_are_ripe()==True:
            self._plant.give_away_all()
            print('the harvest is harvested')
        else:
            print('the harvest is not ready')

    """reference"""
    def knowledge_base(self):
        print("""Nitrogen fertilizers should be applied to the soil better on a sunny day, diluting them in water / n
In hot weather, it is preferable to plant seedlings in the evening, when the sun is no longer so warm
For a good ovary of tomatoes, boric acid is used as foliar top dressing
To get the first harvest faster, you need to cut off all the leaves below the first brush on which the fruits began to ripen
Tall tomatoes should be grown in one stalk
It is necessary to pluck ripe fruits with stalks so that the remaining fruits ripen faster""")