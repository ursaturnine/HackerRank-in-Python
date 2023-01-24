"""Its base and height are both equal to n

. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of sizen 
. """


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    m = n - 2
    for stairs in range(1, n):
        print(' ' * m, '#' * stairs)
        m -=1
    print('#' * n)