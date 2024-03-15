class Solution(object):
    def generate(self, numRows):
        # Initialize Pascal's Triangle with empty lists
        pascal_triangle = [[] for _ in range(numRows)]

        # Set the first element of the first row to 1
        pascal_triangle[0].append(1)

        # Generate the rest of the rows
        for i in range(1, numRows):
            current_row = pascal_triangle[i]
            prev_row = pascal_triangle[i - 1]

            # The first element of each row is always 1
            current_row.append(1)

            # Calculate and populate the middle elements of the row
            for j in range(1, len(prev_row)):
                element_sum = prev_row[j] + prev_row[j - 1]
                current_row.append(element_sum)

            # The last element of each row is also 1
            current_row.append(1)

        return pascal_triangle        
        
