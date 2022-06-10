# ---make a function using def
class Robot:
    # <---make constructor para hindi magerror kung typo, use -- __init__--->
    # <---have constructor get three arguments--->
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)
        # self refers to r

 # <---to set the atttributes for--->
 # <---made up 'constructor'--->

# r1 = Robot()
# r1.name = "Tom"
# r1.weight = 30
# r1.color = "red"

# <---to make another object--->

# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

# <-- new contructor__init__-->

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

# <---to run function introduce_self--->

r1.introduce_self()
r2.introduce_self()
