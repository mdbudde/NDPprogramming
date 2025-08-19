import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'FakeAnimalData.csv'

# Read the CSV into a DataFrame
data = pd.read_csv(file_path)

# Group data by 'Animal' and sum the 'Nsuccessful' points
grouped_data = data.groupby('Rat')['Nsuccessful'].sum()

# Create a bar plot
ax = grouped_data.plot(kind='bar', color='red', edgecolor='black')

# Add labels and title
plt.xlabel('Animal', fontsize=14, fontweight='bold')
plt.ylabel('Total Nsuccessful Points', fontsize=14, fontweight='bold')
plt.title('Total Nsuccessful Points by Animal', fontsize=16, fontweight='bold')

# Customize the plot
ax.spines['top'].set_visible(False)  # Remove top axis
ax.spines['right'].set_visible(False)  # Remove right axis
plt.xticks(rotation=0, fontsize=12, fontweight='bold')  # Make x-axis labels horizontal and bold
plt.yticks(fontsize=12, fontweight='bold')  # Make y-axis labels bold

# Show the plot
plt.savefig('Total_Nsuccessful_Points_by_Animal.png', format='png', dpi=300, bbox_inches='tight')