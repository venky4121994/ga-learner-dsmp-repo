# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path) 

#probability of fico score greater than 700
p_a = df[df['fico'].astype(float)>700].shape[0]/df.shape[0]
print(p_a)

# probability of purpose == debt_consolidation
p_b = df[df['purpose'] == 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

#create a new data frame for condition['purpose'] == debt_consolidation
df1 = df[df['purpose']=='debt_consolidation']

#Calculate the P(A|B)
p_a_b = df1[df1['fico'].astype(float)>700].shape[0]/df1.shape[0]
print(p_a_b)

#Check whether P(A) and P(B) are independent from each other 
result = (p_a == p_a_b)
print(result)
# code ends here


# --------------
# code starts here

#calculate p(A) for the event that paid.back.loan == Yes and store it in a variable prob_1p
prob_lp = df[df['paid.back.loan']=="Yes"].shape[0]/df.shape[0]
print(prob_lp)

#calculate the probability for the event credit.policy ==Yes and store it in a varaible prob_cs
prob_cs = df[df['credit.policy']=="Yes"].shape[0]/df.shape[0]
print(prob_cs)

#set a new data frame 
new_df = df[df['paid.back.loan']=="Yes"]

#calcualte p(B|A) for the event paid.back.loan and credit.policy == "Yes"
prob_pd_cs =  new_df[new_df["credit.policy"]=="Yes"].shape[0]/new_df.shape[0]
print(prob_pd_cs)

#calculate the condionaltiy probabitliy using the bayes theorem
bayes = ((prob_pd_cs)*(prob_lp))/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here

df.purpose.value_counts(normalize=True).plot(kind='bar')
df1 = df[df['paid.back.loan']=='No']
df1.purpose.value_counts(normalize=True).plot(kind='bar')  
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
print("The value of the median of installment",inst_median)
inst_mean = df["installment"].mean()
print("The value of the mean of the installment",inst_mean)
df.hist(column='installment',bins = 8)
df.hist(column='log.annual.inc',bins = 8)



# code ends here


