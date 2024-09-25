for url in urls:  # 外层循环遍历每个网址
    for cred in credentials:  # 内层循环遍历每个账号密码
        # 尝试登录的代码
        if "欢迎" in driver.page_source:  # 检查登录是否成功
            success_f.write(f"{url} - {cred['username']}:{cred['password']}\n")
            break  # 成功登录，退出内层循环
        else:
            continue  # 登录失败，继续尝试下一个账号密码

    else:  # 这个else与内层for循环对应
        # 如果没有成功登录，记录失败的网页
        failure_f.write(f"{url}\n")