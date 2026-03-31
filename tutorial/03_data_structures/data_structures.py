# 03_data_structures.py - 学习列表和字典

# 1. 列表 (Lists)
print("我的书单:")
books = ["Python 基础教程", "计算机网络", "离散数学"]
print(f"书单内容: {books}")

# 2. 列表修改
books.append("算法导论")
print(f"新增一本书: {books}")
print(f"最喜欢的一本: {books[0]}")

# 3. 字典 (Dictionaries) - 就像一个真实的地址簿
user_info = {
    "name": "小明",
    "email": "xiaoming@example.com",
    "score": 95
}
print(f"\n用户信息: {user_info}")
print(f"小明的邮箱: {user_info['email']}")

# 4. 修改字典
user_info["score"] = 98
print(f"小明的成绩更新: {user_info['score']}")
