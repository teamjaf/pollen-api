import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('plant_info.csv')

# Handle null values
df = df.dropna()

# print(df.isnull().sum())

label_cols = ['Season', 'Plant_family', 'Plant_code']
label_encoders = {}

for col in label_cols:
    le = LabelEncoder()
    df[col + '_encoded'] = le.fit_transform(df[col])
    label_encoders[col] = le

X = df[['Pollen_count', 'Season_encoded', 'Plant_family_encoded']]  # or include Plant_code_encoded if useful
y = df['Index_value']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Apply SMOTE on training data only
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

model = RandomForestClassifier(random_state=42)
model.fit(X_train_res, y_train_res)

y_pred = model.predict(X_test)

print("Classification report")
print(classification_report(y_test, y_pred))

print("Confusion matrix")
print(confusion_matrix(y_test, y_pred))

new_sample = pd.DataFrame({
    'Pollen_count': [2500],
    'Season_encoded': [label_encoders['Season'].transform(['Spring'])[0]],
    'Plant_family_encoded': [label_encoders['Plant_family'].transform(['Poaceae'])[0]]
})

predicted_index = model.predict(new_sample)
print("Predicted Allergy Severity Index:", predicted_index[0])

# Feature Importance
importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(8, 5))
sns.barplot(x=importances, y=features)
plt.title('Feature Importance')
plt.xlabel('Importance Score')
plt.ylabel('Features')
plt.show()

# Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=np.unique(y_test),
            yticklabels=np.unique(y_test))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Heatmap')
plt.show()

