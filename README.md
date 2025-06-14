# 🛍️ E-Commerce dashboard

🔗 [👉 View Live Tableau Dashboard](https://public.tableau.com/app/profile/pablo.soriano/viz/E-commerceproject_17412746070040/Dashboard1)

## 📊 Project Overview

This project analyzes how **Discounts** and **COGS (Cost of Goods Sold)** influence profit in an e-commerce business setting. It uses SQL, Python, and Tableau to explore, simulate, and visualize profit dynamics at multiple levels: product, subcategory, state, and customer segments.

The analysis was based on the Superstore dataset, and resulted in the creation of an interactive **Discounts & COGS Dashboard**.

---

## 🎯 Objectives

- Assess the impact of **discounts and COGS** on net profit.
- Simulate profit recovery through **discount and pricing adjustments**.
- Identify **loss-making products** and regions.
- Create a **dashboard** to monitor key metrics.
- Use **clustering** to profile customer behavior for marketing strategies.

---

## 🧰 Tech Stack

- **Python** (Pandas, Matplotlib, Scikit-learn)
- **SQLite** for database queries
- **Tableau** for dashboard visualization
- **VSCode** for notebook development

---

## 📁 Project Structure

```
Ecommerce-Dashboard/
├── data/
│   ├── raw/                 # Raw data files (CSV, original DB)
│   ├── interim/             # Intermediate processed files
│   └── processed/           # Cleaned and final datasets
├── docs/                    # Documentation files
├── images/                  # Schema & dashboard images
├── notebooks/               # Jupyter Notebooks for analysis
│   ├── EDA.ipynb
│   ├── furniture_analysis.ipynb
│   ├── kmeans_clustering.ipynb
│   ├── sql_database_setup.ipynb
│   └── updated_superstore.ipynb
├── src/                     # Source code and helper scripts
│   ├── paths.py
│   ├── helper_functions.py
├── tables/                  # Database schema and data tables
├── superstore.db            # SQLite database
├── README.md
```

---

## 🔎 Key Insights

- **Furniture category** showed high revenue but low profit due to excessive discounting.

![alt text](images/revenue&profit_category.png)

![alt text](images/pm&discount_category.png)

- **Strong correlation** between discount and losses: Most sales with discounts above **%20** result in a loss.

![alt text](images/correlation_discount_profit_margin.png)

- **Huge discount gap**: Some products incur losses in certain states but remain profitable in others. The excessive discounting is the key factor behind losses

![alt text](images/loss_making_products.png)

- **State-level variance** in profitability highlights the need for region-specific strategies.
- **Simulated adjustments** to discount and pricing showed potential for:
  - +10% revenue increase
  - +143% profit increase   
- **Clustering analysis** segmented customers into 3 actionable groups:
  - Cluster 0: Moderate activity
  - Cluster 1: High-value, frequent customers
  - Cluster 2: Inactive or low-frequency buyers

![alt text](images/kmeans_clustering.png)

---

## 📈 Dashboard Highlights

The [Tableau dashboard](https://public.tableau.com/app/profile/pablo.soriano/viz/E-commerceproject_17412746070040/Dashboard1) includes:

- Trends for **COGS, Discount, and Profit Margin** over time.
- **State-level** heatmaps for projected profit.
- Breakdown of **Discount & COGS by Subcategory and Product**.
- Insights into **underperforming products**.
- Visual comparison of **projected vs. original profit**.

![Dashboard Preview](images/dashboard.png)

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ecommerce-dashboard.git
   cd ecommerce-dashboard
   ```

2. Run analysis notebooks in `/notebooks` for EDA, clustering, and profit simulations.

3. Use `superstore.db` to run SQL queries (see `sql_database_setup.ipynb` for schema creation).

4. Explore the Tableau dashboard via `images/Dashboard 1.png` or interactively in Tableau.

---

## 📚 References

- Dataset: [Superstore](https://drive.google.com/file/d/1j3BVqD5_KDfvXdljnZ7beV-G-FVS8df5/view)
- Tools: [Tableau](https://www.tableau.com/), [SQLite](https://www.sqlite.org/index.html), [Pandas](https://pandas.pydata.org/)

---

## 🙋 Author

**Pablo Soriano**  
📅 Project Date: March 2025  
🔍 Created during Code Academy Berlin's bootcamp

## 🤝 Let's Connect

Feel free to [connect with me on LinkedIn](https://www.linkedin.com/in/pabs-soriano) or reach out with questions and feedback!
