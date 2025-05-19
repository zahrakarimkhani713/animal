from abc import ABC, abstractmethod

class Animal(ABC): 
    
    @abstractmethod    
    def __init__(self  ):
        pass

    @abstractmethod
    def can_fly(self):
        dic = self.__class__
        print(dic ,self.__class__.__name__)
        for key,value  in vars(dic).items():
                if key == "wings" and value =="strong":
                    return("the animal is flying")
                return ("can't fly")
    @abstractmethod
    def can_swim(self):
        return("the animal is swimming")

    
    def can_eat(self):
        pass

    @abstractmethod
    def can_walk(self):
        dic = self.__class__
        for key,value  in vars(dic).items():
            if key == "leg" and value =="True":
                return("the animal is walking")
            return ("can't walk")
            
    @abstractmethod
    def can_crawl(self):
        pass


  


class  Fish (Animal):
    i = 0
    gills = True
    baale = True
    baal = False
    leg = False

    def __init__(self  ):
        super().__init__()



    def can_fly(self):
         return super().can_fly()
        

    def can_swim(self):
        return super().can_swim()    
    
    def can_walk(self):
        return super().can_walk()
        
    def can_crawl(self):
        return super().can_crawl()

        
            


fish1 =  Fish() 
# print(fish1.can_swim())
print(fish1.can_fly())
# print(fish1.can_walk())

class Snake(Animal):
    i = 1
    leg = False
    gills = False

    def __init__(self  ):
        super().__init__()


    def can_fly(self):
         return super().can_fly()
        

    def can_swim(self):
        return super().can_swim()    
    
    def can_walk(self):
        return super().can_walk()
        
    def can_crawl(self):
        return super().can_crawl()
    
be = Snake()    
print(be.can_walk())
        

class Dog(Animal):
    i = 2
    leg = True

    def __init__(self ):
        super().__init__()
        



    def can_fly(self):
         return super().can_fly()
        

    def can_swim(self):
        return super().can_swim()    
    
    def can_walk(self):
        return super().can_walk()
        
    def can_crawl(self):
        return super().can_crawl() 
    
dog1 = Dog()
print(dog1.can_walk())    

class Bird(Animal):
    i = 3
    weight = "light"
    leg = True
    gills = False
    wings ="strong"
    scale = False

    def __init__(self ):
            return super().__init__()



    def can_fly(self):
            return super().can_fly()
        

    def can_swim(self):
        return super().can_swim()    

    def can_walk(self):
        return super().can_walk()
        
    def can_crawl(self):
        return super().can_crawl()


bird1 = Bird()
print(bird1.can_fly())