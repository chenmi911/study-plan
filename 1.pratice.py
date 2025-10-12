name = "dji"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_day = 7
final_price = stock_price * (stock_price_daily_growth_factor ** growth_day)
print(f"公司：{name}, 股票代码:{stock_code}, 当前股价:{stock_price}")
print("每日增长系数是：%.1f，经过 %d 天的增长后， 股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_day, final_price))

user_name = input("名字")
user_type = input("类型")
print("hello:%s, you are regal %s account, welcome " % (user_name, user_type))

