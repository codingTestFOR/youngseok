# 일단 입력받기
n = input()
heroes = list(map(int, input().split()))

# 단순히 생각하면 가장 공포도가 적은 사람으로 가장 적은수로 그룹을 만드는것을 반복하면 최대로 많은 그룹이 떠난다.
# 가장 적은 공포도 부터 다음 적은것까지 계산하려면 오름차순으로 리스트를 정렬하면 된다.
heroes.sort()

result = 0 # 결과값 마지막 그룹수
count = 0 # 현재 세고있는 그룹의 인원수

# for a in heroes; 
#   count += 1 
#   if count = a;
#     result += 1
#     count = 0

print(result)
