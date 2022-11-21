import pandas as pd
import numpy as np


def transform_data(dataframe):
    dataframe["NPS interno"] = dataframe["NPS interno"].str.replace(
        ",", ".").astype("float")
    return dataframe
