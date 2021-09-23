# Team-Project-27

## Online Food delivery App for Homemade Food

### Introduction to the problem statement
There are 2 major problems

1) The people who don’t have cook at their home face lot of difficulties to manage daily healthy & hygienic food without burning a nice hole into their pockets.

2) The labour force participation rate for women is falling. It’s not like women don’t want to work, but work opportunities for them are decreasing. 

### Abstract (rough draft) 
We can provide a platform where customers can see a list of real moms and what they’ll be cooking for their family. They can just ask the moms to also prepare food for them by clicking a button. As the food is home cooked as well, so cost to housewife is very low. They can let our app take care of the delivery or even the customer can pick it up if he/she wants to. 

### Approach
The backend of the app will fetch the food items, dishes from various Moms and give it ratings . Based on our algorithm we will decide the rating and show the highest rated food dishes more frequently. We will have categories of dishes like Mexican, Chinese, Continental and people can search names of various dishes.  A database will be maintained for the dishes, the app will store them into the database and send them to front end. The frontend part will get the data and present them in form of different images and icons. These images will be provided by the moms or uploaded by us.

### Persona 
Our target audience will be the potential foodies and people who are looking for heathy snacking options.

## Allergic food detection

### Introduction to the problem statement:
The aim is to identify allergic food from a given image.

### Abstract:
Food allergies are a growing food safety and public health concern that affect an estimated 8% of children in the United States. That’s 1 in 13 children, or about 2 students per classroom. A food allergy occurs when the body has a specific and reproducible immune response to certain foods. The body’s immune response can be severe and life threatening, such as anaphylaxis. Although the immune system normally protects people from germs, in people with food allergies, the immune system mistakenly responds to food as if it were harmful.

There is no cure for food allergies. Strict avoidance of the food allergen is the only way to prevent a reaction. Our app will allow people to take a picture and check if it contains any item they are allergic to.

### Approach:
The front end will help the user to upload an image, which will then be checked for any allergic food using an API call. The data received from the API call will be sent to the front end and presented to the user.

### Persona:
Our target audience is people who are allergic to certain food items.

### API Links:
[link](https://www.clarifai.com/models/ai-food-recognition)
