"""
[难度: ★★★★][所属知识点: 综合][预计完成时间: 30 分钟][类型: 选做]

题目:用 TDD 实现一个 PasswordValidator(密码验证器),要求:≥8 位,包含大小写字母和数字。

参考答案:
def test_password_validator():
    assert PasswordValidator.is_strong("Abc12345") == True
    assert PasswordValidator.is_strong("abc12345") == False  # 无大写
    assert PasswordValidator.is_strong("ABC12345") == False  # 无小写
    assert PasswordValidator.is_strong("Abcdefgh") == False  # 无数字
    assert PasswordValidator.is_strong("Ab1") == False  # 太短

class PasswordValidator:
    @staticmethod
    def is_strong(password):
        return (len(password) >= 8 and
                any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password))
"""
