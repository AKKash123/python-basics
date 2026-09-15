#while loop
#It counts repeated times
# count = 1
# while count<=10:
#     count += 1  #count = count+1
#     print(count)

#NESTED LOOP
# for row in range(1,4):  #outer loop notebooks cover page
#     for col in range(1,4):  #inner loop pages
#         print(row*col, end="\t")
#     print() #new line after each row
'''
                    rowno.    element
*                   1           1
* *                 2           2
* * *               3           3
* * * *             4           4
'''
# n = 4
# for i in range(1,n+1):
#     print('* '*i)

#inverted triangle
# n = 4
# for i in range(n,0,-1):
#     print('* ' *i)

n = 5
for i in range(1, n+1):
    space = ''* (n-i)
    stars = '* ' * i
    net = space+stars
    print(net)