from sklearn import datasets


iris = datasets.load_iris()

digits = datasets.load_digits()

data = digits.images.reshape((digits.images.shape[0], -1))

estimator = Estimator(param1=1, param2=2)

