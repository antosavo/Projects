import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('Iris.csv')

print 'Some Data:\n', df.head()
print 'Unique Species:', df['species'].unique()

le = LabelEncoder()
df['label'] = le.fit_transform(df['species'])

print 'Labels:', le.transform(df['species'].unique())

print 'Correlation with label:\n', df.corr()['label'].abs().sort_values(ascending=False)

colnames = df.columns.values
features = colnames[:4]
target = colnames[5]

x = df[features]
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y)

model = RandomForestClassifier(n_estimators=100)

model.fit(x_train, y_train)

sf = pd.DataFrame({'Name':features,'Importance': model.feature_importances_})

print sf.sort_values('Importance',ascending=False)

print 'score:', model.score(x_test,y_test)
