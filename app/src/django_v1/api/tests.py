# 1.生成code 接/code/?email=邮箱
# 2.校验是否有刷验证码
# 3.如果没有第一条数据就创建第一条数据
# 4.对请求有效时间进行判断
str_bags="mxzxmzmxzzxmzxmmdmssamdadskdasmadskaswewewedoipiroweor"
list1 = []
for index,bag in enumerate(str_bags):
    if len(set(list1)) <= 5:
        list1.append(bag)
    print(set(list1))