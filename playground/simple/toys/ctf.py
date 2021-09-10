"""
需python3运行环境，代码请保存为UTF8格式文件，若提示缺失AES库，则通过pip工具安装AES库
Linux：pip3 install pycrypto
Windows: pip install pycryptodome
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import time
import gzip
from hashlib import md5
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)
username = input('Hello Geek，请输入您的oa开始探索神秘代码：')


def Decrypt(key: str, text: str) -> str:
  if len(key) < 32:
    key += ' ' * (32 - len(key))
  elif len(key) > 32:
    key = key[0:32]

  def unpad(s):
    return s[0:-s[-1]]
  cipher = AES.new(key.encode(), AES.MODE_CBC, bytes(AES.block_size))
  r = gzip.decompress(bytes.strip(unpad(cipher.decrypt(base64.b64decode(text))))).decode()
  print('r=%s\n' % (r))
  return r


def Pass(id, priv_key):
  prefix = str(id) + str(int(time.time())) + str(username)
  pub_key = md5(bytes(prefix + priv_key, 'utf8')).hexdigest() + prefix
  print('恭喜通过第%d关,通关公钥:%s\n' % (id, pub_key))


key = input('1+1=')
exec(Decrypt(key, 'KtBQd1Ix8Cd3eEjtYHd1V7vxxOgq69oqFQsyMZczTU0AiOuRSO65uks1acUNnUp2hDocI2LoI2RBmF8MjWxnHUqZxAONaAO8TbXYSUNq+YeZTOX30D8WI0qBu8mXCAhW/ZLF0Kg9ugT6J212jYBQm+ka+gwJV8tlst4Jf0A72n6MdlPLfm97fkI31vL5Uc5RbWJIRONo1DoSzAnEQ68ON1Nno+MDaAVUQaXF5Ez1jOi1D+qBF2QmjvpJHyVqIsSCQsUWm1kj9RDv0z5vwZcCAcacJHeZsarrWNlNKZdlVAdEyH79Uco5BRZVmNwnF/6g2x+N1osOHqFzTiLQx8/DNfiQe9I57dUA1Cp4kK4ke8+Bi/ZT6Isqd6xpeF4BhtBV8tVmYZ11B/cwdrInW5KDV4ycVaNz7zxAxJB1v+Ptje5rK5D3c6RssKHq4xeawLGmj/cBz/a5J9//xLt7CAbIvnk+3LD0/1VbNBpepumXNCvrYpoYEBVcDYl97LtcUpcrEreZF5tMuEced4X5qXELm614woZb8Fms6zv4iPwvWEcm85tgzyroONwEDS6q8ko2Fl7jqo8NlYSX6siAHgmGwf5HdIxRgQwkO5jdVZ1++rOAB4xfcxiP7a9ya350IFXBs0PsQighgHKwz4Rlhe2C5WBkzNIZm0abFGOx2MnBxBKPGPcdt3xBHkVgExbRZ0+jW/35BNJwO+HArjrKfz2VnZdlzCTl+uCgLPY7rnS/R8ys/LCLfR66jw2Yc5BrTd8dGGSavG9w09ASIc3pYLjRSRq2hhJ9T8Teo8S7F4jetmIAwQc6lwWpHgGSux4hOkqwvRoLQG1Fbojqcs6xuXtG/B5iU3H9npoHzwdYQlGtWMSzAh0qBPQCOg3zgPGTh5zyN4HmDsVwB95BNoaVxG1uaQ9xsGHQqGBovfvZKnE00Do23JmW66IxCrAuaQyFqnif4/iHadtXmuzmk+VVJYPzk3nyTwA3FWt+9ADjZkNKHUY1tzZndfpZoawwxOvxj/tUWeELLX0ukzirdgpal4gZbLOGRDnnBHHMUq0SwkeZwQfJ6XLOqso0LRdLnGyjnq0Iq0y0JIZNm6P2G/MSo5KxSI8CXe5cAVU+UrTcas3CozdC5DrupSJBFjW19QHoOVJhuVXywOQhGdoGLrOnT1M4H2C+CO8bY1Ml8y/6YMo8W8j4ovHowbqIM3vaSZYPxBtv/3A1GuVtkMipqhhCQ9EgHerSX7KXuan2ph6ooMqmCcFrb/vYzH+uzNXf5HVeNpFVE7jW9+8Z671ybCQ6BvFfDyGrcs2MeNAHsR0Non+Il1buYxFh27qccr5SKYbkPtG/avSXRJfY87C6h8xyzljWCZK1j7+oDS6jfj6y+jblqVVOX16NqZLIuvUvSpZNwELTr385uzc1zlTknqPNRcCTw9pWwAIcVaIE1++PVwR9vRauZf0hhfx4zA1rw+9/U2lqdOZhvZSpDedLSjpZZBBYZHefcxWekt3d+xyHpW7NgzlWIYDj8eVbnlKqluYVfpeGVAE/O1YMaSry6WosyzxsmtfHx5HS9b9AZoxLUKl7117PvV5ryP690IeZApvKff4tZ4lzpTwaXYj09rsc8KBph2mbr/3vMCn7818+s1lmz1kqP7rs/0LtLz7svqpK5VD61w6zDnzPo4pxT214mtPR4fV8pFoOBjyHUsbGCVMziDGSjTfFncrsLZB0xtBOguVhjBq6/aJtDUCccXmZh6B7a6VozTImoYNhQee8LwARt+DElTMqnLVTAkMq9UiPKGsiEy4cEGS+VqN9C3WHFiuK3kt36eP8GmDYfrWbEPTVv4RR+S96VeEpY3BToMy05T304HsL+ctIOoJ8FrHT7wVyeb89f+BYkH8u83uamN7xgLz/A9G+sJW/qkLaAwMuLmvENGTcXTsassF9RO3++AQDBYydQZU9Lg699AVkcii9XJg='))
