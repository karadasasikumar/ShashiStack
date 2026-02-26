class Building:
    no_of_rooms=0

    def __init__(self,buildingname,wifi):
        self.buildingname=buildingname
        self.wifi=wifi
        Building.no_of_rooms+=1

c1=Building("cvcorp",1)
c2=Building("sr residency",0)
print(Building.no_of_rooms)
