# import os
import requests
import random
import streamlit as st
# from dotenv import load_dotenv

# load_dotenv()

# url = os.getenv('API_URL')

# headers = {
#     "X-RapidAPI-Key": os.getenv('API_KEY'),
#     "X-RapidAPI-Host": os.getenv('API_HOST')
# }

url = st.secrets['API_URL']

headers = {
    "X-RapidAPI-Key": st.secrets['API_KEY'],
    "X-RapidAPI-Host": st.secrets['API_HOST']
}

def get_background(response:dict):
    images = []

    for image in response["titleMainImages"]["edges"]:
        images.append(image["node"]["url"])

    return images

def get_genres(response:dict):
    genres = response["genres"]["genres"]
    genres_list = []

    for genre in genres:
        genres_list.append(genre["id"])

    return str(genres_list).replace("'", "").replace("[", "").replace("]", "")

def get_directors(response:dict):
    directors = response["directors"][0]["credits"]
    directors_list =[]

    for director in directors:
        directors_list.append(director["name"]["nameText"]["text"])

    return str(directors_list).replace("'", "").replace("[", "").replace("]", "")

def get_details(id:str):
    querystring = {"id": id}

    response = requests.get(url, headers=headers, params=querystring).json()

    result = {
        "title": response["titleText"]["text"],
        "directors": get_directors(response),
        "year": response["releaseYear"]["year"],
        "genres": get_genres(response),
        "poster": response["primaryImage"]['url'],
        "background": get_background(response)
    }

    return result