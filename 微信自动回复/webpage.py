import os, time, json


def webpage(back_string):
	top = back_string[:2]
	bottom = back_string[2:]
	if top == "查询":
		if bottom == "当前目录":
			directory_path = './'
			page_directory = os.path.join(directory_path, 'page')
			# 检查page目录是否存在
			if not os.path.exists(page_directory):
				# 如果不存在，则创建page目录
				os.makedirs(page_directory)
				return "page目录不存在，已创建","text"
			else:
				# 指定要查看的目录路径
				directory_path = './page'
				# 获取目录下的所有文件和文件夹
				items = os.listdir(directory_path)
				# 遍历所有项目并分类
				folders = []
				files = []
				for item in items:
					if os.path.isdir(os.path.join(directory_path, item)):
						folders.append(item)
					elif os.path.isfile(os.path.join(directory_path, item)):
						files.append(item)
				return "文件夹：" + str(folders) + "\n" "文件名：" + str(files),"text"

		elif bottom == "帮助":
			return "文件查询帮助：\n输入(文件+/+查询+目录名)即可查询指定目录下的所有文件和文件夹。\n如需查询某目录下的另一个目录输入(文件+/+查询+目录名+/+目录名）即可。","text"

		else:
			directory_path = './page'
			page_directory = os.path.join(directory_path, bottom)
			# 检查page目录是否存在
			if not os.path.exists(page_directory):
				# 如果不存在，则创建page目录
				# os.makedirs(page_directory)
				return "目录不存在，请输入正确的目录名","text"
			else:
				# 指定要查看的目录路径
				directory_path = f'./page/{bottom}'
				# 获取目录下的所有文件和文件夹
				items = os.listdir(directory_path)
				# 遍历所有项目并分类
				folders = []
				files = []
				for item in items:
					if os.path.isdir(os.path.join(directory_path, item)):
						folders.append(item)
					elif os.path.isfile(os.path.join(directory_path, item)):
						files.append(item)
				return "文件夹：" + str(folders) + "\n" "文件名：" + str(files),"text"

	elif top == "创建":
		if bottom not in [""]:
			directory_path = './page'
			page_directory = os.path.join(directory_path, bottom)
			# 检查page目录是否存在
			if not os.path.exists(page_directory):
				# 如果不存在，则创建page目录
				os.makedirs(page_directory)
				return f"{bottom}目录已创建","text"
			else:
				return f"{bottom}目录已存在" ,"text"
		elif bottom == ["", "帮助"]:
			return "创建目录帮助：\n输入(文件+/+创建+目录名)即可创建指定目录。如需创建多级目录，请用/隔开。","text"

	elif top == "获取":
		startpath = './page'
		# 要排除的前缀
		exclude_prefix = startpath + os.sep
		relative_path = []
		for root, dirs, files in os.walk(startpath):
			for file in files:
				full_path = os.path.join(root, file)
				# 移除指定的前缀
				path = full_path.replace(exclude_prefix, '', 1)
				relative_path.append(path)
		relative_path = str(relative_path).replace("\\\\", "/")
		data_str = relative_path.replace("[", "").replace("]", "").replace("'", '').replace('"', '').replace(' ', '')
		lst = data_str.split(",")
		# print(lst)
		if bottom == "当前目录内容":

			data_str = str(lst)

			# 去掉方括号和引号
			data_str = data_str.replace("[", "").replace("]", "").replace("'", '').replace('"', '')

			# 将逗号替换为换行符
			data_str = data_str.replace(",", "\n")
			return f"{data_str}\n以上是当前目录下所有文件和文件夹。","text"

		elif bottom == ["帮助", "help"]:
			return "获取当前目录内容帮助：\n输入(文件+/+获取+当前目录内容)即可获取当前目录下所有文件和文件夹。","text"
		elif bottom not in lst:
			print(lst)
			return f"{bottom}该文件或目录不存在或出错,使用前请确保文件不要有空格哦！！！","text"
		else:
			return "./page/"+bottom,"file"



