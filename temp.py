class Person:
    # 생성자, dunder(double underscore)
    # 모든 인스턴스들에 변수 생성에 사용
    def __init__(self):
        print('생성자 호출')
        
    # 소멸자
    def __del__(self):
        print('소멸자 호출')
        
p1 = Person()
p2 = Person()