#!/usr/bin/python

import pandas as pd
import pickle
import sys
import os

def predict_price(feat):

    #clf =  pickle.load(open(os.path.dirname(__file__) + '/price_clf.pkl', 'rb'))
    
    
    entrada = feat.split(',')
       # Create features
    feature = pd.DataFrame(columns=["Year","Mileage","State","Make","Model"])
    feature = feature.append({'Year': entrada[0], 'Mileage': entrada[1], 'State': entrada[2], 'Make': entrada[3], 'Model': entrada[4]}, ignore_index=True)
    
    #feature = pd.get_dummies(feature)
    # Make prediction
    #feature 
    #p1 = clf.predict_proba(url_.drop('url', axis=1))[0,1]

    return feature.iloc[0,0]

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please add features')
        
    else:

        feat = sys.argv[1]

        precio = predict_precio(feat)
        
        print(feat)
        print('Precio Probable: ', precio)
        