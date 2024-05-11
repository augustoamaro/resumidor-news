# Resume News: Resumidor de Notícias 📰

<img src="news.png">

O Resumidor de Notícias é uma aplicação Python que utiliza APIs de ponta para buscar automaticamente artigos de notícias baseados em tópicos fornecidos pelo usuário, resumindo-os em um formato conciso. Este projeto utiliza a NewsAPI para recuperar artigos recentes e a API do Google Gemini para gerar resumos inteligentes e informativos.

## Como Funciona 🤔

1. **Digite o tópico:** Você digita o tópico que deseja. Ex: Futebol, IA, Crypto.
2. **Busca na API de notícias:** A ferramenta irá buscar as notícias atuais sobre o tópico.
3. **Extração do HTML:** A ferramenta irá fazer a extração do HTML da URL que foi encontrada referente ao tópico da notícia.
4. **Análise da IA:** O Google Gemini, irá analisar as notícias atuais e fazer um resumo sobre o link da notícia.
5. **Resultado:** A ferramenta retorna em formato de texto, o artigo sobre o tópico escolhido, autor, data de publicação, url e o resumo.

## Tecnologias utilizadas 👩‍💻

1. **Python** 
2. **Beautiful Soup (para parsing HTML)**
3. **NewsAPI** 
4. **Google Generative AI** 