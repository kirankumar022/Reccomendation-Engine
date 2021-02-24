library(recommenderlab)
library(reshape2)
library("readxl")
########################## JOke recomendation################
ratings_list <-read_excel(file.choose())   ### open Ratings.xlsx file please
head(ratings_list)
ratings_list <- ratings_list[,2:4]
head(ratings_list)
dim(ratings_list)

## covert to matrix format
ratings_matrix <- as.matrix(acast(ratings_list, user_id~joke_id, fun.aggregate = mean))
dim(ratings_matrix)


## recommendarlab realRatingMatrix format
R <- as(ratings_matrix, "realRatingMatrix")

rec1 = Recommender(R, method="UBCF") ## User-based collaborative filtering


## create n recommendations for a user id. You can input any user id

uid = 1253

print("recommendations for you:")
prediction <- predict(rec1, R[uid], n=2) ## you may change the model here
as(prediction, "list")


