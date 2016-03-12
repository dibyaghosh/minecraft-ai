import pickle
from sklearn import svm
import numpy as np
from scipy.misc import imresize
from sklearn import linear_model

def array_to_feature(array):
    meanr = np.mean(array[:,:,0])
    meang = np.mean(array[:,:,1])
    meanb = np.mean(array[:,:,2])
    sigmar =np.std(array[:,:,0])
    sigmag =np.std(array[:,:,1])
    sigmab =np.std(array[:,:,2])
    return [meanr,meang,meanb,sigmar,sigmag,sigmab]

def new_feature_array(array):
    array = imresize(array,(5,5))
    return array.flatten()

default_svc = new_feature_array

class NewSVC:
    def __init__(self,function=default_svc):
        self.SVC = linear_model.LogisticRegression()
        self.x = []
        self.y = []
        self.f = array_to_feature
        self.ax = []
    
    def add_prediction(self, image,y):
        self.x.append(image)
        self.y.append(y)
        self.ax.append(self.f(image))
        if len(set(self.y)) > 1:
            self.SVC.fit(self.ax, self.y)
            print(self.check_accuracy())
        self.save_to_file()
    
    def check_accuracy(self):
        return self.SVC.score(self.ax,self.y)
    
    def guess(self,image):
        if len(set(self.y)) > 1:
            return self.SVC.predict(self.f(image))

    def save_to_file(self):
        data = [self.x,self.y]
        pickle.dump(data,open("blockdata",'wb'))
    
    def load_from_file(file):
        svc = NewSVC()
        x,y = pickle.load(open(file,'rb'))
        svc.x = x
        svc.y = y
        svc.ax = [svc.f(i) for i in x]
        svc.SVC.fit(svc.ax,svc.y)
        print(svc.check_accuracy())
        return svc
        

