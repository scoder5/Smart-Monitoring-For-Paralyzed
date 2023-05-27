import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Create a SMTP session
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()

        # Login to your email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)

# Usage example
sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipient_email = "recipient_email@example.com"
subject = "Hello from Python!"
message = "This is a test email."

send_email(sender_email, sender_password, recipient_email, subject, message)