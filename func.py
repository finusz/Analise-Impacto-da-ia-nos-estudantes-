import pandas as pd
import numpy as np

file  = r'ai_student_impact_dataset.csv'

df = pd.read_csv(file, index_col = 'Student_ID')
print(df.head())