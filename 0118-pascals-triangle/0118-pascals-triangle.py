class Solution(object):
    def generate(self, numRows):
       result = [[1]]
       current_row = 0
       while len(result) < numRows:
           temp_array = [1]
           prev_array = result[current_row]
           for i in range(1, len(prev_array)):
               temp_array.append(prev_array[i] + prev_array[i - 1])
           temp_array.append(1)
           result.append(temp_array)
           current_row += 1
       return result

# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]