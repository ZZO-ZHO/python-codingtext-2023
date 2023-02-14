# 단순 연결리스트 구현
class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

# 전역변수
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

def printNodes(start):
    current = start
    if current == None:
        return

    print(current.data, end = ' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end = ' -> ')

# 노드 추가
def insertNote(findData, insertData):
    global memory, pre, current, head

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node
    return

def deletNode(deleteData):
    global memory, pre, current, head

    if head.data ==deleteData:
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.data
            del(current)
            return

def findNode(findData):
    global memory, pre, current, head

    current = head
    if current.data ==findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    
    return Node()

if __name__ == ' __main__':
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    insertNote('재남','문별')
    printNodes(head)

    insertNote('사나','솔라')
    printNodes(head)

    insertNote('다현','화사')
    printNodes(head)

    print('노드삭제 ----')

    deletNode('화사')
    printNodes(head)
    
    deletNode('지효')
    printNodes(head)

    deletNode('재남')
    printNodes(head)

    print('노드검색 ----')

    result = findNode('정연')
    if result.data != None:
        print('데이터를 찾았습니다.')
    else:
        print('검색한 데이터가 없습니다.')
        

    result = findNode('재남')
    print(result.data)
