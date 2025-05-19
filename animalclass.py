from abc import ABC, abstractmethod

class Animal(ABC): 
    
    @abstractmethod    
    def __init__(self  ):
        pass

    @abstractmethod
    def can_fly(self):
        dic = self.__class__
        for key,value  in vars(dic).items():
                if key == "wings" and value =="strong":
                    return("the animal is flying")
                
    @abstractmethod
    def can_swim(self):
        dic = self.__class__
        for key,value  in vars(dic).items():
                if key == "gills" and value ==True:
                    return("the animal is swimming")

    
    def can_eat(self):
        pass

    @abstractmethod
    def can_walk(self):
        dic = self.__class__
        for key,value  in vars(dic).items():
            if key == "leg" and value == True:
                return("the animal is walking")
            
    @abstractmethod
    def can_crawl(self):
        dic = self.__class__
        for key,value  in vars(dic).items():
            if key == "leg" and value == "short" or value == False:
                    return("the animal is crawling")
        


  


class  Fish (Animal):
    
    weight = "light"
    leg = False
    gills = True
    wings = False
    scale = True
    

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
# print(fish1.can_fly())
# print(fish1.can_walk())

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
