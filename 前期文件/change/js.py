// 修改密码
function changePassword() {
    var changePasswordAlert = '';
    $('#changePasswordAlert').hide();
    if ( !$('#oldPassword').val() ) {
        changePasswordAlert += '**  旧密码不能为空！<br />';
    }
    if ( !$('#newPassword').val() ) {
        changePasswordAlert += '**  新密码不能为空！<br />';
    }
    if ( !$('#newPasswordAgain').val() ) {
        changePasswordAlert += '**  确认密码不能为空！<br />';
    }
    if ( $('#newPassword').val() != $('#newPasswordAgain').val() ) {
        changePasswordAlert += '**  两次密码不一致！<br />';
    }
    if ( $('#oldPassword').val() == $('#newPasswordAgain').val() ) {
        changePasswordAlert += '**  新密码和旧密码不能一样！<br />';
    }
    if (changePasswordAlert) {
        $('#changePasswordAlert').html(changePasswordAlert);
        $('#changePasswordAlert').show();

    } else {
        $.ajax({
            url: '/changePassword',
            type: 'POST',
            data: {
                username: $('#loginUsername').text().split(' ')[0],
                oldPassword: $('#oldPassword').val(),
                newPassword: $('#newPassword').val()
            },
            success: function (data, textStatus) {
                if (data == 1) {
                    alert('修改成功！');
                    window.location.href = 'index';

                } else if (data == -1) {
                    alert('旧密码错误！');

                } else if (data == -2) {
                    alert('没有相关权限！');
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        })
    }
}
