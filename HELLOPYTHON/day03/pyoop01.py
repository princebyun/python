class Animal:
    def __init__(self):
        self.fullness = 0
    
    def eat(self):    
        self.fullness += 1
        
    def mantang(self):    
        self.fullness = 10
  
class Human(Animal):      
        def __init__(self):
            super().__init__() #상속받은것을 선언해줘야한다아아 
            self.flag_cook = False
            
        def goHakwon(self):
            self.flag_cook = True
                
hum = Human()        
print(hum.fullness)
hum.eat()
print(hum.fullness)
hum.mantang()
print(hum.fullness)
print(hum.flag_cook)
hum.goHakwon()
print(hum.flag_cook)





















