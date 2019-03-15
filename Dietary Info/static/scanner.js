window.onload=function(){

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
			if("0857682003870".length == result.codeResult.code.length){
				barcodes.push(result.codeResult.code);
				iterations++;
			}
			if(iterations == 5){
				// determine barcodes with most occurences
				$.post( "/barcode", {
					javascript_data: getMode(barcodes)
				});
				Quagga.stop();
			}

		});
	}

	// calls startScan on scan-btn button click
	//console.log( getMode([1,2,2,3,3,3,6,4,3,4,6,3,5,3,3,3,3,3,3,2]) );
	document.getElementById("scan-btn").addEventListener("click", startScan);

	/*
	// scan single image file
	Quagga.decodeSingle({
	    decoder: {
	        readers: ["code_128_reader"] // List of active readers
	    },
	    locate: true, // try to locate the barcode in the image
	    src: 'sampleImg.jpg' // or 'data:image/jpg;base64,' + data
	}, function(result){
	    if(result.codeResult) {
	        console.log("result", result.codeResult.code);
	    } else {
	        console.log("not detected");
	    }
	});
	*/


	/*

	var resultCollector = Quagga.ResultCollector.create({
	    capture: true, // keep track of the image producing this result
	    capacity: 20,  // maximum number of results to store
	    blacklist: [   // list containing codes which should not be recorded
	        {code: "3574660239843", format: "ean_13"}],
	    filter: function(codeResult) {
	        // only store results which match this constraint
	        // returns true/false
	        // e.g.: return codeResult.format === "ean_13";
	        return true;
	    }
	});

	Quagga.registerResultCollector(resultCollector);
	console.log(resultCollector.getResults);
	*/

}
