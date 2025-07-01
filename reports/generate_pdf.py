from jinja2 import Template
from weasyprint import HTML

def generate_report(summaries):
    with open("reports/templates/report_template.html") as f:
        template = Template(f.read())
    
    rendered = template.render(summaries=summaries)
    HTML(string=rendered).write_pdf("reports/weekly_report.pdf")
