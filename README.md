# Wechat_reply
关于微信的自动回复
# 巷的微信AI机器人

## 作者
<img src="https://api.kuleu.com/api/qqimg?qq=2860364991" width="200" height="200">

- 微信号：zx762589
- 帅的一批的男人


## 功能介绍
- 微信AI机器人可以帮助企业快速搭建微信聊天机器人，实现自动回复、智能问答、智能聊天等功能。
- 其中主程序为index.py，主要功能包括：
  - 智能回复：当用户发送消息给机器人时，机器人会智能回复消息。
  - 智能问答：当用户发送消息中包含关键词时，机器人会根据关键词进行智能问答。
  - 表情包下载：当用户发送表情包关键词时，机器人会自动下载并发送表情包。
  - 王者低战区查询功能：当用户发送“王者”关键词时，机器人会自动查询王者低战区的最新战报。
  - ...
- 机器人使用了Python语言，并使用了wxauto库发送消息，用uiautomation库来获取新消息并进行处理。
- 机器人可以部署在服务器上，通过微信登录的方式进行聊天，稳定不封号。
- 其中里面可以根据需求进行修改，比如增加新功能、修改表情包下载功能、增加新游戏查询功能等。

## 部署方法
- 下载代码到本地
- 安装主要依赖库
  - uiautomation
  - wxauto
  - requests
  - os
  - re
  - zhipuai  --王者低战区查询功能依赖库--

## 运行方法
```python

# 允许回复的列表
allowed_nicknames = ["name1", "name2","..."]  # 修改为你想要回复的nickname

```
```python
# 这里可以根据需求修改，其中传入的参数为用户的昵称和用户发送的消息
def dispose(nickname, last_msg):
    # 处理消息
    pass
```

### 可改内容只有这两个地方，其他地方修改会报错。
[巷的主页](https://xiang-520.4everland.app/)
