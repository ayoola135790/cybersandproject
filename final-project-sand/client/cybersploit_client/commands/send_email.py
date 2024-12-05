# import the Python standard library modules for sending email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..commands import Command # Required

def send_email(email_address):
  # Set variables for credentials to our email server
  #
  # Gmail is a bit annoying to set up for sending email with Python,
  # so instead we'll be using a server set up just for this class :D
  smtp_server, port = ("e1-mail.acmcyber.com", 32525)
  # Our email server is set up to allow any username/password combo
  # Note that you should never include passwords in your source code in a real app!
  username, password = ("expert-hacker", "hunter2")

  # Start building a a new "multipart" MIME file
  # (MIME, or "Multipurpose Internet Mail Extensions", is the format that modern email uses)
  message = MIMEMultipart("alternative")
  message["From"] = "sand@e1-mail.acmcyber.com" # put your team name here! (make sure that it's a valid email though)
  message["To"] = email_address
  message["Subject"] = "[ACTION REQUIRED] UCLA Classes Dropped"

  # add your email HTML here!
  html = """\
  <html>
    <body>
      <h1 style="font-family: 'Comic Sans MS'">Due to a system error, you have been unenrolled in all your classes.</h1>
      <h1 style="font-family: 'Comic Sans MS'">Please click the following button for easy access to class planner.</h1>
      <a href="https://www.youtube.com/watch?v=QYlzoplheEU">
        <button style="color: blue;">UCLA LOG-ON</button>
      </a>

      <p>David, Shenran, Nemi, Emmanuel</p>
    </body>
  </html>
  """

  # Make an HTML email attachment from that string, and attach it to our message
  message.attach(MIMEText(html, "html"))

  # Open up an SMTP (Simple Mail Transfer Protocol) to our server, and send your email!
  with smtplib.SMTP(smtp_server, port) as server:
      server.login(username, password)
      server.sendmail(message["From"], message["To"], message.as_string())


class SendEmail(Command):
    def do_command(self, lines):
      send_email(lines)
      print("Email sent!")

command = SendEmail

