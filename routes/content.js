
var path = require('path');
var fs = require('fs');
var express = require('express');

var router = express.Router();

// Initialise function
router.get('/py-1', function(req, res) {
  res.render('py-1');
}); 

// Challenge scoring
router.get('/ch-1', function(req, res) {
  res.render('ch-1');
}); 

// Arguments
router.get('/py-2', function(req, res) {
  res.render('py-2');
}); 

// Challenge scoring parameter
router.get('/ch-2', function(req, res) {
  res.render('ch-2');
}); 

// Return demo
router.get('/py-3', function(req, res) {
  res.render('py-3');
}); 

// Return challenge
router.get('/ch-3', function(req, res) {
  res.render('ch-3');
}); 


module.exports = router;



