# 02_control_flow.py - 学习条件判断和循环

# 1. 条件判断 (Conditionals)
age = int(input("请输入你的年龄: "))
if age < 18:
    print("你还未成年，适合从基础开始学。")
elif age < 30:
    print("年轻有为，加油学 Python！")
else:
    print("活到老学到老，精神可嘉！")

# 2. 循环 (Loops) - for 循环
print("\n正在循环打印数字 0 到 4:")
for i in range(5):
    print(f"当前数字: {i}")

# 3. 循环 (Loops) - while 循环
count = 3
print("\n倒计时开始:")
while count > 0:
    print(count)
    count -= 1
print("完成！")
