# array는 배열 ex) array=[]
# 선택 정렬 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i] # 스와프

#------------------------------------------------------------------------
# 기본 정렬 소스코드
array.sort()

#------------------------------------------------------------------------
# 선택 정렬 소스코드
for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복
        if array[j] < array[j -1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 현 수보다 작은 데이터를 만나면 그자리에서 멈춤
            break

#------------------------------------------------------------------------
# 퀵 정렬 소스코드_직관적
def quick_sort(array, start, end):
    # 원소가 한개인 경우
    if start >= end:
        return
    # 피벗은 첫번째 원소
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽부분과 오른쪽부분에서 각각 정렬 수행
    quick_sort(array, start, left - 1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array) - 1)

# 퀵 정렬_파이썬
def quick_sort(array):
    # 리스트가 하나 이하의 원소를 담고 있다면 종료
    if len(array) <= 1:
        return array
        
    pivot = array[0] # 피벗은 첫번쨰 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
#------------------------------------------------------------------------
# 계수 정렬
# 모든 원소의 값이 0보다 크거나 같다고 가정
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

# 리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
        print(i, end=' ') 
        
#-------------------------------------------------------------------------
# 병합정렬
# (nlogn)수행시간
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    L = merge_sort(arr[:mid]) # 분할
    R = merge_sort(arr[mid:]) # 분할
    mer = []

    i = 0
    j = 0
    while i < len(L) and j < len(R): # 정렬 및 결합
        if (L[i] > R[j]):
            mer.append(R[j])
            j += 1
        else:
            mer.append(L[i])
            i += 1

    if i != len(L):
        mer += L[i:]
    if j != len(R):
        mer += R[j:]
    return mer
