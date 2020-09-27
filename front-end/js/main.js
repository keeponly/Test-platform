$(function(){
    //ajax请求
    $('dl').click(function(){

    //获取账号
    var user = $('#user').val();
    //获取密码
    var pwd = $('#pwd').val();
    //相关加密处理
    //发送ajax请求
    $.ajax({
    url:'/login',
    data:{'user':user,'pwd':pwd},
    method:'post',
    dataType:'json',
    })
    });
})