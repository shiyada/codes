const mongoose = require('mongoose');

const birthSchema = mongoose.Schema({
    year:String,
    month: String,
    day:String,
    gender:String,
    births:String
});

module.exports = mongoose.model('births', birthSchema);
