from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html', data=None)

@app.route("/barcode", methods=['GET','POST'])
def get_barcode():
	if request.method == 'POST':
		barcode = request.form['javascript_data']

		nutritionixKey = "e94199ad7b6a8b0808c66d25cf8ffe62"
		classid = "a54f164e"
		product_url = "https://api.nutritionix.com/v1_1/item?appId=%s&appKey=%s&upc=%s" % (classid, nutritionixKey, barcode)
		#r = requests.get(url=product_url)
		data = requests.get(product_url).json()

		try:
			name = data['item_name']
			brand = data['brand_name']
			ingredients = data['nf_ingredient_statement']
			item_info = "Brand: %s\n Name: %s\n Ingredients:%s\n" % (name, brand, ingredients)
			print("***************************")
			print(item_info)
			print("***************************")

			item = {
				'name': name,
				'brand': brand,
				'ingredients': ingredients
			}
			return render_template('index.html', data=item)
		except:
			print("***************************")
			print(item_info)
			print("***************************")

			item = {
				'name': "N/A",
				'brand': "N/A",
				'ingredients': "N/A"
			}
			return render_template('index.html', data=item)
	else:
		return index()

if __name__ == '__main__':
    app.run()


'''
http://api.walmartlabs.com/v1/search?query=[BARCODE]]&format=json&apiKey=jmrjysyvwn77dsnsrmktru5e
'''