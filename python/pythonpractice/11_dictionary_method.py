# Dictionary method:-
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# get() method returns the value of the item with the specified key.
print(car.get("brand"))
print(car.get("model"))
print(car.get("year"))

x = car.get("price", 15000)
print(x)

# items() method
print(car.items())

# keys() method
print(car.keys())

# value() method
print(car.values())

# pop() method removes the specified item from the dictionary.
car.pop("model")
print(car)

# popitem() method removes the item that was last inserted into the dictionary.
car.popitem()
print(car)

# The setdefault() method returns the value of the item with the specified key.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.setdefault("model")
print(x)

x = car.setdefault("model", "Bronco")
print(x)

x = car.setdefault("color", "white")
print(x)

# update() method inserts the specified items to the dictionary.
print(car)

car.update({"company": "TCS"})
print(car)

car.update({"year": 2023})
print(car)
