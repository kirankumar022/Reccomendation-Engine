
import pandas as pd
 
joke=pd.read_excel("E:/Assignments/Assignments week 6/recc assignments/Ratings.xlsx ")

joke1=joke.iloc[0:10000,:]

final=pd.pivot_table(joke1,values='Rating',index='user_id',columns='joke_id')
final.head()
from sklearn.metrics.pairwise import cosine_similarity

final_user=final.apply(lambda row: row.fillna(row.mean()),axis=1)
final_user.head()


from sklearn.metrics.pairwise import linear_kernel
cosine_sim_matrix=pd.DataFrame(linear_kernel(final_user,final_user))

joke_index=pd.Series(joke.joke_id,index=joke['user_id']).drop_duplicates()
joke_index[1159]

def get_reccomendation(user_id,topN):
    user_id =joke_index[user_id]
    cosine_scores=list(enumerate(cosine_sim_matrix[user_id]))
    cosine_scores=sorted(cosine_scores,key=lambda x:x[1],reverse=True)
    cosine_scores_N=cosine_scores[0:topN+1]
    
    joke_idx= [i[0] for i in cosine_scores_N]
    joke_scores= [i[1] for i in cosine_scores_N]
    joke_similar_show=pd.DataFrame(columns=["user_id","score"])
    joke_similar_show["user_id"]=joke.loc[joke_idx,"user_id"]
    joke_similar_show["score"]=joke_scores
    joke_similar_show.reset_index(inplace=True)
    print(joke_similar_show)
    
    
get_reccomendation(1159, topN =5)
joke_index[1159]

