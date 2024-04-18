class cat:
    name : None
    age : None
    __isHappy : None
    
    # constructor
    def __init__(self, name, age, isHappy = True):
        self.name = name,
        self.age = age,
        self.__isHappy = isHappy
        
    def sound(self):
        print("Meow")
        
    def display(self):
        print("****CAT***")
        print("name: ", self.name)
        print("age: ", self.age)
        print("happy: ", self.happy)
        
    #getter
    def get_isHappy(self):
        return self.__isHappy
    
    #setter
    def set_isHappy(self, new_Happy):
        self.__isHappy = new_Happy
        
# child class
class DometicCat(cat):
    owner: None
    
    def __init__(self, owner, name, age, ishappy=True):
        super().__init__(name, age, ishappy)
        self.owner = owner
        
class WildCat(cat):
    def sound(self):
        print("Hiss")
        
# create instance
cat1 = cat("Mao Mao", 3)
print(cat1.sound())

cat2 = DometicCat("Dairymilk", "Kitkat", 2)
print(cat2.owner)
