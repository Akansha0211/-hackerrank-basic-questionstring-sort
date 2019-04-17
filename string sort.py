'''Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Input Format

The first line of input contains words separated by the comma.

Constraints

NIL

Output Format

Print the sorted words separated by the comma.

Sample Input 0

without,hello,bag,world
Sample Output 0

bag,hello,without,world
Explanation 0

b comes before h which in turn comes before w. In case of 'without' and 'world', w matches but second letter i comes before o. So 'without' comes before 'world'.

Sample Input 1

decision,with,which,Lincoln,despatched
Sample Output 1

Lincoln,decision,despatched,which,with
Explanation 1

Case will remain same while sorting.'''

a=list(input().split(','))               # CODE BEGINS                               
a.sort()
c=0
for i in a:
    if c<len(a)-1:
        print(i,end=",")
    else:
        print(i)
    c=c+1

        
