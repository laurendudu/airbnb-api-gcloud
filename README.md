# airbnb-api-gcloud

The idea we had was to predict the price of an Airbnb room based on a dataset. For that, we searched for a complete dataset on Kaggle with the variables we wanted. After many analyzes on different datasets, we found the more interesting one. The dataset matched all of the Airbnb room price in Boston, in the United States.  We found it on Kaggle, here is the link : https://www.kaggle.com/airbnb/boston?select=listings.csv. 

The name of the dataset is “listings.csv”. We treated the data to select only the variables we were interested in. As features, we wanted the number of guests, bathrooms, bedrooms, beds and reviews. But also, what type of room it was (an entire home/apartment, a private room or a shared room) and if the host is a super host or not. Of course, we had also the price variable, which is the variable we wanted to predict. Since the column associated to the price was in a string format, we had to treat it in order to have a column of integer without the dollar sign. 

We decided to create our prediction model in python through a Jupyter Notebook. The libraries we used are the following: 

  -	Tensorflow
  -	Sklearn 
  -	Keras

We have created a sequential neural network with a test size equal to 0.1. Indeed, our dataset was a very small dataset, with only 3557 lines. That is why the test size is very low. Our sequential neural network has 1 input layer, 4 hidden layers and 1 output layer. We entered the values of the features in the input layer, it is then treated through the hidden layers and then, we have the predicted price associated to those features. 

The issues we encountered when created this model was to provide an accurate model with a very small dataset. We had to choose a low value for the test size to have a low loss and provide a good model. Another problem we have is that, again, since the dataset is very small, when we predict the price with other values, the result is not that accurate (as you will see when you will test our chrome extension). 
