
# “Ассистент по досугу” RecomBot
## Задача
Реализовать чат-бота / веб-интерфейс для ассистента, который в диалоговой форме предлагает места для посещения или прогулки в зависимости от потребности пользователя. 
История задачи: достаточно часто люди сталкиваются с вопросом куда бы сходить развеяться и отдохнуть. Для этого они подписываются на многочисленные группы в телеграмме или в ВК, или спрашивают у друзей. Когда приходит время посоветовать место другу они называют первое что приходит в голову, называя либо не все, либо не учитывая предпочтения. Поэтому компания “Досуг и Ко” решила разработать централизованную систему проведения досуга и предложила вам реализовать прототип данной системы.


## Описание реализации

Данный бот написанн на языке программирования Python. Для его реализации была взята библиотека `telebot`. Для получения информации о локациях было использовано `2GIS Places API`.

## Установка зависимостей

`pip install -r requirements.txt`

## Добавить переменные окружения

В корне создать папку `.env` и в нее записать следующие переменные
```
TOKEN = "your_tg_token"
API_KEY = "your_2gis_api_key"
```

## Запуска бота

`python RecBot/bot.py `