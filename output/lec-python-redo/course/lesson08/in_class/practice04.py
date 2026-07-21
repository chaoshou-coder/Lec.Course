"""
[难度: ★★][所属知识点: @property][预计完成时间: 10 分钟]

题目:在 Order 类中用 @property 给 price 加校验,价格不能为负。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('class Order:')
    print('    @property')
    print('    def price(self):')
    print('        return self._price')
    print('    @price.setter')
    print('    def price(self, value):')
    print('        if value < 0:')
    print('            raise ValueError("价格不能为负")')
    print('        self._price = value')
