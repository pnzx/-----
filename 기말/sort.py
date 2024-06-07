import random
import time
import sys
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic' #한글 깨짐 방지
sys.setrecursionlimit(999999999)

# 선택정렬 (Selection Sort)
def selection_sort(arr):
    n = len(arr)  # 배열의 길이를 변수 n에 저장
    for i in range(n):  # 배열의 각 요소에 대해 반복
        min_idx = i  # 현재 위치를 최소값의 인덱스로 설정
        for j in range(i+1, n):  # 현재 위치 이후의 요소들에 대해 반복
            if arr[j] < arr[min_idx]:  # 현재 위치의 값이 최소값보다 작다면
                min_idx = j  # 최소값의 인덱스를 업데이트
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 현재 위치와 최소값의 위치를 교환
    return arr  # 정렬된 배열을 반환

# 버블정렬 (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)  # 배열의 길이를 변수 n에 저장
    for i in range(n):  # 배열의 각 요소에 대해 반복
        for j in range(0, n-i-1):  # 마지막 i개의 요소는 이미 정렬되었으므로 반복에서 제외
            if arr[j] > arr[j+1]:  # 현재 위치의 값이 다음 위치의 값보다 크다면
                arr[j], arr[j+1] = arr[j+1], arr[j]  # 두 값을 교환
    return arr  # 정렬된 배열을 반환

# 삽입정렬 (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):  # 배열의 두 번째 요소부터 시작하여 각 요소에 대해 반복
        key = arr[i]  # 현재 요소를 변수 key에 저장
        j = i-1  # 현재 요소의 이전 위치부터 시작
        while j >= 0 and key < arr[j]:  # key가 arr[j]보다 작으면
            arr[j+1] = arr[j]  # arr[j]를 오른쪽으로 이동
            j -= 1  # j를 1 감소
        arr[j+1] = key  # key를 올바른 위치에 삽입
    return arr  # 정렬된 배열을 반환

# 병합정렬 (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:  # 배열의 길이가 1보다 크면
        mid = len(arr) // 2  # 배열을 두 부분으로 나누기 위한 중간 인덱스 계산
        left_half = arr[:mid]  # 왼쪽 절반 배열 생성
        right_half = arr[mid:]  # 오른쪽 절반 배열 생성

        merge_sort(left_half)  # 왼쪽 절반을 재귀적으로 정렬
        merge_sort(right_half)  # 오른쪽 절반을 재귀적으로 정렬

        i = j = k = 0  # 왼쪽 절반, 오른쪽 절반, 전체 배열의 인덱스 초기화

        while i < len(left_half) and j < len(right_half):  # 왼쪽 절반과 오른쪽 절반을 병합
            if left_half[i] < right_half[j]:  # 왼쪽 절반의 현재 요소가 작으면
                arr[k] = left_half[i]  # 전체 배열에 왼쪽 절반의 요소를 추가
                i += 1  # 왼쪽 절반의 인덱스를 증가
            else:
                arr[k] = right_half[j]  # 전체 배열에 오른쪽 절반의 요소를 추가
                j += 1  # 오른쪽 절반의 인덱스를 증가
            k += 1  # 전체 배열의 인덱스를 증가

        while i < len(left_half):  # 왼쪽 절반에 남은 요소가 있으면
            arr[k] = left_half[i]  # 전체 배열에 추가
            i += 1  # 왼쪽 절반의 인덱스를 증가
            k += 1  # 전체 배열의 인덱스를 증가

        while j < len(right_half):  # 오른쪽 절반에 남은 요소가 있으면
            arr[k] = right_half[j]  # 전체 배열에 추가
            j += 1  # 오른쪽 절반의 인덱스를 증가
            k += 1  # 전체 배열의 인덱스를 증가
    return arr  # 정렬된 배열을 반환

# 퀵정렬 (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:  # 배열의 길이가 1 이하이면
        return arr  # 그대로 반환
    else:
        pivot = arr[len(arr) // 2]  # 중간 요소를 피벗으로 선택
        left = [x for x in arr if x < pivot]  # 피벗보다 작은 요소들로 구성된 배열 생성
        middle = [x for x in arr if x == pivot]  # 피벗과 같은 요소들로 구성된 배열 생성
        right = [x for x in arr if x > pivot]  # 피벗보다 큰 요소들로 구성된 배열 생성
        return quick_sort(left) + middle + quick_sort(right)  # 왼쪽, 중간, 오른쪽 배열을 재귀적으로 정렬하여 병합

# 힙정렬 (Heap Sort)
def heapify(arr, n, i):
    largest = i  # 루트를 가장 큰 값으로 설정
    left = 2 * i + 1  # 왼쪽 자식의 인덱스
    right = 2 * i + 2  # 오른쪽 자식의 인덱스

    if left < n and arr[largest] < arr[left]:  # 왼쪽 자식이 루트보다 크면
        largest = left  # 가장 큰 값을 왼쪽 자식으로 업데이트

    if right < n and arr[largest] < arr[right]:  # 오른쪽 자식이 가장 큰 값보다 크면
        largest = right  # 가장 큰 값을 오른쪽 자식으로 업데이트

    if largest != i:  # 가장 큰 값이 루트가 아니면
        arr[i], arr[largest] = arr[largest], arr[i]  # 루트와 가장 큰 값을 교환
        heapify(arr, n, largest)  # 재귀적으로 힙 구조를 유지

def heap_sort(arr):
    n = len(arr)  # 배열의 길이를 변수 n에 저장
    for i in range(n // 2 - 1, -1, -1):  # 힙 구조를 만들기 위해 배열의 중간부터 시작하여 역순으로 반복
        heapify(arr, n, i)  # 힙 구조를 만듦

    for i in range(n-1, 0, -1):  # 배열의 끝에서 시작하여 루트와 교환
        arr[i], arr[0] = arr[0], arr[i]  # 루트와 현재 위치를 교환
        heapify(arr, i, 0)  # 힙 구조를 재구성
    return arr  # 정렬된 배열을 반환

# 셸정렬 (Shell Sort)
def shell_sort(arr):
    n = len(arr)  # 배열의 길이를 변수 n에 저장
    gap = n // 2  # 초기 갭 크기를 배열의 길이의 절반으로 설정

    while gap > 0:  # 갭 크기가 0보다 클 때까지 반복
        for i in range(gap, n):  # 갭 크기부터 배열의 끝까지 반복
            temp = arr[i]  # 현재 요소를 변수 temp에 저장
            j = i  # 현재 인덱스를 변수 j에 저장
            while j >= gap and arr[j - gap] > temp:  # 갭 크기 이전 요소들이 현재 요소보다 크면
                arr[j] = arr[j - gap]  # 현재 요소를 갭 크기 이전 요소로 대체
                j -= gap  # j를 갭 크기만큼 감소
            arr[j] = temp  # temp를 올바른 위치에 삽입
        gap //= 2  # 갭 크기를 절반으로 감소
    return arr  # 정렬된 배열을 반환

# 계수정렬 (Counting Sort)
def counting_sort(arr):
    max_val = max(arr)  # 입력 배열에서 가장 큰 값 찾기
    counts = [0] * (max_val + 1)  # 각 정수의 등장 횟수를 저장할 배열 초기화

    # 각 정수의 등장 횟수를 세기
    for num in arr:
        counts[num] += 1

    # 누적 합 계산
    for i in range(1, max_val + 1):
        counts[i] += counts[i - 1]

    # 정렬된 배열을 저장할 배열 초기화
    sorted_arr = [0] * len(arr)

    # 입력 배열을 순회하면서 정렬된 배열에 요소 채우기
    for num in reversed(arr):
        sorted_arr[counts[num] - 1] = num
        counts[num] -= 1

    return sorted_arr

# 기수정렬 (Radix Sort)
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 각 자릿수 별로 등장 횟수를 센다
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # 누적합을 구한다
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 정렬한다
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # 결과를 복사
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)  # 입력 배열에서 가장 큰 값 찾기

    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

# 버킷정렬 (Bucket Sort)
# 버킷정렬 (Bucket Sort)
def bucket_sort(arr):
    n = len(arr)
    bucket_size = 10  # 예시로 버킷 크기를 10으로 설정합니다. 실제로는 입력 데이터의 특성에 따라 적절한 크기를 선택해야 합니다.
    
    # 입력 배열의 최대값과 최소값을 찾습니다.
    min_val = min(arr)
    max_val = max(arr)
    
    # 각 버킷을 초기화합니다.
    buckets = [[] for _ in range(bucket_size)]
    
    # 입력 배열의 값에 따라 버킷에 값을 할당합니다.
    for num in arr:
        index = min((num - min_val) // ((max_val - min_val + 1) // bucket_size), bucket_size - 1)  # 각 값에 대한 인덱스 계산
        buckets[index].append(num)
    
    # 각 버킷을 정렬합니다.
    for bucket in buckets:
        bucket.sort()
    
    # 정렬된 버킷을 합쳐서 결과를 반환합니다.
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr




# 랜덤 리스트 생성
A = [random.randint(0, 99) for _ in range(300)]  # 0에서 99까지의 랜덤 숫자 300개를 가지는 리스트 생성

# 정렬 시간 측정 함수
def measure_time(sort_func, arr):
    start_time = time.time()  # 시작 시간 기록
    for _ in range(10000):  # 10,000번 반복하여
        arr_copy = [random.randint(0, 99) for _ in range(300)]  # 매 시행마다 새로운 랜덤 배열 생성
        sort_func(arr_copy)  # 정렬 함수 호출
    end_time = time.time()  # 종료 시간 기록
    return (end_time - start_time) / 10000  # 평균 정렬 시간 계산


# 정렬 함수 리스트
sort_functions = [selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort, shell_sort, counting_sort, radix_sort, bucket_sort]
sort_function_names = ['선택정렬', '버블정렬', '삽입정렬', '병합정렬', '퀵정렬', '힙정렬', '셸정렬', '계수정렬', '기수정렬', '버킷정렬']

# 정렬 시간 측정 및 저장
times = {}
for func, name in zip(sort_functions, sort_function_names):
    times[name] = measure_time(func, A)

# 측정된 시간 출력
print(times)

# 결과를 그래프로 표시
names = list(times.keys())
values = list(times.values())

plt.figure(figsize=(12, 6))
plt.bar(names, values, color='skyblue')
plt.xlabel('정렬 알고리즘')
plt.ylabel('평균 시간 (초)')
plt.title('정렬 알고리즘 성능 비교')
plt.show()