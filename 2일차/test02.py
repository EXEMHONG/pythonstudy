# 컬렉션
# : '모음집'
# 여러 값을 하나의 이름으로 묶어서 관리하는 자료형
# 컬렉션 종류
# 1. 리스트
# 2. 튜플
# 3. 세트 
# 4. 딕셔너리

# 리스트
# : 서로 다른 자료형의 값을 저장
# li = [값1, 값2, .....]
list = [100, 12.34, 'hello']
print ('list : ', 'li')

# 리스트 인덱싱
# 리스트 슬라이싱
list2 = ['월', '화','수', '목', '금']
print ('list2[:5] : ', list2[:5]) 
print ('li2[:5] : ', list2[5:]) 


#요소 추가 및 삭제
# - 요소 추가함수 :     append(), insert()
# - 요소 삭제함수 :      pop()

print('### append() ###')
list3 = [1,2,3,4,5]
print(list3)

list3.append(6)
print(list3)

list3.append(7)
print(list3)

# insert(index, 추가할 요소) : 특정 index 에 요소 추가
print('### index() ###')
list4 = [1,3,5,7,9]
print(list4)

list4 = [1,2]
print(list4)

list4 = [3, 4]
print(list4)


# pop(inex) : 특정 indesx 를 지정하여 삭제
# index를 생략하여 삭제
print('### pop() ###')
print(list4)

list4.pop()
list4.pop()
list4.pop()
list4.pop()
list4.pop()
print(list4)

list4.pop(2)
print(list4)


