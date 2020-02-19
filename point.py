# Створити клас "Точка" (Point), який складається з двох полів типу int: X та Y. Необхідно забезпечити: 

# Введення координат точки користувачем 
# Вивід інформації про точку на екран 
# Можливість зміни будь-якої з координат на запит користувача (X або Y) 

x = 0
y = 0
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_info(self):
        print("Координата точки по вісі 'X': ", self.x,
              "\nКоордината точки по вісі 'Y': ", self.y)
              


while True:
    print(""" 
    -------------------MENU---------------------
    1. Enter coordinate "X"
    2. Enter coordinate "Y"
    3. Show coordinate your point
    0. Exit
    """)          
    try:
        menu = int(input("Enter number: "))
        if menu == 1:
            print("Enter coordinate 'X': ")
            x = int(input())
        elif menu == 2:
            print("Enter coordinate 'Y': ")
            y = int(input())
        elif menu == 3:
            new_point = Point(x, y)
            new_point.show_info()
        elif menu == 0:
            print("Bye!")
            break
    except Exception as err:
        print("Error -> ", err)             