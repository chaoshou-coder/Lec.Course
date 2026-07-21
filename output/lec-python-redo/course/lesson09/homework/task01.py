"""
[难度: ★★★][所属知识点: 生成器综合][预计完成时间: 15 分钟][类型: 选做]

题目:定义一个无限素数生成器 gen_primes(),
用 yield 产生无限个素数,取前 10 个。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def gen_primes():')
    print('    def is_prime(n):')
    print('        return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))')
    print('    n = 2')
    print('    while True:')
    print('        if is_prime(n): yield n')
    print('        n += 1')
    print()
    print('gen = gen_primes()')
    print('print([next(gen) for _ in range(10)])  # [2,3,5,7,11,...]')
