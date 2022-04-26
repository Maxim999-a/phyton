class Neravenstvo:
    
    def __init__(self, first = 0, second = 0):
        self.__first = int(first)
        self.__second = int(second)
        
    def get_first(self):
        return self.__first
    
    def set_first(self, f):
        self.__first = f
        
    def get_second(self):
       return self.__second
   
    def set_second(self, s):
        self.__second = s
    
    def ipart(self):
        return self.__first / self.__second
    
    def read(self):
        self.set_first(int(input("Введите числитель ")))
        self.set_second(int(input("Введите знаменатель ")))
   
    def display(self):
        print(f'Целая часть и остаток: {self.ipart()}')
        
if __name__=='__main__':
        neravenstvo = Neravenstvo()
        neravenstvo.read()
        neravenstvo.display()
        