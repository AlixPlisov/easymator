import email
import imaplib
import os
import codecs

def connect_gmail_start() -> 'mail':
    global mail
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('<Login>', '<Password>') # GMail Login and Password
    mail.select("inbox")
    return mail

path_to_current_file = os.path.realpath(__file__)
path_to_current_folder = os.path.dirname(path_to_current_file)

def update_num(mail) -> 'tel_num':
    voronezg = eval(codecs.open(path_to_current_folder+'\\voronezg.txt', 'r', 'utf-8').read())
    volgograd = eval(codecs.open(path_to_current_folder+'\\volgograd.txt', 'r', 'utf-8').read())
    spb = eval(codecs.open(path_to_current_folder+'\\spb.txt', 'r', 'utf-8').read())
    samara = eval(codecs.open(path_to_current_folder+'\\samara.txt', 'r', 'utf-8').read())
    rnd = eval(codecs.open(path_to_current_folder+'\\rnd.txt', 'r', 'utf-8').read())
    ekb = eval(codecs.open(path_to_current_folder+'\\ekb.txt', 'r', 'utf-8').read())
    krd = eval(codecs.open(path_to_current_folder+'\\krd.txt', 'r', 'utf-8').read())
    mobilki = eval(codecs.open(path_to_current_folder+'\\mobilki.txt', 'r', 'utf-8').read())
    nsk = eval(codecs.open(path_to_current_folder+'\\nsk.txt', 'r', 'utf-8').read())
    sip = eval(codecs.open(path_to_current_folder+'\\sip.txt', 'r', 'utf-8').read())
    nn = eval(codecs.open(path_to_current_folder+'\\nn.txt', 'r', 'utf-8').read())

    ads = 0
    while True:
        try:
            ever_connect()
            print('Обновляю почту')
            term = u'"<Key word>"'.encode("utf-8") # Key word for serach
            mail.literal = term
            result, data = mail.search("utf-8", "SUBJECT")
            ids = data[0]
            id_list = ids.split()
            latest_email_id = id_list[-1]
            result, data = mail.fetch(latest_email_id, "(RFC822)")
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')

            break
        except Exception as e:
            print('MangoParser;Ошибка. Программа остановлена.: ', e)
            update_num(mail)
            continue
    email_message = email.message_from_string(raw_email_string)
    subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
    print(subject)
    a = subject.split(' ')
    x = 0
    z = 0
    print('Успешно')
    try:
        while True:
            if '+' in a[x]:
                if len(a[x]) == 12:
                    a = list(a[x])
                    del a[0]
                    a = ''.join(a)
                    break
                else:
                    a = a[x]
                    break

            x += 1
    except IndexError:
        print('ОШИБКА! Короткий или длинный номер')
        a = 'НОМЕР НЕ ОПРЕДЕЛЕН'
    print('Почта обновлена успешно')
    generaldict = {**voronezg, **volgograd, **spb, **samara, **rnd, **ekb, **krd, **mobilki, **nsk, **sip, **nn}
    for i in generaldict:
        if i in raw_email_string:
            print(generaldict[i])
            ads = generaldict[i]
    if ads ==0:
        ads = 'НЕОПОЗНАННЫЙ ИСТОЧНИК'
        print('НЕОПОЗНАННЫЙ ИСТОЧНИК')

    return a, ads


def ever_connect() -> None:
    print('Соединение...')
    mail.noop()
    print('Соединение подтверждено')


