"""
[难度: ★★★][所属知识点: BankAccount 综合][预计完成时间: 15 分钟]

题目:独立完成 BankAccount 类,要求:
1. __init__(owner, balance) 绑定属性
2. @property 保护 balance(不允许为负)
3. deposit(amount) 存款,返回余额
4. withdraw(amount) 取款,超额拒绝
5. 类属性 bank_name = "Python 银行"
6. __str__ 输出友好信息
"""

class BankAccount:
    bank_name = "Python 银行"
    # TODO: 补全
    pass

if __name__ == '__main__':
    # 参考答案
    class BankAccount:
        bank_name = "Python 银行"

        def __init__(self, owner, balance):
            self.owner = owner
            self.balance = balance

        @property
        def balance(self):
            return self._balance

        @balance.setter
        def balance(self, value):
            if value < 0:
                print("余额不能为负,已忽略")
                return
            self._balance = value

        def deposit(self, amount):
            self._balance += amount
            return self._balance

        def withdraw(self, amount):
            if amount > self._balance:
                print("余额不足")
                return False
            self._balance -= amount
            return True

        def __str__(self):
            return f"BankAccount(owner={self.owner}, balance={self._balance})"

    acc = BankAccount("张三", 1000)
    print(acc)               # BankAccount(owner=张三, balance=1000)
    print(acc.deposit(500))  # 1500
    print(acc.withdraw(2000))  # False(余额不足)
    print(acc.withdraw(300))   # True
    print(acc)               # BankAccount(owner=张三, balance=1200)
