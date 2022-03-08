#_*_ coding:utf-8 _*_

#1.字符串中不重复连续字符串的最大长度
#双指针
s='qweesdffer'
def longestS(s:str) -> int:
	length = l = r = 0
	while r<len(s):
		print(length,l,r)
		if s[r] not in s[1:r]:
			r += 1
			length = max(length,r-1)
		else:
			l += 1
	print(length)
	return length
longestS(s)

#2.两数之和：给定一个整数数组nums和一个目标值target，在该数组中找出两数之和等于目标值的那两个整数，并返回他们的数组下标
nums = [2,7,9,11]
target = 9
def twoSum(nums,target):
	lens = len(nums)
	j = -1
	for i in range(1,lens):
		temp = nums[:i]
		if (target - nums[i]) in temp:
			j = temp.index(target-nums[i])
			break
	if j>=0:
		print([j,i])
		return[j,i]
#twoSum(nums,target)

#3.回文数：给定一个整数，正序和倒序读取都是同一个整数
#x = 121
def ispalindrome(x):
	if (x < 0):
		return False
	else:
		str_x = str(x)
		if str_x == str_x[::-1]:
			print(True)
			return True
		else:
			print(False)
			return False
#ispalindrome(123)

#4.整数反转:给出一个32位的有符号整数，你需要将这个整数中的每位上的数字进行反转
def reverse(x):
	s = str(x)
	if s[0] == '-':
		x = int('-' + s[1:][::-1])
		print(x)
	else:
		x = int(s[::-1])
		print(x)
	return x if -2147483648< x <2147483647 else 0
#reverse(-2147483646)

#5.删除排序数组中的重复项：给定一个排序数组，你需要--原地--删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度
nums = [1,1,2]
def deleteNums(nums):
	num_new = []
	lens = len(nums)
	for i in range(len(nums)):
		if nums[i] not in nums[i+1:]:
			num_new.append(nums[i])
			continue
	print(len(num_new),num_new)
	return len(num_new)
#deleteNums(nums)

def removeDuplicates(nums):
	i = 0
	j = 0
	if len(nums) == 0:
		return 0
	for _ in range(len(nums)):
		print('j:',j)
		if nums[j] != nums[i]:
			i += 1
			print('i:',i)
			nums[i],nums[j] = nums[j],nums[i]
			print(nums[i],nums[j])
			print(nums[j],nums[i])
		j += 1
	print(i+1)
	return i+1
removeDuplicates(nums)

#6.合并两个有序链表：将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
#递归
def mergeTwoLists(l1,l2):
	if l1 and l2:
		if l1.val > l2.val :
			l1,l2 = l2,l1
		l1.next = mergeTwolists(l1.next,l2)
	print(l1 or l2)
	return l1 or l2
#mergeTwoLists(l1,l2)

#7.罗马数字转整数
def romanToInt(s):
    a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ans = 0
    for i in range(len(s)):
        if i<len(s)-1 and a[s[i]]<a[s[i+1]]:
            ans-=a[s[i]]
        else:
            ans+=a[s[i]]
    print(ans)
    return ans
#romanToInt('CDXLIVIII')

#8.最长公共前缀
#采用zip打包成元组的形式，（*str）代表传的形参
strs = ['flpe','flower','flop']
def longestCommonPrefix(strs):
    if not strs: return ''
    result = ''
    for temp in zip(*strs):
        print(*strs)
        print(temp)
        if len(set(temp)) == 1:
            print(set(temp))
            result += temp[0]
        else:
            break
    print(result)
    return result
#longestCommonPrefix(strs)

#9.有效的括号
#辅助栈法
def isValid(s):
	dic = {'{':'}','[':']','(':')','?':'?'}
	stack = ['?']
	for c in s:
		print('0:',stack)
		if c in dic: stack.append(c)
		elif dic[stack.pop()] != c: return False
	return len(stack) == 1
#isValid('{(({)}')

#10.实现strStr()：给定一个haystack字符串和一个needle字符串，在haystack字符串中找出needle字符串出现的第一个位置（从0开始）。如果不存在，则返回-1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        a, b, c = 0, 0, 0 # a记录起点，b为haystack的滑动指针，c为needle的滑动指针
        while b < len(haystack):
            if haystack[b] == needle[c]:
                b += 1
                c += 1
            else: # 重置
                a += 1
                b = a
                c = 0
            
            if c == len(needle):
                return a
        
        return -1
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。

def run2(A) :
    B =[]
    while i < len(A):
        if A[i]<0:
            B.append(abs(A[i])*abs(A[i]))
        if A[i]>=0:
            B.append(A[i]*A[i])
    B = sorted(B)
    print(B)
    #if len(B) == len(A)
    return B
#run([-4])


def run1(A):
    for i in range(len(A)):
        if A[i] < 0:
            A[i] *= -1
        else:
            break
    A.sort()
    for i in range(len(A)):
        A[i] *= A[i]
    return A
#sortedSquares([-4])


def run(A) :
    print(A)
    B =[]
    i = 0
    while i < len(A):
            B.append(A[i]*A[i])
            B = sorted(B)
    print(B)
    #if len(B) == len(A)
    return B


def run11(self, A):
        index = len(A)
        for i in range(len(A)):
            if A[i] >= 0:
                index = i
                break
        negative = [x * x for x in A[:index]]
        positive = [y * y for y in A[index:]]
        if negative == []:
            return positive
        negative.reverse()
        if positive == []:
            return negative
        result = []
        a = 0
        b = 0
        while a < len(positive) or b < len(negative):
            if positive[a] >= negative[b]:
                result.append(negative[b])
                b += 1
            else:
                result.append(positive[a])
                a += 1
            if a == len(positive) and b < len(negative):
                return result + negative[b:]
            elif a < len(positive) and b == len(negative):
                return result + positive[a:]


def run333(A) :
    print(A,100)
    B =[]
    i = 0
    while i < len(A):
        B.append(A[i]*A[i])
        i = i+1
    B = sorted(B)
    return B
run333([-4,100,2,10])  




















	


