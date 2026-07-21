### Day 01 · pytest 基础

> **痛点**:你用 `assert` 测试代码,但测试散乱、不能自动运行、没有报告。今天你将学会用 pytest 写第一个测试 —— 从零开始。
> **类比**:pytest 就像"自动阅卷系统" —— 你出考卷(测试),它自动批改并生成报告。
> **解释**:**pytest = Python 测试框架**。今天学:写测试 + fixture + 运行。

---

#### 你的第一个 pytest 测试

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

```python
# test_calculator.py
from calculator import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
```

```bash
# 运行测试
pytest test_calculator.py -v
```

**逐行解剖**

- `def test_add()` = 测试函数(必须以 test_ 开头)
- `assert add(2, 3) == 5` = 断言:如果失败,测试失败
- `pytest -v` = 运行测试(verbose 模式)

> **ASCII 测试流程**
> ```
> 写测试(test_*) → 运行 pytest → 收集测试 → 执行断言 → 输出报告
>                                                    ↓
>                                             PASSED/FAILED
> ```

**常见错误**

> 1. **错误现象**:测试函数没以 test_ 开头,pytest 没收集到
>    **原因:**pytest 只收集 test_ 开头的函数。修正:改名
> 2. **错误现象**:assert 失败但不知道具体值
>    **原因:**assert 只告诉失败,不显示实际值。修正:用 pytest.approx()或手动打印

---

#### fixture —— 测试的"准备"

```python
import pytest

@pytest.fixture
def sample_data():
    """测试前置准备"""
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_length(sample_data):
    assert len(sample_data) == 5
```

**逐行解剖**

- `@pytest.fixture` = 装饰器,标记这是一个 fixture
- `sample_data()` = fixture 函数,返回测试数据
- `test_sum(sample_data)` = 测试函数接收 fixture 作为参数

---

#### 执行过程跟踪

```python
# --- 执行过程 ---
# $ pytest test_calculator.py -v
#   ① 收集测试:找到 test_add 和 test_subtract
#   ② 运行 test_add:
#      - assert add(2, 3) == 5 → PASSED
#      - assert add(-1, 1) == 0 → PASSED
#      - assert add(0, 0) == 0 → PASSED
#   ③ 运行 test_subtract(同上)
#   ④ 输出报告:2 passed in 0.01s
```

---

#### 学员代码区

```python
# TODO: 写一个 divide 函数
# TODO: 写 test_divide(测试正常除法 + 除零异常)
# TODO: 运行 pytest 查看结果
```

---

#### 参考答案

```python
# calculator.py
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# test_calculator.py
def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
```

---

## 明日衔接

- 明天 Day 02 学什么:**parametrize 与 mock**
- 今天遗留的概念:今天学了基本测试,但还没学参数化测试和 mock
- NCDL 反模式预告:Day 2 展示"测试实现细节而不是行为"的反模式
