N = 5
queue = [None] * N
#큐의 현재 맨 앞요소와 맨 뒷요소의 인덱스를 가지고 있는 변수
# front : 맨 앞요소의 -1 인덱스,
# rear : 맨 뒷요소의 인덱스
front = rear = -1
# is_empty() : 큐가 비었는지 확인하는 함수,
def is_empty(): # 큐가 비었으면 True를 반환 아니라면 False 반환
    # front랑 rear랑 같으면 비어있는거
    if front == rear:
        return True
    return False
# is_full()  : 큐가 가득 찼는지 확인하는 함수
def is_full():  #
    #선형 큐에서 full이란, rear가 queue마지막 인덱스를 가리키고 있을때
    if rear == N-1:
        return True
    return False
# enQueue(data) 큐의 맨뒤에 data 삽입
def enQueue(data):
    global rear
    if not is_full():
        rear += 1
        queue[rear] = data
    else:
        raise IndexError('큐가 가득 찼습니다.')
# deQueue() 큐의 맨 앞에서 데이터 반환 및 삭제
def deQueue():
    global front
    if not is_empty():
        front += 1
        return queue[front]
    else:
        raise IndexError('큐가 비었습니다.')

enQueue('A')
print(deQueue())
enQueue('A')
print(deQueue())
enQueue('A')
print(deQueue())
enQueue('A')
print(deQueue())
enQueue('A')
print(deQueue())
enQueue('A')
print(deQueue())
enQueue('A')
print(deQueue())
enQueue('A')
print(deQueue())













