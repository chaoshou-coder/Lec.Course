"""
[难度: ★★★★]
[所属知识点: 综合项目(通讯录 v1)]
[预计完成时间: 25 分钟]
[类型: 选做]

题目描述:
  独立完成通讯录 v1,要求:
  1. 用字典存储联系人
  2. 菜单循环(添加/查找/删除/全部/退出)
  3. 查找用 get,删除前检查是否存在
  4. 查看全部时处理空通讯录

  提示:参考知识点的综合练习示例,
  请独立写一遍,不要复制粘贴。
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    contacts = {}

    while True:
        print("\n=== 通讯录 ===")
        print("1.添加  2.查找  3.删除  4.全部  0.退出")
        choice = input("请选择:")
        if choice == "1":
            name = input("姓名:")
            phone = input("电话:")
            contacts[name] = phone
            print("添加成功")
        elif choice == "2":
            name = input("查找姓名:")
            print(contacts.get(name, "未找到"))
        elif choice == "3":
            name = input("删除姓名:")
            if name in contacts:
                contacts.pop(name)
                print("删除成功")
            else:
                print("查无此人")
        elif choice == "4":
            if not contacts:
                print("通讯录为空")
            else:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
        elif choice == "0":
            print("再见!")
            break
        else:
            print("无效选择")
