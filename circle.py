#A Circle instance accepts attribute radius (r)
#It has a method area that returns the area (A) of the circle using the formula A=πr2
#It has a method to calculate circumference (c) using the formula C=2πr


class Circle:
  def __init__(self,radius):
    self.radius = radius

    def areaof_circle(self):
      total = self.radius*self.radius
      pie = 3.14
      area = total*pie
      return area

    def circumference(self):
       pie = 3.14
       circum = self.radius*pie*2
       return circum 
      
#A Square instance accepts the attribute side (a)
#It has method area that returns the area (A) of the square using the formula A=a2
#It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square:
    def __init__(self,height,width):
        self.height = height
        self.width = width


    def area_of_square(self):
        total = self.height*self.width
        return total

    def perimeter_of_square(self): 
        total = self.width*4   
        return total

#A Rectangle instance accepts two sides of a rectangle (w,l)
#It has method to calculate the area (A) of the rectangle using the formula A=wl
#It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length


    def area_of_rectangle(self):
        total = self.length*self.width
        return total

    def perimeter_of_rectangle(self):
        total = self.width+self.length*2
        return total    

#A Sphere Instance accepts the radius of the sphere (r)
#It has a method to calculate the surface area (A) using the formula A=4πr2
#It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere:
    def __init__(self,radius):
     self.radius = radius

    def areaof_sphere(self):
      total = self.radius*self.radius
      pie = 3.14
      area = total*pie*4
      return area

    def circumfrence(self):
       pie = 3.14
       circum = self.radius*pie*3
       return circum 
   