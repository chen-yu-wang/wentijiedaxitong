# 修改密码
def db_change_password(username, oldPassword, newPassword):
    user = authenticate(username=username, password=oldPassword)
    if user is not None:
        if user.is_active:
            user.set_password(newPassword)
            user.save()
            return 1    # 修改成功，允许特殊符号
        else:
            return -2   # 没有权限
    else:
        return -1      # 旧密码错误
