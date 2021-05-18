import json
import pandas as pd
import numpy as np
from fuzzywuzzy import process
import nltk
import spacy
import pprint
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def Patient(disease):
    df = pd.read_csv('clean_csv.csv')
    data = df[df['Condition Name'] == disease].values.tolist()[0][2:]
    return data


def convert_to_dict(l1, l2):
    d = dict(zip(l1, l2))
    return d


def convert_dict_json(d):
    json_object = json.dumps(d, indent=4)
    return json_object


def Diseases(filtered_sentence):
    for word in filtered_sentence:
        # print(word)
        str2Match = word
        df = pd.read_csv('clean_csv.csv')
        strOptions = df[df['Condition Name'].notnull(
        )]['Condition Name'].values.tolist()
        # print(type(strOptions))
        # Ratios = process.extract(str2Match,strOptions)
        # print(Ratios)
        # You can also select the string with the highest matching percentage
        highest = process.extractOne(str2Match, strOptions)
        (disease, ratio) = highest
        if ratio > 70:
            l1 = ['name', 'overview', 'symptoms', 'prevention', 'treatment']
            print(disease, " and ", ratio)
            return convert_dict_json(convert_to_dict(l1, Patient(disease)))
        else:
            return word


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
        returned_word = Diseases(filtered_sentence=removeWords(details))
        if returned_word in exit_list:
            print('Doc Bot: Chat with you later, and remember... stay safe!')
            exit()
        elif len(returned_word) < 20:
            print('Doc Bot: Hi ' + returned_word +
                  ' What is your age (Enter only number)')
            
        else:
            print(returned_word)
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




                
df1=pd.read_csv("DoctorList.csv")
df1.drop(['Unnamed: 0'], axis = 1,inplace=True)


df1["area"]=df1["area"].str.lower()
df1["city"]=df1["city"].str.lower()


def area_doc(df,user_area,user_city):
    if df["city"].any()!=user_city:
        print("doctors for given city not available")
    elif df.area[df.city==user_city].any()!=user_area:
        
        print("doctors in the given area are not available, but below are some suggestions of doctors in other areas of your city")
        print(df[df.city==user_city].sample(n=5).to_string(index=False))

    else:
        print(df[(df.area==user_area) & (df.city==user_city)].to_string(index=False))
       

    

    
            






