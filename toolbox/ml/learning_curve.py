""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
print data.DESCR
num_trials = 10
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

# train a model with training percentages between 5 and 90 (see train_percentages) and evaluate
# the resultant accuracy.
# You should repeat each training percentage num_trials times to smooth out variability
# for consistency with the previous example use model = LogisticRegression(C=10**-10) for your learner

# TODO: your code here
for i in range(len(train_percentages)):
	size=0.05+0.05*i # increment size of the training set
	sum_accuracy=0
	for j in range(num_trials): #number_times per size

		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=size)
		model = LogisticRegression(C=10**-10)
		model.fit(X_train, y_train) #get model fit
		
		print "Test accuracy %f"%model.score(X_test,y_test)
		sum_accuracy+=model.score(X_test, y_test)
	sum_accuracy=sum_accuracy/num_trials # get average of accuracy
	test_accuracies[i]=sum_accuracy

fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training(%)')
plt.ylabel('Accuracy on Test Set')
plt.show()
