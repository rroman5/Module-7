#Roberto Roman
#11-12-2021

#Problem 6
#In this code we will modify the existing code add an additional attribute of
#'type' and 'manufacturer'
#add corresponding methods and print
#modify fullspecs()
class car:
#Here we added the missing attributes which are 'type' and 'manufacturer'
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type        #<------ added type
        self.manufacturer = manufacturer   #<----- added manufacturer

    def get_type(self): #<------ added missing function type
        return self.type

    def get_manufacturer(self):   #<------ added missing function manufacturer
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def fullspecs(self): #Within the fullspecs modified for the additional type and manufacturer
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.type + ' ' + self.manufacturer
#This is where we insert the type of car and brand manufacturer
car1 = car("Hatchback", 2015, "black", "Golf", "volkswagen")
car2 = car("SUV", 2005, "red", "MDX", "Acura")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())


