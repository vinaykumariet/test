
# # list_test =[4,3,2,1]
# num_list =  [1,2,3,4]


# if num_list[0] < num_list[1]:
#     num1 = num_list[0]
#     num2 = num_list[1]
# else:
#     num2 = num_list[0]
#     num1 = num_list[1]

# for v in num_list[2:]:
#     if v < num1:
#         num2 = num1
#         num1 = v
#     elif num1 == num2:
#         num2 = v
#     elif v < num2 and v != num1:
#         num2 = v


# print('first minimum is '+str(num1))
# print('second minimum is '+str(num2))

# subject_score=[8,3,5,4]
# second_min=subject_score[0]
# minxcc=subject_score[0]

# # for name,score in rank.items():
# #     if score<min:
# #         second_min=min        
# #         min=score
# #     elif second_min > score:
# #         second_min=score
# print(subject_score)
# for k in subject_score:
#     if k < minxcc:
#         second_min=minxcc
#         minxcc=k
#     elif((minxcc >= second_min) and k > second_min ):    
#         second_min=k
#     elif():
        

# print(second_min) 
# 
import pickle 
import json
dict='{"key1":"ggh","key2":"ddf"}'
gdf={"installed":{"client_id":"870242970578-7de398s3vll3lggf6hqos0is1jqv7qmo.apps.googleusercontent.com","project_id":"quickstart-1549256356802","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"g4Xv1plqmrCq5ao8XT3HqejC","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}

# print(gdf)


# kkk={"key1":"jjjjjj","key2":"dsgdfhg"}
# dbfile =  open('testsss.pickle', 'ab')
# pickle.dump(gdf,dbfile)
# dbfile.close()     

with open('token.pickle', 'rb') as f:
# dbfile = open('I:/logical/data_structure/token.pickle', 'rb')      
    db = pickle.load(f)
    print(db) #gives value1)  
# for keys in db: 
#     print(keys, '=>', db[keys])

         