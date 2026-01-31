import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("student_habits_performance.csv", encoding="utf-8")

# clean the data 
df = df.dropna(subset=['student_id','age','gender','study_hours_per_day','social_media_hours','netflix_hours','part_time_job','attendance_percentage','sleep_hours','diet_quality','exercise_frequency','parental_education_level','internet_quality','mental_health_rating','extracurricular_participation','exam_score'])

# print(df.head())
# print(df.shape)
# print(df.info())
