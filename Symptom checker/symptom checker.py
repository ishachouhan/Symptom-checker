import pickle
import pandas as pd
from utils import *
import time
import numpy as np
from fuzzywuzzy import process
import nltk
import spacy
import pprint
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def main():
    # text = input('Please Enter your condition: ').lower()
    # Diseases(filtered_sentence=removeWords(text))

    print('Doc Bot: '+'Hi! What is your name?')
    name=input()
    print('Doc Bot: Hi ' + name +
                  ' What is your age (Enter only number)')


    while(True):
        user_input = input()
        userDetail(user_input)



def combined_model(test):
        LGBM_classifier=pickle.load(open("LGBM_classifier.sav", 'rb'))
        NB_classifier=pickle.load(open("NB_classifier.sav", 'rb'))
        DT_classifier=pickle.load(open("DT_classifier.sav", 'rb'))
        le2=pickle.load(open("label_encoder.sav", 'rb'))
        df=pd.read_csv("symptoms.csv")
        test1=[]
        for i in df.iloc[:,0:-2].columns:
            if i in test:
                    test1.append(1)
            else:
                    test1.append(0)
        test1=np.array(test1)
        test1=test1.reshape(1,-1)
        
        
        pred_lgbm=LGBM_classifier.predict(test1)
        pred_nb=NB_classifier.predict(test1)
        pred_dt=DT_classifier.predict(test1)
        print(pred_lgbm,pred_nb,pred_dt)

        if pred_lgbm==pred_nb:
                return le2.inverse_transform(pred_lgbm)
        elif pred_nb==pred_dt:
                return le2.inverse_transform(pred_nb)
        else:
                result=(le2.inverse_transform(pred_lgbm),"or",le2.inverse_transform(pred_nb),"or",le2.inverse_transform(pred_dt))
                return result
        




  



def removeWords(text):

    nlp = spacy.load("en_core_web_sm")
    nlp.Defaults.stop_words |= {"feeling", "little", "having",
                                "feel", 'age', 'years', 'old', 'name'}
    stop_words = set(nlp.Defaults.stop_words)

    word_tokens = word_tokenize(text)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    # for term in filtered_sentence:
    #     print(type(term))
    #     print(term + " This was from utils")
    return filtered_sentence




def userDetail(details):
    
    exit_list = ['exit', 'see you later', 'bye', 'quit', 'break', 'stop']

    temp = 'How can I assist you with, you may begin with how are you feeling, for example I am feeling cold'
    if details.isnumeric():
        age = int(details)

        print(temp)
        return age

    else:
        returned_word=removeWords(details)
        #print(returned_word)
        if returned_word in exit_list:
            print('Doc Bot: Chat with you later, and remember... stay safe!')
            exit()
                    
        else:
            print(combined_model(returned_word))
            print("\n\nDo you want suggestions of doctors in your area? (Enter yes/no)")
            choice=input()
            choice=choice.lower()
            if(choice=="yes"):
                print("Enter your city")
                city=input()
                city=city.lower()
                print("Enter your area")
                area=input()
                area=area.lower()
                area_doc(df1,area,city)
                
            else:
                print('Doc Bot: Chat with you later, and remember... stay safe!')
                exit()

if __name__ == "__main__":

    start_time = time.process_time()
    main()
    print(time.process_time() - start_time, "seconds")



    
    

