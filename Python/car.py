class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        print(speed)
        print(color)


ford = Car(200,'red')
honda = Car(220,'blue')
audi = Car(250,'green')

#with pass we can add attributes on the fly



print(ford.speed)
print(ford.color)

