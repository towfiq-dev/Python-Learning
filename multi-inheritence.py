class Bike1:
    brand = "Yamaha"
    model = "R15 V4"
    engine = "155cc"
    price = 600000

class Bike2:
    brand = "Honda"
    model = "CBR 150R"
    engine = "149cc"
    price = 565000

class Bike3:
    brand = "Suzuki"
    model = "Gixxer SF"
    engine = "155cc"
    price = 350000
    
class cycle(Bike1, Bike2, Bike3):
    name = ""
    models = ""
    engines = ""
    prices = ""

c = cycle()
print(c.price)