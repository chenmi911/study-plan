import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("D:/河南疫情.txt", "r", encoding="utf-8")
data = f.read()
f.close()

data_dict = json.loads(data)
data_dict["areaTree"][0]["children"] = []
city_data = data_dict["areaTree"][1]["children"][3]

data_list = []
for city in city_data:
    city_name = city_data["cityName"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))
    data_list.append(("济源市", 5))

map = Map()
map.add("河南疫情", data_list, "河南")

map.add("测试地图", data, "china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":0, "max":99, "label": "0-99", "color": "#CCFFFF"},
            {"min":100, "max":199, "label": "100-199", "color": "#FF6666"},
            {"min":200, "max":500, "label": "200-500", "color": "#990033"}
        ]
    )
)

map.render("map.html")





