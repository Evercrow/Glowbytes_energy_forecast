# Glowbytes_energy_forecast
обучаем нейронку для предсказания потребления энергии

# Запуск
*Если проект скачан из репозитория(кнопка Код->Скачать архивом), то сначала получите файл модели(из-за размера на репо не попал),
для этого запустите ноутбук ***notebooks/maria_model.ipynb*** 

Для работы кладем проверочный датасет в папку **data** и запускаем в командной строке:

    python main.py [имя csv-файла, например, secret.csv]
Результат сохраняется в корне, файл **result.csv**  

# Обучение
Велось через ноутбук **maria_model.ipynb**
Модель обучена по методу RandomForestRegressor ,
по столбцам time,temp,temp_pred 


# Логика работы программы
1) Подаваемый командной строкой датасет обрезает лишние колонки и создает колонку datetime для дальнейшей сортировки по времени(индекс-колонка) через **clean.prepare_raw**. 
2) Датасет нарезается по 24 часа и подается на обработку в модуль train_data
3) Задача train_data -это выделение тех же признаков, по которым обучалась модель.  
Происходит сортировка по datetime;
при необходимости,train_data заменяет неизвестные данные  рандомными в рассчитаном диапазоне или усредненными значениями;
на выход получаем shape c нужными колонками признаков, индексов по datetime и длиной в 24 записи
*Например, расчет диапазона случайной поправки для заполнения неизвестной фактической температуры от известной температуры прогноза, в ноутбуке **temp_coefficient_cal***
5) В предобученную модель(загружается из 'model\trained.joblib') подаются упакованные в предыдущем шаге блоки признаков за 24 часа, отражающие 1 день, на которые просят прогноз(дата и часы известны всегда, прогноз берется из данных или подгружается из интернета).
6) Полученный прогноз за 24 часа суммируется и пишется в результирующий 'data\result.csv' файл с меткой даты.

# ToDO:
- Предсказание только по дате:
  1) Парсер температуры по часам из яндекса на конкретную дату и регион
  2) Прогноз без входного датасета на конкретную дату и регион
- выделение и исследование категориальных признаков погоды
- парсинг и исследование дополнительных признаков из других источников
- предсказание и оценка по другим математическим моделям 




