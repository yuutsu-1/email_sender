import smtplib
import ssl
from passwordthingy import pyssword
from xlrd import open_workbook
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_contacts(file):
    full_list = []
    book = open_workbook(file, on_demand=True)
    for name in book.sheet_names():
        sheet = book.sheet_by_name(name)
        for cell in sheet.col(1):
            full_list.append(cell.value)

    return full_list


sender_email = input('email: ')
receiver_email = get_contacts('C:\\Users\\guilh\\PycharmProjects\\email_project\\email_sender\\emails.xlsx')
password = pyssword()

message = MIMEMultipart("alternative")
message["Subject"] = "test"
message["From"] = sender_email


html = """\
<html>
  <body>
       <img src="https://images.sftcdn.net/images/t_app-cover-l,f_auto/p/ce2ece60-9b32-11e6-95ab-00163ed833e7/260663710/the-test-fun-for-friends-screenshot.jpg">
  </body>
</html>
"""

part2 = MIMEText(html, "html")
message.attach(part2)

filename = 'C:\\Users\\guilh\\PycharmProjects\\email_project\\email_sender\\mapa.jpg'

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()  # envia os emails e criptografa
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    while True:
        try:
            server.login(sender_email, password)
            break
        except smtplib.SMTPAuthenticationError:
            print('Você precisa mudar as configurações de segurança do gmail. Tente de novo')
            input('Pessione enter para continuar')
    for clientes2 in receiver_email:
        print(f'sending email to {clientes2}')
        server.sendmail(sender_email, clientes2, message.as_string())

input('Todos emails enviados, pressione enter para sair.')
