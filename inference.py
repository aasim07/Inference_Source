import pickle

pickle_in = open("Random_forest_regressor.pkl","rb")
random_forest_regressor=pickle.load(pickle_in)

def predict(Average_Temperature,Maximum_Temperature,Minimum_Temperature,Atm_pressure_at_sea_level,Average_wind_speed):


  output=random_forest_regressor.predict([[ Average_Temperature,Maximum_Temperature,Minimum_Temperature, Atm_pressure_at_sea_level,Average_wind_speed]])

  return output