# Team-Project-27

# How to run in your system
- Clone the github repo in your system using ```git clone https://github.com/sjsucmpe272-fall21/Dont-Sleep.git```
- Navigate to the directory ``Dont-sleep``
- Install the requirements mentioned in the ``requirements.txt`` using the command ``pip install -r requirements.txt ``
- Run ``python manage.py makemigrations`` to create migrations based on changes made to models.
- Run ``python manage.py migrate`` to apply the migrations created.
- Run ``python manage.py runserver`` to start the server in ``localhost``.
- Navigate to the URL in the terminal to use the tool.

# Proposal
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
[Drowsiness Data](https://www.kaggle.com/serenaraju/yawn-eye-dataset-new)

