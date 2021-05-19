class Plane:
    def __init__(self,name,speed,wings):
        self.name = name
        self.speed = speed
        self.wings = wings


    def to_fly(self):
        print('flies at speed of: ' , self.speed)
    def get_wing_length(self):
        print('length of wings are: ', self.wings)


class Boeing(Plane):
    def to_fly(self):
        print('passanger flight flies at speed of: ' , self.speed)
    def get_wing_length(self):
        print('length of passanger flight^s wings are: ', self.wings)


me_plane = Plane(
   name = 'cucumber',
   speed = 350,
   wings = 15

)

b747 = Boeing(
    name = 'boeing 747',
    speed = 750,
    wings = 28
)


me_plane.to_fly()
me_plane.get_wing_length()


b747.to_fly()
b747.get_wing_length()