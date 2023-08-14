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
        """Selects a subset from the data using a specific id.

        Args:
            id (int): To get all the samples associated with the id number.

        Returns:
            Dataframe: Subset of data associated with the id, Empty otherwise.
        """
        if self.df is not None:
            return self.df[self.df["id"] == id]
        return pd.DataFrame()

    def filter(self, fun):
        """To filter based on input functions.

        Args:
            fun (function): To get all the samples associated with the id number.

        Returns:
            Dataframe: List of latitudinal and longitudinal values of the trajectory, Empty otherwise.
        """
        return fun[["x", "y"]]
