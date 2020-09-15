# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# recursive
# 이 문제에서는 sorted list라는 점이 중요
# 첫 번째부터 비교하면서 리턴하면 쉽게 풀이 가능



from dataclasses import dataclass
@dataclass
class Solution:
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode):
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2, = l2, l1 #swqp
        if l1:
            l1.next = self.mergeTwoLists2(l1.next, l2)
        return l1



# 사실 (1)의 if문에서는 괄호를 생략해도 동일한 순서로 실행된다
# 가장 우선순위가 높은 것은 비교연산 > 이고 그 다음으로는 not, 그 다음은 and, 그 다음은 or이다
# 명확하게 괄호로 구분해보면
# if (not l1) or (l2 and (l1.val > l2.val))
# 괄호를 모두 제거해도 의도한 순서대로 실행은 되지만
# 괄호가 없을 시 어느 것이 먼저 실행되는지 헷갈린다
# 그리고 or보다 and가 먼저 실행된다는 점은 공부하지 않았다면 알기 어렵다
# 코딩 테스트 시에는 사소한 실행 순서 문제로도 트러블에 빠지게 되면 해결이 매우 어려워짐
# 명확하게 괄호로 처리하는 편이 낫다
# 가장 좋은 것은 연산자의 실행 순서를 분명하게 파악해두는 것!

# explanation
# 1(a)-2-4(c), 1(b)-3-4(d) 두 개의 정렬된 리스트가 있다
# 첫 번째 노드부터 하나씩 비교
# 재귀적 호출임에 유의!
# 순서대로 한 번 적어본다
# step1
# l1 : 1(a), l2 : 1(b)
# (1) if문 만족 x
# l1은 exist, l1.next = mergeTwoLists(l1.next, l2)
# 1(a).next = mergeTwoLists(2, 1)

# step2
# l1: 2, l2: 1(b)
# (1) if문 만족 -> swap
# l1 = l2(1(b)), l2 = l1(2)
# l1 exist, l1.next = mergeTwoLists(l1.next l2)
# 1(b).next = mergeTwoLists(3, 2)

# step3
# l1: 3, l2 : 2
# (1) if문 만족 -> swap
# l1 = l2(2), l2 = l1(3)
# l1 exist, l1.next = mergeTwoLists(l1.next, l2)
# 2.next = mergeTwoLists(4(c), 3)

# step4
# l1: 4(c), l2: 3
# (1) if문 만족 -> swap
# l1 = l2(3), l2 = l1(4(c))
# l1 exist, l1.next = mergeTwoLists(l1.next, l2)
# 3.next = mergeTwoLists(4(d), 4(c))

# step5
# l1: 4(d), l2: 4(c)
# if문 만족 x
# l1 exist, l1.next = mergeTwoLists(l1.next, l2)
# 4(d).next = (none, 4(c))

# step5
# not l1 조건 만족
# l1 = 4(c), l2 = none
# l1.next = mergeTwolists(l1.next, l2)
# 4(c).next = mergeTwoLists(none, none)
# end

# 1(a) - 1(b) - 2 - 3 - 4(d) - 4(c)


