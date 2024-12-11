# 导入模块
import json, re, time, requests, threading
from uiautomation import WindowControl
from wxauto import *
from AI_chat import * 
from Honor_of_Kings import * 
from webpage import * 
from gif_download import *

wxchat = WeChat()

allowed_nicknames = []  # 修改为你想要回复的nickname
wx = WindowControl(
	Name='微信', ClassName="WeChatMainWndForPC"
)
wx.SwitchToThisWindow()
hw = wx.ListControl(Name='会话')
we = hw.TextControl(searchDepth=4)


def check_wechat_messages(hw):
	bbb = hw.GetChildren()
	while not we.Exists(0):
		time.sleep(0.5)
	for chatMsg in bbb:
		if "条新消息" in chatMsg.Name:
			match = re.match(r'(.+?)(\d+)条新消息', chatMsg.Name)
			if match:
				nickname = match.group(1)
				if nickname in allowed_nicknames:
					message_count = int(match.group(2))
					printInfo = f"来自 {nickname} 的{message_count} 条消息"
					print(printInfo)
					getMsg_send(nickname)


def getMsg_send(nickname):
	if we.Name:
		we.Click(simulateMove=False)
		last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name
		print(f"{nickname}:", last_msg)
		dispose(nickname, last_msg)


def dispose(nickname, last_msg):
	slash_index = last_msg.find('/')
	front_string = last_msg[:slash_index]
	back_string = last_msg[slash_index + 1:]
	if slash_index == -1:
		if last_msg in ["帮助", "help"]:
			print(f"来自 {nickname} 的帮助请求")
			help = f"欢迎使用wxchat帮助文档\n当前可用指令： \n王者、Excel、文件、表情包、爬网页、微信传...（待添加）\n例：指令+“\”or“/”+请求"
			wxchat.SendMsg(help, nickname)
		elif last_msg in [" ", "[动画表情]", "[图片]"]:
			sey = "[微笑]"
			wxchat.SendMsg(sey, nickname)
		else:
			zp_ai = zp_chat(nickname, last_msg)
			ai_sey = zp_ai
			print(f"AI回复：{ai_sey}")
			wxchat.SendMsg(ai_sey, nickname)
	else:
		if front_string in ["王者", "王者荣耀", "wz", "WZ", "王者战区"]:
			sey = wz_hero(back_string)
			wxchat.SendMsg(sey, nickname)
		elif front_string in ["excel", "Excel"]:
			pass
		elif front_string in ["表情", "表情包"]:
			sey = gif_download(back_string)
			print(sey)
			wxchat.SendMsg(sey, nickname)
		elif front_string == "爬网页":
			pass
		elif front_string == "文件":
			sey=webpage(back_string)
			if sey[1] =="text":
				wxchat.SendMsg(sey[0], nickname)
			elif sey[1] == "file":
				wxchat.SendFiles(sey[0], nickname)
			else:
				wxchat.SendMsg("出错了", nickname)
		elif front_string == "微信传":
			pass


if __name__ == "__main__":
	i = 1
	try:
		while True:
			print(f"{i}.检测中,等待消息...")
			check_wechat_messages(hw=hw)
			time.sleep(1)
			i += 1
	except KeyboardInterrupt:
		print("程序退出~")
	except Exception as e:
		print(f"程序执行出现了问题: {str(e)}")

# 死循环接受消息
while True:
	we = hw.TextControl(searchDepth=4)
	while not we.Exists(0):
		pass
