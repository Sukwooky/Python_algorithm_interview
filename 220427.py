list(map(lambda x : x +10 , [1,2,3]))
[n*2 for n in range(1,10+1) if n % 2 == 1 ] 
a : {key : value for key, value in orignal.items()}

# yield = return for generator
# generator가 여기까지 실행 중이던 값을 내보낸다는 의미 , 리턴 후 함수가 종료되지 않고 끝까지 실행된다. 
# 값 추출을 위해서라면 next()를 사용해보자.

def get_natural_num():
   n = 0 
   while True:
      n += 1
      yield n
   
g = get_natural_num()
for _ in range(0,100):
   print(next(g))
   
# range() 함수의 활용
a = [n for n in range(0,100000)]
b= range(100000)
# b에는 생성해야 한다는 조건이 담겨있어서, 비교적 메모리 차지가 적다. 

#enumerate : 순서가 있는 자료형을 인덱스를 포함한 enumerate 객체가 된다.
a = [1,2,3,2,45,2,5]
list(enumerate(a))
#[(0,1),(1,2),(2,3)... 처럼 객체가 튀어나옴]
for i,v in enumerate(a):
   print(i,v) 
#깔끔하게 뽑을 수 있음 

#몫과 나머지를 같이 구하는 것 
divmod (5,3)

#print에 대한 기술
print(a,b,sep=',')
print(a,end=' ')
print(b)

#list의 원소만 뽑을 때 , join을 사용할 수도 있다 
print(''.join(a))

#about f-format
idx =1
fruit = 'banana'
print(f'{idx +1}: {fruit}')

#pass를 이용하면 나중에 코드를 완성시킬 수도 있다.
class my_class(object):
   def my_function():
      pass

#snake case and clean code
#주석을 영어로 작성하는 연습을 하자.
