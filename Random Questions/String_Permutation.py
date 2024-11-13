# WAP to print all permutation of the given string s */
# Input : PQR
# Output : PQR,PRQ,QPR,QRP,RPQ,RQP

main_str = "pqr"
l = len(main_str)
res = (["x"*l]*2*l)
print(res[0][0])
for i in range(l):
    j = 0
    for q in range(l):
        lst1 = list(res[j])
        lst2 = list(res[j+1])
        lst1[q] = main_str[i]
        lst2[q] = main_str[i]
        res[j] = ''.join(lst1)
        res[j+1] = ''.join(lst1)
        j = j+2
print(res)
