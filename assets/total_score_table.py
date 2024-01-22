import matplotlib.pyplot as plt

from src.data_loader import DataLoader

plt.style.use('ggplot')

df = DataLoader().load_data()

# Count of Reviewer Score
ax = df['Reviewer_Score'].value_counts().sort_index().plot(kind='bar', title='Count of Reviewer Score', figsize=(12, 6))
ax.set_xlabel('Reviewer Score')
plt.show()

# Count of Average Score
ay = df['Average_Score'].value_counts().sort_index().plot(kind='bar', title='Count of Average Score', figsize=(12, 6))
ay.set_xlabel('Average Score')
plt.show()

# Average per Country
df['Hotel_Address'] = df['Hotel_Address'].apply(lambda x: x.replace('United Kingdom', 'UK'))
df['Country'] = df['Hotel_Address'].apply(lambda x: x.split()[-1])
az = df.groupby('Country')['Average_Score'].mean().sort_values(ascending=False).plot(kind='bar', figsize=(12, 6),
                                                                                     title='Average Score per Country')
az.set_xlabel('Country')
plt.show()
