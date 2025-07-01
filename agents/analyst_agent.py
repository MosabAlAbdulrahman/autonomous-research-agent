def analyze_articles(articles, model_pipe):
    summaries = []
    for article in articles:
        prompt = f"Summarize this news headline and explain why it matters in the AI startup landscape:\n{article['title']}"
        result = model_pipe(prompt, max_new_tokens=100)[0]["generated_text"]
        summaries.append({"title": article["title"], "summary": result.strip()})
    return summaries
