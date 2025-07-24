# google-authenticator

## 项目背景

公司线上权限控制采用统一入口+中央控制，访问所有线上机器必须通过跳板机登录。  
跳板机使用公钥加 Google Authenticator 验证码的双重认证方式，且只能以 `nginx` 用户身份登录后访问其他业务机器。  

每次登录跳板机时都需要打开手机查看验证码，操作繁琐且耗时。

## 项目目的

基于学习和研究目的，编写了该 Python 脚本，实现：

- 根据 Google Authenticator 的密钥自动生成当前有效的 TOTP 验证码
- 自动将验证码复制到剪贴板，方便粘贴使用
- 运行后自动执行指定 SSH 命令，快速登录跳板机

**仅供学习参考，请勿用于生产环境。**

## 代码说明

脚本核心功能：

- `get_hotp_token(secret, intervals_no)`：根据密钥和时间间隔生成 HMAC 一次性密码
- `get_totp_token(secret)`：基于当前时间生成 TOTP 6位验证码
- `write_to_clipboard(output)`：将验证码复制到 macOS 剪贴板（依赖 `pbcopy`）
- 自动执行预设的 SSH 登录命令

## 使用方法

1. 在脚本中替换以下两处：

   ```python
   key = 'YOUR_SECRET_KEY'        # 你的 Google Authenticator 秘钥，16位 base32 编码
   ssh_command = 'YOUR_SSH_CMD'   # 用于登录跳板机的 SSH 命令，例如：ssh nginx@jump.server.com
