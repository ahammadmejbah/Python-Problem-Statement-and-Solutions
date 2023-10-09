

import pickle
​
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
​
    def __str__(self):
        return f'{self.name}, {self.age} years old'
​
# Create a Person object
person = Person('Alice', 30)
​
# Serialize the Person object into a byte stream
with open('person.pkl', 'wb') as f:
    pickle.dump(person, f)
​
# Deserialize the byte stream back into a Person object
with open('person.pkl', 'rb') as f:
    loaded_person = pickle.load(f)
​
print(loaded_person) # Output: Alice, 30 years old
