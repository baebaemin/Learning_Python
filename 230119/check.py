# from calc import tools

# print(tools.add(1, 2))
# print(tools.sub(3, 2))
# 코드가 복잡해지면 이 방법이 좀 더 좋을수도 ! 
# 어떤 모듈에서의 함수인지 명시하고 있기 때문

from calc.tools import add, sub
# calc 폴더 안의 tools.py 에서 add와 sub 함수를 가져와
# calc 안에는 '__init__.py', 'tools.py' 있어야 함

print(add(1, 3), sub(39, 2))