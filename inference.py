import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl','rb'))
class_names=['27.9','31.5','20.6','1011.5','8.5']

def predict(df):
  df = df[['T', 'TM', 'Tm', 'SLP' ,'V']]
 
  predictions=model.predict([['T', 'TM', 'Tm', 'SLP' ,'V']])
  
  output=[class_names[class_predict] for class_predict in predictions]
  return output
