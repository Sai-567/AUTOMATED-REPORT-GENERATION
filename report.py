import pandas as pd
from fpdf import FPDF

df = pd.read_csv("data.csv")
summary = df.describe()
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200,10,txt="Data Analysis Report", ln=True, align="C")
for index, row in summary.iterrows():
    pdf.cell(200,10,txt=f"{index}:{row.to_list()}",ln=True)
pdf.output("Report.pdf")
print("Report generated successfully!")