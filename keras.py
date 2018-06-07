import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.optimizers import SGD
from sklearn.datasets import load_iris
iris=load_iris()
print(iris["target"])
from sklearn.preprocessing import LabelBinarizer
print(LabelBinarizer().fit_transform(iris["target"]))
from sklearn.cross_validation import train_test_split
train_data,test_data,train_target,test_target = train_test_split(iris.data,iris.target,test_size=0.2)
label_train = LabelBinarizer().fit_transform(train_target)
label_test = LabelBinarizer().fit_transform(test_target)

# 
model = Sequential(
    [
        Dense(5,input_dim = 4),
        Activation("relu"),
        Dense(3),
        Activation("sigmoid"),
    ]
)
sgd = SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(optimizer = sgd,loss="categorical_crossentropy")
model.fit(train_data,label_train,nb_epoch=200,batch_size=40)
print(model.predict_classes(test_data))
model.save_weights("nn")
model.load_weights("nn")
