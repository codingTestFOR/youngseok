n = int(input())
plans = input().split()

# 계획서 L R U D]
x = 1 # 초기값
y = 1
directions = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1] # 방향값을 반복시켜 문자와 숫자를 일치
dy = [-1, 1, 0, 0]

print(">> 디버그", plans)
# 예를들어 디렉션즈가 R R R U D D 라면?

for a in plans:
    for b in range(len(directions)):
        if directions[b] == a:
            ax = x + dx[b] # 바로 x에 대입하지않고 ax라는 변수값을 만든것은 예외처리를 하고 남은 ax만 x에 대입하기위해
            ay = y + dy[b]
    if ax < 1 or ay < 1 or ax > n or ay > n:
        continue
    x = ax
    y = ay

print(x,y)
