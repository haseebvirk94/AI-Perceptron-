import pandas

data_csv=pandas.read_csv('iris.csv')
data=data_csv.values.tolist()
colunms=['sepal_length','sepal_width','petal_length','petal_width','species']
mdf=pandas.DataFrame(columns=colunms)
for i in range(0,len(data)):
    values=[]
    values.append(data[i][0])
    values.append(data[i][1])
    values.append(data[i][2])
    values.append(data[i][3])
    if data[i][4]=='Iris-setosa':
        values.append(1)
    elif data[i][4]=='Iris-virginica':
        values.append(0)
    mdf.loc[len(mdf)]=values
    print(values)
mdf.to_csv("ANDGate.csv", index=False)