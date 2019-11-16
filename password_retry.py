# 密码重试程序
# 设定密码为 ‘abc123’
# 请使用者输入3次
# 若输入错误，则显示 ’密码错误！还有__次机会‘
# 若输入正确，则显示 ’登入成功！
password = 'abc123'
i = 3 # 剩余机会
while i > 0:
    input_password = input('请输入密码：')
    if input_password == password:
        print('登入成功！')
        break  # 退出循环
    else:
        i = i - 1
        if i > 0:
            print('密码错误！还有 ', i, ' 次机会')
        else:
        	print('Opps, 木有机会咯')
