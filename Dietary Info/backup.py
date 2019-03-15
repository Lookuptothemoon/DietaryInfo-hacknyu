from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route("/barcode", methods=['GET','POST'])
def get_barcode():
	if request.method == 'POST':
		barcode = request.form['javascript_data']

		# get JSON file for product
		barcode_url = ("http://api.walmartlabs.com/v1/search?query=%s&format=json&apiKey=" + walmartKey) % barcode
		barcode_response = requests.get(barcode_url)
		barcode_data = barcode_response.json()

		# prints id of barcodes if there are any
		walmartKey = 'jmrjysyvwn77dsnsrmktru5e'
		message = ""
		if(barcode_data['numItems'] == 0):
			return jsonify(error="This item can not be found")
		else:
			# get first id of product with barcode
			nutritionixKey = "420146a314d511263c1c33479a8fed23"
			item_id = barcode_data["items"][0]["itemId"]
			id_url = ("http://api.walmartlabs.com/v1/items/%s?format=json&apiKey=" + walmartKey) % item_id
			id_response = requests.get(id_url)
			id_data = id_response.json()

			product_info = id_data["name"]
			data = {
				"appId":"c2ea5310",
				"appKey": nutritionixKey,
				"query": product_info,
				"fields":["item_name","brand_name","nf_calories","nf_serving_size_qty","nf_serving_size_unit"],
				"sort":{
					"field":"_score",
					"order":"desc"
				},
				"filters":{
					"item_type":2
				}
			}

			product_url = "https://api.nutritionix.com/v1_1/search/%s?" % product_info
			r = requests.get(url=product_url, data=data)
			product_data = r.text
			#return render_template('index.html', message=product_data)
			return product_data
		else:
			index()

if __name__ == '__main__':
    app.run()


'''
http://api.walmartlabs.com/v1/search?query=[BARCODE]]&format=json&apiKey=jmrjysyvwn77dsnsrmktru5e
'''