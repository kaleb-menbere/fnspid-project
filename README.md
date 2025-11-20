# Financial News Analytics: Predicting Price Moves with News Sentiment

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![NLP](https://img.shields.io/badge/NLP-Topic%20Modeling-green)
![Finance](https://img.shields.io/badge/Finance-Analytics-yellow)

**10 Academy: Artificial Intelligence Mastery**  
**Week 1 Challenge: Predicting Price Moves with News Sentiment**  
**Date: 19 Nov - 25 Nov 2025**

## 📊 Project Overview

Comprehensive analysis of **1.4 million financial news articles** to uncover patterns in financial media coverage, temporal trends, and publisher dynamics. This project establishes the foundation for sentiment-based stock prediction models for Nova Financial Solutions.

## 🎯 Business Objective

**Nova Financial Solutions** aims to enhance predictive analytics capabilities by:
- Analyzing patterns in financial media coverage
- Identifying correlations between news volume and market events
- Establishing foundation for sentiment-based stock prediction models
- Developing actionable insights for investment strategies

## 🚀 Key Insights

### 📈 Massive Dataset Analysis
- **1,407,328 articles** analyzed spanning 2009-2020
- **Clear growth trajectory**: 12,000%+ increase from 2009 (11K) to 2019 (150K articles)
- **Peak activity**: March 2020 (24,995 articles) during COVID market volatility

### 🏢 Publisher Dominance
- **Paul Quintaro leads** with 228,373 articles (16.2% market share)
- **Top 3 publishers control 40%** of all financial news content
- **Benzinga ecosystem** dominates with multiple branded channels

### ⏰ Temporal Patterns
- **Thursday is peak day** (302,619 articles) for pre-weekend positioning
- **Weekend gap**: 97% less activity on Saturdays (7,759 articles)
- **March 12, 2020**: Record day with 2,739 articles during market crash

### 🔍 Topic Modeling (10 Clear Categories)
Using NMF algorithm, identified distinct financial news topics:
1. **52-week Highs/Lows** - Stock performance milestones
2. **Earnings Reports** - EPS, sales, estimates comparisons  
3. **Market Movers** - Session activity and premarket movers
4. **Analyst Actions** - Upgrades, downgrades, initiations
5. **Biggest Movers** - Volume and price movers analysis
6. **Price Targets** - Analyst maintains/raises/lowers targets
7. **Earnings Schedule** - Scheduled company reports
8. **Market Updates** - General market commentary
9. **New Milestones** - Stocks setting new records
10. **Premarket Activity** - Gainers/losers analysis

## 🛠️ Technical Implementation

### Data Challenges & Solutions

#### ⚠️ Challenge: Mixed Date Formats
The dataset contained **two different date formats** causing analysis issues:
- **Format 1**: `"2020-06-05 10:30:54-04:00"` (with timezone)
- **Format 2**: `"2013-04-18 00:00:00"` (without timezone, 96% had hour=0)

#### ✅ Solution: Robust Date Parsing
```python
# Detect timezone presence with regex
mask_tz = df['date'].str.contains(r"[+-]\d{2}:\d{2}", na=False)

# Conditional parsing for different formats
df.loc[mask_tz, 'date'] = pd.to_datetime(df.loc[mask_tz, 'date'], utc=True)
df.loc[~mask_tz, 'date'] = pd.to_datetime(df.loc[~mask_tz, 'date'], 
                                         format="%Y-%m-%d %H:%M:%S", utc=True)
```

**Result**: 100% successful parsing with 0 NaT values, enabling accurate time series analysis.

### NLP & Machine Learning Pipeline
- **Text Preprocessing**: Lowercase, punctuation removal, whitespace cleaning
- **TF-IDF Vectorization**: 20,000 features with bigram/trigram support
- **NMF Topic Modeling**: 10 components for optimal financial topic separation
- **Automated Classification**: All 1.4M articles assigned to dominant topics

### Key Technical Features
- **Multi-frequency time series analysis** (daily, weekly, monthly, yearly)
- **Publisher market share** and specialization analysis
- **Spike detection** for major market events
- **Email domain extraction** for organizational insights

## 📁 Project Structure

```
fnspid-project/
├── notebooks/
│   └── task1.ipynb                    # Complete Task 1 analysis
├── data/
│   └── raw_analyst_ratings.csv        # Original dataset (1.4M rows)-not commited
├── requirements.txt                   # Project dependencies
└── README.md
```

## 🚀 Quick Start

1. **Clone Repository**
```bash
git clone https://github.com/kaleb-menbere/fnspid-project.git
cd fnspid-project
```

2. **Install Dependencies**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

3. **Run Analysis**
```bash
jupyter notebook notebooks/task1.ipynb
```

## 📊 Key Findings Summary

### Top 10 Days by Article Volume
```
2020-03-12: 2,739 articles  # COVID market crash
2020-02-28: 1,620 articles  # Pre-crash volatility  
2020-03-19: 1,595 articles  # Recovery attempts
2020-02-27: 1,567 articles
2020-03-06: 1,428 articles
```

### Publisher Market Share
```
Paul Quintaro:      228,373 articles
Lisa Levin:         186,979 articles
Benzinga Newsdesk:  150,484 articles
Charles Gross:       96,732 articles
Monica Gerson:       82,380 articles
```

### Most Frequent Financial Phrases
```
price target:        47,266 occurrences
stocks moving:       40,072 occurrences  
market update:       33,089 occurrences
earnings scheduled:  32,055 occurrences
initiates coverage:  28,980 occurrences
```

## ✅ Task 1 Deliverables Completed

### 📊 Descriptive Statistics
- [x] Basic statistics for headline lengths (characters and words)
- [x] Article count per publisher with top 20 analysis
- [x] Publication date trends and temporal patterns

### 📝 Text Analysis & Topic Modeling
- [x] NLP processing for common keywords and phrases
- [x] NMF topic modeling with 10 distinct financial topics
- [x] Extraction of significant events ("price target", "earnings", etc.)

### ⏰ Time Series Analysis
- [x] Publication frequency analysis (daily, weekly, monthly)
- [x] Spike detection correlating with market events
- [x] Publishing time patterns and temporal distributions

### 🏢 Publisher Analysis
- [x] Identification of most active publishers and market share
- [x] Analysis of publisher specialization and content types
- [x] Email domain extraction for organizational analysis

## 🔮 Business Applications

### Immediate Insights for Nova Financial:
- **News Volume Forecasting**: Predict high-activity periods for resource allocation
- **Publisher Strategy**: Focus monitoring on top publishers covering majority of content
- **Topic-based Alerts**: Real-time categorization of market-moving events
- **Temporal Optimization**: Schedule analysis during peak news days (Thursdays)

### Trading & Investment Applications:
- **Event Detection**: Automatic identification of earnings, analyst actions, price targets
- **Volume Spikes**: Early warning for market volatility periods
- **Sector Analysis**: Topic distribution across different market sectors
- **Strategy Timing**: Optimize trade execution based on news flow patterns

## 📈 Next Steps

### Task 2: Quantitative Analysis (Planned)
- Integrate yFinance for stock price data
- Implement TA-Lib for technical indicators (MA, RSI, MACD)
- Calculate daily returns and volatility metrics

### Task 3: Correlation Analysis (Planned)
- Sentiment analysis using TextBlob/NLTK
- Statistical correlation between news sentiment and stock returns
- Investment strategy development based on findings

## 🤝 Team & Timeline

- **Facilitators**: Kerod, Mahbubah, Filimon
- **Challenge Period**: 19 Nov - 25 Nov 2025
- **Current Progress**: Task 1 Completed ✅
- **Next Deadline**: Task 2 & 3 - 25 Nov 2025

## 📞 Support

- **Slack Channel**: #all-week1
- **Office Hours**: Mon-Fri, 08:00-15:00 UTC

---