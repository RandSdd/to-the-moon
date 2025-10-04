"""
an easy try of data forecasting based on titanic dataset
i am busy these days and i will attempt to maintain a learning log
at least every two days
long time off, sorry for that, I just own few whole days after some chores
to make a complete project, i need to learn a lot of things
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

n = '\n\n'
train = pd.read_csv('train.csv')
print(f'data shape: {train.shape}')
print(f'{n}this is info')
print('\n')
train.info()
print('\n' + f'this is describe{n}{train.describe()}')
print('\n' + f'this is head{n}{train.head()}')

print(f'{n}---Preliminary investigation results---')
survived_rate = train['Survived'].mean
print(f'{n}the total survived rate:\n{survived_rate}')

test = train.groupby('Sex')

print(n)
for name, group in test:
    print(f'Group: {name}')
    print(group)
    print(f'{n}-------------{n}')
print(n)

print(f'this is group{n}{test.groups}{n}')
print(f'this is size {n}{test.size()}{n}')

Sex_mean = test['Survived'].mean()
print(n)
print(f'this is Sex_mean{n}{Sex_mean}')
Pclass_mean = train.groupby('Pclass')['Survived'].mean()
print(n)
print(f'this is Pclass_mean{n}{Pclass_mean}')
print(n)
print(f'the missing value of Pclass: {train["Pclass"].isnull().sum()}{n}')

fig, axes = plt.subplots(1, 2, figsize=(6, 4))
Sex_mean.plot(kind='bar', ax=axes[0], title='Survival Rate by Sex')
Pclass_mean.plot(kind='bar', ax=axes[1], title='Survival Rate by Pclass')
plt.show(block=False)

train['Sex_encoded'] = train['Sex'].map({'female': 1, 'male': 0})

pclass_dummies = pd.get_dummies(train['Pclass'], prefix='Pclass')
train = pd.concat([train, pclass_dummies], axis=1)

age_median = train['Age'].median()
train['Age_filled'] = train['Age'].fillna(age_median)
for col in ['Pclass_1', 'Pclass_2', 'Pclass_3']:
    if col not in train.columns:
        train[col] = 0

features = ['Sex_encoded', 'Pclass_1', 'Pclass_2', 'Pclass_3', 'Age_filled',
            'SibSp', 'Parch', 'Fare']
X = train[features]
Y = train['Survived']

print("features after process:")
print(X.head())

X_train_val, X_test, Y_train_val, Y_test = train_test_split(X, Y,
test_size=0.2, random_state=42)

X_train, X_val, Y_train, Y_val = train_test_split(X_train_val, Y_train_val,
test_size=0.25, random_state=42)

print(f"train: {X_train.shape[0]} people")
print(f"validation: {X_val.shape[0]} people")
print(f"test: {X_test.shape[0]} people")

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression(max_iter=1000)

history = model.fit(X_train, Y_train)
print("learned weights (coefficients):")
for feature, coef in zip(features, model.coef_[0]):
   print(f"{feature}: {coef:.3f}")
print(f"intercept: {model.intercept_[0]:.3f}")
print(model.classes_)

val_predictions = model.predict(X_val)
val_accuracy = accuracy_score(Y_val, val_predictions)
print(f"\nthe validation accuracy: {val_accuracy:.2%}")

test_predictions = model.predict(X_test)
test_accuracy = accuracy_score(Y_test, test_predictions)
print(f"\n!!!final test accuracy:{test_accuracy:.2%} !!!")

test_df = pd.read_csv('test.csv')
test_df['Sex_encoded'] = test_df['Sex'].map({'female': 1, 'male': 0})
pclass_dummies_test = pd.get_dummies(test_df['Pclass'], prefix='Pclass')
test_df = pd.concat([test_df, pclass_dummies_test], axis=1)
age_median_test = test_df['Age'].median()
test_df['Age_filled'] = test_df['Age'].fillna(age_median_test)
for col in ['Pclass_1', 'Pclass_2', 'Pclass_3']:
    if col not in test_df.columns:
        test_df[col] = 0

print(test_df.isnull().sum())
test_df['Fare'] = test_df['Fare'].fillna(train['Fare'].median())
X_submit = test_df[features]
submit_pred = model.predict(X_submit)
print(X_submit.isnull().sum())

submission = pd.DataFrame({
    'PassengerId': test_df['PassengerId'],
    'Survived': submit_pred
})
submission.to_csv('submission.csv', index=False)
print("The prediction results have been saved in submission.csv")