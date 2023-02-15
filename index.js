const express = require('express');
const app = express();

const port = 5566;
app.listen(port,function() {
	console.log('listening on port '+port);
});

app.get('/',function(req,res) {
	if(req.query.lat1) {
		console.log(req.query.lat1+'\n');
	}
	if(req.query.lon1) {
		console.log(lon1+'\n');
	}
	if(req.query.lat2) {
		console.log(lat2+'\n');
	}
	if(req.query.lon2) {
		console.log(lon2+'\n');
	}
	res.send(req.query.lat1);
});