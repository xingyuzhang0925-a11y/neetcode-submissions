class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A=[]
        for i,n in enumerate(nums):
            A.append([n,i])
        A.sort()
        left,right=0,len(A)-1
        while left<right:
            cur=A[left][0]+A[right][0]
            if cur==target:
                return[min(A[left][1],A[right][1]),
                        max(A[left][1],A[right][1])]
            elif cur<target:
                left+=1
            else:
                right-=1