# 使用逻辑判断来解决特殊情况，当然也可以先不考虑特殊情况，求出res,然后用字符创替换来解决问题。后者时间复杂度高。
class Solution:
    def intToRoman(self, num: int) -> str:
        inttoroman = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
        res = ''
        for n in inttoroman:
            temp = num//n
            if temp==4:
                if n==100:
                    if res!='' and res[-1]=='D':
                        res =  res[:-1] + 'CM'
                    else:
                        res += 'CD'
                elif n==10:
                    if res!='' and res[-1]=='L':
                        res =  res[:-1] +'XC'
                    else:
                        res += 'XL'
                elif n==1:
                    if res!='' and res[-1]=='V':
                        res =  res[:-1] + 'IX'
                    else:
                        res += 'IV'
            else:
                res += inttoroman[n]*(num//n)
            num = num%n
            
        return res
