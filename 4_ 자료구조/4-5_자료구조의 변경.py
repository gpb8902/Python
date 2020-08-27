menu = {"캡틴 아메리카노", "카키푸치노", "에스익스프레소", "아야어여오요우유", "바나나라떼는 말이야", "딸기라떼는 말이야", "초코라떼는 말이야", "NoseNose아"} #menu가 캡틴 아메리카노...로 출력된다.
print(menu) #캡틴 아메리카노...가 출력된다.
print(menu, type(menu)) #set인 상태로 출력된다.

menu = list(menu) #menu를 list상태로 전환한다.
print(menu, type(menu)) #list인 상태로 출력된다.

menu = tuple(menu) #menu를 tuple상태로 전환한다.
print(menu, type(menu)) #tuple인 상태로 출력된다.
#set:중괄호, list:대괄호, tuple:소괄호