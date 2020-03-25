df<-read.csv("dataset_Facebook.csv",sep = ';')#import dataset
#View(df)
print(df)
View(df)

#Subsetting of dataset
myvars<-c("Page.total.likes","Type","Category","comment","like","share")
newdata<-df[myvars]#selecting some columns
View(newdata)

myvars1<-c("Page.total.likes","Type","Post.Month","Post.Weekday","Post.Hour","like","comment","share")
newdata1<-df[myvars1]
newdata2<-subset(newdata1,newdata1$Type=="Photo" & newdata1$Post.Month==12,select=c(Page.total.likes,Post.Weekday,like,comment,share))
View(newdata2)


#Merging of dataset
total<-merge(newdata,newdata2,by="Page.total.likes")
View(total)

#Sorting
newdata3<-df[order(df$Post.Month),]
View(newdata3)

#transpose
View(t(df))

#Melting
library(reshape)
data<-melt(data=df,id.vars="Lifetime.Engaged.Users",measure.vars=c("Total.Interactions"))
View(data)

#Casting
data1<-cast(data =data,Lifetime.Engaged.Users~variable,mean)
View(data1)
