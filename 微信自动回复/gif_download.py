import requests,os,time

def gif_download(key):
	if key not in ['', None]:
		url = f"https://api.doutub.com/api/bq/getBqlistByKeyword?keyword={key}&curPage=1&pageSize=100"
		headers = {
			"User-Agent": ""
		}
		response = requests.get(url, headers=headers)
		data = response.json()["data"]["rows"]
		# print(data)
		result = []
		i = 1
		for item in data:
			url = item['path']
			layout = url.split('.')[-1]
			result.append({'id': i, 'imgName': item['imgName'], 'path': item['path'], 'layout': layout})
			i += 1
		os.makedirs("./page/gif", exist_ok=True)
		folder_path = os.path.join("./page/gif", key)
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)
			time.sleep(1)
		else:
			time.sleep(1)
		for i in result:
			uid = i['id']
			imgName = i['imgName']
			path = i['path']
			# print(path)
			layout = i['layout']
			# print(uid, imgName, path, layout)
			headers = {
				"User-Agent": ""
			}
			response = requests.get(path, headers=headers)
			with open(f"./page/gif/{key}/{imgName}.{layout}", "wb") as file:
				file.write(response.content)
		return f"关于{key}共{len(result)}张表情包，以全部下载成功"
	else:
		return "请输入关键词"
