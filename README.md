# 📊 Supermarket Sales Analysis | End-to-End EDA with Python

An exploratory data analysis of **1,000 supermarket transactions across 17 variables**, covering three branches and cities (Yangon, Mandalay, Naypyitaw) from January to March 2019. The project turns raw sales data into clear, decision-ready insights.

## 🎯 Objective
Understand customer behavior, payment preferences, and sales patterns across branches, product lines, and time periods.

## 🔍 What Was Analyzed
- Customer demographics: gender split and member vs. normal customers by branch
- Payment behavior: Cash, Credit Card, and E-wallet usage across branches
- Customer satisfaction: rating distribution (4.0 to 10.0) and its link to gross income
- Sales trends by product line, city, branch, and day of week
- Peak shopping hours and quantity distribution

## 💡 Key Findings
- Clean dataset: zero missing values across all 17 columns
- Balanced customer base: 501 female vs. 499 male
- Even transaction spread: Branch A (340), Branch B (332), Branch C (328)
- Busiest hour: **7 PM (113 transactions)**, followed by 1 PM (103) and 3 PM (102)
- Quietest hour: 5 PM (74 transactions)

## 🛠️ Tech Stack
Python · Pandas · NumPy · Matplotlib · Seaborn · Google Colab

## 📁 Project Structure
```
supermarket-sales-analysis/
├── data/
│   └── supermarket.csv        # add your dataset here
├── notebook/
│   └── EDA_Project.ipynb      # original Colab notebook
├── images/                    # charts (auto-generated)
├── sales_analysis.py          # full analysis script
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Analysis Sequence
1. Load data
2. Data inspection (head, tail, info, shape, describe, null check)
3. Feature engineering (weekday and hour from date and time)
4. Customer demographics (gender, customer type by branch)
5. Payment behavior by branch
6. Customer satisfaction (rating distribution, rating vs. gross income, rating by branch)
7. Revenue analysis (gross income by branch, gender, product line, city)
8. Product analysis (quantity, product line by gender, rating by product line)
9. Time-based analysis (sales by weekday, transactions by hour, quantity by hour)

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/supermarket-sales-analysis.git
cd supermarket-sales-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Place supermarket.csv inside the data/ folder, then run
python sales_analysis.py
```

All charts are saved to the `images/` folder.

## 📈 Takeaway
Staffing and promotions can be aligned with peak hours, and payment and customer-type patterns can guide targeted loyalty offers for each branch.

## 🔮 Next Steps
- Interactive dashboard (Streamlit or Power BI)
- Sales prediction model

## 👤 Author
**Saim Patel**
[LinkedIn](https://www.linkedin.com/) · [GitHub](https://github.com/)
