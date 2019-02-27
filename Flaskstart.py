from MangoParser import connect_gmail_start, update_num, ever_connect
from flask import Flask, render_template, request, redirect
from datetime import datetime
from Save_in_sheet import save_data
from threading import Thread
import pytz
import time


app = Flask(__name__)
mail = connect_gmail_start()
pr = 0
correct_num = 0


def evr() -> None:
    """Updates the connection every 120 seconds to prevent disconnection"""
    global pr
    while True:
        if pr == 'start':
                time.sleep(5)
                continue
        else:
            pr = 'start'
            ever_connect()
            pr = 0
            print('Connection success. Up to update 120 seconds.')
            time.sleep(120)
            continue


ev = Thread(target=evr)  # Thread for check connect
ev.start()


def get_time() -> 'time':
    """Return current time"""
    tz = pytz.timezone('Europe/Moscow')
    times = datetime.now(tz=tz).strftime('%H:%M')
    print('Get time')
    return times


@app.route('/', methods=['GET', 'POST'])
def newstart() -> 'html':
    return render_template('newindex.html')


@app.route('/res_page', methods=['POST'])
def res_page() -> 'html':
    global ads, description, times, req, pr, tel_num
    if pr == 'start':
        while True:
            time.sleep(2)
            if pr == 'start':
                continue
            else:
                break
    ads = request.form['ads']
    description = request.form.get('description')
    note = request.form['note']
    ads = ''.join(list(ads))
    note = ''.join(list(note))
    description = ''.join(list(description))
    times = get_time()
    req = request.form['res']
    while True:
        if pr == 'start':
            time.sleep(2)
            continue
        else:
            break
    if req == 'order':
        processing(ads, description, times, req)
        ptel_num = list(tel_num)
        ptel_num.remove("7")
        ptel_num = ''.join(ptel_num)
        print('Order page is ok')
        return render_template('cool.html', ads=ads, tel_num=ptel_num, note=note, res='ЗАКАЗ', status=status)
    elif req == 'preorder':
        processing(ads, description, times, req)
        ptel_num = list(tel_num)
        ptel_num.remove("7")
        ptel_num = ''.join(ptel_num)

        return render_template('cool.html', ads=ads, tel_num=ptel_num, note=note, res='ПРЕДЗАКАЗ', status=status)
    else:
        th = Thread(target=processing, args=(ads, description, times, req))
        th.start()
        return redirect('/')


def processing(ads, description, times, req) -> None:
    """Load email from Gmail and safe data in Google Sheet"""
    print('Processing start')
    global correct_num, tel_num, status, globalcounst, pr
    pr = 'start'
    globalcounst = 'start'
    tel_num = update_num(mail)
    tel_num = ''.join(list(tel_num))
    c = 0
    print('Processing while start')
    while True:
        if correct_num == tel_num:
            if c < 4:
                tel_num = update_num(mail)
                c += 1
                print('While processing lose')
                continue
        break
    print('Processing while end')
    if req == 'order':
        r = 'Курьер'
        cel = 1
        if tel_num == correct_num:
            print('ВНИМАНИЕ! Полученный номер совпал с предыдущим!')
            th2 = Thread(target=save_data, args=(times, tel_num+' ВНИМАНИЕ! Полученный номер совпал с предыдущим!', ads, r, cel))
            th2.start()
            status = 'ПРОВЕРЬ НОМЕР!'
        else:
            print('Получена информация: ', time, tel_num, ads, r)
            th2 = Thread(target=save_data, args=(times, tel_num, ads, r, cel))
            th2.start()
            status = 'ОК'
    elif req == 'preorder':
        cel = 1
        if tel_num == correct_num:
            print(' ВНИМАНИЕ! Полученный номер совпал с предыдущим!')
            th2 = Thread(target=save_data, args=(times, tel_num+' ВНИМАНИЕ! Полученный номер совпал с предыдущим!', ads, 'Предзаказ', cel))
            th2.start()
            status = 'ПРОВЕРЬ НОМЕР!'
        else:
            th2 = Thread(target=save_data, args=(times, tel_num, ads, 'Предзаказ', cel))
            th2.start()
            print('Получена информация: ', times, tel_num, ads, 'Предзаказ')
            status = 'ОК'
    elif req == 'lose':
        cel = 1
        if tel_num == correct_num:
            print(' ВНИМАНИЕ! Полученный номер совпал с предыдущим!')
            th2 = Thread(target=save_data, args=(times, tel_num+' ВНИМАНИЕ! Полученный номер совпал с предыдущим!', ads, 'Недожал. ' + description, cel))
            th2.start()
            status = 'ПРОВЕРЬ НОМЕР!'
        else:
            th2 = Thread(target=save_data, args=(times, tel_num, ads, 'Недожал. ' + description, cel))
            th2.start()
            print('Получена информация: ', times, tel_num, ads, 'Недожал. ' + description)
            status = 'ОК'
    elif req == 'pass':
        cel = 0
        if tel_num == correct_num:
            print(' ВНИМАНИЕ! Полученный номер совпал с предыдущим!')
            th2 = Thread(target=save_data, args=(times, tel_num+' ВНИМАНИЕ! Полученный номер совпал с предыдущим!', ads, 'Нецелевой. ' + description, cel))
            th2.start()
            status = 'ПРОВЕРЬ НОМЕР!'
        else:
            print('Получена информация: ', times, tel_num, ads, 'Нецелевой. ' + str(description))
            th2 = Thread(target=save_data, args=(times, tel_num, ads, 'Нецелевой. ' + description, cel))
            th2.start()
            status = 'ОК'
    correct_num = tel_num
    globalcounst = 0
    print('Processing end')
    pr = 0


if __name__ == '__main__':
    app.debug = True
    app.run()
