# providing a class that helps build different entities
# instead defining it initially


class House:
    
    def __init__(self):
        self._floors = 0
        self._bedrooms = 0
        self._bathrooms = 0
        self._garage = False
        self._swimmingPool = False
    
    def __str__(self) -> str:
        return f'''floors : {self._floors}
    bedrooms : {self._bedrooms}
    bathrooms : {self._bathrooms}
    garage : {self._garage}
    swimming pool : {self._swimmingPool}'''

class HouseBuilder(House):
    def floorCount(self, count: int) -> None:
        self._floors = count

    def bedRoomCount(self, count: int) -> None:
        self._bedrooms = count
    
    def bathroomCount(self, count: int) -> None:
        self._bathrooms = count
    
    def addGarage(self) -> None:
        self._garage = True
    
    def addSwimmingPool(self) -> None:
        self._swimmingPool = True



house1 = HouseBuilder()
house1.floorCount(2)
house1.bedRoomCount(3)
house1.bathroomCount(2)

# --- 
house2 = HouseBuilder()
house2.floorCount(1)
house2.bedRoomCount(2)
house2.bathroomCount(1)
house2.addGarage()

# ---
house3 = HouseBuilder()
house3.floorCount(3)
house3.bedRoomCount(5)
house3.bathroomCount(4)
house3.addGarage()
house3.addSwimmingPool()

# --- 
print("HOUSE 1")
print(house1)

print("-"*20)
print("HOUSE 2")
print(house2)

print("*"*20)
print("HOUSE 3")
print(house3)