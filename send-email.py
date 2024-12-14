from flask import Flask, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
load_dotenv()

# Initializing the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    # Email configuration
    sender_email = "chdvanshsingh@gmail.com"
    sender_password = os.getenv('password')
    receiver_email = "tech@themedius.ai"
    cc_email = "hr@themedius.ai"
    subject = "Python (Selenium) Assignment - Vansh Singh Chaudhary"

    # Creating the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['CC'] = cc_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Email body
    body = """
    Dear Tech Team,

    I am submitting my Python (Selenium) assignment as per the instructions. Below are the required items:

    1. Screenshot of the form filled via code (attached as screenshot.png).
    2. Source code of the assignment: https://github.com/Vansh3140/Google-Form-Bot.
    3. Brief documentation of my approach is present in the Readme in the github repo.
    4. My resume (attached).
    5. Links to past projects/work samples - https://github.com/Vansh3140/Live-Crypto-Price, https://github.com/Vansh3140/X-ScreenshotBot, https://github.com/Vansh3140/GoVault-Database.
    6. I am not available to work full time (10 am to 7 pm), but if there are any part-time openings, I’m interested.

    Please find the attached files for your review.

    Best regards,
    Vansh Singh Chaudhary
    """

    # Attaching the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Attaching screenshot
        filename_screenshot = "screenshot.png"
        with open(filename_screenshot, "rb") as attachment_screenshot:
            part_screenshot = MIMEBase('application', 'octet-stream')
            part_screenshot.set_payload(attachment_screenshot.read())
            encoders.encode_base64(part_screenshot)
            part_screenshot.add_header('Content-Disposition', f'attachment; filename={filename_screenshot}')
            msg.attach(part_screenshot)

        # Attaching resume
        filename_resume = "resume.pdf"
        with open(filename_resume, "rb") as attachment_resume:
            part_resume = MIMEBase('application', 'octet-stream')
            part_resume.set_payload(attachment_resume.read())
            encoders.encode_base64(part_resume)
            part_resume.add_header('Content-Disposition', f'attachment; filename={filename_resume}')
            msg.attach(part_resume)

        # Setting the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Sending the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)

        return "Email sent successfully!"

    except Exception as e:
        return f"Error sending email: {e}"

if __name__ == '__main__':
    app.run(debug=True)
