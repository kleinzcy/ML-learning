
# my solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        output = []
        flag = 0
        
        while(True):

            if flag==1:
                if (l1.val + l2.val) >= 9:
                    output.append(l1.val + l2.val - 10 + 1)
                    flag = 1
                else:
                    output.append(l1.val + l2.val + 1)
                    flag = 0
            else:
                if (l1.val + l2.val) > 9:
                    output.append(l1.val + l2.val - 10)
                    flag = 1
                else:
                    output.append(l1.val + l2.val)
                    flag = 0
                
            
            if l1.next==None and l2.next!=None:
                l2 = l2.next
                while(True):
                    if flag==1:
                        if l2.val + 1 > 9:
                            output.append(0)
                            flag=1
                        else:
                            output.append(l2.val + 1)
                            flag=0
                    else:
                        output.append(l2.val)

                    if l2.next==None:
                        break
                    l2 = l2.next
                if flag==1:
                    output.append(1)
                    
                break
                
            elif l1.next!=None and l2.next==None:
                l1 = l1.next
                while(True):
                    if flag==1:
                        if l1.val + 1 > 9:
                            output.append(0)
                            flag=1
                        else:
                            output.append(l1.val + 1)
                            flag=0
                    else:
                        output.append(l1.val)

                    if l1.next==None:
                        break
                    l1 = l1.next
                if flag==1:
                    output.append(1)                    
                break
            elif l1.next==None and l2.next==None:
                if flag==1:
                    output.append(1)
                    flag=0
                break
            
            l1 = l1.next
            l2 = l2.next
        

        return output
