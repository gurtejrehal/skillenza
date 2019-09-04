#Skillenza - Hacknight 2019

##APP: Pragati - Medical App

## What is this?
This is app was made in 12 hours long hackathon in Microsoft Office, Bengaluru.
The Problem statement for this app to build an app which can predict that whether an user requires a medical treatment or not.

##Deployed on Heroku

Deployed [here](http://gurtej123.herokuapp.com "here").

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Remeber while deploying to hide your enviorment variables.

##Installation
- ```git clone https://github.com/gurtejrehal/skillenza.git``` 
- create .env file and add
```python
MICROSOFT_AUZRE_KEY=your_key
GOOGLE_MAP_API_KEY=your_key
```
- Run setup.py
- source .env and the app is up!



## Features
- Predicts whether an user requires a medical treatment or not.
- If user requires medical treatment, it searches for nearest hospital location all by it self.
- User can set the radius to search for the hospital


###EASY TO USE
- Pragati is minimally design with hiding all the  complexities behind and a minimal design to the user.
- User either search for existing person or may add a new patient all in the home page.
- Search results are dynamic and is provided with ready to edit and view options.
- Adding a new patient requires the user to fill the form in 4 steps. 
-  After the filling the form the Pragati AI predicts the whether the patient needs a treatment or not.
- Nearest Hospital search are also provided to the user to look for nearest hospital with radius as a parameter.
- More analysis likes expenses are also covered in the dashboard.
- Apart from this an Admin panel is also provided to get the supreme power and command over all the features of dashboard.

### WORKING PROCEDURE
- Form filling is done in 4 steps as follow:
  - Personal Details
  - Company Details
  - Health Condition
  - Mental Condition
- Then the trained model runs its against the input values and predicts the Treatment requirement.
- Google maps API are used to get Map feature integrated to get the nearest location to the hospital with radius as a parameter.
- Admin panel gives more command to control the software.

### Important URLS
 Home: ```https://localhost/medical/```

 Admin: ```https://localhost/admin/```
 
 
 ### Future Scope
-  User Authorisation 
-  More Effective ML Model
- Locate Treatment related hospitals





