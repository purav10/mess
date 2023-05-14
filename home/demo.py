import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
password = input("Type your password and press enter: ")
server.login("me210003039@iiti.ac.in", password)

# smtp_server = "smtp.gmail.com"
sender_email = "me210003039@iiti.ac.in"
receiver_email = "ishaanmittal123@gmail.com"
# message = """\
# Subject: Hi there

# This message is sent from Python."""
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

server.sendmail(sender_email, receiver_email, message.as_string())
print("Email sent successfully")




# # Create a secure SSL context
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("me210003039@gmail.com", password)
#     # TODO: Send email here
#     server.sendmail(sender_email, receiver_email, message)
