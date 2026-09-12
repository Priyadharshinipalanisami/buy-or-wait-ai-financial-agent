import pandas as pd


def load_dataset():

    df = pd.read_csv(
        "data/sample_requests.csv"
    )

    return df


def clean_dataset(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove missing rows
    df = df.dropna(
        how="all"
    )

    return df


def get_dataset_summary(df):

    summary = {

        "total_records": len(df),

        "total_columns": len(df.columns),

        "missing_values":
        df.isnull().sum().sum()

    }

    return summary