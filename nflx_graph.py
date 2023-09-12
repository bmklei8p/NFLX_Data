import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('NFLX_Top_10.csv')  

grouped_data = data.groupby(['category', 'week'])['weekly_hours_viewed'].sum().reset_index()

plt.figure(figsize=(12, 6))
ax = plt.subplot(1, 1, 1)

for category in grouped_data['category'].unique():
    category_data = grouped_data[grouped_data['category'] == category]
    sns.lineplot(data=category_data, x='week', y='weekly_hours_viewed', label=category)

plt.title('Weekly Hours Viewed Over Time')
plt.xlabel('Week')
plt.ylabel('Weekly Hours Viewed')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
