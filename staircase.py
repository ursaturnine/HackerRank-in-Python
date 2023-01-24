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
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)