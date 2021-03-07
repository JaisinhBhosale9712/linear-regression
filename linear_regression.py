import pandas
import sklearn
from sklearn import model_selection
from sklearn import linear_model
import xlsxwriter
import pickle
df=pandas.read_excel(r'C:\Users\Jay Bhosale\PycharmProjects\Regression\venv\Lib\site-packages\Students.xlsx')
df=df.drop(['Names'],1)
predict='Sem3'
pandas.set_option('display.max_rows',None)
x=df.drop([predict],1)
y=df[predict]
xtrain, xtest, ytrain, ytest = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
#xtrain.to_excel(r'C:\Users\Jay Bhosale\PycharmProjects\First_Project\venv\Lib\site-packages\xtrain.xlsx',index=False, engine='xlsxwriter')
#xtest.to_excel(r'C:\Users\Jay Bhosale\PycharmProjects\First_Project\venv\Lib\site-packages\xtest.xlsx', index=False,engine='xlsxwriter')
#ytrain.to_excel(r'C:\Users\Jay Bhosale\PycharmProjects\First_Project\venv\Lib\site-packages\ytrain.xlsx',index=False, engine='xlsxwriter')
#ytest.to_excel(r'C:\Users\Jay Bhosale\PycharmProjects\First_Project\venv\Lib\site-packages\ytest.xlsx', index=False,engine='xlsxwriter')
#model= sklearn.linear_model.LinearRegression()
#model.fit(xtrain,ytrain)
#with open('studentmodel.pickle','wb') as  f:
#    pickle.dump(model,f)
newmodel=open('studentmodel.pickle','rb')
model=pickle.load(newmodel)
acc= model.score(xtest,ytest)

#print(dftest)
prediction=model.predict(xtest)
prediction=pandas.DataFrame(prediction)
acc= model.score(xtest,ytest)
print(acc)


