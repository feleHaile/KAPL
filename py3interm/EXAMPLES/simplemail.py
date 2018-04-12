#!/usr/bin/env python
# (c) 2016 John Strickler
#
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

FILE_TYPES = {
    # type:   (MIME class, file-mode)
    'text': (MIMEText, "r"),
    'image': (MIMEImage, "rb"),
    'data': (MIMEApplication, "rb"),
}

class SimpleMail():

    def __init__(self, *, server, sender, to, **kwargs):
        self._server = server
        self._sender = sender
        self._to = to
        self._user = self._args.setdefault('username',"")
        self._password = self._args.setdefault('password',"")
        self._body = self.args.setdefault('message', '')
        self._subject = self.args.setdefault('subject', '')

        self._server = smtplib.SMTP(

        )


    def add_attachment(self, file_name, file_type):
        mime_class, file_mode = FILE_TYPES.get(file_type, (MIMEApplication, "rb"))
        with open(file_name, file_mode) as file_in:
            attachment_data = file_in.read()

        short_name = os.path.basename(file_name)
        attachment = mime_class(attachment_data)
        attachment.add_header(
            'Content-Disposition', 'attachment', filename=short_name
        )

        self._message.attach(attachment)


    def send(self):
        email = MIMEMultipart(body)
        email['Subject'] = self._args.setdefault('subject', "")

if __name__ == '__main__':
    m = SimpleMail(
        server=('mail.smtpcorp.com', 2525),
        auth=('jstrickpython', 'python(monty)'),
        sender=['jstrick@mindspring.com'],
        to=['jstrickler@gmail.com'],
        debug=1,
        subject="This is a test",
        message="Hello, world",
    )
    m.add_attachment('../DATA/parrot.txt', 'text')
    m.add_attachment('../DATA/chimp.bmp', 'image')
    m.send()
