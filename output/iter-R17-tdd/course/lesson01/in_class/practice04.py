"""
[难度: ★★][所属知识点: 综合][预计完成时间: 10 分钟]

题目:用 TDD 实现 fizzbuzz(先写测试,再写代码)

参考答案:
def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(1) == "1"

def fizzbuzz(n):
    if n % 15 == 0: return "FizzBuzz"
    if n % 3 == 0: return "Fizz"
    if n % 5 == 0: return "Buzz"
    return str(n)
"""
