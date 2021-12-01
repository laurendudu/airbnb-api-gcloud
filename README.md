## The Prediction Model
### Overview

The idea we had was to predict the price of an Airbnb room based on a dataset. In order to do so, we searched for a complete dataset on Kaggle with the variables we wanted. We chose [this one](https://www.kaggle.com/airbnb/boston?select=listings.csv). The dataset matched all of the Airbnb room price in Boston, in the United States. 

The name of the dataset is “listings.csv”. We treated the data to select only the variables we were interested in. As features, we wanted the `number of guests`, `bathrooms`, `bedrooms`, `beds` and `reviews`. But also, what `type of room` it was (an entire home/apartment, a private room or a shared room) and if the host is a `superhost` or not. Of course, we had also the price variable, which is the variable we wanted to predict. Since the column associated to the price was in a string format, we had to treat it in order to have a column of integer without the dollar sign. 

We decided to create our prediction model in python through a Jupyter Notebook. The libraries we used are the following: 
  -	`Tensorflow`
  -	`Sklearn` 
  -	`Keras`

We have created a sequential neural network with a test size equal to 0.1. Indeed, our dataset was a very small dataset, with only 3557 lines. That is why the test size is very low. Our sequential neural network has 1 input layer, 4 hidden layers and 1 output layer. We entered the values of the features in the input layer, it is then treated through the hidden layers and then, we have the predicted price associated to those features. 


### Issues
The issue we encountered while training this model was the accuracy. Since our dataset is relatively small, we had to choose a small test size, so we could minimize the loss. This lead to a bad accuracy when predicting the prices, generally the prices are predicted higher than expected. To solve this porblem, we could gather data from other locations, not only boston to construct a bigger dataset, and also use more input variables. 

## The API


### Overview
The repository for this project can be found [here](https://github.com/laurendudu/airbnb-api-gcloud). The API imports the model mentioned previously. It is coded in Python, with the `Flask` library, and was deployed with [Google Cloud Platform](https://cloud.google.com/). It is callable by a `POST` method, by specifying the header `Content-Type: application/json`

The input should be specified in the body as a raw format. The parameters are:
```
[[
  number of guests, 
  number of bathrooms, 
  number of bedrooms, 
  number of beds, 
  number of reviews, 
  room type, 
  superhost boolean
]]
```

## Issues 
While deploying the API, there was some conflict between the keras and tensorflow versions. If the keras version was unspecified, the API had an internal server error. To solve this problem, we had to spcify a downgraded version of keras in `requirements.txt`.

The second issue which was the biggest, was dealing with the CORS policy. When calling the API from the extension, the ports are not the same, which causes a block from the CORS policy. 

```js
Access to fetch at 'xxx' from origin 'chrome-extension://xxx' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```

To solve this problem, we used [cors-anywhere](https://github.com/Rob--W/cors-anywhere). This repository allowed to easily deploy a proxy with `Heroku`, which added the correct headers to the request. 

```bash
git clone https://github.com/Rob--W/cors-anywhere.git
cd cors-anywhere/
npm install
heroku create
git push heroku master
```

This:
1. Forwards the request to the API.
2. Receives the response from the API.
3. Adds the Access-Control-Allow-Origin header to the response.
4. Passes that response, with that added header, back to the requesting frontend code.

### Costs
- Continer Registry

The container is situated in the US (multi-region) is about $0.026 per GB per month. 

- Cloud Run

The cloud run is deploye in `europe-north` which is subject to Tier 1 pricing. 

The cost for the CPU which is allocated only during request processing is $0.00002400 / vCPU-second beyond free tier. 

The cost for the memory is $0.00000250 / GiB-second beyond free tier. 

The cost for requests is $0.40 / million requests beyond free tier. 

The cost is estimated [here](https://cloud.google.com/products/calculator/#id=ac02c40b-a2bf-4240-8a64-7bcbd5409b57)
