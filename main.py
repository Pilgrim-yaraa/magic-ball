import random

answers = ['Бесспорно',	'Мне кажется - да',	'Пока неясно, попробуй снова',	'Даже не думай',
'Предрешено',	'Вероятнее всего',	'Спроси позже',	'Мой ответ - нет',
'Никаких сомнений',	'Хорошие перспективы',	'Лучше не рассказывать',	'По моим данным - нет',
'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
user = input(f'Как вас зовут?  ')
print(f'Привет {user}')
user1 = input(f"Задайте вопрос: ")
while True:
    print(random.choice(answers))
    user1 = input(f'Хотите задать еще вопрос? ').lower()
    if user1 == "нет":
        print('Возвращайся если возникнут вопросы!')
        break
    user3 = input(f'{user} задайте вопрос ')
