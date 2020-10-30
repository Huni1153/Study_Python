# from DBAdressBook import myModule
#
# if __name__ == "__main__":
#     pass
#     # myModule.myAdress()
# id = "991225-2051234"
# print(id.replace("-","\n"))
# print(id[7])
#
# a = [1,2,3,4,5]
# #a.reverse()
# a.sort(reverse = True)
# print(a)
#
#
# print(' '.join(['Thank', 'you', 'for', 'your', 'compliment']))
#
# s = "string"
#
# print(list(s))
#
a = (1,2,3,4,5)
print(sum(a,1))
a = {'a':70, 'b':90, 'c':80}
test = a.values()
print(sum(test))
cnt = 0
sum = 0
for num in a.values():
    sum += num
    cnt += 1
print(sum,sum//cnt)
#
# print(list(range(100,300,50)))
#
#
# num = list(range(1,7))
# tempList = []
# #print(num)
# for  check in num:
#     if check % 2 == 0:
#         tempList.append(check ** 2)
# print(tempList)
#
# num = [check ** 2 for check in range(1,7) if check % 2 == 0]
# print(num)
#

# def get_avg(*args):
#     sum = 0
#     cnt = 0
#     for num in args:
#         sum += num
#         cnt += 1
#     res = sum/cnt
#     print(type(res))
#
#
#
# print(get_avg(1,2,3,4,5,6,7,8,9,10))
# print(get_avg(5,10,15))

# li = [1,'2',3,'4','5']
#
# res = []
# for check in li:
#     if type(check) == int:
#         check += 10
#         res.append(check)
#     else :
#         check = int(check)
#         check += 10
#         res.append(check)
#
# print(res)
#
# def outer_f():
#     msg = "string"
#     def inner_f():
#         print(msg)
#     return inner_f
# outer_f()

#
# s = 'string'
# print(list(s[::2]))
#
# str = 'a:b:c:d'
# print(str.replace(':','*'))
# test = [True,'True']
# print(test)
#
# a = ['1', '12', '43', '4', '15', 'a']
# resList = []
#
# for check in a:
#     if check.isnumeric() == True:
#         resList.append("True")
#     else:
#         resList.append("False")
# print(resList)
#
# a =['Thank', 'you', 'for', 'your', 'compliment']
# strTmp = ""
# for i in a:
#     strTmp += i + " "
# print(strTmp)




def outer_f():
    msg = 'string'
    def inner_f():
        print(msg)
    print(type(inner_f()))
outer_f()

