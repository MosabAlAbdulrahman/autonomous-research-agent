from scraping.scraper import scrape_techcrunch_ai_articles
from models.load_local_model import load_model
from agents.analyst_agent import analyze_articles
from reports.generate_pdf import generate_report

if __name__ == "__main__":
    print("Starting Autonomous Research Agent...")

    articles = scrape_techcrunch_ai_articles()
    model = load_model()
    summaries = analyze_articles(articles, model)
    generate_report(summaries)

    print("Report generated at: reports/weekly_report.pdf")
