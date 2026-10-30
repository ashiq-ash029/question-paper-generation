const express = require('express');
const { generateQuestions } = require('../controllers/questionController');

const router = express.Router();

// Route for generating questions via GPT Wrapper
router.post('/generate', generateQuestions);

module.exports = router;
