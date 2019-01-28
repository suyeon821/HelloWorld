#팰린드롬인지 아닌지 판별하는 함수 짜기 C언어를 python으로 바꿔라
# 01. 앞에서 읽으나 뒤에서 읽으나 같은 'Palindrome' 문자열인지를 식별하는 함수를 만드시오.

def is_palindrome(string):
#[input] string
#[output] boolean
    for i in range(len(string)):
        if(string[i] == string[-i]):
            return True
        else :
            return False

print(is_palindrome('ada'))

def is_palindrome2(string):
    string2 = string
    string2.reverse()
    return string == string2

def is_palindrome3(string):
    return string == string[::-1]

    
# arr= [1,2,3,4,5]
# arr[::2] = [1,3,5]
# arr[::-1] = [5,4,3,2,1]

def is_palindrome4(string):
    length = len(string)
    for index, value in enumerate(string):  #인덕스와 값을 저장시켜줌
        if(string[index]==string[-index]):
            return True

print(is_palindrome4('ada'))

#2,3번이 제일 이상적! 파이썬의 함수를 잘 사용해라.


#02. array에서 근접 두개의 원소를 뽑아서 만들 수 있는 제일 큰 값을 리턴하시오.

def adjacentElementsProduct(inputArray):
# [input] array
# [output] integer
   
    array=[1,5,8,3,2,7]
    for i in range(len(array)): 
        if(i<len(array)):
            array[i]*array[i+1]

def adjacentElementsProduct2(inputArray):
    Array=[1,5,8,3,2,7]
    return max([Array[i] * Array[i+1] for i in range(len(Array)-1)])

#03. 10 미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다. #
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
def method(num):
    hap =0
    for i in range(num):
        if(i%3==0 | i%5==0):
            hap = hap+i
    return hap

print(method(1000))

#04. 정수의 값이 있는 리스트가 있습니다. 오름차순으로 정렬된 리스트로 만들 수 있는 최소한의 이동횟수를 출력하는 함수를 만들어라.

