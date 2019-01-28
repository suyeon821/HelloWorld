import math
## import만 해서는  모듈인지 패키지인지 확인할 수 없음
#일단 모듈이라고 생각하자

##패키지란 무엇인가? 여러개의 모듈이 모인 집합.
#패키지를 잘 사용하는 방법을 익혀라
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result = self.result = num
        return self.result

    def mul(self, num):
        self.result=num
        return self.result

    def div(self, num):
        self.result /= num
        return self.result

    def floor(self):
        self.result = math.floor(self.result)   ##소수점을 잘라주는 가우스 함수
        return self.result

    def print_result(self):
        print(self.result)
        return

call = Calculator() #클래스를 통해서 인스턴스를 만들어주는 과정.
call.add(3)
call.print_result()

class Human:    #객체
    def __init__(self):
        self.name = '이름없음'
        self.age = 0
        self.major = '전공없음'

    def set_name(self, name):
        self.name = name

    def get_name(self): #메소드 methond
        print(self.name)
        return self.name

kjh = Human()   #Human은 클래스(붕어빵틀), kjh는 인스턴스(붕어빵).
#kjh는 Human 클래스로 생성된 하나의 인스턴스다.
kjh.get_name()
kjh.set_name('김지형')
kjh.get_name()

ysy = Human()
ysy.get_name()
ysy.set_name('임수연')
ysy.get_name()
# C언어까지는 순차적인 코드라고 해서 이거 다음에 이거 이거 다음에 이거라 클래스라는 개념이 없음.
#객체 지향 프로그래밍에서 나오는 개념.


#예외처리

#프로그래머는 내가 항상 실수를 한 수 있다는 걸 생각하고 예외처리를 해줘야한다~
#c언어의 try catch가 파이썬에서는 try except
#try안에 있는 코드가 조금이라도 오류가 나면 바로 except로 넘어간다.


try:

    a=[1,2]

    a[3]=3
    print(a[3])
except ZeroDivisionError  as e:
    print('0으로 나눴다')
except IndexError:
    print('해당 리스트에 내용이 없습니다.')
finally:    #마지막에 나오는 내용
    print('??')


