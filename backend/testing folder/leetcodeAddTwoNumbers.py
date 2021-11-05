class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
# def addTwoNumbers(self, l1, l2):
#     pass


def getNum(head:ListNode):
    current = head
    i = 0
    result = 0
    while current != None:
        print('current val: ', current.val)
        result = result + current.val * (10 ** i)
        i = i + 1
        current = current.next
        print(head)
    
    return result


if __name__ == '__main__':
    # l = [1,3,5,7,2]
    # head = ListNode(l[0])
    # current = head
    # for i in range(1, len(l)):
    #     nex = ListNode(l[i])
    #     print(ListNode(l[i]).val)
    #     current.next = nex
    #     current = nex

    # print(getNum(head))

    # inumber = 2356
    # number = str(inumber)
    # head = LinstNode(number[0])
    # current = head
    # for i in range(len(number)- 1):
    #     next = ListNode(number[i+1])
    #     current.next = next
    #     current = next

    # next = listNode[-1]
    # current.ext = next

    input = 321
    num = str(input)
    result = ''
    for i in range(-1, -len(num) -1, -1):
        result = result + num[i]
        print(result)
    print(int(result))





