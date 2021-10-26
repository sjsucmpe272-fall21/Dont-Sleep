# Team-Project-27

## Idea: Drowsiness Detection System
### Introduction to problem statement:

“1 in 25 adult drivers report that they have fallen asleep at the wheel in the past 30 days”

If you have driven before, you’ve been drowsy at the wheel at some point. It’s not something we like to admit but it’s an important problem with serious consequences that needs to be addressed. 1 in 4 vehicle accidents are caused by drowsy driving and 1 in 25 adult drivers report that they have fallen asleep at the wheel in the past 30 days. The scariest part is that drowsy driving isn’t just falling asleep while driving. Drowsy driving can be as small as a brief state of unconsciousness when the driver is not paying full attention to the road. Drowsy driving results in over 71,000 injuries, 1,500 deaths, and $12.5 billion in monetary losses per year. 

### Abstract:

To tackle this problem, the current-generation cars can be installed with a system that detects if a drive is drowsy or not.
We will be developing a solution using multi-layer neural network. In real scenario, it can be used to then activate autonomous driving system to help prevent any unfortunate events.

### Approach:
The front-end part will contain taking in the video feed and feeding it to the model. The trained model will then help predict if the drive is drowsy or not.

### Persona:
Our target audience would be anyone who drives a car, truck or any other kind of vehicle.

### Dataset Link:
[Drowsiness Data](http://www.cs.unc.edu/~abyrnes1/dataset.htm)



<br><br><br>
# Previous Ideas 

## Idea 1: Real Time Car Price Analyser
### 1. Introduction to the problem statement

The current car market is very hot. The price of a used car can easily go beyond the MSRP of a new one. And users need to pay hundreds or even thousands more to get a new car. Real time car price analyzer provides an intuitive way to the users by showing them the trend in charts. Moreover, price prediction powered by machine learning is also provided in this application. In this way, the users can get to know more about the whole market and make their decisions correspondingly. 

### 2. Abstract (rough draft)

There are so many websites such as KBB, edmunds, Truecar and etc that provide sales info about different cars. And users can easily find out the current selling price of the car they want on these websites. However, none of these sites provides any chart which includes historical data and visualizes the trend of the price. Users will have a hard time when they want to know when to buy or sell their cars. Real time car price analyser solves this problem. By showing the car prices in a chart and predicting the price in the future, this app can clearly visualize the potential top or bottom price of the car they want. In this way, they will have a clear picture about what kind of market they are in and make their decision accordingly.

### 3. Approach

The backend of the app will fetch the car prices on a daily/weekly basis from different websites such as Truecar and Craigslist. After getting the up to date data, the app will store them into the database and send them to the front end. A machine learning model will also be introduced to serve the prediction functionality.
The frontend part will get the data and present them into a chart, which indicates the current price trend such as going up or going down.

![Architecture (1)](https://user-images.githubusercontent.com/26152890/134454319-1a04047e-4e29-46ae-a32b-bf34c2ea6e3d.jpeg)



### 4. Persona

Our target audience will be the potential car buyers and sellers.

### 5. Dataset links

https://www.kaggle.com/austinreese/craigslist-carstrucks-data

https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho

https://www.kaggle.com/avikasliwal/used-cars-price-prediction


## Idea 2: Online Food delivery App for Homemade Food

### 1. Introduction to the problem statement
There are 2 major problems

1) The people who don’t have cook at their home face lot of difficulties to manage daily healthy & hygienic food without burning a nice hole into their pockets.

2) The labour force participation rate for women is falling. It’s not like women don’t want to work, but work opportunities for them are decreasing. 

### 2. Abstract (rough draft) 
We can provide a platform where customers can see a list of real moms and what they’ll be cooking for their family. They can just ask the moms to also prepare food for them by clicking a button. As the food is home cooked as well, so cost to housewife is very low. They can let our app take care of the delivery or even the customer can pick it up if he/she wants to. 

### 3. Approach
The backend of the app will fetch the food items, dishes from various Moms and give it ratings . Based on our algorithm we will decide the rating and show the highest rated food dishes more frequently. We will have categories of dishes like Mexican, Chinese, Continental and people can search names of various dishes.  A database will be maintained for the dishes, the app will store them into the database and send them to front end. The frontend part will get the data and present them in form of different images and icons. These images will be provided by the moms or uploaded by us.

![Architecture (2)](https://user-images.githubusercontent.com/26152890/134455351-2c3da48c-1070-482f-a603-ed7956bf7d40.png)

### 4. Persona 
Our target audience will be the potential foodies and people who are looking for heathy snacking options.

## Idea 3: Allergic food detection

### 1. Introduction to the problem statement:
The aim is to identify allergic food from a given image.

### 2. Abstract:
Food allergies are a growing food safety and public health concern that affect an estimated 8% of children in the United States. That’s 1 in 13 children, or about 2 students per classroom. A food allergy occurs when the body has a specific and reproducible immune response to certain foods. The body’s immune response can be severe and life threatening, such as anaphylaxis. Although the immune system normally protects people from germs, in people with food allergies, the immune system mistakenly responds to food as if it were harmful.

There is no cure for food allergies. Strict avoidance of the food allergen is the only way to prevent a reaction. Our app will allow people to take a picture and check if it contains any item they are allergic to.

### 3. Approach:
The front end will help the user to upload an image, which will then be checked for any allergic food using an API call. The data received from the API call will be sent to the front end and presented to the user.

<img width="837" alt="Architecture (3)" src="https://user-images.githubusercontent.com/26152890/134455562-ef08a120-fab8-4232-a494-3bee33a6dc62.png">


### 4. Persona:
Our target audience is people who are allergic to certain food items.

### 5. API Links:
[link](https://www.clarifai.com/models/ai-food-recognition)
