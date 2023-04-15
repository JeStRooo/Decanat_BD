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
            specialty_name INT NOT NULL, 
            subject_id INT NOT NULL, 
            exam_form_id INT NOT NULL, 
            grade INT NOT NULL, 
            FOREIGN KEY (specialty_name) REFERENCES spec(id),
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


        # Заполнение формы сдачи предметов
        cursor.execute("""INSERT INTO sub_form VALUES (1, "Программирование")""")
        cursor.execute("""INSERT INTO sub_form VALUES (2, "Математика")""")
        cursor.execute("""INSERT INTO sub_form VALUES (3, "Физическая культура")""")

        # Заполнение учебного плана
        cursor.execute("""INSERT INTO curriculum VALUES (1, 1, 1, 1, 30, 20, 10, 1)""") # Для ОАП, Форма сдачи предмета - Программирование
        cursor.execute("""INSERT INTO curriculum VALUES (2, 1, 2, 1, 40, 30, 20, 0)""") # Для БД, Форма сдачи предмета - Программирование
        cursor.execute("""INSERT INTO curriculum VALUES (3, 1, 3, 1, 50, 40, 30, 1)""") # Для Web'а, Форма сдачи предмета - Программирование
        cursor.execute("""INSERT INTO curriculum VALUES (4, 1, 9, 2, 60, 50, 40, 0)""") # Для Дискретки, Форма сдачи предмета - Математика
        cursor.execute("""INSERT INTO curriculum VALUES (5, 1, 10, 2, 70, 40, 30, 1)""") # Для Теории Вероятности, Форма сдачи предмета - Математика
        cursor.execute("""INSERT INTO curriculum VALUES (6, 1, 6, 3, 70, 40, 30, 1)""") # Для Физ-ры, Форма сдачи предмета - Физическая культура
        cursor.execute("""INSERT INTO curriculum VALUES (7, 1, 7, 4, 70, 40, 30, 1)""") # Для Истории, Форма сдачи предмета - Гуманитарные
        cursor.execute("""INSERT INTO curriculum VALUES (8, 1, 8, 4, 70, 40, 30, 1)""") # Для Стандартизации, Форма сдачи предмета - Гуманитарные
        cursor.execute("""INSERT INTO curriculum VALUES (9, 1, 5, 5, 70, 40, 30, 1)""") # Для АПС, Форма сдачи предмета - Сетевые
        cursor.execute("""INSERT INTO curriculum VALUES (10, 1, 4, 5, 70, 40, 30, 1)""") # Для КС, Форма сдачи предмета - Сетевые

        # Заполнение абитуриентов
        cursor.execute("""INSERT INTO applicants VALUES (1, "Кобелев", "Евгений", "Николаевич", "М", "2005-04-21", "г. Ростов-на-Дону", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
        cursor.execute("""INSERT INTO applicants VALUES (2, "Касьянов", "Максим", "Юрьевич", "М", "2005-06-15", "г. Батайск", "Номер телефона", "Email", "2021-09-01", "Разработчик мобильных/десктопных приложений")""")
        cursor.execute("""INSERT INTO applicants VALUES (3, "Кмета", "Антон", "Геннадиевич", "М", "2005-07-22", "г. Красный Сулин", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
        cursor.execute("""INSERT INTO applicants VALUES (4, "Медведев", "Иван", "Юрьевич", "М", "2005-04-08", "г. Азов", "Номер телефона", "Email", "2021-09-01", "Неопределившийся")""")
        cursor.execute("""INSERT INTO applicants VALUES (5, "Зубков", "Роман", "Сергеевич", "М", "2005-04-09", "г. Батайск", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
        cursor.execute("""INSERT INTO applicants VALUES (6, "Пермяков", "Руслан", "Денисович", "М", "2005-03-23", "г. Гуково", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")

        # Заполнение студенческих карточек
        cursor.execute("""INSERT INTO academic_card VALUES (1, "Евгений", "ИС-24", 1, 1, 1, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (2, "Максим", "ИС-24", 2, 3, 1, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (3, "Антон", "ИС-24", 1, 4, 1, 2)""")
        cursor.execute("""INSERT INTO academic_card VALUES (4, "Роман", "ИС-24", 1, 9, 1, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (5, "Иван", "ИС-24", 9, 10, 2, 5)""")
        cursor.execute("""INSERT INTO academic_card VALUES (6, "Руслан", "ИС-24", 1, 6, 1, 2)""")
        con.commit()

#insert (Макс)
#1 задание
with sq.connect('dekanat.db') as con:
    cursor = con.cursor()
    print("ЗАДАНИЕ 1")
    grsts = cursor.execute("""SELECT student_name, group_name FROM academic_card""")
    for grst in grsts:
        print(grst)

    print("-------------------------------------")

    #2 задание
    print("ЗАДАНИЕ 2")
    grsts = cursor.execute("""SELECT specialty_name FROM academic_card""")
    i = 0
    for grst in grsts:
        print(f"Все специальности: {grst}")
        i = i+1
    print(f"Количество студентов на специальности: {i}")

    print("-------------------------------------")

    #3 задание
    print("ЗАДАНИЕ 3")
    grsts = cursor.execute("""SELECT name FROM spec""")
    for grst in grsts:
        print(grst)
        

    print("-------------------------------------")

    #4 задание
    print("ЗАДАНИЕ 4")
    for i in cursor.execute("""SELECT lec_hours, pract_hours, lab_hours, name FROM curriculum INNER JOIN subject ON curriculum.subject_id = subject.id"""):
        print(i)

    print("-------------------------------------")

    #5 задание
    print("ЗАДАНИЕ 5")
    print("студенты с оценкой меньше 4:")
    for i in cursor.execute("""SELECT student_name FROM academic_card WHERE grade < 4"""):
        print(i)