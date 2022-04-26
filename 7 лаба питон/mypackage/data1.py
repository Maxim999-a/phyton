def input_data(students):
       # Запросить данные .
            Fullname = input("ФИО студента ")
            numbergroup = input("номер группы ")
            ochenka = input("Оценка ")
 
            # Создать словарь.
            student = {
                'Fullname': Fullname,
                'numbergroup': numbergroup,
                'ochenka': ochenka,
            }
 
            # Добавить словарь в список.
            
            students.append(student)
            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('Fullname', ''))
            return students
def output_data(students):
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-'.format(
                '-' * 4,
                '-' * 17,
                '-' * 17,
                '-' * 17,
            )
            print(line)
            print(
                '| {:^4} | {:^17} | {:^17} | {:^17} | '.format(
                    "No",
                    "ФИО",
                    "Номер группы",
                    "Оценка"
                ))
            print(line)
 
            # Вывести данные о всех студентах.
            for idx, student in enumerate(students, 1):
                
                print( '| {:^4} | {:^17} | {:^17} | {:^17} | '.format(
                      idx,
                      student.get('Fullname', ''),
                      student.get('numbergroup', ''),
                      student.get('ochenka', '')
            ))
 
            print(line)
 
def outputbadmark_data(students):
            line = '+-{}-+-{}-+-{}-+-{}-'.format(
                '-' * 4,
                '-' * 17,
                '-' * 17,
                '-' * 17,
            )
            print(line)
            print(
                '| {:^4} | {:^17} | {:^17} | {:^17} | '.format(
                    "No",
                    "ФИО",
                    "Номер группы",
                    "Оценка"
                ))
            print(line)
 
            # Вывести данные о всех студентах.
            for idx, student in enumerate(students, 1):
             if student.get('ochenka','')=='2':
                print( '| {:^4} | {:^17} | {:^17} | {:^17} | '.format(
                      idx,
                      student.get('Fullname', ''),
                      student.get('numbergroup', ''),
                      student.get('ochenka', '')
                ))
 
            print(line)
            
            


