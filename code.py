import pandas as pd
import os 

data = {"Name" : ["sagar","vineet","lalit"],
        "age" : [18,34,34]

}

df = pd.DataFrame(data)
# print(df)
#new row 
new = {"Name":"ganesh",
        "age": 34
        }

df.loc[len(df.index)] = new

data_dir = 'Data'

os.makedirs(data_dir,exist_ok =True)

file_path = os.path.join(data_dir,"sample.csv")
#define file path 
df.to_csv(file_path,index = False)


print(f"file_path : {file_path}")
