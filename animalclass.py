from abc import ABC, abstractmethod

class Animal(ABC): 
    wings = True
    weight = True
    gills = True
    leg = True
    scale = True
    @abstractmethod    
    def __init__(self):
        pass

    @abstractmethod
    def can_fly(self):
        if self.wings  == "strong" and self.weight == "light":
            return("the animal is flying")
        else:
             return("this animal can't fly")
    @abstractmethod
    def can_swim(self):
        if self.gills == True:
            return("the animal is swimming")
        else:
             return("this animal can't swim")
    
    def can_eat(self):
        pass

    @abstractmethod
    def can_walk(self):
        if self.leg ==True :
            return("the animal is walking")
        else:
             return("this animal can't walk")
            
    @abstractmethod
    def can_crawl(self):
        if self.scale == True and self.leg =="short" or self.leg == False  and self.scale == True:
            return("the animal is crawling")
        
        else:
             return("this animal can't crawl")

  


class  Fish (Animal):
    
    weight = "light"
    leg = False
    gills = True
    wings = False
    scale = True
    

    def __init__(self):
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
# print(fish1.can_fly())
# print(fish1.can_walk())
# print(fish1.can_crawl())

class Snake(Animal):
    
   weight = "light"
   leg = False
   gills = True
   wings = False
   scale = True
   

   def __init__(self):
         super().__init__()


   def can_fly(self):
         return super().can_fly()
        

   def can_swim(self):
        return super().can_swim()    
    
   def can_walk(self):
        return super().can_walk()
        
   def can_crawl(self):
        return super().can_crawl()
    
snake1 = Snake()    
print(snake1.can_crawl())
        

class Dog(Animal):
    weight = "heavy"
    leg = True
    gills = False
    wings = False
    scale = False

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
# print(dog1.can_walk())    

class Bird(Animal):
    
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
# print(bird1.can_fly())
