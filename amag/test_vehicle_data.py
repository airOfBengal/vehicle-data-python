import pytest
from .vehicle_data import VehicleData


class TestVehicleData:
    @pytest.fixture
    def vehicle_data(self):
        return VehicleData(
            "E:\\Projects\\Interviews\\pythonAssignmentV2\\amag\\data\\data.npy"
        )

    def test_segment(self, vehicle_data):
        data = vehicle_data.segment_by_id(0)
        assert data.shape[0] > 0

    def test_invalid_segment_id(self, vehicle_data):
        data = vehicle_data.segment_by_id(150)
        assert data.shape[0] == 0

    def test_filter_list_of_lats_lngs(self, vehicle_data):
        def get_data(df, id):
            return df[df["id"] == id][["x", "y"]]

        data = vehicle_data.filter(get_data, 1)
        assert data.shape[0] > 0
        assert data.shape[1] == 2

    def test_filter_empty_list_of_lats_lngs(self, vehicle_data):
        def get_data(df, id):
            return df[df["id"] == id][["x", "y"]]

        data = vehicle_data.filter(get_data, -1)
        assert data.shape[0] == 0
        assert data.shape[1] == 2

        data = vehicle_data.filter(get_data, 200)
        assert data.shape[0] == 0
        assert data.shape[1] == 2
