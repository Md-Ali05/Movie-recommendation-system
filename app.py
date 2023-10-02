import streamlit as st
import pickle
import time
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Content based Movie Recommender System")
selected_movie_name = st.selectbox("Please type or select the movie you want recommendation for",movies['title'].values)



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



if st.button("Recommend Movies"):
    progress_text = "Recommendation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.subheader(i)
        time.sleep(0.75)
    st.snow()
    st.info("Image posters are not available due to poster api key issues",icon="ℹ️")