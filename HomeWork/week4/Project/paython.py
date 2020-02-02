from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

# target_movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
# print (target_movie['star'])
#
# taget_star = db.movies.find_one({'title':'사운드 오브 뮤직'})['star']
# seach_result = list(db.movies.find({'star':taget_star}))
#
# for movie in seach_result:
#     print(movie['title'])

taget_star = db.movies.find_one({'title':'사운드 오브 뮤직'})['star']
search_query = {'star':taget_star}
update_query = {'$set':{'star':0}}
db.movies.update_many(search_query,update_query)
# db.movies.find_one({'title':'사운드 오브 뮤직'})

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
target_movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
target_star = target_movie['star']

db.movies.update_many({'star':target_star},{'$set':{'star':0}})

