'''Author: Ellyn Hindle
File Name: listsfunctionsclasses
Purpose: accept user input for a car and car info, then output info in accessible format for user'''

class Vehicle():
    def __init__(self, vtype):
        self.vtype = vtype


class Automobile(Vehicle):
    def __init__(self, vtype, year, make, model, doors, roof):
        super().__init__(vtype)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def __str__(self):
        return f"Vehicle type: {self.vtype}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of Doors: {self.doors}\nType of Roof: {self.roof}"

def vehicleinput():
    testvehicle = Automobile("car","toyota","2011","corolla","2","sunroof")
    print(testvehicle)
    operateloop = input("Start program? Y/N\n")
    while operateloop == "Y":
        itype = input("What type of vehicle do you have?\nWrite car, truck, plane, boat, or broomstick.\n")
        userVehicle = Vehicle(itype)
        if operateloop != "N":
            iyear = input("What year is the car?\n")
            imake = input("What is the make of the car?\n")
            imodel = input("What is the model of the car?\n")
            idoors = input("How many doors does the car have (2 or 4)?\n")
            iroof = input("What type of roof does the car have (solid or sunroof)?\n")
            autoInfo = Automobile(userVehicle.vtype, iyear, imake, imodel, idoors, iroof)
            print(autoInfo)  
            operateloop = ("Input another vehicle? Y/N")      
        else:
            break
    print("Ending input.")    
    return    


def main():
    print("Welcome to the vehicle information collector.")
    print("At this time, only cars are supported.")
    vehicleinput()
    return



if __name__ == "__main__":
    main()