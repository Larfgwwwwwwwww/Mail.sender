import smtplib

class Emailer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.smtpObj = smtplib.SMTP(self.host, self.port)

    def starttls(self):
        self.smtpObj.starttls()

    def login(self, username, password):
        self.smtpObj.login(username, password)

    def sendmail(self, sender, recipients, message):
        self.smtpObj.sendmail(sender, recipients, message)

    def quit(self):
        self.smtpObj.quit()


emailer = Emailer('smtp.gmail.com', 587)

# Запуск
emailer.starttls()

# Вход в аккаунт с которого будет воспроизводиться рассылка
emailer.login('email.rassialky1@gmail.com', 'pkcb hoda qrdn zkea')

# Отправка писем
emailer.sendmail("email.rassialky1@gmail.com", ["shadrunov_kr@mail.ru"], "Hello from Python!")

# Завершение
emailer.quit()