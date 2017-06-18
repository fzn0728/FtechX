import pandas as pd
import os
import graphlab
# pass in column names for each CSV and read them using pandas. 
# Column names available in the readme file

#Reading users file:
os.chdir(r'C:\Users\Chandler\Desktop\FtechX\Recomendation Engine Demo')
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/ml-100k/u.user', sep='|', names=u_cols,encoding='latin-1')


# Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/ml-100k/u.data', sep='\t', names=r_cols,encoding='latin-1')

# Reading items file:
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/ml-100k/u.item', sep='|', names=i_cols,encoding='latin-1')

print(users.head())

print(ratings.head())

print(items.head())

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_base = pd.read_csv('ml-100k/ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('ml-100k/ml-100k/ua.test', sep='\t', names=r_cols, encoding='latin-1')

print(ratings_base.head())
print(ratings_test.head())