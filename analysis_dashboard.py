# -------------------------------------------------------------
# FULL DATA ANALYSIS + MULTI-GRAPH DASHBOARD (MATPLOTLIB, SEABORN,
# PLOTLY, BOKEH) - SINGLE PYTHON FILE
# -------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
import plotly.express as px

# --------------------------
# LOAD DATA
# --------------------------
df = pd.read_csv("vehicle_sales_data.csv")   # Change file name as needed
print("Data Loaded Successfully!\n")
print(df.head())

# Detect numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
print("\nNumeric Columns:", numeric_cols)

# --------------------------
# MATPLOTLIB GRAPHS
# --------------------------

# 1) Histogram
plt.figure(figsize=(7, 5))
plt.hist(df[numeric_cols[0]], bins=20)
plt.title(f"Histogram of {numeric_cols[0]}")
plt.xlabel(numeric_cols[0])
plt.ylabel("Frequency")
plt.show()

# 2) Bar Chart
plt.figure(figsize=(7, 5))
df[numeric_cols[1]].head(10).plot(kind='bar')
plt.title(f"Bar Chart of {numeric_cols[1]}")
plt.xlabel("Index")
plt.ylabel(numeric_cols[1])
plt.show()

# 3) Scatter Plot
plt.figure(figsize=(7, 5))
plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
plt.title(f"Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}")
plt.xlabel(numeric_cols[0])
plt.ylabel(numeric_cols[1])
plt.show()

# --------------------------
# SEABORN GRAPHS
# --------------------------

# 4) Pair Plot
sns.pairplot(df[numeric_cols])
plt.show()

# 5) Box Plot
plt.figure(figsize=(7, 5))
sns.boxplot(data=df[numeric_cols])
plt.title("Seaborn Box Plot")
plt.show()

# 6) Heatmap Correlation
plt.figure(figsize=(7, 5))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# --------------------------
# PLOTLY INTERACTIVE GRAPHS
# --------------------------

# 7) Plotly Scatter
fig1 = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1], title="Plotly Scatter Plot")
fig1.show()

# 8) Plotly Histogram
fig2 = px.histogram(df, x=numeric_cols[0], title="Plotly Histogram")
fig2.show()

# 9) Plotly Line Chart
fig3 = px.line(df[numeric_cols], title="Plotly Line Chart")
fig3.show()

# --------------------------
# BOKEH INTERACTIVE GRAPHS
# --------------------------
output_file("bokeh_graphs.html")

p1 = figure(title=f"Bokeh Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}",
            width=700, height=400)
p1.circle(df[numeric_cols[0]], df[numeric_cols[1]], size=7)

p2 = figure(title=f"Bokeh Line Chart ({numeric_cols[0]})", width=700, height=400)
p2.line(df.index, df[numeric_cols[0]], line_width=2)

show(column(p1, p2))

print("\nAll Graphs Generated Successfully!")
