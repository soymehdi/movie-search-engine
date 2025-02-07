import requests
import streamlit as st
###############################

def url_req(title, year=None):
    if not year:
        url = f"http://www.omdbapi.com/?t={title}&apikey=147050ea"
    else:
        url = f"http://www.omdbapi.com/?t={title}&y={year}&apikey=147050ea"
    
    response = requests.get(url)
    
    if response.status_code == 200:   
        return response.json()
    else:
        return f"error {response.status_code}"

def st_display():

    st.title("movie search engine :popcorn:")
    st.write("enter movie's title: ")
    
    movie_t = st.text_input("movie title")
    movie_y = st.text_input("release year")

    movie_t = movie_t.strip()
    movie_t = movie_t.lower()
    
    if movie_y:
        movie_y = movie_y.strip()
    else:
        movie_y = None
        
    movie = url_req(movie_t, movie_y)
    try:
        movie_title = movie["Title"] 
        movie_year = movie["Year"] 
        movie_genre = movie["Genre"] 
        movie_dir = movie["Director"] 
        movie_actors = movie["Actors"] 
        movie_plot = movie["Plot"]  
        movie_country = movie["Country"] 
        movie_awards = movie["Awards"]
        movie_poster = movie["Poster"] # poster image's URL
        meta_score = movie["Metascore"]
        imdb_rating = movie["imdbRating"]

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(movie_poster, caption=f"{movie_title} - {movie_year}")
        with col2:
            st.write(f"Title: {movie_title} ({movie_year})")
            st.write(f"Meta {meta_score} | IMDB {imdb_rating}")
            st.write(f"Genre: {movie_genre}")
            st.write(f"Director: {movie_dir}")
            st.write(f"Actors: {movie_actors}")
            st.write(f"Country: {movie_country}")
            st.write(f"Awards: {movie_awards}")
        with col3:
            st.write(f'"{movie_plot}"')
    except KeyError as e:
        st.write("No Film")
    except TypeError as e:
        st.write("No Film")

def main():
    st_display()

main()