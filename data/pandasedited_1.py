import pandas as pd
df = pd.read_csv('Students_Grading_Dataset.csv')
df
student_ids = df['Student_ID']
student_ids
df['Student_ID'].tail(10)
df_json = pd.read_json('Students_Grading_Dataset.json')
df_json
summary_stats = df.describe()
summary_stats
df.info()
mean_age = df['Age'].median()
mean_age
# df.set_index('Student_ID', inplace=True)
df
# df['Age'] = df['Age'].astype(object)
# df['Gender'] = df['Gender'].map({'Male':0, 'Female':1})
# df['Gender']
df