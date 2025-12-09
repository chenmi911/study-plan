from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar = Bar()
bar.add_xaxis(["china", "america", "britain"])
bar.add_yaxis("GDP", [10, 50 ,90],
              label_opts=LabelOpts(position="right"))
# 反转xy轴
bar.reversal_axis()

bar.render("基础柱状图.html")