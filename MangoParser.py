import email
import imaplib


def connect_gmail_start() -> 'mail':
    """Connect to Gmail with set login and password"""
    global mail
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('<Login>', '<Password>')  # Auth data
    mail.select("inbox")
    return mail


def update_num(mail) -> 'tel_num':
    """Load tel number from Gmail inbox"""
    while True:
        try:
            ever_connect()
            print('Update mail start')
            term = u'"<Key word>"'.encode("utf-8")  # Key word for searching
            mail.literal = term
            result, data = mail.search("utf-8", "SUBJECT")
            ids = data[0]
            id_list = ids.split()
            latest_email_id = id_list[-1]
            result, data = mail.fetch(latest_email_id, "(RFC822)")
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            break
        except:
            print('An error occurred while searching for a new phone number. '
                  'Update mail and repeat download search')
            continue
    email_message = email.message_from_string(raw_email_string)
    subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
    print(subject)
    a = subject.split(' ')
    x = 0
    print('While true update mail start')
    while True:
        if '+' in a[x]:
            if len(a[x]) == 12:
                a = list(a[x])
                del a[0]
                a = ''.join(a)
                break
        x += 1
    print('While true update mail end')
    return a


def ever_connect() -> None:
    print('Everconnect start')
    mail.noop()
    print('Everconnect end')
