class Animal:
    def make_sound(self):
        print("정현이가 소리를 냅니다.")

class Yoon(Animal):
    def make_sound(self):
        print("꿀꿀!")

class Yoon2(Animal):
    def make_sound(self):
        print("개꿀꿀!")

# 부모 클래스의 메서드를 호출
animal = Animal()
animal.make_sound()  # 출력: "정현이가이 소리를 냅니다."

# 자식 클래스의 메서드를 호출
Yoon = Yoon()
YoonS.make_sound()  # 출력: "꿀꿀!"

Yoon2 = Yoon2()
Yoon2.make_sound()  # 출력: "개꿀꿀!"