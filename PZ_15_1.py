"""
Вариант 4
Кобелев, Касьянов, Кмета, Пермяков
"""

import sqlite3 as sq
import os

if not os.path.exists('dekanat.db'):
    with sq.connect('dekanat.db') as con:
        cursor = con.cursor()

        # Создание таблицы facults (факультеты)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS facults (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """)

        # Создание таблицы departments (кафедры)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            id_facults INT NOT NULL,
            FOREIGN KEY (id_facults) REFERENCES facults(id)
        )
        """)

        # Создание таблицы spec (специальности)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS spec (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            id_departments INT NOT NULL,
            FOREIGN KEY (id_departments) REFERENCES departments(id)
        )
        """)
 
 #
        # Создание таблицы subject (предметы)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subject (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """)

        # Создание таблицы sub_form (форма сдачи предмета)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sub_form (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """)

        # Создание таблицы curriculum (учебный план)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS curriculum (
            id INT AUTO_INCREMENT PRIMARY KEY,
            spec_id INT NOT NULL,
            subject_id INT NOT NULL,
            sub_form_id INT NOT NULL,
            lec_hours INT NOT NULL,
            pract_hours INT NOT NULL,
            lab_hours INT NOT NULL,
            course_work BOOLEAN NOT NULL,
            FOREIGN KEY (spec_id) REFERENCES spec(id),
            FOREIGN KEY (subject_id) REFERENCES subject(id),
            FOREIGN KEY (sub_form_id) REFERENCES sub_form(id)
        )
        """)

        # Создание таблицы applicants (абитуриенты)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS applicants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            last_name VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL,
            sex VARCHAR(1) NOT NULL,
            birth_date DATE NOT NULL,
            address VARCHAR(255) NOT NULL,
            phone_number VARCHAR(20) NOT NULL,
            email VARCHAR(255) NOT NULL,
            receipt_date DATE NOT NULL,
            speciality VARCHAR(255) NOT NULL
        )
        """)

        # Создание таблицы academic_record (учебная карточка)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS academic_card ( 
            id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
            student_name VARCHAR(255) NOT NULL, 
            group_name VARCHAR(255) NOT NULL, 
            specialty_name VARCHAR(255) NOT NULL, 
            subject_id VARCHAR(255) NOT NULL, 
            exam_form_id VARCHAR(255) NOT NULL, 
            grade INT NOT NULL, 
            FOREIGN KEY (subject_id) REFERENCES subject(id), 
            FOREIGN KEY (exam_form_id) REFERENCES sub_form(id)
            )
            """)

        # Заполнение факультетов
        cursor.execute("""INSERT INTO facults VALUES (1, "Информационные технологии")""")
        cursor.execute("""INSERT INTO facults VALUES (2, "Экономика")""")

        # Заполнение кафедр
        cursor.execute("""INSERT INTO departments VALUES (1, "Информационные системы и программирование", 1)""")
        cursor.execute("""INSERT INTO departments VALUES (2, "Обеспечение информационной безопасности телекоммуникационных систем", 1)""")
        cursor.execute("""INSERT INTO departments VALUES (3, "Обеспечение информационной безопасности автоматизированных систем", 1)""")
        cursor.execute("""INSERT INTO departments VALUES (4, "Сетевое и системное администрирование", 1)""")
        cursor.execute("""INSERT INTO departments VALUES (5, "Инфокоммуникационные сети и системы связи", 1)""")
        cursor.execute("""INSERT INTO departments VALUES (6, "Экономика и бухгалтерский учет", 2)""")
        cursor.execute("""INSERT INTO departments VALUES (7, "Банковское дело", 2)""")
        cursor.execute("""INSERT INTO departments VALUES (8, "Коммерция", 2)""")

        # Заполнение специальностей
        cursor.execute("""INSERT INTO spec VALUES (1, "Разработчик Web-мультимедийных приложений", 1)""")
        cursor.execute("""INSERT INTO spec VALUES (2, "Разработчик мобильных/десктопных приложений", 1)""")
        cursor.execute("""INSERT INTO spec VALUES (3, "Прикладной программист", 1)""")
        cursor.execute("""INSERT INTO spec VALUES (4, "Безопасник телекоммуникационных систем", 2)""")
        cursor.execute("""INSERT INTO spec VALUES (5, "Безопасник автоматизированных систем", 3)""")
        cursor.execute("""INSERT INTO spec VALUES (6, "Системный администратор", 4)""")
        cursor.execute("""INSERT INTO spec VALUES (7, "Связист", 5)""")
        cursor.execute("""INSERT INTO spec VALUES (8, "Экономист", 6)""")
        cursor.execute("""INSERT INTO spec VALUES (9, "Бухгалтер", 6)""")
        cursor.execute("""INSERT INTO spec VALUES (10, "Банкир", 7)""")
        cursor.execute("""INSERT INTO spec VALUES (11, "Менеджер", 8)""")
        cursor.execute("""INSERT INTO spec VALUES (12, "Информатика", 1)""")
        cursor.execute("""INSERT INTO spec VALUES (13, "Информационные технологии", 1)""")

        # Заполнение предметов
        cursor.execute("""INSERT INTO subject VALUES (1, "Основы алгоритмизации и программирования")""")
        cursor.execute("""INSERT INTO subject VALUES (2, "Основы проектирования баз данных")""")
        cursor.execute("""INSERT INTO subject VALUES (3, "Основы web-технологий")""")
        cursor.execute("""INSERT INTO subject VALUES (4, "Компьютерные сети")""")
        cursor.execute("""INSERT INTO subject VALUES (5, "Архитектура аппаратных средств и технические средства информатизации")""")
        cursor.execute("""INSERT INTO subject VALUES (6, "Физическая культура")""")
        cursor.execute("""INSERT INTO subject VALUES (7, "История")""")
        cursor.execute("""INSERT INTO subject VALUES (8, "Стандартизация, сертификация и техническое документирование")""")
        cursor.execute("""INSERT INTO subject VALUES (9, "Дискретная математика с элементами математической логики")""")
        cursor.execute("""INSERT INTO subject VALUES (10, "Теория вероятностей")""")
        cursor.execute("""INSERT INTO subject VALUES (11, "Информатика")""")
        cursor.execute("""INSERT INTO subject VALUES (12, "Математика")""")
        cursor.execute("""INSERT INTO subject VALUES (13, "Программирование")""")
        cursor.execute("""INSERT INTO subject VALUES (14, "Физика")""")
        cursor.execute("""INSERT INTO subject VALUES (15, "Алгоритмы и структуры данных")""")

        # Заполнение формы сдачи предметов
        cursor.execute("""INSERT INTO sub_form VALUES (1, "Программирование")""")
        cursor.execute("""INSERT INTO sub_form VALUES (2, "Математика")""")
        cursor.execute("""INSERT INTO sub_form VALUES (3, "Физическая культура")""")
        cursor.execute("""INSERT INTO sub_form VALUES (4, "Гуманитарные")""")
        cursor.execute("""INSERT INTO sub_form VALUES (5, "Сетевые")""")
        cursor.execute("""INSERT INTO sub_form VALUES (6, "Мусорный")""")
        cursor.execute("""INSERT INTO sub_form VALUES (7, "Физика и информатика")""")

        # Заполнение учебного плана
        cursor.execute("""INSERT INTO curriculum VALUES (1, 1, 1, 1, 30, 20, 10, 1)""") # Для ОАП, Форма сдачи предмета - Программирование
        cursor.execute("""INSERT INTO curriculum VALUES (2, 1, 2, 1, 40, 30, 20, 0)""") # Для БД, Форма сдачи предмета - Программирование
        cursor.execute("""INSERT INTO curriculum VALUES (3, 1, 3, 1, 50, 40, 30, 1)""") # Для Web'а, Форма сдачи предмета - Программирование
        cursor.execute("""INSERT INTO curriculum VALUES (4, 1, 13, 1, 50, 40, 30, 1)""") # Для Программирование, Форма сдачи предмета - Программирование
        cursor.execute("""INSERT INTO curriculum VALUES (5, 1, 9, 2, 60, 50, 40, 0)""") # Для Дискретки, Форма сдачи предмета - Математика
        cursor.execute("""INSERT INTO curriculum VALUES (6, 1, 10, 2, 70, 40, 30, 1)""") # Для Теории Вероятности, Форма сдачи предмета - Математика
        cursor.execute("""INSERT INTO curriculum VALUES (7, 1, 11, 2, 70, 40, 30, 1)""") # Для Информатики, Форма сдачи предмета - Математика
        cursor.execute("""INSERT INTO curriculum VALUES (8, 1, 12, 2, 70, 40, 30, 1)""") # Для Математика, Форма сдачи предмета - Математика
        cursor.execute("""INSERT INTO curriculum VALUES (9, 1, 6, 3, 70, 40, 30, 1)""") # Для Физ-ры, Форма сдачи предмета - Физическая культура
        cursor.execute("""INSERT INTO curriculum VALUES (10, 1, 7, 4, 70, 40, 30, 1)""") # Для Истории, Форма сдачи предмета - Гуманитарные
        cursor.execute("""INSERT INTO curriculum VALUES (11, 1, 8, 4, 70, 40, 30, 1)""") # Для Стандартизации, Форма сдачи предмета - Гуманитарные
        cursor.execute("""INSERT INTO curriculum VALUES (12, 1, 5, 5, 70, 40, 30, 1)""") # Для АПС, Форма сдачи предмета - Сетевые
        cursor.execute("""INSERT INTO curriculum VALUES (13, 1, 4, 5, 70, 40, 30, 1)""") # Для КС, Форма сдачи предмета - Сетевые
        cursor.execute("""INSERT INTO curriculum VALUES (14, 1, 14, 7, 70, 40, 30, 1)""") # Для Физики, Форма сдачи предмета - Физика и информатика

        # Заполнение абитуриентов
        cursor.execute("""INSERT INTO applicants VALUES (1, "Кобелев", "Евгений", "Николаевич", "М", "2005-04-21", "г. Ростов-на-Дону", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
        cursor.execute("""INSERT INTO applicants VALUES (2, "Касьянов", "Максим", "Юрьевич", "М", "2005-06-15", "г. Батайск", "Номер телефона", "Email", "2021-09-01", "Разработчик мобильных/десктопных приложений")""")
        cursor.execute("""INSERT INTO applicants VALUES (3, "Кмета", "Антон", "Геннадиевич", "М", "2005-07-22", "г. Красный Сулин", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
        cursor.execute("""INSERT INTO applicants VALUES (4, "Медведев", "Иван", "Юрьевич", "М", "2005-04-08", "г. Азов", "Номер телефона", "Email", "2021-09-01", "Не определившийся")""")
        cursor.execute("""INSERT INTO applicants VALUES (5, "Зубков", "Роман", "Сергеевич", "М", "2005-04-09", "г. Батайск", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
        cursor.execute("""INSERT INTO applicants VALUES (6, "Пермяков", "Руслан", "Денисович", "М", "2005-03-23", "г. Гуково", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
        cursor.execute("""INSERT INTO applicants VALUES (7, "Путин", "Владимир", "Владимирович", "М", "1952-10-07", "г. Москва", "Номер телефона", "Email", "2021-09-01", "Информатика")""")

        # Заполнение студенческих карточек
        cursor.execute("""INSERT INTO academic_card VALUES (1, "Евгений", "ИС-24", "Разработчик Web-Мультимедийных приложений", 1, 1, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (2, "Максим", "ИС-24", "Разработчик мобильных/десктопных приложений", 3, 1, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (3, "Антон", "ИС-24", "Разработчик Web-Мультимедийных приложений", 4, 1, 2)""")
        cursor.execute("""INSERT INTO academic_card VALUES (4, "Роман", "ИС-24", "Разработчик Web-Мультимедийных приложений", 9, 1, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (5, "Иван", "ИС-24", "Прикладной программист", 10, 2, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (6, "Руслан", "ИС-24", "Разработчик Web-Мультимедийных приложений", 6, 1, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (7, "Никита", "ИС-101", "Связист", 2, 1, 2)""")
        cursor.execute("""INSERT INTO academic_card VALUES (8, "Ян", "ИС-23", "Системный администратор", 6, 3, 2)""")
        cursor.execute("""INSERT INTO academic_card VALUES (9, "Мария", "ИС-101", "Прикладной программист", 8, 6, 3)""")
        cursor.execute("""INSERT INTO academic_card VALUES (10, "Евдокимия", "ИС-21", "Банкир", 2, 1, 4)""")
        cursor.execute("""INSERT INTO academic_card VALUES (11, "Себастьян", "ИС-21", "Информатика", 9, 2, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (12, "Рамальдо", "ИС-101", "Системный администратор", 3, 1, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (13, "Илья", "ИС-124", "Информационные технологии", 15, 1, 2)""")
        cursor.execute("""INSERT INTO academic_card VALUES (14, "Тихон", "ИС-124", "Информационные технологии", 15, 1, 5)""")
        con.commit()

#select (Макс)
# #1 задание
# with sq.connect('dekanat.db') as con:
#     cursor = con.cursor()
#     print("ЗАДАНИЕ 1")
#     print("Список всех студентов с номером группы:")
#     grsts = cursor.execute("""SELECT student_name, group_name FROM academic_card""")
#     for grst in grsts:
#         print(grst)

#     #2 задание не делаю, не имею понятия, как делать

#     print("-------------------------------------")

#     #3 задание не делаю, не имею понятия, как делать

#     #4 задание
#     print("ЗАДАНИЕ 4")
#     print("Количество часов:")
#     for i in cursor.execute("""SELECT lec_hours, pract_hours, lab_hours, name FROM curriculum INNER JOIN subject ON curriculum.subject_id = subject.id"""):
#         print(i)

#     print("-------------------------------------")

#     #5 задание
#     print("ЗАДАНИЕ 5")
#     print("Студенты с оценкой меньше 4:")
#     for i in cursor.execute("""SELECT student_name FROM academic_card WHERE grade < 4"""):
#         print(i)

#     #6 задание не делаю, нет курсов
#     #7 задание
#     print("-------------------------------------")
#     print("ЗАДАНИЕ 7")
#     print("Студенты, которые сдают курсовую:")
#     for i in cursor.execute("""SELECT student_name FROM academic_card INNER JOIN subject ON academic_card.subject_id = subject.id INNER JOIN curriculum ON subject.id = curriculum.subject_id WHERE course_work = 1"""):
#         print(i)
#     print("-------------------------------------")
#     #8 задание
#     print("ЗАДАНИЕ 8")
#     print("Абитуриенты зачисленные на специальность \"Информатика и вычислительная техника\":")
#     for i in cursor.execute("""SELECT student_name FROM academic_card WHERE specialty_name = 12"""):
#         print(i)

#     print("-------------------------------------")
#     #9 задание
#     print("ЗАДАНИЕ 9")
#     print("Предметы, которые изучают студенты группы 101")
#     for i in cursor.execute("""SELECT name FROM academic_card INNER JOIN subject ON academic_card.subject_id = subject.id WHERE group_name = 'ИС-101'"""):
#         print(i)

#     #10 задание не делаю, не имею понятия, как делать


# # UPDATE (ЖЕНЯ)
# with sq.connect('./dekanat.db') as con:
#     cursor = con.cursor()

#     cursor.execute("""UPDATE facults SET name = 'Новый факультет' WHERE id = 1""") # 1
#     cursor.execute("""UPDATE departments SET name = 'Новая кафедра' WHERE id = 2""") # 2
#     cursor.execute("""UPDATE spec SET name = 'Новая специальность' WHERE id = 3""") # 3
#     cursor.execute("""UPDATE subject SET name = 'Новый предмет' WHERE id = 4""") # 4
#     cursor.execute("""UPDATE sub_form SET name = 'Новая форма сдачи' WHERE id = 6""") # 5
#     cursor.execute("""UPDATE curriculum SET lec_hours = 30 WHERE id = 6""") # 6
#     cursor.execute("""UPDATE curriculum SET lec_hours = 30 WHERE id = 8""") # 7
#     cursor.execute("""UPDATE curriculum SET lab_hours = 30 WHERE id = 4""") # 8
#     cursor.execute("""UPDATE curriculum SET lec_hours = 30, pract_hours = 20 WHERE id = 7""") # 9
#     cursor.execute("""UPDATE curriculum SET lec_hours = 20 WHERE lec_hours > 30""") # 10

#     id = input('Введите идентификатор: ')
#     newName = input('Введите новое имя: ')

#     cursor.execute(f"""UPDATE applicants SET name = '{newName}' WHERE id = {id}""") # 11
#     cursor.execute("""UPDATE departments SET name = 'Другое имя кафедры' WHERE id = 1""") # 12

#     student_id = input('Введите идентификатор: ')
#     newGrade = input('Введите новую оценку: ')

#     cursor.execute(f"""UPDATE academic_card SET grade = {newGrade} WHERE id = {student_id}""") # 13
#     cursor.execute("""UPDATE applicants SET speciality = 'Другая специальность' WHERE speciality = 'Разработчик мобильных/десктопных приложений'""") # 14 сделал без INNER JOIN не через id, а через имя специальности
#     cursor.execute("""UPDATE academic_card SET grade = 5 WHERE student_name = 'Иван'""")
#     cursor.execute("""UPDATE facults SET name = 'Другой факультет' where id = 1""") # 15
#     cursor.execute("""UPDATE curriculum SET lab_hours = 30 where id = 14""") # 16


#DELETE (РУСЛАНУС)

with sq.connect('dekanat.db') as con:
    cursor = con.cursor()

    # cursor.execute("""DELETE FROM applicants WHERE receipt_date < '2020-01-01'""") #1

    # cursor.execute("""SELECT DISTINCT id_departments FROM spec""")
    # spec = cursor.fetchall()
    # spec_ids = [s[0] for s in spec]
    # cursor.execute(f"DELETE FROM curriculum WHERE spec_id NOT IN ({','.join('?' * len(spec_ids))})", spec_ids) #2

    # cursor.execute("""SELECT DISTINCT id FROM facults""")
    # facults = cursor.fetchall()
    # facults_ids = [s[0] for s in facults]
    # cursor.execute(f"DELETE FROM departments WHERE id_facults NOT IN ({','.join('?' * len(facults_ids))})", facults_ids) #3

    # cursor.execute("""SELECT DISTINCT subject_id FROM curriculum""")
    # sub_id = cursor.fetchall()
    # sub_ids = [s[0] for s in sub_id]
    # cursor.execute(f"DELETE FROM subject WHERE id NOT IN ({','.join('?' * len(sub_ids))})", sub_ids) #4

    # cursor.execute("""DELETE FROM academic_card WHERE grade = null""") #5

    # cursor.execute("""DELETE FROM academic_card WHERE exam_form_id = 2""") #6

    # cursor.execute("""DELETE FROM academic_card WHERE facult = 'Информационные технологии'""") #7

    # cursor.execute("""DELETE FROM academic_card WHERE exam_form_id = null""") #8

    # cursor.execute("""SELECT DISTINCT specialty_name FROM academic_card""")
    # academic_card = cursor.fetchall()
    # academic_card_specs = [s[0] for s in academic_card]
    # cursor.execute(f"DELETE FROM applicants WHERE speciality NOT IN ({','.join('?' * len(academic_card_specs))})", academic_card_specs) #9

    # for value in cursor.execute("""SELECT * FROM applicants"""):
    #     print(value)



    #DELETE (Антонус)

    # cursor.execute("""DELETE FROM academic_card WHERE subject_id NOT IN 
    # (SELECT subject_id FROM curriculum WHERE spec_id = 1 );""") #10

    # cursor.execute("""DELETE FROM applicants WHERE id IN 
    # (SELECT id FROM academic_card WHERE subject_id = 1);""") #11

    # cursor.execute("""""") #12 - inner join

    # cursor.execute("""DELETE FROM academic_card WHERE exam_form_id = 1;""") #13

    # cursor.execute("""""") #14 - inner join

    # cursor.execute("""DELETE FROM applicants WHERE speciality = 'Информатика';""") 
    # cursor.execute("""DELETE FROM academic_card WHERE specialty_name = 'Информатика';""") #15

    # cursor.execute("""DELETE FROM academic_card
    #                 WHERE specialty_name = 'Информационные технологии'
    #                 AND subject_id = 15
    #                 AND grade < (SELECT grade FROM academic_card
    #                             WHERE specialty_name = 'Информационные технологии'
    #                             AND subject_id = 15
    #                             ORDER BY grade DESC LIMIT 1)""") #16

    # cursor.execute("""""") #17 - без понятия как сделать