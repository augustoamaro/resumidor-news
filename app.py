from datetime import datetime, timedelta
import streamlit as st
from newsapi import NewsApiClient
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

news_api_key = st.secrets["news_api_key"]
google_api_key = st.secrets["google_api_key"]

newsapi = NewsApiClient(api_key=news_api_key)
genai.configure(api_key=google_api_key)


def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    return date_obj.strftime('%d/%m/%Y %H:%M')


st.sidebar.title("Resumidor de notícias")
query = st.sidebar.text_input(
    "Digite o tópico de interesse:", value="Inteligência Artificial")

if st.sidebar.button("Buscar notícias"):
    with st.spinner('Buscando e processando notícias...'):
        all_articles = newsapi.get_everything(q=query,
                                              language='pt',
                                              sort_by='relevancy',
                                              page_size=3,
                                              from_param="2024-06-24",
                                              to="2024-06-26")
        news_data = []

        for article in all_articles['articles']:
            article_url = article['url']
            response = requests.get(article_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                full_text = ' '.join(p.text for p in soup.find_all('p'))

                generation_config = {
                    "candidate_count": 1,
                    "temperature": 0.5,
                }

                model = genai.GenerativeModel(
                    model_name="gemini-1.5-pro-latest", generation_config=generation_config)
                model_response = model.generate_content(full_text)
                summary = model_response.text

                news_data.append({
                    'title': article['title'],
                    'author': article.get('author', 'Autor desconhecido'),
                    'publishedAt': format_date(article['publishedAt']),
                    'summary': summary,
                    'url': article_url
                })

        if news_data:
            for article in news_data:
                st.write(f"### {article['title']}")
                st.write(f"**Autor:** {article['author']}")
                st.write(f"**Publicado:** {article['publishedAt']}")
                st.write(f"**URL:** ({article['url']})")
                st.write(f"**Resumo:** {article['summary']}")
                st.write("---")
        else:
            st.error("Não foram encontradas notícias para o tópico selecionado.")
