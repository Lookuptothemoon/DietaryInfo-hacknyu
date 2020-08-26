#Dietary Info Program

###To Access --> ###
1. Before you can start this project, create an account at https://www.nutritionix.com/business/api and get your API keys.

2. Then, create a config.py file visible to productInfo.py as such:
```
nutritionixKey = "enter key here"
appId = "enter app id here"
```

3. After you have completed that step, follow these steps:
$ source venv/bin/activate
$ export FLASK_ENV=development					//puts you in developer mode
$ FLASK_APP=productInfo.py flask run

Copy and paste url into web browser.

Done!
**Note: May not give data for product because might be out of database lookups**
