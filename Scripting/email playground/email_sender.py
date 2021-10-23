import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Noman Baig'
email['to'] = 'noman-baig-1998@outlook.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am python master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('msgfromnoman@gmail.com', '**********')
    smtp.send_message(email)
    print('all good boss!')
