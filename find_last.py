def first_last_position(arr, target):
      def find_last(arr, target):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                result = mid
                left = mid + 1     # keep searching RIGHT for last
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    return [find_first(arr, target), find_last(arr, target)]

print(first_last_position([5,7,7,8,8,10], 8))   # [3,4]
print(first_last_position([5,7,7,8,8,10], 6)) 
