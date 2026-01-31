import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("student_habits_performance.csv", encoding="utf-8")

# LIFESTYLE IMPACT 
## Sleep vs Exam score
sns.boxplot(x='sleep_hours', y='exam_score', data=df)
plt.title("Sleep Hours vs Exam Score")
plt.show()
# CONCLUSION 
''' The student which take a sleep more then 8 hours and which take it less then 5 hours have least score'''
