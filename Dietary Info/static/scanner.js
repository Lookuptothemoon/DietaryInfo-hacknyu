// MAIN JS

// given an array, returns the mode
function getMode(arr){
	// determine item in array with most occurences
	arr.sort();
	var num = arr[0];
	var max_occur = 1;
	var current_occur = 1;
	var i = 1;
	while(i < arr.length){
		if(arr[i] != arr[i-1]){
			current_occur = 1;
		}else{
			current_occur++;
			if(current_occur > max_occur){
				max_occur = current_occur;
				num = arr[i];
			}
		}
		i++;
	}
	return num;
}

// camera scanner
// gets first barcode with 5 instances and send to barcode route in Flask
function startScan(){
	Quagga.init({
		inputStream: {
			name: "Live",
			type: "LiveStream",
			target: document.querySelector("#scanner-container"),
			constraints: {
				width: 480,
				height: 320,
				facingMode: "environment"
			},
		},
		decoder: {
			readers: [
				"code_128_reader",
	            "ean_reader",
	            "ean_8_reader",
	            "code_39_reader",
	            "code_39_vin_reader",
	            "codabar_reader",
	            "upc_reader",
	            "upc_e_reader",
	            "i2of5_reader"
			]
		}

	}, function(err) {
		if (err) {
			console.log(err);
			return
		}
		console.log("Initialization finished. Ready to start!");
		Quagga.start();
	});

	var barcodes = [];
	var iterations = 0;
	Quagga.onDetected(function(result){
		console.log(result.codeResult.code);
		if("0857682003870".length == result.codeResult.code.length){	// used ex. barcode for fixed length constraint
			barcodes.push(result.codeResult.code);
			iterations++;
		}
		if(iterations == 5){
			// determine barcodes with most occurences
			resp = $.post( "/barcode", {
				javascript_data: getMode(barcodes)
			}, function(data, status){
				console.log(data);
				console.log(status);
				$("#results").replaceWith(data);
			});
			Quagga.stop();
		}

	});
}
