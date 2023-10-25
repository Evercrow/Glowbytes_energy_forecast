import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from .paths import *
import pandas as pd


def run_feature_clean_notebook(new_data: Path = None):
    """
    Прогоняем ноутбук NOTE_DATA_PREP_NAME с подготовкой данных unprepared.csv

    :param new_data: При передаче объекта пути, unprepared.csv перезаписывается на переданный файл
    (должен лежать в той же папке data)
    :return: перезаписывается numeric_features.csv
    """
    if new_data is not None:
        replace_raw_data(new_data)
    else:
        init_config()
    with open(path_to_note_dir / Path(NOTE_DATA_PREP_NAME), "r", encoding="UTF-8") as fp:
        nb_in = nbformat.read(fp, nbformat.NO_CONVERT)
        ep = ExecutePreprocessor(timeout=600)  # , kernel_name='python3')
        ep.preprocess(nb_in)


def prepare_raw(df: pd.DataFrame, cut_cols: list):
    def make_dt_col(row_date, row_time):
        return pd.to_datetime(row_date) + pd.to_timedelta(row_time, unit='h')

    df['datetime'] = df.apply(lambda x: make_dt_col(x['date'], x['time']), axis=1)
    df = df.drop(["date", 'weather_fact', "weather_pred"], axis=1)
    return df
