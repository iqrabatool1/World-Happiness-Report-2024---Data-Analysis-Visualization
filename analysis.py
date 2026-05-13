import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. CONNECT & PULL DATA
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="iqrajan14",
        database="world_happiness_project"
    )
    
    # We pull everything from your whr2024 table
    query = "SELECT * FROM whr2024"
    df = pd.read_sql(query, db)
    db.close()
    print("✅ Data successfully loaded from MySQL!")

except Exception as e:
    print(f"❌ Error: {e}")

# 2. DATA AUDIT (Check for missing values)
print("\n--- Data Health Check ---")
print(df.isnull().sum())

# 3. CORRELATION HEATMAP
# This shows the relationship between all numeric factors
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn', fmt='.2f')
plt.title('The Happiness Drivers: Correlation Matrix')
plt.tight_layout()
plt.show()

# 4. TOP 10 HAPPINESS SCORES BAR CHART
plt.figure(figsize=(10, 6))
top_10 = df.nlargest(10, 'Ladder score')
sns.barplot(data=top_10, x='Ladder score', y='Country', palette='viridis')
plt.title('Top 10 Happiest Countries')
plt.show()

# 5. WEALTH VS HAPPINESS SCATTER PLOT
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Explained by: Log GDP per capita', y='Ladder score', scatter_kws={'alpha':0.5})
plt.title('Relationship: Money (GDP) vs. Happiness Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()