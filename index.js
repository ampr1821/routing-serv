const express = require('express');
const app = express();

const port = 5566;
app.listen(port,function() {
	console.log('listening on port '+port);
});
