import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("student_habits_performance.csv", encoding="utf-8")

'''Let's check if the data is centerlized or are there any extreme values'''
sns.histplot(df['exam_score'], kde=True)
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.show()
# CONCLUSION
''' Most score are in between the range of 65 to 75
 althrough highest score which is 100, is also been repeated 80 times '''
