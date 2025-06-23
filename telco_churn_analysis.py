import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import warnings 
warnings.filterwarnings('ignore')

telco = pd.read_csv('/Users/volkanguner/Desktop/Study Python/Telco/telco_customer_churn.csv')
telco.head()
telco.info() #7043

#TotalCharges needs to be float.

telco[telco['TotalCharges'].str.contains(' ')] # 11 data contains strings.

telco = telco[~telco['TotalCharges'].str.contains(' ')]
telco['TotalCharges'] = telco['TotalCharges'].astype(float)
telco.info() #7032

telco.duplicated().sum() # no duplicates.

# ----------

categorical = ["customerID","gender","Partner","Dependents","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","Churn"]
numerical = ["SeniorCitizen","tenure","MonthlyCharges","TotalCharges"]

telco[numerical].describe()

telco.SeniorCitizen.value_counts()

telco[categorical].describe()

for col in categorical:
  print(f"Value in {col} are")
  print(telco[col].value_counts(), "\n")
  
# DEMOGRAPHICS

plt.figure(figsize = (8,4))
ax = sns.countplot(x = telco["Churn"], palette={"Yes": "skyblue", "No": "tomato"})
ax.bar_label(ax.containers[0], color = "black")
plt.title("Distribution Churn")
plt.ylabel("Number of Customers")
plt.show()



features = ["gender","Partner","Dependents","SeniorCitizen"]

features = ["gender","Partner","Dependents","SeniorCitizen"]
plt.figure(figsize = (14,4))
for i in range(0,len(features)):
  plt.subplot(1, len(features), i+1)
  ax = sns.countplot(x=telco[features[i]], palette="Set2")
  ax.bar_label(ax.containers[0], color = "Black")
  plt.title("Distribution " + features[i])
  plt.ylabel("Number of Customers")
  plt.tight_layout()

#SERVICE_TYPE

telco.info()

service_type = ["PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies"]
telco[service_type].describe()

plt.figure(figsize = (12,16))
for i in range(0,len(service_type)):
  plt.subplot(4, len(service_type)//3, i+1)
  fx = sns.countplot(x=telco[service_type[i]], palette= "Set2")
  fx.bar_label(fx.containers[0], color = "Black")
  plt.title("Distribution " + service_type[i])
  plt.ylabel("Number of Customers")
  plt.tight_layout()


# PAYMENT TYPE

telco.info()

payment_type = ["Contract","PaperlessBilling","PaymentMethod"]

plt.figure(figsize = (24, 12))
for i in range(0, len(payment_type)):
  plt.subplot(1, len(payment_type), i+1)
  gx = sns.countplot(x=telco[payment_type[i]], palette="Set2")
  gx.bar_label(gx.containers[0], color = "black")
  plt.title("Distribution " + payment_type[i])
  plt.ylabel("Number of Customers")
  plt.tight_layout()
  
  
# CHURN DEMOGRAPHICS

features = ["gender","Partner","Dependents","SeniorCitizen"]
plt.figure(figsize = (10,8))
for i in range(0,len(features)):
  churn_demografi = telco.groupby(features[i],as_index = False)["Churn"].value_counts()
  plt.subplot(2, len(features)//2, i+1)
  ax = sns.barplot(x=features[i], y = "count", hue="Churn", data = churn_demografi, palette={"Yes": "mediumseagreen", "No": "lightcoral"})
  ax.bar_label(ax.containers[0], color = "Black")
  ax.bar_label(ax.containers[1], color = "Black")
  plt.title("Churn by " + features[i])
  plt.ylabel("Number of Customers")
  plt.tight_layout()
  
# CHURN SERVICE TYPE

plt.figure(figsize = (12,16))
for i in range(0, len(service_type)):
  churn_service = telco.groupby(service_type[i], as_index= False)["Churn"].value_counts()
  plt.subplot(4, len(service_type)//3, i+1)
  fx = sns.barplot(x=service_type[i], y = "count", hue="Churn", data = churn_service, palette={"Yes": "mediumseagreen", "No": "lightcoral"})
  fx.bar_label(fx.containers[0], color = "black")
  plt.title("Churn by " + service_type[i])
  plt.ylabel("Number of Customers")
  plt.tight_layout()
  
# CHURN PAYMENT TYPE

payment_type = ["Contract","PaperlessBilling","PaymentMethod"]
plt.figure(figsize = (16,6))
for i in range(0, len(payment_type)):
  churn_payment = telco.groupby(payment_type[i], as_index = False)["Churn"].value_counts()
  plt.subplot(1, len(payment_type), i+1)
  gx = sns.barplot(x=payment_type[i], y = "count", hue = "Churn", data = churn_payment, palette={"Yes": "mediumseagreen", "No": "lightcoral"})
  gx.bar_label(gx.containers[0], color = "black")
  plt.title("Churn by " + payment_type[i])
  plt.ylabel("Number of Customers")
  plt.tight_layout()
  
# PAIRPLOT

sns.pairplot(telco, hue="Churn", palette={"Yes": "mediumseagreen", "No": "lightcoral"})
plt.tight_layout()
plt.show()

