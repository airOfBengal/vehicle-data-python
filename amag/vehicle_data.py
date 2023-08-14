import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class VehicleData:
    def __init__(self, filepath, columns=["index", "id", "x", "y"]) -> None:
        try:
            self.df = pd.DataFrame(
                np.load(filepath),
                columns=columns,
            )
        except Exception as e:
            print(f"An error occurred: {e}")
            self.df = None

    def segment_by_id(self, id):
        if self.df is not None:
            return self.df[self.df["id"] == id]
        return pd.DataFrame()
