from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts, VisualMapOpts, ToolboxOpts

line = Line()

line.add_xaxis(["中国", "美国", "英国"])

line.add_yaxis("GDP", [100, 50, 20])

# 设置全局配置set_global_opts
line.set_global_opts(
    title_opts=TitleOpts(title="GPD展示", pos_left="center",pos_bottom="1"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)



# 通过render方法，将代码生成图像
line.render()