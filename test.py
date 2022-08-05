import pandas as pd

# data = pd.read_csv("accounts.csv")
# for i, row in data.iterrows():
#     print(row[0], row[1])

# data = pd.read_csv("groups-data.csv")
# for i, row in data.iterrows():
#     print(row[0])

import pandas as pd

# # Dataframe example
# df = pd.DataFrame([[1,5,7,8], [9,7,4,3]])

# # Save dataframe as csv file in the current folder
# df.to_csv('filename.csv', index = False,header=False, encoding='utf-8') # False: not include index
# print(df)



# d = pd.DataFrame([['jimam', 'name'], ['jimam2', 'name2']])
# d2 = pd.DataFrame([])
# for i, row in d.iterrows():
#     # print(row)
#     d2 = d2.append(row)
#     break
#     pass
    
# # print()
# print(d2)



# accountsData = pd.read_csv("accounts.csv")
# for i, accountsRow in accountsData.squeeze():
#     print(accountsRow)



from datetime import datetime

print(datetime.strftime(datetime.now(), "%Y-%m-%d__%H:%M:%S"))