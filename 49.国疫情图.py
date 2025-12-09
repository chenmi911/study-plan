import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("D:/text", "r", encoding="utf-8")
data = f.read()
f.close()

data_dict = json.loads(data)
province_data_list = data_dict["aearTrea"][0]["children"]
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_confirm, province_name))

map = Map()

map.add("各省份确诊人数", data, "china")

map.set_global_opts(
    title_opts=TitleOpts("全国疫情图"),
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

map.render("全国各地疫情分布.html")