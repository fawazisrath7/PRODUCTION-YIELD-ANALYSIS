import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('data/yield_data.csv')

# Display basic info
print("Basic Dataset Info:")
print(data.info())

# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Correlation matrix
correlation = data.corr()
print("\nCorrelation Matrix:")
print(correlation)

# Plotting correlation heatmap
sns.heatmap(correlation, annot=True, cmap='YlGnBu')
plt.title('Correlation Heatmap of Yield Factors')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()

# Scatter plot: Rainfall vs Yield
sns.scatterplot(x='rainfall', y='yield', data=data)
plt.title('Rainfall vs Yield')
plt.savefig('rainfall_vs_yield.png')
plt.show()
