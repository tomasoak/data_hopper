import pandas as pd
from pandas.testing import assert_frame_equal
from ds_toolkit.data_manager.data_normalize import normalize_string

def test_normalize_string():
  df = pd.DataFrame(columns=["id", "name"],
            data=[[1,"john coltRanE-"],
                    [2,"eLLa FiTzgeralD"],
                    [3,"MiLes DaviS"]])

  df_clean = pd.DataFrame(columns=["id","name"],
            data=[[1, "John Coltrane"],
                    [2, "Ella Fitzgerald"],
                    [3, "Miles Davis"]])             

  df = normalize_string(df, "name", case="title", clean=True)
  # assert_frame_equal(df, df_clean)
  assert all(df["name"] == df_clean["name"])