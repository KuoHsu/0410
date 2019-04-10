#http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm
import requests as re
response = re.get('http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm')
response.encoding = 'big5'
i = response.text.index('胡')
e = response.text.rindex('發')+1
content = response.text[i:e]
content = content.replace('<BR>','\n')
print(content)