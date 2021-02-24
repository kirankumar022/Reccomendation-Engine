import pandas as pd

rating=pd.read_excel("E:/Assignments/Assignments week 6/recc assignments/Ratings.xlsx", encoding = 'utf8')

rating.shape
# I dont think id will make any sens e, so iam dropping the column[0], but we still have user_id
rating1=rating.iloc[:,1:5]
rating2=rating1.iloc[:,2:]
rating1.columns
newdata=pd.DataFrame(rating2,index=rating1['user_id'])
newdata.isnull().sum()
new=rating1.set_index('user_id')
exp=new.drop_duplicates()
exp=pd.series()
from sklearn.metrics.pairwise import cosine_similarity
c_1=(cosine_similarity(exp,exp))


####  Unable to allocate 7.64 GiB for an array with shape (32025, 32025) and data type float64
### This error was popping up for me when I tried to create a cosine similarity Matrix. 
### I have worked for more than 4 hours this sunday but couldn't solve . I will get this error clarifed with in the clarrifications session tomorrow.
### I hope this won't count as a late submission as I am submitting my R code, if this error wasn't coming. I would have submitted the whole code.