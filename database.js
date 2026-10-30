const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/yourDatabaseName')
    .then(() => console.log('MongoDB Connected Successfully'))
    .catch(err => console.error('MongoDB Connection Error:', err));
