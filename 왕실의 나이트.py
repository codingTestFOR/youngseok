# 일단 a4 c7 이런식으로 들어오는 값을 좌표값으로 바꾸기

def xycode_changer(ab):
    change = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    x = change[ab[0]]
    y = int(ab[1])
    return (x, y)

input_code = input()
print(xycode_changer(input_code)) # 디버그
xycode = xycode_changer(input_code)

move = [(2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (1, -2)] # 동 남 서 북

result = 0

for loop in move :
  x = xycode[0] + loop[0]
  y = xycode[1] + loop[1]
  if x>=1 and x<=8 and y>=1 and y<=8 :
    result += 1

print(result)
