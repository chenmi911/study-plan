from pyecharts.charts import Map
from pyecharts.options import LegendOpts, VisualMapOpts

map = Map()

data = [
    ("北京市", 99),
    ("上海市", 199),
    ("江西省", 299),
    ("四川省", 399),
    ("云南省", 499)
]

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


map.render()

