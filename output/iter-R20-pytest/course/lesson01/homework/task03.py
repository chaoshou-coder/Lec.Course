"""
[难度: ★★★★][所属知识点: 综合][预计完成时间: 30 分钟][类型: 选做]

题目:用 pytest + mock 测试一个发送邮件的函数(不真发邮件)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  @patch('module.smtplib.SMTP')")
    print("  def test_send_email(mock_smtp):")
    print("      send_email('to@test.com', 'Subject', 'Body')")
    print("      mock_smtp.return_value.sendmail.assert_called_once()")
