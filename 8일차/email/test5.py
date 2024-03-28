# 이터레이터 

#방법 1
list = [1, 2, 3, 4, 5]
iter_obj = iter(list)
i = 0
while i < len(list):
    print(next(iter_obj))  # 출력: 1
    i += 1

# 방법2    
iter_obj = iter(list)    
while True:
    next_element = next(iter_obj, None) # 다음요소가 없으면 None
    if next_element is None:
        print('마지막')
        break
    print(next_element)
    
    # 응용
    iter_obj = iter(list)
    while True:
        next_element = next(iter_obj, None)
        if next_element is None:
            break
        else:
            print(next_element, end="")
            if next_element is not None:
                print(',', end = '')
        