def send_email(massage, recipient, *, sender='university.help@gmail.com'):

    text = '@'
    text2 = '.ru'
    text3 = '.com'
    text4 = '.net'
    y = 1
    while y <= 5:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
            y += 5
        elif not ((text4 in recipient) or (text2 in recipient) or (text3 in recipient)) and (text in recipient):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            y += 5
        elif not ((text4 in sender) or (text2 in sender) or (text3 in sender)) and (text in sender):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            y += 5
        elif sender != 'university.help@gmail.com':
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса',sender, 'на адрес', recipient)
            y += 5
        else:
            print('Письмо успешно отправлено  с адреса', sender, 'на адрес', recipient)
            y += 5



send_email('Это сообщение для проверки связи','vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!','urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре','urban.teacher@mail.ru', sender='urban.teacher@mail.ru')