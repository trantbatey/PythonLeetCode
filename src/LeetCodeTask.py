'''
Created on Jan 28, 2019

@author: Trant
'''
from symbol import factor

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def testAddTwoNumbers(self):
        
        l1 = ListNode(2)
        node = l1
        node.next = ListNode(4)
        node = node.next
        node.next = ListNode(3)
        
        l2 = ListNode(5)
        node = l2
        node.next = ListNode(6)
        node = node.next
        node.next = ListNode(4)
        
        l3 = self.addTwoNumbers(l1, l2)
        print(l3.val)
        l3 = l3.next
        print(l3.val)
        l3 = l3.next
        print(l3.val)
        print('')
                
        l3 = self.addTwoNumbers02(l1, l2)
        print(l3.val)
        l3 = l3.next
        print(l3.val)
        l3 = l3.next
        print(l3.val)
    
    
    def addTwoNumbers02(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.build_numbers02(l1)       
        num2 = self.build_numbers02(l2)
        listOut = self.build_list(num1 + num2)
        return listOut
            
    
    # build numbers from reversed linked list
    def build_numbers02(self, list):
        strNum = ''
        while (list != None):
            strNum = str(list.val) + strNum
            list = list.next
        return int(strNum)
    
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.build_numbers(l1)       
        num2 = self.build_numbers(l2)
        listOut = self.build_list(num1 + num2)
        return listOut
            
    
    # build numbers from reversed linked list
    def build_numbers(self, list):
        factor = 1
        num = 0
        while (list != None):
            num += list.val * factor
            factor *= 10
            list = list.next
        return num
            
    
    # build numbers from reversed linked list
    def build_list(self, sum):
        letters = str(sum)
        for i in range (len(letters)-1, -1, -1):
            if (i == len(letters)-1):
                node = ListNode(int(letters[i]))
                listOut = node
            else:
                node.next = ListNode(int(letters[i]))
                node = node.next
            node.next = None

        return listOut
    
class DemoClass:
    num = 101

    # a method
    def read_number(self):
        print(self.num)

        

def main():
    Solution().testAddTwoNumbers()

    # creating object of the class
    obj = DemoClass()
    
    # calling the instance method using the object obj
    obj.read_number()
    
if __name__ == '__main__':
    main()