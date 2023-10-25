import pandas as pd
from service.paths import *
from sys import argv
from service.load import get_model
from training.train_data import prep_test_X
from datetime import datetime as dt
from service.clean import prepare_raw
if len(argv) > 1:
    new_data = path_to_data_dir / Path(argv[1])
    # run_feature_clean(new_data)
try:
    new_test = pd.read_csv(new_data)
except FileNotFoundError:
    print("Новый датасет кладите в папку проекта data")
    exit(1)

model = get_model()


def get_temp_forecast_by_24(df: pd.DataFrame):
    result = []
    df = prepare_raw(df,["date", 'weather_fact', "weather_pred"])
    for i in range(0, len(df), 24):
        slice_end = min(i + 24, len(df))
        result.append(prep_test_X(df.iloc[i:slice_end]))
    return result


forecast = get_temp_forecast_by_24(new_test)
energy_set = pd.DataFrame(columns=["date", "predict"])

predicts=[]
dates=[]
for day in forecast:
    # print(day)
    energy = model.predict(day)
    predicts.append(sum(energy))
    last_row_dt = day.iloc[1].name
    # print(last_row)
    date_to_wr = dt.fromtimestamp(int(last_row_dt.timestamp())).date()
    # print(date_to_wr)
    dates.append(date_to_wr)
energy_set["predict"] = predicts
energy_set["date"] = dates
energy_set.to_csv(path_to_data_dir / Path("result.csv"), float_format='%.2f', mode='w',index=False)

