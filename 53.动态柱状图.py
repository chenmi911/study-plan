# list = [["a", 33], ["b", 55], ["c", 11]]
#
#  def choose_sort_key(element):
#      return element[1]
#
#  list.sort(key=choose_sort_key, reverse=True)
#
# list.sort(key=lambda element: element[1], reverse=True)
#
#
# print(list)

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 读取数据
f = open("D:/1960-2014全球GDP.csv", "r", encoding="utf-8")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字典格式
# { 年份：[[国家，GDP][国家，GDP]……}
data_dict = {}
# 切分数据
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    # 判断是否有key
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# print(data_dict[2021])
# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})
# 取出所有年份进行排序
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出前八国家
    year_data = data_dict[year][0:8]
    # 构建轴
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # x轴添加国家
        y_data.append(country_gdp[1])  # y轴添加GDP数据

        # 构建柱状图
        x_data.reverse()
        y_data.reverse()
        bar = Bar()
        bar.add_xaxis(x_data)
        bar.add_yaxis("GDP(万亿美元)", y_data, label_opts=LabelOpts(position="right"))
        # 反转xy轴
        bar.reversal_axis()
        timeline.add(bar, str(year))
        # 设置每一年的标题
        bar.set_global_opts(
            title_opts=TitleOpts(title=f"{year}年的GDP")
        )
# 设置自动循环播放
timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeline.render("2017-2024全球GDP前四国家.html")



