# 스택 전체 구현

# 전역변수 선언
SIZE = 0
stack = []
top = -1

# 스택이 꽉 찼는지 여부확인
def isStackFull():
    global SIZE, stack, top

    if (top >= SIZE-1):
        return True
    else:
        return False

# 스택이 비었는지 여부확인
def isStackEmpty():
    global SIZE, stack, top

    if (top == -1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print('Stack is Full')
    else:
        top += 1
        stack[top] = data

# 스택에서 데이터 추출
def pop():
    global SIZE, stack, top
    if(isStackEmpty()):
        print('Stack is Empty')
        return None
    else:
        data =  stack[top]
        stack[top] = None
        top -= 1
        return data

# top의 데이터 확인
def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is Empty')
        return None
    else:
        return stack[top]

'''
if __name__ == '__main__':
    SIZE = int(input('스택사이즈 입력 > '))
    stack = [None for _ in range(SIZE)]

    while True:
        select = input('삽입(I) / 추출(E) / 확인(V) / 종료(X) >> ')
        if select.lower() == 'x':
            break
        elif select.lower() == 'i':
            data = input('추가할 데이터 >> ')
            push(data)
            print(f'스택상태 : {stack}')
        elif select.lower() == 'e':
            data = pop()
            print(f'추출데이터 : {data}')
            print(f'스택상태 : {stack}')
        elif select.lower() == 'v':
            data = peek()
            print(f'확인데이터 : {data}')
            print(f'스택상태 : {stack}')
        else:
            continue

    print('스택 프로그램 종료')

'''
