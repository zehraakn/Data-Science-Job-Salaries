import pandas as pd

df = pd.read_csv('ds_salaries.csv')
print("İlk 5 satır:")
print(df.head())

######

average_salary = df['salary'].mean()
print("\nOrtalama maaş:", average_salary)

######

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ds_salaries.csv')
avg_salary_by_experience = df.groupby('experience_level')['salary'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(avg_salary_by_experience['experience_level'], avg_salary_by_experience['salary'], color='skyblue')
plt.title('Deneyim Seviyesine Göre Ortalama Maaş')
plt.xlabel('Deneyim Seviyesi')
plt.ylabel('Ortalama Maaş')
plt.show()

######

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ds_salaries.csv')
avg_salary_by_country = df.groupby('employee_residence')['salary'].mean().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(avg_salary_by_country['employee_residence'], avg_salary_by_country['salary'], color='lightgreen')
plt.title('Ülkeye Göre Ortalama Maaş')
plt.xlabel('Çalışanın Bulunduğu Ülke')
plt.ylabel('Ortalama Maaş')
plt.xticks(rotation=45)
plt.show()

######

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ds_salaries.csv')
avg_salary_by_experience_and_employment = df.groupby(['experience_level', 'employment_type'])['salary'].mean().reset_index()
plt.figure(figsize=(12, 8))
sns.barplot(x='experience_level', y='salary', hue='employment_type', data=avg_salary_by_experience_and_employment, palette='viridis')
plt.title('Deneyim Seviyesi ve İstihdam Türüne Göre Ortalama Maaşlar')
plt.xlabel('Deneyim Seviyesi')
plt.ylabel('Ortalama Maaş')
plt.legend(title='İstihdam Türü')
plt.show()

######

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ds_salaries.csv')
avg_salary_by_experience_and_employment = df.groupby(['experience_level', 'employment_type'])['salary'].mean().reset_index()
plt.figure(figsize=(12, 8))
sns.barplot(x='experience_level', y='salary', hue='employment_type', data=avg_salary_by_experience_and_employment, palette='viridis')
plt.title('Deneyim Seviyesi ve İstihdam Türüne Göre Ortalama Maaşlar')
plt.xlabel('Deneyim Seviyesi')
plt.ylabel('Ortalama Maaş')
plt.legend(title='İstihdam Türü')
plt.show()

######

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ds_salaries.csv')
avg_salary_by_employment_type = df.groupby('employment_type')['salary'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(avg_salary_by_employment_type['employment_type'], avg_salary_by_employment_type['salary'], color='lightblue')
plt.title('İstihdam Türlerine Göre Ortalama Maaş')
plt.xlabel('İstihdam Türü')
plt.ylabel('Ortalama Maaş')
plt.show()

