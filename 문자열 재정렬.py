#  알파벳과 숫자로 구성된 문자열이 입력된다.

first_input = input()

#  입력받은 뒤죽박죽을 숫자끼리, 문자끼리 정렬해야 마지막에 문자 오름차순 숫자더한것, 이렇게 나열할수 있다.

strList = []
number = 0
for a in first_input : # 받은것이 숫자이라면, 혹은 문자라면 둘중에 하나의 방법이 필요한데, 제미나이에게서 문자를 표현하는 법을 배웠다.
  if a.isalpha() :
    strList.append(a)
  else :
    number += int(a)

# 이후 문자열을 정렬하고 문자열 뒤에 숫자를 넣어주면 끝

strList.sort()

strList.append(str(number))

print(strList)
