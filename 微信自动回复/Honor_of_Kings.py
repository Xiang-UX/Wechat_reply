import requests,re


def wz_hero(back_string):
	# 请将 '元歌' 改为你想要查询的英��的名称
	pattern = r'(wx|ios_wx|qq|ios_qq)(.*)'
	match = re.search(pattern, back_string)
	type = match.group(1)  # 区
	hero = match.group(2)  # 英雄
	url = f'https://api.pearktrue.cn/api/hero/?hero={hero}&type={type}'
	response = requests.get(url)
	data = response.json()
	if data["code"]==200:
		# Code = data["code"]
		# Message = data["msg"]
		data_data = data["data"]
		UID = data_data["uid"]  # 英雄uid
		Name = data_data["name"]  # 英雄名称
		Alias = data_data["alias"]  # 英雄名称
		platform = data_data["platform"]  # 区
		Photo_URL = data_data["photo"]  # 头像照片
		Province = data_data["province"]  # 金标位置
		Province_Power = data_data["provincePower"]  # 金标分
		city = data_data["city"]  # 银标位置
		city_Power = data_data["cityPower"]  # 银标分
		area = data_data["area"]  # 区标位置
		area_Power = data_data["areaPower"]  # 铜标分
		guobiao = data_data["guobiao"]  # 国标
		# stamp = data_data["stamp"]  # 更新时间戳
		update_Time = data_data["updatetime"]  # 更新时间
		a = f"""
 英雄UID: {UID}
 英雄名称: {Name}
 英雄别称: {Alias}
 区： {platform}
 头像照片: {Photo_URL}
 金标区域: {Province}
 金标分: {Province_Power}
 银标区域: {city}
 银标分: {city_Power}
 铜标区域: {area}
 铜标分: {area_Power}
 国标分: {guobiao}
 更新时间: {update_Time}
		"""

		return a
	else:
		a = """     
	查询失败,请检查输入是否正确
	获取数据失败,请按照‘王者+\+qq+英雄名’格式输入
	qq(不填默认安卓QQ)
	wx(安卓微信)
	ios_qq(苹果QQ)
	ios_wx(苹果微信)"""
		return a

