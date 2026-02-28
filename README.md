# 🏦 Company Bankruptcy Prediction

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0+-orange?style=for-the-badge&logo=scikit-learn)
![Accuracy](https://img.shields.io/badge/Accuracy-96.70%25-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> A Machine Learning powered web application that predicts whether a company is at risk of bankruptcy based on key financial indicators.

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Demo](#-demo)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Model](#-model)
- [Installation](#-installation)
- [Usage](#-usage)
- [Input Features Explained](#-input-features-explained)
- [Test Values](#-test-values)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 About the Project

Bankruptcy is a legal proceeding initiated when a person or business is unable to repay outstanding debts or obligations. Early prediction of bankruptcy can save investors, creditors, and stakeholders from significant financial loss.

This project uses a **Gradient Boosting Classifier** trained on real financial data to predict the likelihood of a company going bankrupt. The model takes 10 key financial ratios as input and outputs a **Bankrupt** or **Not Bankrupt** prediction with **96.70% accuracy**.

---

## 🎥 Demo

```
Enter financial ratios → Click Predict → Get instant result
✅ Not Bankrupt (Low Risk)   or   ⚠️ Bankrupt (High Risk)
```

> 🔗 Run locally by following the [Installation](#-installation) steps below.

---

## ✨ Features

- 🔍 Predicts company bankruptcy using 10 financial indicators
- ⚡ Fast predictions powered by a pre-trained ML model
- 🌐 Clean and intuitive web interface built with Flask
- 📊 96.70% model accuracy on test data
- 🛡️ Error handling for invalid inputs

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3 |
| Backend | Python, Flask |
| ML Model | Scikit-Learn (Gradient Boosting Classifier) |
| Data Processing | Pandas |
| Model Persistence | Pickle |

---

## 📊 Dataset

The model was trained on the **Company Bankruptcy Prediction Dataset** containing financial records of **6,819 companies** with **96 financial features**.

- **Target variable:** `Bankrupt?` (1 = Bankrupt, 0 = Not Bankrupt)
- **Training features used:** 10 key financial ratios (see below)
- **Train/Test Split:** 80% / 20%

---

## 🤖 Model

| Property | Value |
|---|---|
| Algorithm | Gradient Boosting Classifier |
| Test Accuracy | **96.70%** |
| Features Used | 10 |
| Training Samples | ~5,455 |
| Test Samples | ~1,364 |

The Gradient Boosting Classifier was chosen for its strength in handling imbalanced financial datasets and its high interpretability for tabular data.

---

## ⚙️ Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/your-username/company-bankruptcy-prediction.git
cd company-bankruptcy-prediction
```

**2. Install dependencies**
```bash
pip install flask scikit-learn pandas
```

**3. Run the application**
```bash
python app.py
```

**4. Open your browser and visit**
```
http://localhost:5000
```

---

## 🚀 Usage

1. Open the web app at `http://localhost:5000`
2. Enter values for all 10 financial indicators
3. Click the **Predict** button
4. View the result — `✅ Not Bankrupt` or `⚠️ Bankrupt`

---

## 📋 Input Features Explained

| # | Feature | Description |
|---|---|---|
| 1 | **Operating Gross Margin** | Revenue remaining after operating costs. Higher = healthier. |
| 2 | **Cash Flow Rate** | Cash generation ability vs liabilities. Negative = danger. |
| 3 | **Tax Rate (A)** | Effective tax rate paid. Zero often means no profit was made. |
| 4 | **Net Worth / Assets** | Shareholder ownership ratio. Close to 1 = low debt. |
| 5 | **Total Asset Turnover** | Revenue generated per unit of asset. Higher = more efficient. |
| 6 | **Cash / Total Assets** | Liquidity ratio. Too low = can't cover sudden expenses. |
| 7 | **Cash / Current Liability** | Can the company pay short-term debts with cash alone? |
| 8 | **Total Income / Total Expense** | **Most critical.** > 1 = healthy. < 1 = spending more than earning. |
| 9 | **Total Expense / Assets** | Expense burden on assets. > 1 is unsustainable. |
| 10 | **Gross Profit to Sales** | Profit after cost of goods. Negative = selling below cost. |

---

## 🧪 Test Values

Use these values to verify the model is working correctly:

### ✅ Not Bankrupt (Healthy Company)

| Feature | Value |
|---|---|
| Operating Gross Margin | 0.32 |
| Cash Flow Rate | 0.15 |
| Tax Rate (A) | 0.25 |
| Net Worth / Assets | 0.65 |
| Total Asset Turnover | 0.85 |
| Cash / Total Assets | 0.12 |
| Cash / Current Liability | 0.45 |
| Total Income / Total Expense | 1.15 |
| Total Expense / Assets | 0.72 |
| Gross Profit to Sales | 0.30 |

### ⚠️ Bankrupt (High Risk Company)

| Feature | Value |
|---|---|
| Operating Gross Margin | -0.45 |
| Cash Flow Rate | -0.20 |
| Tax Rate (A) | 0.00 |
| Net Worth / Assets | 0.05 |
| Total Asset Turnover | 0.18 |
| Cash / Total Assets | 0.02 |
| Cash / Current Liability | 0.04 |
| Total Income / Total Expense | 0.72 |
| Total Expense / Assets | 1.35 |
| Gross Profit to Sales | -0.12 |

---

## 📁 Project Structure

```
company-bankruptcy-prediction/
│
├── app.py                  # Flask application (main entry point)
├── modelg.pkl              # Pre-trained Gradient Boosting model
├── data.csv                # Training dataset
│
├── templates/
│   └── indexs.html         # Frontend HTML page
│
├── static/
│   └── img/
│       └── background image.jpg   # Background image for UI
│
└── README.md               # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developed By

**Team** — Built with ❤️ using Machine Learning and Flask.

---

> ⭐ If you found this project useful, please consider giving it a star on GitHub!
