#Note: Python will automatically pass the object as the first parameter. This is commonly known as self.
    # Self refers to current object, when Instantiation takes place.

class Student():
    # characteristics / data / variables / attributes
    # student_name = 'Aaeron'
    # student_email = 'AeronV@gmail.com' # These two variables are at class level and can be accessed throghout the class.

    def __init__(self, student_name, student_email):
        # print(student_name)
        # print(student_email)
        self.student_name = student_name
        self.student_email = student_email # These both are known as instance variable

    def infoy(self): # Known as instance method, as the first parameter is self. Can access both instance and class variables. Calling is done using object --> object.method()
        print(f'Student Name: {self.student_name}, Student Email: {self.student_email}')
    # def info(self):
    #     print(self.student_name, self.student_email)

    # def infox(Student):
    #     print(Student.student_name, Student.student_email)

S_Object = Student() # -> Known as Instantiation, and S-Object is the object for the class Student() in this case.
# self refers to the current class Student()
S_Object.info()
S_Object.infox()
# because self refers to the current class, S_Object.info() and S_Object.infox() perform the same functionality.

# __init__ is a constructor, special method in python. It will automatically run, when a new object is created.
    # It is used to initialise the objects data.

StudentOne = Student("Aeron Veyra", "aeronv@gmail.com") #The function doesn't have to be called like S_Object.info(). It
    # will automatically run because of the constructor. It is useful for making objects specific.

S1 = Student('Aaeron Veyra', 'aeronv@gmail.com')
S2 = Student('Veckunar', 'veckunar@gmail.com')
S3 = Student('Varshith', 'varshith@gmail.com')

S1.infoy()
S2.infoy()
S3.infoy()

# Instance Varibles (IV) belong to the object. IVs are defined inside the __init__ methods using self keyword.
# Each object had its own copy of Instance variable. Accessing Instance variables is done using self.variable 

#Class Variables: Variables that are shared data or same for all the methods within the class or for all objects.
# Accessing ClassName.variable -> Object can be used to access Class variables, but it is usually more complicated and not preffered.
    # Updating the variables' values will update the class variable used by objects.
    # Memory Efficiency.

#Class Methods:
    # Methods defined inside class, that will operate on class variables, not so commonly used.
    # These are bound to class, not objects.
    # NOTE: For class methods, we generally use (cls as first parameter)
    # NOTE: @classmethod decorator is used
