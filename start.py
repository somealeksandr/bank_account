# class Person:
#     # name = "Bill"
#     def show_Person(self):
#         print("Hello,", self.name)

# Bill = Person()
# Bill.show_Person()
# Tom = Person()
# Tom.show_Person()
# Tom.name = "Tom"
# Tom.show_Person()

# class Person:
#     def __init__(self, name):
#         self.__name = name
#         print("Person constructor", self.__name)
#     def __del__(self):
#         print("Person destructor", self.__name)    
#     def __show_Person(self):
#         print("Hello,", self.__name)
      
# Jack = Person("Jack")
# Jack.__show_Person()
# Bobik = Person("Bobik")
# Bobik.__show_Person()


class Person:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        if self.__name == new_name:
            print("The same name")
        else:
            self.__name = new_name
                   

Bill = Person("Bill")
Bill.set_name("Bill2")
print(Bill.get_name())