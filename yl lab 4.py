#problem 1
class rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2
rect1 = rectangle(5 , 6)
print(rect1.perimeter())

class person(object):
    def __init__(self,name,age,city,gender,favorite_brakefast,favorite_song):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
        self.favorite_brakefast = favorite_brakefast
        self.favorite_song = favorite_song
        
    def eat_fav(self):
        print(self.name + " is eating " + self.favorite_brakefast)

    def play_fav_song(self):
        print(self.name +  " is playing " + self.favorite_song + ", which is his favorite song")
    
guy1 = person('tal', 15, 'haifa', 'male', 'pancakes', 'bohemian raphsody')
print(guy1.play_fav_song())
