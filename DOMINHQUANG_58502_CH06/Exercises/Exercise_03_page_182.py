"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_03_page_182.py
Problem:
3. Describe the costs and benefits of defining and using a recursive function.
Solution:
They are often easier to understand.
A lot of interesting algorithms use a divide-and-conquer approach.
Some languages do not have looping constructs, or the constructs are awkward to use.
Dynamic programming solutions can often be rewritten to be recursive with memoization.
If an algorithm has to use an explicit stack (LIFO) then using the call stack has minimal impact on the memory footprint.
The risk is that many operating systems and language runtimes have strict limits on stack size versus heap size.
"""
