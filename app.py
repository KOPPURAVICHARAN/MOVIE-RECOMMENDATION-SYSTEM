

import streamlit as st
import pickle


movies=pickle.load(open("movies_list.pk1","rb"))
similarity=pickle.load(open("similarity.pk1","rb"))
movies_list=movies['title'].values
st.header("movie recommendation system")
selected_movie=st.selectbox("select a movie :",movies_list)

import streamlit.components.v1 as components

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    for i in distance[1:6]:
        mobies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie
if st.button("Show Recommend"):
    movie_name=recommend(selected_movie)
    c1,c2,c3,c4,c5=st.columns(5)
    with c1:
        st.text(movie_name[0])
    with c2:
        st.text(movie_name[1])
    with c3:
        st.text(movie_name[2])
    with c4:
        st.text(movie_name[3])
    with c5:
        st.text(movie_name[4])