import pandas as pd

def detailed(df: pd.DataFrame) -> pd.DataFrame:
    desc = df.describe().T.round(2)
    desc["variance"] = (desc["std"] ** 2).round(2)
    desc["z_score(median)"] = (
        (df.median(numeric_only=True) - desc["mean"]) / desc["std"]
    ).round(2)
    return desc
