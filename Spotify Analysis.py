#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#pd.options.display.max_columns = 10 (to display the number of coloumns in the output as not all are shown)
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


df_tracks=pd.read_csv("C:\Users\Divyen\Downloads\archive (1)\tracks.csv")
(df_tracks.head())


# In[7]:


#check null values
pd.isnull(df_tracks).sum()


# In[8]:


#check info
df_tracks.info()


# In[9]:


#10 least spotify artists based on popularity
sorted_df=df_tracks.sort_values('popularity',ascending=True).head(10)
sorted_df


# In[10]:


#to get descriptive stats
df_tracks.describe().transpose()


# In[11]:


#most popular top 10
most_popular=df_tracks.query('popularity>90',inplace=False).sort_values('popularity',ascending=False)#inplace is false so ther wont be any change in the og dataframe
most_popular[:10]


# In[12]:


#to change the index
df_tracks.set_index("release_date",inplace=True)
df_tracks.index=pd.to_datetime(df_tracks.index)#changing the value to date time format
df_tracks.head()


# In[13]:


#to check which artists is prestent in the following row suppose 18
df_tracks[['artists']].iloc[18]


# In[14]:


#convert duration of miliseconds to seconds
df_tracks['duration']=df_tracks['duration_ms'].apply(lambda x:round(x/1000))
df_tracks.drop('duration_ms',inplace=True,axis=1)
df_tracks.duration.head()


# In[20]:


#finding correlation using pearson method and dropping 3 attributes.
corr_df=df_tracks.drop(["key","mode","explicit"],axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))#figure size
heatmap=sns.heatmap(corr_df,annot=True,fmt=".1g",vmin=-1,vmax=1,center=0,cmap="inferno",linewidths=1,linecolor="black")
#using heatmap from seaborn setting annotations as true to show the value and fmt as.1g it is string formatting code when adding annotations 
#vmin and vmax are the values added to the color map and cmap is the colormap we want to use can check on seaborn cmap website for
#different colors.
heatmap.set_title("Correlation Heatmap Between Variable")
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)


# In[26]:


sample_df=df_tracks.sample(int(0.004*len(df_tracks)))
print(len(sample_df))


# In[25]:


plt.figure(figsize=(10,6))
sns.regplot(data=sample_df,y="loudness",x="energy",color="c").set(title="Loudness vs Energy correlation")


# In[33]:


plt.figure(figsize=(10,6))
sns.regplot(data=sample_df,y="popularity",x="acousticness",color="b").set(title="Populariy VS Accousticness correlation")


# In[34]:


df_tracks['dates']=df_tracks.index.get_level_values('release_date')
df_tracks.dates=pd.to_datetime(df_tracks.dates)
years=df_tracks.dates.dt.year
#creating a new column year from release date column


# In[36]:


sns.displot(years,discrete=True,aspect=2,height=5,kind="hist").set(title="Number of songs per year")
#number of songs released over the years


# In[39]:


total_dr=df_tracks.duration
fig_dims=(18,7)
fig,ax=plt.subplots(figsize=fig_dims)
fig=sns.barplot(x=years,y=total_dr,ax=ax,errwidth=False).set(title="Year vs Duration")
plt.xticks(rotation=90)


# In[43]:


total_dr=df_tracks.duration
sns.set_style(style="whitegrid")
fig_dims=(10,5)
fig,ax=plt.subplots(figsize=fig_dims)
fig=sns.lineplot(x=years,y=total_dr,ax=ax).set(title="Year vs Duration")
plt.xticks(rotation=60)


# In[44]:


#now based on genres dataset
df_genre=pd.read_csv(r"C:\Users\Divyen\Downloads\archive\SpotifyFeatures.csv")


# In[45]:


df_genre.head()


# In[46]:


plt.title("Duration of songs in different genres")
sns.color_palette("rocket",as_cmap=True)
sns.barplot(y="genre",x="duration_ms",data=df_genre)
plt.xlabel("Duration in milli seconds")
plt.ylabel("Genres")


# In[47]:


sns.set_style(style="darkgrid")
plt.figure(figsize=(10,5))
famous=df_genre.sort_values("popularity",ascending=False).head(10)
sns.barplot(y="genre",x="popularity",data=famous).set(title="Top 5 Genres By Popularity")


# In[ ]:




