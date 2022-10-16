ТЗ в ReadmeTasks.md<br>
Инструкция по запуску в ReadmeStart.md<br>

<h1>Реализовано.</h1>

Используемый стек<br>
Django<br>
DRF<br>

Клиент вводит следующие данные:
<ol>
    <li>Стоимость объекта недвижимости, в рублях без копеек. Тип данных: integer</li>
    <li>Первоначальный взнос, в рублях без копеек. Тип данных: integer</li>
    <li>Срок, в годах. Выбирает из списка как в примере. Тип данных: integer</li>
    <li>Варианты сортировкм. Выбирает из списка - Сортировка ипотечных предложений
        по ставке(процент по ипотеке) и по платежу.</li>
</ol>


В ответ ему приходит массив с объектами ипотечных предложений.<br>
Как и в примере:
<ul>
    <li>если указаны как минимум Стоимость объекта недвижимости и Срок, в годах, то<br>
        В каждом объекте есть следующие данные:<br>
        <ol>
            <li>Наименование банка. Тип данных: string</li>
            <li>Ипотечная ставка, в процентах. Тип данных: float</li>
            <li>Платеж по ипотеке, в рублях без копеек.  Тип данных: integer</li>
            <li>Переплата, в рублях без копеек. Как в примере. Тип данных: integer</li>
        </ol>
        <p align="center">
            <img src="https://github.com/zorokonStepan/MortgageCalculator_DjangoDRF/raw/main/img_git/mort1.png" width="450"
           title="mort1">
        </p>
    </li>
    <li>если не указаны Стоимость объекта недвижимости и Срок, в годах, то<br>
        В каждом объекте есть следующие данные:<br>
        <ol>
            <li>Наименование банка. Тип данных: string</li>
            <li>Ипотечная ставка, в процентах. ОТ-ДО. Тип данных: float</li>
            <li>Возможная сумма кредита, ОТ-ДО, в рублях без копеек.  Тип данных: integer</li>
            <li>Первоначальный взнос, ОТ-ДО, в процентах. Тип данных: integer</li>
        </ol>
        <p align="center">
            <img src="https://github.com/zorokonStepan/MortgageCalculator_DjangoDRF/raw/main/img_git/mort2.png" width="450"
           title="mort2">
        </p>
    </li>
    <li>
        если указаны Стоимость объекта недвижимости и Срок, в годах, то
        можно вывести данные с сортировкой по Сортировка ипотечных предложений
        по ставке(процент по ипотеке) и по платежу, в противном случае дуступна
        сортировка только по по ставке(процент по ипотеке)
        <p align="center">
        <img src="https://github.com/zorokonStepan/MortgageCalculator_DjangoDRF/raw/main/img_git/mort3.png" width="450"
        title="mort3">
        </p>
        <p align="center">
        <img src="https://github.com/zorokonStepan/MortgageCalculator_DjangoDRF/raw/main/img_git/mort4.png" width="450"
        title="mort4">
        </p>
    </li>
</ul>


Технические требования<br>
<ol>
    <li>Написана - модель для хранения ипотечных предложений.</li>
    <li>Реализован - ViewSet для реализации функционала CRUD ипотечных предложений.</li>
    <li>Реализована - Фильтрация ипотечных предложений, по введенным параметрам.</li>
    <li>Реализован - функционал, который будет рассчитывать платеж у всех валидных ипотечных предложений.</li>
    <li>Сортировка ипотечных предложений по ставке(процент по ипотеке) и по платежу.</li>
</ol>

<h2>API:</h2>
<ol>
    <li>GET Получение списка всех ипотечных предложений http://localhost:8000/api/offer
        <p align="center">
        <img src="https://github.com/zorokonStepan/MortgageCalculator_DjangoDRF/raw/main/img_git/api_get.png" width="450"
        title="api_get">
    </li>
    <li>POST Создание http://localhost:8000/api/offer/
        <p align="center">
        <img src="https://github.com/zorokonStepan/MortgageCalculator_DjangoDRF/raw/main/img_git/api_post.png" width="450"
        title="api_post">
    </li>
    <li>PATCH Изменение http://localhost:8000/api/offer/12/
        <p align="center">
        <img src="https://github.com/zorokonStepan/MortgageCalculator_DjangoDRF/raw/main/img_git/api_patch.png" width="450"
        title="api_patch">
    </li>
    <li>DEL Удаление http://localhost:8000/api/offer/12/
        <p align="center">
        <img src="https://github.com/zorokonStepan/MortgageCalculator_DjangoDRF/raw/main/img_git/api_del.png" width="450"
        title="api_del">
    </li>
    <li>GET Фильтры иптечных предложений http://localhost:8000/api/offer/?price=10000000&deposit=10&term=20
        <p align="center">
        <img src="https://github.com/zorokonStepan/MortgageCalculator_DjangoDRF/raw/main/img_git/api_get_param.png" width="450"
        title="api_get_param">
    </li>
</ol>