#LINEAR REGRESSION

#import and create model
from sklearn.linear_model import LinearRegression

your_model = LinearRegression()

#fit
#.coef_ contiene los coeficientes
#.intercept_ contiene el intercept
your_model.fit(x_training_data, y_training_data)

#predict
#.score() devuelve el coeficiente de R^2
predictions = your_model.predict(your_x_data)

#-------------------------------------------------
#-------------------------------------------------

#NAVIE BAYES

#import and create model
from sklearn.naive_bayes import MultinomialNB

your_model = MultinomialNB()

#fit
your_model.fit(x_training_data, y_training_data)

#predict
# Returns a list of predicted classes - one prediction for every data point
predictions = your_model.predict(your_x_data)

# For every data point, returns a list of probabilities of each class
probabilities = your_model.predict_proba(your_x_data)

#-------------------------------------------------
#-------------------------------------------------

#K-MEANS

#Import and create the model:
from sklearn.cluster import KMeans

your_model = KMeans(n_clusters=4, init='random')
#n_clusters: number of clusters to form and number of centroids to generate
#init: method for initialization
#	k-means++: K-Means++ [default]
#	random: K-Means
#random_state: the seed used by the random number generator [optional]

#Fit
your_model.fit(x_training_data)

#Predict:
predictions = your_model.predict(your_x_data)

#-------------------------------------------------
#-------------------------------------------------

#VALIDATING THE MODEL

#Import and print accuracy, recall, precision, and F1 score:

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

print(accuracy_score(true_labels, guesses))
print(recall_score(true_labels, guesses))
print(precision_score(true_labels, guesses))
print(f1_score(true_labels, guesses))

#Import and print the confusion matrix:

from sklearn.metrics import confusion_matrix

print(confusion_matrix(true_labels, guesses))

#-------------------------------------------------
#-------------------------------------------------

#TRAINING SETS AND TEST SETS

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
#train_size: the proportion of the dataset to include in the train split
#test_size: the proportion of the dataset to include in the test split
#random_state: the seed used by the random number generator [optional]