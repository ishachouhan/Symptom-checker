import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import lightgbm as lgb
import pickle
from sklearn.preprocessing import LabelEncoder
import re
#df=pd.read_csv("")
def Decisiontree_classifier(x_train, y_train):
  
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
            criterion = "entropy", random_state = 100,
            max_depth = 3, min_samples_leaf = 5)
  
    # Performing training
    clf_entropy.fit(x_train, y_train)
    return clf_entropy

def naivebias_classifier(x_train, y_train):
    gnb = GaussianNB()
    gnb.fit(x_train, y_train)
    return gnb

def lgbm_classifier(x_train, y_train):
    lgbclf = lgb.LGBMClassifier()
    lgbclf.fit(x_train, y_train)
    return lgbclf


df=pd.read_csv("symptoms.csv")
df = df.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
print(df.columns)
x_train=df.iloc[:,0:-2]
y_train=df["D_trans"]
#x_train , x_test , y_train , y_test = train_test_split(x,y, test_size =0.25, random_state =10)
LGBM_classifier=lgbm_classifier(x_train, y_train)
pickle.dump(LGBM_classifier, open("LGBM_classifier.sav", 'wb'))
#loaded_model = pickle.load(open(filename, 'rb'))
NB_classifier=naivebias_classifier(x_train, y_train)
pickle.dump(NB_classifier, open("NB_classifier.sav", 'wb'))
DT_classifier= Decisiontree_classifier(x_train, y_train)
pickle.dump(DT_classifier, open("DT_classifier.sav", 'wb'))
