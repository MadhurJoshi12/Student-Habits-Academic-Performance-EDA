import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("student_habits_performance.csv", encoding="utf-8")

# Save the Heatmap 
plt.savefig('Heatmap.png', dpi=300, bbox_inches='tight')
