from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
bar1 = Bar()
bar1.add_xaxis(["china", "america", "britain"])
bar1.add_yaxis("GDP", [10, 50 ,90],
               label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["china", "america", "britain"])
bar2.add_yaxis("GDP", [60, 80 ,150],
               label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["china", "america", "britain"])
bar3.add_yaxis("GDP", [200, 150 ,160],
               label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline = Timeline({"theme": ThemeType.ROMANTIC})
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
# 自动播放时间间隔，单位毫秒
# 是否显示时间线
# 是否自动播放
# 是否循环自动播放
timeline.render("基础时间柱状图.html")