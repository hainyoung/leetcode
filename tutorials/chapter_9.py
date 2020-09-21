# 9장 스택, 큐

# 스택(Stack)과 큐(Queue)는 프로그래밍이라는 개념이 탄생할 때부터 사용된 가장 고정적인 자료구조 중 하나
# 그중 스택은 거의 모든 애플리케이션을 만들 때 사용되는 자료구조
# 스택은 LIFO(Last-In-First-Out), 큐는 FIFO(First-In-Frist-Out)로 처리된다
# 비유하자면,,
# 스택은 쌓여 있는 접시를 생각, 마지막에 쌓은 접시가 맨 위에 놓일 것이고 그 접시가 가장 먼저 꺼내진다
# 큐는 맛집에 서 있는 사람들의 줄을 생각, 가장 먼저 줄 선 사람이 가장 먼저 입장한다

# 파이썬은 스택 자료형을 별도로 제공하지는 않지만, 리스트가 사실상 스택의 모든 연산을 지원
# 큐 또한 마찬가지, 리스트는 큐의 모든 연산을 지원한다
# 다만 리스트는 동적 배열로 구현되어 있어 큐의 연산을 수행하기에는 효율적이지 X
# 따라서 큐를 위해서는 Deque, 데크라는 별도의 자료형을 사용해야 좋은 성능을 낼 수 있다
# 그러나 굳이 성능을 고려하지 않는다면 리스트는 스택과 큐의 모든 연산을 지원하기 때문에
# 사실상 리스트를 잘 사용하기만 해도 충분

# 스택
# stack은 다음의 2가지 주요 연산을 지원하는 요소의 컬렉션으로 사용되는 추상 자료형이다
# push() : 요소를 컬렉션에 추가
# pop() : 아직 제거지되지 않은 가장 최근에 삽입된 요소를 제거

# 연결리스트를 이용해 스택 ADT(추상자료형, Abstract Data Type) 구현

from dataclasses import dataclass
@dataclass
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# 초기화 함수 __init__()에서 노드의 값은 item으로
# 다음 노드를 가리키는 포인터는 next로 정의한다
# 이제 스택의 연산인 push()와 pop()을 담은 Stack Class를 다음과 같이 정의
@dataclass
class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


# push()는 연결리스트에 요소를 추가하면서 가장 마지막 값을 next로 지정하고,
# 포인터인 last는 가장 마지막으로 이동시킨다
# pop()은 가장 마지막 아이템을 끄집어내고
# last 포인터를 한 칸 앞으로 전진시킨다
# 이전에 추가된 값을 가리키게 된다

# 다음과 같이 1부터 5까지 값을 스택에 입력해보자
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# 위를 도식화하면
# None <- 1 <- 2 <- 3 <- 4 < 5(last)

# stack은 각각 "이전의 값"을 가리키는 연결 리스트로 구현!
# pop() 메소드를 통해 스택의 값을 차례대로 출력

for _ in range(5):
    print(stack.pop())

# 5
# 4
# 3
# 2
# 1


