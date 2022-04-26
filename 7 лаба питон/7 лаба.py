from mypackage import data1
from os import sep
if __name__ == '__main__':
    # Список .
    students = []
     
    while True:
        
               # Вывести справку о работе с программой.
        print("Список команд:\n")
        print("1 - добавить студента;")
        print("2 - вывести список студентов;")
        print("3 - информация о студентов с двойками;")
        print("4 - завернешние программы")
        
            
        command= int(input(">>"))
            
        if command == 1:
          students = data1.input_data(students)
                
        elif command == 2:
          students = data1.output_data(students)
            
        elif command == 3:
          students =  data1.outputbadmark_data(students)
                
        elif command == 4:
            break  
          
        else:
         print("Неизвестная команда {command}", )
         input("Нажмите Enter для продолжения")