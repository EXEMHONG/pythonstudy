'''
    주소록 프로그램 만들기
    김조은,010-1234-1234, 인천시 부평구
    
    [기능]
    1. 새로운 주소 등록하기
    2. 기존 주소 삭제하기
    3. 기존 주소 수정하기
    4. 기존 주소 검색하기
    5. 전체 주소 출력하기
    6. 주소록 정보를 파일로 관리하기
    
    [객체]
    📗 AddressBook - 주소록
    🙂 Person      - 사람
    
    
    [주소록 정보]
    😁 AddressBook.csv 파일로 관리
    🎨 이름, 전화번호, 주소 정보를 저장
    
    [함수]
    file_reader()           : AddressBook.csv 파일 읽기
    file_generator()        : AddressBook.csv 파일 생성
    menu()                  : 메뉴 소개 및 입력
    exit()                  : 프로그램 종료
    run()                   : 프로그램 실행
    insert()                : 추가
    update()                : 수정
    search()                : 검색
    print_all()                : 전체 출력
    
    __init__()              : 생성자 - 주소록 리스트, 파일객체 초기화
    
'''


# 사람 : persion 클래스
# 💚 생성자
#   - 변수 : name, phone, addr
# 💚 메소드
#   - info()
#       : 이름, 전화번호, 주소를 문자열 템플릿으로 출력하는 기능

# 주소록 : AddressBook 클래스
# 💚 변수 : 주소록 리스트 - address_list
# 💚 생성자
# 💚  함수


# 주소록 : AddressBook 클래스
# ✅ 변수 : 주소록 리스트 - address_list
# ✅ 생성자
# ✅ 메소드
#     - file_reader()           : AddressBook.csv 파일 읽기
#     - file_generator()        : AddressBook.csv 파일 생성
#     - menu()                  : 메뉴 소개 및 입력
#     - exit()                  : 프로그램 종료
#     - run()                   : 프로그램 실행
#     - insert()                : 추가
#     - update()                : 수정
#     - search()                : 검색
#     - print_all()             : 전체 출력



#---------------------------------------------------------------------------------------------------

import csv                    # ctrl + . (quick path)

class Person:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

class AddressBook:
    def __init__(self):
        self.address_list = []  # 주소록 리스트
        self.file_name = 'D:\python/AddressBook.csv'  # 주소록 파일명

    def file_reader(self):
        """AddressBook.csv 파일을 읽어서 주소록에 추가하는 메서드"""
        try:
            with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, phone_number, address = row
                    person = Person(name, phone_number, address)
                    self.address_list.append(person)
            print("주소록 파일을 성공적으로 읽었습니다.")
        except FileNotFoundError:
            print("주소록 파일이 존재하지 않습니다.")
    
    def file_generator(self):
        """샘플 주소록을 생성하여 AddressBook.csv 파일로 저장하는 메서드"""
        sample_address_list = [
            ['김조은', '010-1234-1234', '인천시 부평구']
        ]
        try:
            with open(self.file_name, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for person in sample_address_list:
                    writer.writerow(person)
            print("샘플 주소록 파일을 생성하였습니다.")
        except Exception as e:
            print("주소록 파일 생성 중 오류가 발생하였습니다:", e)

    def menu(self):
        """메뉴를 소개하고 사용자 입력을 받는 메서드"""
        print("===== 주소록 프로그램 메뉴 =====")
        print("1. 새로운 주소 등록하기")
        print("2. 기존 주소 삭제하기")
        print("3. 기존 주소 수정하기")
        print("4. 기존 주소 검색하기")
        print("5. 전체 주소 출력하기")
        print("6. 주소록 정보를 파일로 관리하기")
        print("7. 종료")
        choice = input("메뉴를 선택하세요: ")
        return choice
    
    def exit(self):
        """프로그램 종료 메서드"""
        print("프로그램을 종료합니다.")
        exit()
    
    def run(self):
        """프로그램 실행 메서드"""
        self.file_reader()  # 주소록 파일 읽기
        while True:
            choice = self.menu()  # 메뉴 표시
            if choice == '1':
                self.insert()  # 추가
            elif choice == '2':
                self.delete()  # 삭제
            elif choice == '3':
                self.update()  # 수정
            elif choice == '4':
                self.search()  # 검색
            elif choice == '5':
                self.print_all()  # 전체 출력
            elif choice == '6':
                self.file_generator()  # 파일로 저장
            elif choice == '7':
                self.exit()  # 종료
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")
    
    def insert(self):
        """주소록에 새로운 연락처를 추가하는 메서드"""
        name = input("이름을 입력하세요: ")
        phone_number = input("전화번호를 입력하세요: ")
        address = input("주소를 입력하세요: ")
        person = Person(name, phone_number, address)
        self.address_list.append(person)
        print(f"{name} 님의 연락처가 추가되었습니다.")
    
    def delete(self):
        """주소록에서 기존 연락처를 삭제하는 메서드"""
        name = input("삭제할 연락처의 이름을 입력하세요: ")
        for person in self.address_list:
            if person.name == name:
                self.address_list.remove(person)
                print(f"{name} 님의 연락처가 삭제되었습니다.")
                return
        print(f"{name} 님의 연락처가 주소록에 없습니다.")
        
    def search(self):
        """주소록에서 기존 연락처를 검색하는 메서드"""
        name = input("검색할 연락처의 이름을 입력하세요: ")
        for person in self.address_list:
            if person.name == name:
                print(f"이름: {person.name}, 전화번호: {person.phone_number}, 주소: {person.address}")
                return
        print(f"{name} 님의 연락처가 주소록에 없습니다.")
    
    def print_all(self):
        """주소록에 있는 모든 연락처를 출력하는 메서드"""
        if self.address_list:
            print("===== 주소록 =====")
            for person in self.address_list:
                print(f"이름: {person.name}, 전화번호: {person.phone_number}, 주소: {person.address}")
        else:
            print("주소록에 연락처가 없습니다.")

# 프로그램 실행
if __name__ == "__main__":
    address_book = AddressBook()
    address_book.run()