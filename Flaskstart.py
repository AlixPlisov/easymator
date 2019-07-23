#!/usr/bin/env python3
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


def evr():
    global pr
    while True:
        if pr == 'start':
                time.sleep(5)
                continue
        else:
            pr = 'start'
            ever_connect()
            pr = 0
            print('Подключение подтверждено, ждем 120с.')
            time.sleep(120)
            continue


ev = Thread(target=evr)
ev.start()


def get_time() -> 'time':
    tz = pytz.timezone('Europe/Moscow')
    times = datetime.now(tz=tz).strftime('%H:%M')
    print('Время загружено: ', times)
    return times


@app.route('/', methods=['GET', 'POST'])
def newstart():
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

    description = request.form.get('description')  # сделать async, имя во фронт
    note = request.form['note']
    note = ''.join(list(note))
    description = ''.join(list(description))
    times = get_time()  # сделать async
    req = request.form['res']
    while True:
        if pr == 'start':
            time.sleep(2)
            continue
        else:
            break
    if req == 'order':
        processing(description, times, req)
        ptel_num = list(tel_num)
        ptel_num.remove("7")
        ptel_num = ''.join(ptel_num)
        print('Заказ. Данные обработаны')
        return render_template('cool.html', ads=ads, tel_num=ptel_num, note=note, res='ЗАКАЗ', status=status)
    elif req == 'preorder':
        processing(description, times, req)
        ptel_num = list(tel_num)
        ptel_num.remove("7")
        ptel_num = ''.join(ptel_num)

        return render_template('cool.html', ads=ads, tel_num=ptel_num, note=note, res='ПРЕДЗАКАЗ', status=status)
    else:
        th = Thread(target=processing, args=(description, times, req))
        th.start()
        return redirect('/')


def processing(description, times, req):
    print('Работаю...')
    global correct_num, tel_num, status, globalcounst, pr, ads
    pr = 'start'
    globalcounst = 'start'
    tel_num, ads = update_num(mail)
    tel_num = ''.join(list(tel_num))
    c = 0
    print('Проверяю номер...')
    while True:
        if correct_num == tel_num:
            if c < 4:
                tel_num,ads = update_num(mail)
                c += 1
                print('Не удалось проверить номер, повторяю операцию...')
                continue
        break
    print('Успешно! отправляю данные браузеру...')
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
    print('Всё супер!')
    pr = 0


app.run(port=1024, debug=True)




