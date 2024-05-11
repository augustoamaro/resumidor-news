import streamlit as st
from newsapi import NewsApiClient
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import google.generativeai as genai

news_api_key = '2f894c8b49164d67b711a06341302b2a'
google_api_key = "AIzaSyCdEAyy3yuFvQtQOXBPhaduygmz6YQY5RQ"

newsapi = NewsApiClient(api_key=news_api_key)
genai.configure(api_key=google_api_key)

st.sidebar.title("Resumidor de notícias")
query = st.sidebar.text_input("Digite o tópico de interesse:", value="Inteligência Artificial")

if st.sidebar.button("Buscar notícias"):
    all_articles = newsapi.get_everything(q=query, language='pt', sort_by='relevancy', page_size=3)
    news_data = []
    
    for article in all_articles['articles']:
        article_url = article['url']
        response = requests.get(article_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            full_text = ' '.join(p.text for p in soup.find_all('p'))
            
            generation_config = {"candidate_count": 1, "temperature": 0.5}
            model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config)
            model_response = model.generate_content(full_text)
            summary = model_response.text
            
            news_data.append({
                'title': article['title'],
                'author': article.get('author', 'Autor desconhecido'),
                'publishedAt': article['publishedAt'],
                'summary': summary,
                'url': article_url
            })

    for article in news_data:
        st.write(f"### {article['title']}")
        st.write(f"**Autor:** {article['author']}")
        st.write(f"**Publicado:** {article['publishedAt']}")
        st.write(f"**URL:({article['url']})")
        st.write(f"**Resumo:** {article['summary']}")
        st.write("---")
