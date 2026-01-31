import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("student_habits_performance.csv", encoding="utf-8")

# THE CORE RELATIONSHIP
sns.scatterplot(
    x='study_hours_per_day',
    y='exam_score',
    data=df
)
plt.title("Study Hours vs Exam Score")
plt.show()
# CONCLUSION
''' The relatonship is almost linear 
There are some outlier, Student who study 0 hours and student who study between 2 to 4 hours'''
