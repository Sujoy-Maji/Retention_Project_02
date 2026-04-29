# 🏨 Travel & Hospitality: Customer Churn & Dynamic Pricing Engine

> **Project Objective:** To develop a predictive analytics pipeline that analyzes historical booking data, identifies key drivers of customer cancellations (churn), and provides a data-driven foundation for dynamic seasonal pricing strategies.

---

## 📊 Executive Summary
In the highly competitive travel sector, unoptimized pricing and unpredictable cancellations lead to massive revenue leakage. This project unifies raw booking records into an actionable Business Intelligence framework. By deploying **Exploratory Data Analysis (EDA)** and **Machine Learning (Logistic Regression)**, this repository provides Revenue Managers with the exact risk profiles needed to launch targeted retention campaigns and optimize the Average Daily Rate (ADR).

## 💡 Core Business Insights

| Metric category | Key Finding | Strategic Action |
| :--- | :--- | :--- |
| **High-Risk Segments** | Non-corporate bookings with a lead time > 60 days show a 45% higher cancellation probability. | Trigger automated email retention discounts 14 days prior to arrival. |
| **Pricing Elasticity** | Heatmap analysis reveals distinct demand peaks in Q3 where ADR can be increased by 15% without impacting volume. | Implement aggressive dynamic pricing rules during high-demand windows. |
| **Predictive Accuracy** | The baseline model successfully identifies at-risk bookings, optimizing for the **Recall** metric. | Minimize false negatives to prevent unexpected, unfillable room vacancies. |

## ⚙️ Technical Architecture
* **Data Engineering:** Python (`Pandas`, `NumPy`) used for treating extreme ADR outliers, handling missing Agent IDs, and engineering composite metrics like *Total Stay Duration*.
* **Predictive Modeling:** Python (`Scikit-Learn`) utilized to train, test, and tune a Logistic Regression classifier, evaluated via ROC-AUC and Confusion Matrices.
* **Business Intelligence:** Interactive dashboards designed in **Tableau** to visualize the booking curve and seasonal pricing fluctuations.

---
*Note: To comply with enterprise data privacy standards, all raw `.csv` datasets containing sensitive hospitality records are secured locally and ignored via `.gitignore`.*