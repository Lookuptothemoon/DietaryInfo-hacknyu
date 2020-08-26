from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import json
import config

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route("/barcode", methods=['GET','POST'])
def barcode():
	if request.method == 'POST':
		barcode = request.form['javascript_data']

		nutritionixKey = config.nutritionixKey
		appId = config.appId
		product_url = "https://api.nutritionix.com/v1_1/item?appId=%s&appKey=%s&upc=%s" % (appId, nutritionixKey, barcode)
		data = requests.get(product_url).json()
		#data = {'item_name':'N/A', 'brand_name':'N/A', 'nf_ingredient_statement':'N/A'}

		item_info = ""
		print("***************************")
		try:
			name = data['item_name']
			brand = data['brand_name']
			ingredients = data['nf_ingredient_statement']
			item_info = "Brand: %s\nName: %s\nIngredients: %s\n" % (name, brand, ingredients)
			print(item_info)
			return render_template("results.html", hasData=True, data=data)
		except:
			print("Item not found!")
			return render_template("results.html", hasData=False, data="Item not found. Refresh the page and try again!")

	else:
		return index()

if __name__ == '__main__':
    app.run()



'''
http://api.walmartlabs.com/v1/search?query=[BARCODE]]&format=json&apiKey=jmrjysyvwn77dsnsrmktru5e
'''