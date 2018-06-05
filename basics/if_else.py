# 条件判断

'''
小明身高 1.75，体重 80.5kg。请根据 BMI 公式（体重除以身高的平方）
帮小明计算他的 BMI 指数，并根据 BMI 指数

  低于 18.5：过轻
  18.5-25：正常
  25-28：过重
  28-32：肥胖
  高于 32：严重肥胖
'''
h = float(input("身高(米)："))
w = float(input("体重(kg)："))
result = w / pow(h, 2)
if result < 18.5:
    print('偏瘦')
elif result >= 18.5 and result < 25:
    print("正常")
elif result >= 25 and result < 28:
    print("过重")
elif result >= 28 and result < 32:
    print("肥胖")
else:
    print("严重肥胖")
