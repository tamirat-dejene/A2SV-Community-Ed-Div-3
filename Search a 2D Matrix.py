class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Implement binary search for 2d matrix
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            # get middle row
            middle_row = (top + bottom) // 2
            mid = matrix[middle_row]

            left = 0
            right = len(mid) - 1

            if target >= mid[left] and target <= mid[right]:
                # do binary search for the row
                while left <= right:
                    mid_col = (left + right) // 2
                    if target == mid[mid_col]:
                        return True
                    elif target < mid[mid_col]:
                        right = mid_col - 1
                    else:
                        left = mid_col + 1
                # not found
                return False

            elif target < mid[left]:
                bottom = middle_row - 1
            else:
                top = middle_row + 1
        # not found
        return False
            



        
