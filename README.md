# Glowbytes_energy_forecast
обучаем нейронку для предсказания потребления энергии

# Запуск
Для работы кладем проверочный датасет в папку **data** и запускаем в командной строке:

    python main.py [имя csv-файла, например, secret.csv]
Результат сохраняется в корне, файл **result.csv**  

# Обучение
Велось через ноутбук **maria_model.ipynb**
Модель обучена по методу RandomForestRegressor ,
по столбцам time,temp,temp_pred 


