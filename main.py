from amag.vehicle_data import VehicleData


def get_data(df, id):
    return df[df["id"] == id][["x", "y"]]


if __name__ == "__main__":
    vd = VehicleData(
        "amag/data/data.npy"
    )

    data_segment = vd.filter(get_data, 0)

    vd.plot(data_segment)
