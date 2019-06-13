import requests
import json

# 通过观察得到我们要的数据通过后台返回，故有下面的连接
url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1559184997897&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
response = requests.get(url)
# 把后台返回的数据转成字典
content = json.loads(response.text)
# 建一个空的list，把我们要的数据放到里面，从而得到数组的长度
items = []
for i in content["Data"]["Posts"]:
    items.append(i)
#循环输入岗位名称
for i in range(len(items)):
   print(content["Data"]["Posts"][i]["RecruitPostName"])
   