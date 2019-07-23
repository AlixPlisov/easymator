voronezg = eval(open('/Users/access/Documents/automator+R/Project/voronezg.txt', 'r').read())
volgograd = eval(open('/Users/access/Documents/automator+R/Project/volgograd.txt', 'r').read())
spb = eval(open('/Users/access/Documents/automator+R/Project/spb.txt', 'r').read())
samara = eval(open('/Users/access/Documents/automator+R/Project/samara.txt', 'r').read())
rnd = eval(open('/Users/access/Documents/automator+R/Project/rnd.txt', 'r').read())
ekb = eval(open('/Users/access/Documents/automator+R/Project/ekb.txt', 'r').read())
krd = eval(open('/Users/access/Documents/automator+R/Project/krd.txt', 'r').read())
mobilki = eval(open('/Users/access/Documents/automator+R/Project/mobilki.txt', 'r').read())
nsk = eval(open('/Users/access/Documents/automator+R/Project/nsk.txt', 'r').read())
nn = eval(open('/Users/access/Documents/automator+R/Project/nn.txt', 'r').read())

# Здесь должен быть файл с сип линиями

generaldict = {**voronezg,**volgograd,**spb,**samara,**rnd,**ekb,**krd,**mobilki,**nsk}
for i in generaldict:
    if i in raw_email_string:
        print(generaldict[i])
        reklama = generaldict[i]



sip = '''ekb_partner@vpbx300326172.mangosip.ru;ЕКБ партнер 1 клиентский;
        line10885@vpbx300326172.mangosip.ru;Lenovo (РНД);
        line11669@vpbx300326172.mangosip.ru;Самсунг  (ВЛГ);
        line12792@vpbx300326172.mangosip.ru;Самсунг  (РНД);
        line14738@vpbx300326172.mangosip.ru;Мега (СМР);
        line18707@vpbx300326172.mangosip.ru;Apple  (ВР);
        line19150@vpbx300326172.mangosip.ru;КИТ  (РНД);
        line19392@vpbx300326172.mangosip.ru;КИТ  (СПБ);
        line20426@vpbx300326172.mangosip.ru;IT Скупка  (НН);
        line20725@vpbx300326172.mangosip.ru;IT Скупка (РНД);
        line21399@vpbx300326172.mangosip.ru;IT Скупка (КРС);
        line23760@vpbx300326172.mangosip.ru;Lenovo (НН);
        line26719@vpbx300326172.mangosip.ru;IT Скупка (СМР);
        line27236@vpbx300326172.mangosip.ru;Apple  (Самара);
        line28909@vpbx300326172.mangosip.ru;Мега  (РНД);
        line29731@vpbx300326172.mangosip.ru;КИТ  (НН);
        line31053@vpbx300326172.mangosip.ru;Самсунг  (НСК);
        line31404@vpbx300326172.mangosip.ru;Apple (РНД);
        line31586@vpbx300326172.mangosip.ru;КИТ  (ВЛГ);
        line34811@vpbx300326172.mangosip.ru;КИТ  (ВР);
        line38853@vpbx300326172.mangosip.ru;Мега  (НСК);
        line39298@vpbx300326172.mangosip.ru;Мега  (КРС)
        line40348@vpbx300326172.mangosip.ru;Скупка  (ВР);
        line40442@vpbx300326172.mangosip.ru;Lenovo (ВНЖ);
        line40787@vpbx300326172.mangosip.ru;Apple  (ЕКБ);
        line41403@vpbx300326172.mangosip.ru;Apple new (ЕКБ);
        line41799@vpbx300326172.mangosip.ru;Huawei (СПБ);
        line46073@vpbx300326172.mangosip.ru;IT Скупка (ВЛГ);
        line46748@vpbx300326172.mangosip.ru;Apple new (НН);
        line46841@vpbx300326172.mangosip.ru;Apple  (КРС);
        line48137@vpbx300326172.mangosip.ru;Мега  (ВРН);
        line51472@vpbx300326172.mangosip.ru;Самсунг  (ВР);
        line51504@vpbx300326172.mangosip.ru;I-Assist (НСК);
        line52461@vpbx300326172.mangosip.ru;Lenovo (СПБ);
        line53061@vpbx300326172.mangosip.ru;КИТ  (Самара);
        line65175@vpbx300326172.mangosip.ru;КИТ  (КРС);
        line65624@vpbx300326172.mangosip.ru;IT Скупка (СПБ);
        line66647@vpbx300326172.mangosip.ru;Мега (СПБ);
        line66795@vpbx300326172.mangosip.ru;Самсунг  (СПБ);
        line70121@vpbx300326172.mangosip.ru;Мега (НН);
        line71914@vpbx300326172.mangosip.ru;Самсунг  (НН);
        line72629@vpbx300326172.mangosip.ru;I-Assist  (СПБ);
        line72713@vpbx300326172.mangosip.ru;Apple new (КРС);
        line75557@vpbx300326172.mangosip.ru;IT Скупка  (ЕКБ);
        line76265@vpbx300326172.mangosip.ru;Самсунг  (КРС);
        line76843@vpbx300326172.mangosip.ru;Самсунг  (Самара);
        line77757@vpbx300326172.mangosip.ru;КИТ  (ЕКБ);
        line79261@vpbx300326172.mangosip.ru;Самсунг  (ЕКБ);
        line81200@vpbx300326172.mangosip.ru;Apple new (ВНЖ);
        line81475@vpbx300326172.mangosip.ru;Apple new (РНД);
        line82989@vpbx300326172.mangosip.ru;Apple  (СПБ);
        line85479@vpbx300326172.mangosip.ru;Мега  (ВЛГ);
        line87200@vpbx300326172.mangosip.ru;Apple new (СПБ);
        line87759@vpbx300326172.mangosip.ru;Lenovo (ЕКБ);
        line88983@vpbx300326172.mangosip.ru;Apple  (НН);
        line98297@vpbx300326172.mangosip.ru;Apple  (ВЛГ);
        nn_partner@vpbx300326172.mangosip.ru;НН Люстей клиентский;
        novosib_partner1@vpbx300326172.mangosip.ru;НСК партнер 1;
        partner1_samara@vpbx300326172.mangosip.ru;СМР Партнер 1;
        rnd_partner@vpbx300326172.mangosip.ru;РНД Люстей клиентский;
        vlg_partner@vpbx300326172.mangosip.ru;ВЛГ Люстей клиентский;
        vor_partner@vpbx300326172.mangosip.ru;ВОР Люстей клиентский;'''





text, encoding = email.header.decode_header(raw_email_string)[0]
text.decode('utf-8')































