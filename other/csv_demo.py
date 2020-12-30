from util import GetCSV

a = GetCSV().get(r'selenium\ranzhi\login_success.csv')
print(a)


# with open(r'selenium\ranzhi\login_success.csv','r',) as file:
#     login_success = file.read()
#     # print(login_success)
#     l = login_success.split('\n')
#     # print(l)
#     n = []
#     # for s in l:
#     #     a = s.split(',')
#     #     print(a)
#     #     n.append(tuple(a))
#     n = [tuple(s.split(',')) for s in l]
#     print(n)
#     # l.append(s)
#     # print(l)