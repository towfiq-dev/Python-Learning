class baba:
    brand = "Yamaha"
    model = "R15 V4"
    engine = "155cc"
    price = 600000

class son1(baba):
    brand = "Honda"
    model = "CBR 150R"
    engine = "149cc"
    price = 565000

class son2(son1):
    brand = "Suzuki"
    model = "Gixxer SF"
    engine = "155cc"
    price = 350000
    
class son3(son2):
    name = ""
    models = ""
    engines = ""
    prices = ""

c = son3()
print(c.brand)