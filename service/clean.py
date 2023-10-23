import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from .paths import *


def run_feature_clean(new_data: Path = None):
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
