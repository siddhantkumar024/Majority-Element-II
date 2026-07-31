#soln 1
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        h=n//3

        print(h)
        d={}
        c=0
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        y=[]
        for key,value in d.items():
            if value>h:
                y.append(key)
        return y
      #----------------------------------------------------------------------------
# sol 2
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        h=n//3
        y=[]
        c=1
        nums.sort()
        for i in range(1,n+1):
            if i<n and nums[i-1]==nums[i]:
                c+=1
                print(c)        
            else:
                if c>h:
                    y.append(nums[i-1])
                c=1
        return y

       
        
