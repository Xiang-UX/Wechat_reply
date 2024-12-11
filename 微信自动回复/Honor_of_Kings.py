import requests,re


def wz_hero(back_string):
	pattern = r'(wx|ios_wx|qq|ios_qq)(.*)'
	match = re.search(pattern, back_string)
	type = match.group(1)
	hero = match.group(2) 
	url = f'https://api.pearktrue.cn/api/hero/?hero={hero}&type={type}'
	response = requests.get(url)
	data = response.json()
	if data["code"]==200:
		# Code = data["code"]
		# Message = data["msg"]
		data_data = data["data"]
		UID = data_data["uid"] 
		Name = data_data["name"]
		Alias = data_data["alias"]
		platform = data_data["platform"]
		Photo_URL = data_data["photo"]
		Province = data_data["province"]
		Province_Power = data_data["provincePower"]
		city = data_data["city"]
		city_Power = data_data["cityPower"]
		area = data_data["area"]
		area_Power = data_data["areaPower"]
		guobiao = data_data["guobiao"]
		# stamp = data_data["stamp"]
		update_Time = data_data["updatetime"]
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

