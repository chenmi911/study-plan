# json本质是字符串
# json.dumps()将python转换为json
import json
data = [{"name": "alan", "age": 23}, {"name": "lisa", "age": 24}]
json_str = json.dumps(data)  # 如果有中文则可以在data后加, ensure_ascii=False
print(type(json_str))
print(json_str)
# 将字典转换为json
d = {"name": "周杰伦", "addr": "台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(json_str)
# json.loads将json转变为python
data = '[{"name": "张大山", "age": 23}, {"name": "王大锤", "age": 24}]'
l = json.loads(data)
print(type(l))  # 字符串
print(l)

d = '{"name": "周杰伦", "addr": "台北"}'
l = json.loads(d)
print(l)
print(type(l))

