from amag.vehicle_data import VehicleData


if __name__ == "__main__":
    vd = VehicleData(
        "amag/data/data.npy"
    )

    x = lambda o, id: o.df[o.df["id"] == id]
    data_segment = vd.filter(x(vd, 0))

    vd.plot(data_segment)
