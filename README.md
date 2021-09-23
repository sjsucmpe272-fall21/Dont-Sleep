# Team-Project-27
Real Time Car Price Analyser
1. Introduction to the problem statement

The current car market is very hot. The price of a used car can easily go beyond the MSRP of a new one. And users need to pay hundreds or even thousands more to get a new car. Real time car price analyzer provides an intuitive way to the users by showing them the trend in charts. Moreover, price prediction powered by machine learning is also provided in this application. In this way, the users can get to know more about the whole market and make their decisions correspondingly. 

2. Abstract (rough draft)

There are so many websites such as KBB, edmunds, Truecar and etc that provide sales info about different cars. And users can easily find out the current selling price of the car they want on these websites. However, none of these sites provides any chart which includes historical data and visualizes the trend of the price. Users will have a hard time when they want to know when to buy or sell their cars. Real time car price analyser solves this problem. By showing the car prices in a chart and predicting the price in the future, this app can clearly visualize the potential top or bottom price of the car they want. In this way, they will have a clear picture about what kind of market they are in and make their decision accordingly.

3. Approach

The backend of the app will fetch the car prices on a daily/weekly basis from different websites such as Truecar and Craigslist. After getting the up to date data, the app will store them into the database and send them to the front end. A machine learning model will also be introduced to serve the prediction functionality.
The frontend part will get the data and present them into a chart, which indicates the current price trend such as going up or going down.

![Architecture (1)](https://user-images.githubusercontent.com/26152890/134454319-1a04047e-4e29-46ae-a32b-bf34c2ea6e3d.jpeg)



4. Persona

Our target audience will be the potential car buyers and sellers.

5. Dataset links

https://www.kaggle.com/austinreese/craigslist-carstrucks-data
https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho
https://www.kaggle.com/avikasliwal/used-cars-price-prediction

