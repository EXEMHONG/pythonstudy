# 멤버쉽 연산자
# a in c : 컬렉션 c 요소에 a 가 포함되어 있으면 true
# 그렇지 않으면 false

a = [1,2,3]

x = 3 in a
y = 10 in a
z = 100 not in a

print('x : {}'.format(x))
print('y : {}'.format(y))
print('z : {}'.format(z))