# google-authenticator
公司线上权限控制采用了统一入口+中央控制，访问线上所有机器都要通过一个跳板机。
跳板机使用 public key + 验证码 的方式登录，且只能以 nginx 用户身份登录被授权其他业务机器。
每次登陆跳板机就要打开手机看一下验证码……

# so
抱着研究的心理，写了个简单的脚本, 大家工作中不要使用这个哦
