import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("student_habits_performance.csv", encoding="utf-8")

# Social Media vs Exam score
sns.scatterplot(
    x='social_media_hours',
    y='exam_score',
    data=df
)
plt.title("Social Media Usage vs Exam Score")
plt.show()
# CONCLUSION
'''This graph is linear
Student with less social media hour tend to have more score
But some student high social media hours have better result then many of less social media using student'''
