#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hmac, base64, struct, hashlib, time, sys , os, subprocess
   
def get_hotp_token(secret, intervals_no):
  key = base64.b32decode(secret)
  msg = struct.pack(">Q", intervals_no)
  h = hmac.new(key, msg, hashlib.sha1).digest()
  o = ord(h[19]) & 15
  h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
  return h
   
def get_totp_token(secret):
  return get_hotp_token(secret, intervals_no=int(time.time())//30)
   
def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

key = 'XXXXXXXXX'    #这里是密钥共16位
validation_code = str(get_totp_token(key))
write_to_clipboard(validation_code + '\n')

print validation_code + "验证码已复制到剪贴板"

ssh_command = 'XXXXXXXXXXXXXXX'    #这里是ssh命令
os.system(ssh_command)

