# -*- coding: utf-8 -*-
"""1주차 첫 번째 알고리즘 선형회귀.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zF_Dua4kviiqRMhS36CEPbD7mKyfrOMW
"""

# 선형회귀
# 연속형 변수일 경우, 목표변수 예측이 목적
# 연속된 변수를 예측하는 최적의 직선을 찾는 알고리즘.
# 예측할 종속변수만 연속변수이면 되며, 예측하는데 쓰일 그 외 변수들은 연속형일 필요는 없음.
# 머신러닝의 기초 알고리즘
# 복잡한 알고리즘에 비해 예측력이 떨어지지만, 데이터의 트겅이 복잡하지 않을 때는 쉽고 빠르기 때문에 많이 사용됨.
# 다른 모델과 성능을 비교하는 기준 모델로 사용하기도 함.

# 1. 데이터 수집
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 소수자릿수 정제
pd.options.display.float_format = '{:.2f}'.format

file_name = 'insurance.csv'
file_url = f"https://raw.githubusercontent.com/bigdata-young/bigdata_16th/main/data/{file_name}"
df = pd.read_csv(file_url)
df.head()

# 결측치 없음.
# object(sex, smoker, region)
df.info()

# 편차는 
df.describe()

# 2. 데이터 전처리
# 범주형 변수 처리
# sex, smoker, region
# smoker
df['smoker'].unique()

# smoker은 2개 종류.
df['smoker'] = df['smoker'].map({'yes':1, 'no':0})

df['smoker'].unique()

# 나머지 sex, region은 pd.get_dummies로 처리
# 고유값을 덜어서 부하를 줄이기 위해 drop_first
df = pd.get_dummies(df, columns = ['sex', 'region'], drop_first = True)

df.info()

# 3. 모델 학습
# 독립변수와 종속변수, 데이터셋 나누기
X = df[['age','bmi','children','smoker','sex_male','region_northwest','region_southeast','region_southwest']]
y = df['expenses']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 100
)

# 모델링
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# model fit(train set)
model.fit(X_train, y_train)# 학습셋, 독립변수, 종속변수

# 모델 예측
pred = model.predict(X_test)

# 4. 모델 평가
# 두 데이터를 비교하여 정확도 확인
comparison = pd.DataFrame({'actual': y_test, 'pred': pred})
comparison

# 비교가 잘 되지 않으므로
# 산점도 그려서 비교
plt.figure(figsize = (10, 10))
sns.scatterplot(x = 'actual', y = 'pred', data = comparison)
# 양의 상관관계?

# 5. 배포

# MLOps