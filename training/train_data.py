import pandas as pd
from numpy.random import uniform

temp_pred_typical_error = TEMP_ERROR = 0.547  # расчет в ноутбуке temp_coefficient_calc


def prep_test_X(test_dataset: pd.DataFrame) -> pd.DataFrame:
    td = test_dataset.copy()

    td['temp_pred'].fillna(test_dataset['temp_pred'].mean(), inplace=True)
    td['temp'].fillna(td['temp'].mean(), inplace=True)
    td.set_index('datetime', inplace=True)
    td.sort_index(inplace=True)
    td = td.astype('float32')
    td = td[['temp', 'time', 'temp_pred']]
    td['temp'] = replace_temp_random(td['temp_pred'])
    # print(td)
    return td


def replace_temp_random(t: pd.Series):
    global TEMP_ERROR
    return t + uniform(-TEMP_ERROR, TEMP_ERROR, size=len(t))
