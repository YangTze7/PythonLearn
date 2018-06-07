# 数据预处理
from sklearn.datasets import  load_iris
iris=load_iris()
print(iris)
print("type:",type(iris))
from sklearn.cross_validation import train_test_split
train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.2)
#模型
from sklearn import tree
clf=tree.DecisionTreeClassifier(criterion="entropy")
clf.fit(train_data,train_target)
y_pred = clf.predict(test_data)
# 验证
from sklearn import metrics
print("准确度：",metrics.accuracy_score(y_true=test_target,y_pred= y_pred))
print("混淆矩阵：",metrics.confusion_matrix(y_true=test_target,y_pred=y_pred))
# 
with open("tree.dot","w") as f:
    tree.export_graphviz(clf,out_file=f)
