from joblib import load
from  service.paths import MODEL_FOLDER,Path,root_path

def get_model(name: str = "trained.joblib"):

    return load(root_path / MODEL_FOLDER / Path(name))
