Absolutely — here is a **clean, polished, fully rewritten version** of your entire document, keeping **all structure, all insights, all results**, but improving clarity, flow, and professional tone.

---

# **Financial News Analytics: Predicting Price Moves with News Sentiment**

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![NLP](https://img.shields.io/badge/NLP-Topic%20Modeling-green)
![Finance](https://img.shields.io/badge/Finance-Analytics-yellow)
![Machine Learning](https://img.shields.io/badge/ML-Classification-red)

**10 Academy – Artificial Intelligence Mastery**
**Week 1 Challenge: Predicting Price Moves with News Sentiment**
**Completed: November 2025**

---

## 📊 **Project Overview**

This project presents a complete quantitative framework analyzing **1.4 million financial news articles**, integrating them with **stock price data** and **technical indicators** to uncover how news sentiment affects short-term stock movements. The work combines natural language processing, technical analysis, statistics, and visualization to deliver actionable trading insights.

---

## 🎯 **Business Objective**

**Nova Financial Solutions** aims to strengthen its predictive capabilities by:

* Measuring the relationship between **news sentiment** and **stock returns**
* Creating **multi-factor trading signals** using sentiment + technical patterns
* Building an **automated monitoring system** for real-time signals
* Improving **risk management** and decision-making through data-driven insights

---

## 🚀 **Key Insights & Results**

### 📈 **Dataset Scale**

* **1,407,328 financial articles** (2009–2020)
* **6 major tech stocks**: AAPL, AMZN, GOOG, META, MSFT, NVDA
* **74,364** company-relevant articles after filtering
* Advanced **sentiment scoring** with financial-context weighting

---

## 📊 **Sentiment–Stock Return Correlation**

| Stock | Correlation | Strength  | Variance Explained | Significant |
| ----- | ----------- | --------- | ------------------ | ----------- |
| NVDA  | **0.1315**  | Very Weak | 1.73%              | ✅ YES       |
| GOOG  | 0.0640      | Very Weak | 0.41%              | ✅ YES       |
| MSFT  | 0.0595      | Very Weak | 0.35%              | ✅ YES       |
| AAPL  | 0.0531      | Very Weak | 0.28%              | ✅ YES       |
| AMZN  | 0.0461      | Very Weak | 0.21%              | ✅ YES       |
| META  | 0.0152      | Very Weak | 0.02%              | ❌ NO        |

### **Core Insights**

* **Average variance explained**: 0.50%
* **5/6 stocks** show significant sentiment-return relationships
* **Success rate** of sentiment prediction: **37.9%**
* **NVDA** shows strongest response to sentiment (8.6× META’s sensitivity)

---

## 🏢 **Publisher & Temporal Behavior**

* **Top publisher**: *Paul Quintaro* (228,373 articles, 16.2% share)
* **Highest weekday volume**: **Thursday** → pre-weekend trading prep
* **Major spike**: March 2020 (COVID crash) → **24,995 articles**
* **Busiest day**: March 12, 2020 (market collapse) → **2,739 articles**

---

## 🔍 **Topic Modeling: 10 Financial Themes**

Generated using **NMF + TF-IDF**, yielding:

1. 52-Week Highs/Lows
2. Earnings Reports
3. Market Movers
4. Analyst Actions
5. Price Targets
6. Biggest Movers
7. Earnings Calendar
8. Market Updates
9. New Record Highs
10. Premarket Activity

These categories reflect common patterns in professional financial reporting.

---

## 🛠️ **Technical Implementation**

### **Sentiment Pipeline**

```python
def enhanced_sentiment_analysis(text):
    financial_terms = {
        'positive': ['profit', 'growth', 'beat', 'surge', 'rally', 'upgrade', 'bullish'],
        'negative': ['loss', 'decline', 'miss', 'plunge', 'downgrade', 'bearish', 'cut']
    }
    enhanced_sentiment = base_sentiment + positive_boost - negative_boost
    return enhanced_sentiment
```

### **Trading Signal Engine**

```python
def generate_trading_signal(stock_data, sentiment_data):
    bullish_technical = (
        (stock_data['MACD'] > stock_data['MACD_Signal']) &
        (stock_data['RSI_14'] < 70)
    )
    
    positive_sentiment = sentiment_data['avg_sentiment'] > 0.3
    high_confidence = sentiment_data['article_count'] >= 3
    
    return bullish_technical & positive_sentiment & high_confidence
```

---

## 🧱 **Project Structure**

```
fnspid-project/
├── notebooks/
│   ├── task1.ipynb
│   ├── task2.ipynb
│   └── task3.ipynb
├── src/
│   ├── data_loader.py
│   ├── sentiment_analyzer.py
│   └── correlation_engine.py
├── data/
│   ├── raw_analyst_ratings.csv
│   ├── AAPL.csv
│   └── ...
├── requirements.txt
└── README.md
```

---

## 🚀 **Quick Start**

### 1. Clone Repository

```bash
git clone https://github.com/your-username/fnspid-project.git
cd fnspid-project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Notebooks

```bash
jupyter notebook notebooks/task1.ipynb
jupyter notebook notebooks/task2.ipynb
jupyter notebook notebooks/task3.ipynb
```

---

# 📊 **Complete Analysis Pipeline**

## **Task 1 – Financial News Analytics** ✅

* Processed **1.4M articles**
* Resolved **mixed-format dates**
* Extracted **10 topic clusters**
* Found **weekly & crisis-driven patterns**
* Publisher dominance and timelines analyzed

---

## **Task 2 – Technical Analysis** ✅

* Applied **SMA, RSI, MACD (TA-Lib)**
* Multi-panel price-indicator visualizations
* Identified bullish/bearish turning points
* Prepared inputs for combined signal engine

---

## **Task 3 – Sentiment Correlation** ✅

* Context-weighted sentiment scoring
* Company-targeted keyword filtering
* Pearson/Spearman correlation testing
* High-confidence, multi-article filtering
* Full dashboard visualization

---

# 💡 **Business Applications**

## **1. Multi-Factor Trading Strategies**

Combine:

* **Positive sentiment**
* **MACD crossover**
* **RSI < 70**

## **2. Position Sizing Based on Sentiment Strength**

* Strong signals: **70–80%** size
* Medium signals: **40–50%**
* Low confidence: **20–30%**

## **3. Sector-Specific Optimization**

* Tech stocks show **higher sentiment responsiveness**
* NVDA & AAPL = best sentiment-reactive candidates

---

# 📈 **Performance Impact**

* **10–15% improvement** in signal accuracy
* **20–30% reduction** in drawdown via sentiment warning
* **2–4% annual alpha** potential
* **Higher Sharpe ratio** through improved timing

---

# 🔮 **Strategic Recommendations**

### **Short-Term **

1. Integrate sentiment confirmation into technical models
2. Deploy real-time article ingestion + scoring
3. Build stock-specific sentiment thresholds
4. Backtest sentiment-technical hybrid systems

---

# 📈 **Results Summary**

### **Core Finding**

> **News sentiment alone explains only 0.5% of stock movement, but when combined with technical indicators it becomes a powerful confirmation tool that significantly boosts trading performance.**

### Additional Insights

* Sentiment works best as a **secondary signal**
* Sensitivity varies widely by stock (NVDA >> META)
* High-confidence sentiment significantly improves accuracy
* Extreme sentiment (>0.3 or <-0.3) is most predictive

---

# 🤝 **Acknowledgments**

* **Program**: 10 Academy AI Mastery
* **Mentors**: Kerod, Mahbubah, Filimon
* **Completion**: November 2025
* **Status**: All Tasks Completed Successfully ✅

---

# 📄 **License**

This project is part of the 10 Academy AI Mastery Program. Usage is subject to program guidelines.

---

# 🎯 **Final Conclusion**

This project provides a robust quantitative system transforming financial news into **actionable trading intelligence**. By integrating **NLP sentiment**, **technical indicators**, and **correlation analysis**, the framework delivers measurable improvements in prediction accuracy, risk management, and trading performance.

**Fully production-ready.** 🚀

---