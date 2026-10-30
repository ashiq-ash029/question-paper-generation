const axios = require('axios');  // Install Axios: npm install axios

// Generate Questions API
const generateQuestions = async (req, res) => {
    const { notes } = req.body;

    try {
        const response = await axios.post('http://localhost:5000/generate-questions', { notes });

        if (response.data.error) {
            return res.status(400).json({ error: response.data.error });
        }

        res.status(200).json({
            message: 'Questions generated successfully!',
            questions: response.data.questions
        });

    } catch (error) {
        res.status(500).json({ error: 'Failed to connect to GPT Wrapper API' });
    }
};

module.exports = { generateQuestions };
