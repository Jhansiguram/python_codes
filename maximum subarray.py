nums=list(map(int,input().split()))
res=0
temp=0
if len(nums)==1:
    print(nums[0])
    #temp=0
    res=nums[0]
for i in nums:
    temp+=i
    if temp<i:
        temp=i
    if res<temp:
        res=temp
print(res)