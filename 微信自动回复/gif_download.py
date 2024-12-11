

import requests,os,time,threading



def gif_download(key):
	if key not in ['', None]:
		url = f"https://api.doutub.com/api/bq/getBqlistByKeyword?keyword={key}&curPage=1&pageSize=100"
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",

		}
		response = requests.get(url, headers=headers)
		data = response.json()["data"]["rows"]
		# print(data)
		result = []
		i = 1
		# 遍历每个对象，提取imgName和path属性，并将它们添加到结果数组中
		for item in data:
			url = item['path']
			layout = url.split('.')[-1]
			result.append({'id': i, 'imgName': item['imgName'], 'path': item['path'], 'layout': layout})
			i += 1
		os.makedirs("./page/gif", exist_ok=True)
		# 构建文件夹的完整路径
		folder_path = os.path.join("./page/gif", key)
		# 检查文件夹是否存在
		if not os.path.exists(folder_path):
			# 如果文件夹不存在，则创建它
			os.makedirs(folder_path)
			# print(f"文件夹 '{key}' 已创建。")
			print(f"文件夹 '{key}' 已创建。")
			time.sleep(1)
		else:
			# print(f"文件夹 '{key}' 已存在，跳过创建。")
			print(f"文件夹 '{key}' 已存在，跳过创建。")
			time.sleep(1)
		for i in result:
			uid = i['id']
			imgName = i['imgName']
			path = i['path']
			# print(path)
			layout = i['layout']
			# print(uid, imgName, path, layout)
			headers = {
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
				"referer": "https://api.doutub.com/",
				"host": "qn.doutub.com"
			}
			response = requests.get(path, headers=headers)
			with open(f"./page/gif/{key}/{imgName}.{layout}", "wb") as file:
				file.write(response.content)
		# print(f"{uid}:{imgName}已下载")

		print('下载完成')
		return f"关于{key}共{len(result)}张表情包，以全部下载成功"

	# 打印结果数组
		# print(result)
		# thread = threading.Thread(target=download_img, args=(result, key))
		# 启动线程
		# thread.start()
		# # 等待线程完成
		# thread.join()

	else:
		return "请输入关键词"
