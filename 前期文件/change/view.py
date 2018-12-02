# 修改密码
@login_required(login_url='slg:login')
@require_http_methods(["POST"])
@permission_required('slg.views_slg_manager_tem', login_url='slg:get_permissionDenied')
def change_password(request):
    username = request.POST['username']
    oldPassword = request.POST['oldPassword']
    newPassword = request.POST['newPassword']
    changeResult = db_change_password(username, oldPassword, newPassword)
    return HttpResponse(changeResult)
