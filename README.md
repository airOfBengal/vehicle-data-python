# vehicle-data-python
This project is to evaluate vector data that is directly taken from videos showing vehicles driving over a scene (e.g intersection). This vector data is a set of trajectories on a latitudinal/longitudinal plain.
Given data is evaluated implemeinting a VehicleData class following OOP approach.

#### To Run this Project:
- Create a python virtual environment using the following command:
  `python -m venv venv`
- Activate the virtual environment on Windows OS:
  `venv\Scripts\activate`
  Or on Unix system:
  `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Run python test: `pytest amag/test_vehicle_data.py`
- Run project: `python main.py`

*Note: You may need to update the data file path based on your OS you are using to run this project.
