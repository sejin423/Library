# 순차 탐색 소스코드

def sequential_search(n, target, array):
    # 각 원소를 한개씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 일치할 경우
        if array[i] == target:
            return i + 1 # 현재 위치를 반환
print("생성할 원소 개수를 입력한 다음 한 칸을 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
# 원소의 개수
n = int(input_data[0])
# 찾고자 하는 문자열
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 지정")
array = input().split()

print(sequential_search(n, target, array))
