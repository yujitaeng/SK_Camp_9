# # our_class.py 모듈을 가져와서 (import 수문 사용)
# import our_class

# # 선생님 이름과 학생 수를 출력하고
# print(our_class.teacher_name, our_class.student_count)

# # study() 함수와 lecture() 함수를 호출하고
# our_class.study()
# our_class.lecture()

# # 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# menus = ['붕어빵', '호떡', '국화빵', '호빵', '계란빵빵']

# # go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
# print(our_class.go_lunch(menus))

##############################################################################

# # our_class.py 모듈을 가져와서 (from-import 수문 사용)
# from our_class import teacher_name, student_count, study, lecture, go_lunch

# # 선생님 이름과 학생 수를 출력하고
# print(teacher_name, student_count)

# # study() 함수와 lecture() 함수를 호출하고
# study()
# lecture()

# # 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# menus = ['붕어빵', '호떡', '국화빵', '호빵', '계란빵']

# # go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
# print(go_lunch(menus))

##################################################################################

# 3. 패키지 내 모듈 import
import our_class_dir.official.official_module as om
from our_class_dir.unofficial.unofficial_module import study, go_lunch

# 선생님 이름과 학생 수를 출력하고
print(om.teacher_name)
print(om.student_count)

# study() 함수와 lecture() 함수를 호출하고
study()
om.lecture()

# 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
menus = ['붕어빵', '호떡', '국화빵', '호빵', '계란빵']

# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
print(go_lunch(menus))