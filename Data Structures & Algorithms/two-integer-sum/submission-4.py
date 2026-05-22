class Solution: #sort the array and use two pointers to find the solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num,i]) #value and index
        
        A.sort()
        i = 0 #point to beginning of array
        j = len(nums)-1 #point to end of array

        while i < j:
            sum = A[i][0] + A[j][0]
            if sum == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif sum < target:
                i += 1
            else:
                j -= 1
        return []
