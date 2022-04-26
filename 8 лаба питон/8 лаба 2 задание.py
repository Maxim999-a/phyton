import os


class Money():

    
   def __init__(self, ruble = 0, penny  = 0):
    
       if type(ruble) != int:
           raise TypeError('ruble должен быть целым числом')
       if penny not in range(0,100):
           raise ValueError('penny должен быть  числом от 0 до 99')
       self.__ruble = int(ruble)
       self.__penny = int(penny)

   def get_ruble(self):
        return self.__ruble
     
   def set_ruble(self, r):
        self.__ruble = r
         
   def get_penny(self):
        return self.__penny
    
   def set_penny(self, s):
        self.__penny = s

  
    # Вывод на экран
   def display(self):
        print(f"Рубли: {self.get_ruble()}")
        print(f"Копейки: {self.get_penny()}")
        

   def vvodruble(self):
       self.set_ruble(int(input(f"введите рубли:")))
       self.set_penny(int(input(f"введите копейки:")))
   
    
      
   
   def __str__(self):
        return f'{self.get_ruble()},{self.get_penny()}' 
 
   def __add__(self, other):
        kopSum = self.get_penny() + other.get_penny()
        rub = self.get_ruble() + other.get_ruble() + (kopSum // 100)
        kop = (kopSum % 100)
        return Money(rub, kop)
    
   def __sub__(self, other):
        kopSum = self.get_penny() - other.get_penny()
        rub = self.get_ruble() - other.get_ruble() + (kopSum // 100)
        kop = (kopSum % 100)
        return Money(rub, kop)

   def __mul__(self, other):
        kopSum = self.get_penny() * other.get_penny()
        rub = self.get_ruble() * other.get_ruble() + (kopSum // 100)
        kop = (kopSum % 100)
        return Money(rub, kop)
 
   def __truediv__(self, other):
        kopSum = self.get_penny() / other.get_penny()
        rub = self.get_ruble() / other.get_ruble() + (kopSum // 100)
        kop = (kopSum % 100) 
        return Money(rub, kop)
   
   def sravnenie(self,a,b):
       if a > b :
           return 1 
       elif a == b :
           return 2 
       elif a < b: 
           return 3 

    # Ввод данных
    
if __name__ == '__main__':
    acc = Money()
    acc1=Money()
    acc2=Money()
    while True:
        os.system('cls')
        acc.display()
    
        print("ввод>> [1]")
        print("сумма>> [2]")
        print("вычитание>> [3]")
        print("произведение>> [4)")
        print("разность>> [5]")
        print("сравнение>> [6]")
        print("Выход >> [7]")
        
        command = int(input(">>"))
        
        if command == 1:
           
           print("ввод первого числа ") 
           acc1.vvodruble()
           print("ввод второго числа ") 
           acc2.vvodruble()
           
           
        elif command == 2:
          acc=acc1+acc2
          print(acc) 
          
        elif command == 3:
          acc=acc1-acc2
          print(acc) 
            
        elif command == 4:
          acc=acc1*acc2
          print(acc) 
          
        elif command == 5:
          acc=acc1/acc2
          print(acc) 
            
        elif command == 6:
           # print (acc.sravnenie(acc1.get_ruble()+acc1.get_penny(),acc2.get_ruble()+acc2.get_penny()))
            if(acc.sravnenie(acc1.get_ruble()+acc1.get_penny(),acc2.get_ruble()+acc2.get_penny())) == 1:
                print(f"{acc1.get_ruble()} руб, {acc1.get_penny()} коп больше {acc2.get_ruble()} руб, {acc2.get_penny()} коп" )
            elif(acc.sravnenie(acc1.get_ruble()+acc1.get_penny(),acc2.get_ruble()+acc2.get_penny())) == 2:
                print(f"{acc1.get_ruble()} руб, {acc1.get_penny()} коп равны {acc2.get_ruble()} руб, {acc2.get_penny()} коп" )
            elif(acc.sravnenie(acc1.get_ruble()+acc1.get_penny(),acc2.get_ruble()+acc2.get_penny())) == 3:
                print(f"{acc1.get_ruble()} руб, {acc1.get_penny()} коп меньше {acc2.get_ruble()} руб, {acc2.get_penny()} коп" )
                
        elif command == 7:
            break
        else:
            print(f"Неизветсная команда: {command}\n")
            input("Нажмите 'Enter' для продолжения")  