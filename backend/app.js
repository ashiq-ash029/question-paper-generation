const express = require('express');
const mysql = require('mysql2');
const app = express();
const port = 3000;

// MySQL Database Connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',  // Change this if you have a different username
    password: 'ashiq123',  // Enter your MySQL root password
    database: 'mcq_question_bank'
});

db.connect((err) => {
    if (err) {
        console.error('Database connection failed:', err);
        return;
    }
    console.log('✅ Connected to the database');
});

// API to fetch questions based on department, semester, and subject
app.get("/questions", (req, res) => {
    const { department_id, semester_id, subject_id } = req.query;

    if (!department_id || !semester_id || !subject_id) {
        return res.status(400).json({ error: "Missing query parameters" });
    }

    const sql = `SELECT * FROM questions WHERE department_id = ? AND semester_id = ? AND subject_id = ?`;
    
    db.query(sql, [department_id, semester_id, subject_id], (err, results) => {
        if (err) {
            console.error("Error fetching questions:", err);
            return res.status(500).json({ error: "Database error" });
        }
        res.json(results);
    });
});


    const query = `
        SELECT q.id, q.question_text, q.option_a, q.option_b, q.option_c, q.option_d, q.correct_option
        FROM questions q
        JOIN subjects s ON q.subject_id = s.id
        WHERE s.department_id = ? AND s.semester_id = ? AND s.id = ?`;

    db.query(query, [department_id, semester_id, subject_id], (err, results) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json(results);
    });

// Start server
app.listen(port, () => {
    console.log(`🚀 Server running on port ${port}`);
});
