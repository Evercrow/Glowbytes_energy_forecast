import codecs
from json import load
from pathlib import Path

NOTEBOOKS_FOLDER = Path("notebooks/")
filename = 'preparing_starter_dataset.ipynb'
path_to_data_dir = Path(__file__).resolve(strict=True).parent / NOTEBOOKS_FOLDER


with codecs.open(path_to_data_dir / Path(filename)) as fp:
    nb = load(fp)
    print(nb)

# for cell in nb['cells']:
#     if cell['cell_type'] == 'code':
#         source = ''.join(line for line in cell['source'] if not line.startswith('%'))
#         exec(source, globals(), locals())