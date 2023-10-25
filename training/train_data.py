import pandas as pd


def prep_test_X(test_dataset: pd.DataFrame) -> pd.DataFrame:
    td = test_dataset.copy()

    td['temp_pred'].fillna(test_dataset['temp_pred'].mean(), inplace=True)

    td['temp'].fillna(td['temp'].mean(), inplace=True)
    td.set_index('datetime', inplace=True)
    td.sort_index(inplace=True)

    td = td.astype('float32')

    # test_dataset = test_dataset.apply(pd.to_numeric, errors='coerce')
    return td[['temp', 'time', 'temp_pred']]
