import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.header import Header
from base64 import encodebytes
import email
import mimetypes
import os
import setting



mail_from = setting.MAIL_FROM # отправитель
mail_to = setting.MAIL_TO  # получатель
mail_text = 'Отчет о прохождении автотеста'  # текст письма
mail_subj = 'Результаты прохождения'  # заголовок письма
mail_coding = 'windows-1251'
attach_file = 'autotestlog.log'  # прикрепляемый файл
attach_file2 = 'autotestlogneg.log'  # прикрепляемый файл2

# Параметры SMTP-сервера
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = setting.SMTP_USER  # пользователь smtp
smtp_pwd = setting.SMTP_PWD  # пароль smtp

# формирование сообщения
multi_msg = MIMEMultipart()
multi_msg['From'] = Header(mail_from, mail_coding)
multi_msg['To'] = Header(mail_to, mail_coding)
multi_msg['Subject'] = Header(mail_subj, mail_coding)

msg = MIMEText(mail_text.encode('cp1251'), 'plain', mail_coding)
msg.set_charset(mail_coding)
multi_msg.attach(msg)

# присоединяем атач-файл
if (os.path.exists(attach_file) and os.path.isfile(attach_file)):
    file = open(attach_file, 'rb')
    attachment = MIMEBase('application', "octet-stream")
    attachment.set_payload(file.read())
    email.encoders.encode_base64(attachment)
    file.close()
    only_name_attach = Header(os.path.basename(attach_file), mail_coding);
    attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % only_name_attach)
    multi_msg.attach(attachment)
    if (os.path.exists(attach_file2) and os.path.isfile(attach_file2)):
        file = open(attach_file2, 'rb')
        attachment = MIMEBase('application', "octet-stream")
        attachment.set_payload(file.read())
        email.encoders.encode_base64(attachment)
        file.close()
        only_name_attach = Header(os.path.basename(attach_file2), mail_coding);
        attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % only_name_attach)
        multi_msg.attach(attachment)
else:
    if (attach_file.lstrip() != ""):
        print("Файл для атача не найден - " + attach_file)

# отправка
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(smtp_user, smtp_pwd)
smtp.sendmail(mail_from, mail_to, multi_msg.as_string())
smtp.quit()
