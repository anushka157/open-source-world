#Problem: Largest Rectangle in Histogram

#Problem Statement:
#Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.



def largestRectangleArea(heights):
    stack = []  # Stack to store indices
    maxArea = 0
    heights.append(0)  # Append 0 to handle remaining bars
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        stack.append(i)
    
    return maxArea

# Example usage
heights = [2,1,5,6,2,3]
print("Largest Rectangle Area:", largestRectangleArea(heights))
