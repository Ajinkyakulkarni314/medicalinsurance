#This File have all the functions
import pickle
import json 
import config # File wecreated for paths
import numpy as np
import pandas as pd


class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region) -> None: # Creation of COnstructor func where we define all the necessary variable 
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+region

    def load_model(self):    # load_model is a funct with which we load our model
        with open(config.MODEL_FILE_PATH,'rb') as f:     # we stored model path in config file and taking it from there
            self.model=pickle.load(f)                     #we stored pickle file in variable and created instance of it


        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data=json.load(f)


    def get_predicted_charges(self):

        self.load_model()             # As we need these files for test data hence need to call this func too
        print('*'*30,self.json_data)

        region_index=self.json_data['columns'].index(self.region)

        test_array=np.zeros(len(self.json_data['columns']))

        test_array[0]=self.age
        test_array[1]=self.json_data['sex'][self.sex]         #label_encoded_data['sex'][sex]
        test_array[2]=self.bmi
        test_array[3]=self.children
        test_array[4]=self.json_data['smoker'][self.smoker]          # label_encoded_data['smoker'][smoker]
        test_array[region_index]=1

        print ('Test Array:--',test_array) 

        predicted_charges=self.model.predict([test_array]) 

        return predicted_charges  


if __name__=='__main__':
    age= 67.0
    sex='male'
    bmi=28.3
    children=3
    smoker='yes'
    region='southeast'

    med_ins=MedicalInsurance( age ,sex,bmi,children,smoker,region)
    med_ins.get_predicted_charges