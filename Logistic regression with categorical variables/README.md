<h2>Logistic regression with categorical variables</h2>
<h3>Working with reference categories and interpretting odds ratios</h3>

You've probably arrived at this notebook becuase you've read my article on TowardsDataScience about interpretting odds ratios of categorical variables and learning how to work with reference categories, so welcome!

In this example, I've used an open-source dataset of bike trips with NYC Citibike data (https://www.kaggle.com/datasets/gabrielramos87/bike-trips) and added plenty of derived categorical variables to play with. From the trip duration feature, I've generated a boolean target variable denoting whether a bike trip exceeded 20 minutes or not which I've arbitrarily decided is a 'long' trip. We’ll be looking at which categorical features significantly increase or decrease the odds of a bike trip exceeding 20 minutes.
