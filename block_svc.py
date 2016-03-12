import pickle
from sklearn import svm

def array_to_feature(array):
    meanr = np.mean(array[:,:,0])
    meang = np.mean(array[:,:,1])
    meanb = np.mean(array[:,:,2])
    sigmar =np.std(array[:,:,0])
    sigmag =np.std(array[:,:,1])
    sigmab =np.std(array[:,:,2])
    return [meanr,meang,meanb,sigmar,sigmag,sigmab]


class NewSVC:
    def __init__(self,function=array_to_feature):
        self.SVC = svm.SVC()
        self.x = []
        self.y = []
        self.f = array_to_feature
        self.ax = []
    
    def add_prediction(self,image,y):
        self.x.append(image)
        self.y.append(y)
        self.ax.append(self.f(image))
        self.SVC.fit(self.ax,self.y)
    
    def check_accuracy(self):
        return SVC.score(self.ax,self.y)
    
    def save_to_file(self):
        data = [self.x,self.y]
        pickle.dump(data,open("data"+len(self.y)))
    
    def load_from_file(file):
        svc = NewSVC()
        x,y = pickle.load(open(file))
        for image,yval in zip(x,y):
            svc.add_prediction(image,yval)
        print(check_accuracy)
        return svc
        

