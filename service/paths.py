from pathlib import Path
from shutil import copyfile
import json

NOTEBOOKS_FOLDER = Path("notebooks/")
DATA_FOLDER = Path("data/")
NOTE_DATA_PREP_NAME = 'preparing_raw_dataset.ipynb'
SERVICE_FOLDER = Path("service/")
DEFAULT_DATA_TO_PREP = Path("backup/train_dataset.csv")
DEFAULT_TEST_DATA = Path("test_dataset.csv")
MODEL_FOLDER = Path("model/")

root_path = Path(__file__).resolve(strict=True).parents[1]
path_to_note_dir = root_path / NOTEBOOKS_FOLDER
path_to_data_dir = root_path / DATA_FOLDER


def init_config():
    global root_path,SERVICE_FOLDER
    with open(root_path/SERVICE_FOLDER/"cfg.json", "w", encoding="UTF-8") as c_f:
        config = {
            "RAW_DATA_NAME": str(Path("unprepared.csv"))
        }
        json.dump(config, c_f)


def get_path_to_raw_data() -> Path:
    global path_to_data_dir,SERVICE_FOLDER,root_path
    built_path = root_path/SERVICE_FOLDER/Path("cfg.json")
    print(built_path)
    with open(built_path, "r", encoding="UTF-8") as c_f:
        config = json.load(c_f)
        return path_to_data_dir / config['RAW_DATA_NAME']


def replace_raw_data(name=DEFAULT_DATA_TO_PREP):
    """
    Перезаписывает рабочий файл для подгрузки датасета в ноутбук подготовки данных
    :param name: имя файла, который должен будет обработать ноутбук NOTE_DATA_PREP_NAME(=preparing_raw_dataset.ipynb)
    по умолчанию возвращает исходник DEFAULT_DATA_TO_PREP(=backup/train_dataset.csv) на место RAW_DATA_NAME(=unprepared.csv)
    :return:
    """
    if not isinstance(name, Path):
        name = Path(name)
    global root_path, SERVICE_FOLDER
    with open(root_path/SERVICE_FOLDER/Path("cfg.json"), "w", encoding="UTF-8") as c_f:
        config = json.load(c_f)
        config['RAW_DATA_NAME'] = name
        json.dump(config, c_f)
        # copyfile(name, RAW_DATA_NAME)

if __name__ == "__main__":
    init_config()