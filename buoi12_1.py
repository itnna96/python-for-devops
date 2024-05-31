class Car():
    
    def __init__(self,color="red",year=1800,speed=0) -> None:
        if color == "green" and year < 2015:
            raise Exception("Green car must be 2015 or older") #xảy ra khi cả 2 điều kiện cùng đúng
        self.color = color
        self.year = year
        self.speed = speed

car1 = Car(color="red",year= 2016)
print(car1.color,car1.year,car1.speed)
