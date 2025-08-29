#!/usr/bin/env python3
"""
Email Test Script for Django Portfolio
This script tests if your email configuration is working correctly.
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_email():
    """Test email sending functionality"""
    
    # ===== CONFIGURE THESE VALUES =====
    smtp_server = "smtp.gmail.com"  # For Gmail. Change if using another provider
    port = 587  # For starttls
    sender_email = "venkateshbuddhi887@gmail.com"  # Your email address
    password = "dxjeplstlnhraqul"  # Your app password (not your regular password)
    receiver_email = "varunsaraka3@gmail.com"  # Where to send the test email
    # ==================================
    
    print("Testing email configuration...")
    print(f"SMTP Server: {smtp_server}:{port}")
    print(f"From: {sender_email}")
    print(f"To: {receiver_email}")
    
    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email from Portfolio Website"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    varun saraka 
    ochi na MG
    """
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           This is a <b>test email</b> from your portfolio website.<br>
           If you received this, your email configuration is working correctly!
        </p>
      </body>
    </html>
    """
    
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")
    
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    # message.attach(part2)
    
    # Create secure connection with server and send email
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        
        # Try to log in to server and send email
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        
        print("✅ Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def check_email_providers():
    """Display common email provider settings"""
    providers = {
        "Gmail": {
            "smtp_server": "smtp.gmail.com",
            "port": 587,
            "notes": "Requires app password if 2FA is enabled"
        },
        "Outlook/Hotmail": {
            "smtp_server": "smtp-mail.outlook.com",
            "port": 587,
            "notes": "Uses STARTTLS"
        },
        "Yahoo": {
            "smtp_server": "smtp.mail.yahoo.com",
            "port": 587,
            "notes": "Requires app password"
        },
        "Office 365": {
            "smtp_server": "smtp.office365.com",
            "port": 587,
            "notes": "Uses STARTTLS"
        }
    }
    
    print("\nCommon Email Provider Settings:")
    print("=" * 40)
    for provider, settings in providers.items():
        print(f"{provider}:")
        print(f"  SMTP Server: {settings['smtp_server']}")
        print(f"  Port: {settings['port']}")
        print(f"  Notes: {settings['notes']}")
        print()

if __name__ == "__main__":
    print("Portfolio Email Testing Script")
    print("=" * 40)
    
    # Show provider settings first
    check_email_providers()
    
    # Run the test
    success = test_email()
    
    if not success:
        print("\nTroubleshooting Tips:")
        print("1. Make sure you're using an APP PASSWORD, not your regular email password")
        print("2. For Gmail, enable 2-factor authentication and generate an app password")
        print("3. Check if your email provider allows SMTP access")
        print("4. Try using a different port (465 for SSL)")
        print("5. Check your firewall settings")
    
    exit(0 if success else 1)