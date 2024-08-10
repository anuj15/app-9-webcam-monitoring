from smtplib import SMTP


def send_email(msg):
    with SMTP(host='gmail.smtp.com', port=587) as conn:
        conn.starttls()
        conn.login(user='anuj.nits2@gmail.com', password='wzgpcyhchhcdoret')
        conn.sendmail(from_addr='anuj.nits2@gmail.com', to_addrs='anuj.nits@gmail.com', msg=msg)


def print_send_mail():
    print('Send Mail')
