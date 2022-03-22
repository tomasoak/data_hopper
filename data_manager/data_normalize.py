import pandas as pd

# pyment -w -o numpydoc data_normalize.py -- generates automatic docstrings

def print_name(name=None):
    """ Test function """
    if name:
        print("Hello", name)
    else:
        print("Hello stranger")


def normalize_string(df: pd.DataFrame, col: str, case=None, clean=False):
    """
    Adjust column value characters encoding to UTF-8.
    Case parameter makes your column string upper, lower or titlecase
    If clean:
        Removes special characters such as whitespace, ".", "-", "/", ",", '"'

    Parameters
    __________
    df : pandas Dataframe
        input DataFrame
    col : string 
        string column to be normalize
    case : string
        lower or upper string values
    clean : bool
        remove specific characters

    Returns
    _______
    df: pandas DataFrame

    Example
    _______
        df = pd.DataFrame(
            columns=["id",  "name"],
            data=[  [  1,   "john coltra.ne"],
                    [  2,   "eLLa FiTzger-d"],
                    [  3,   "MiLes DaviS"]])
        df = normalize_string(df, name, case="title", clean=True)       

        returns:
        `df = pd.DataFrame(
            columns=["id",  "name"],
            data=[  [  1,   "John Coltrane"],
                    [  2,   "Ella Fitzgerald"],
                    [  3,   "Miles Davis"]])`
    """
    df[col] = (
        df[col]
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
    )
    if case is None:
        df[col] = df[col]
    elif case == "lower":
        df[col] = df[col].str.lower()
    elif case == "upper":
        df[col] = df[col].str.upper()
    elif case == "title":
        df[col] = df[col].str.title()
    else:
        raise ValueError("The chosen case must be 'lower' or 'upper'.")

    if clean is True:
        df[col] = (
            df[col]
            .str.replace(" ", "")
            .str.replace(".", "")
            .str.replace("-", "")
            .str.replace("/", "")
            .str.replace(",", "")
            .str.replace('"', "")
        )
    else:
        df[col] = df[col]

    return df

def rename(df, columns):
    """ Rename columns """
    return df.rename(columns=columns, errors="raise")