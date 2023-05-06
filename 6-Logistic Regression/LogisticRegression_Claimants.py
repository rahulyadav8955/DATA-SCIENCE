import pandas as pd
import numpy as np

#Importing Data
claimants1 = pd.read_csv("C:/Datasets_BA/Logistic regression/claimants.csv",sep=",")

#removing CASENUM
claimants1 = claimants1.drop('CASENUM', axis=1)
claimants1.head(11)

# Imputating the missing values           
# claimants = claimants1.apply(lambda x:x.fillna(x.value_counts().index[0]))

### Splitting the data into train and test data 
from sklearn.model_selection import train_test_split
train_data,test_data = train_test_split(claimants1,test_size = 0.3) # 30% test data

# Model building 
import statsmodels.formula.api as sm
logit_model = sm.logit('ATTORNEY ~ CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT',data = train_data).fit()

#summary
logit_model.summary()

predict = logit_model.predict(pd.DataFrame(test_data[['CLMAGE','LOSS','CLMINSUR','CLMSEX','SEATBELT']]))

from sklearn.metrics import confusion_matrix

cnf_matrix = confusion_matrix(test_data['ATTORNEY'], predict > 0.5 )
cnf_matrix

accuracy = (149+120)/(149+47+86+120)
accuracy
