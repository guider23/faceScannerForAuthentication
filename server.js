const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const { spawn } = require('child_process');

const app = express();

// Increase the limit for JSON payload to handle larger images
app.use(bodyParser.json({ limit: '50mb' }));  // Adjust the size as needed

// MySQL Database Configuration
const db = mysql.createConnection({
  host: 'monorail.proxy.rlwy.net', 
  user: 'root',                    
  password: 'zXWDfwKjtWblWnESNVQnHrrnVjOfLVAC', 
  database: 'railway',         
  port: 24027,                     
  connectTimeout: 10000,
});

// Connect to the database
db.connect(err => {
  if (err) {
    console.error('Failed to connect to database:', err);
    process.exit(1); // Exit if the database connection fails
  } else {
    console.log('Connected to the database.');
  }
});

// Face processing and registration
app.post('/register', (req, res) => {
  const { real_name, unique_code, image } = req.body;

  if (!real_name || !unique_code || !image) {
    return res.status(400).json({
      status: 'error',
      message: 'Please provide all required fields: real_name, unique_code, image.',
    });
  }

  // Call the Python script to process the face
  const python = spawn('python', ['face_processor.py']);

  python.stdin.write(JSON.stringify({ image }));
  python.stdin.end();

  let dataString = '';

  python.stdout.on('data', (data) => {
    dataString += data.toString();
  });

  python.stderr.on('data', (data) => {
    console.error(`Python error: ${data}`);
  });

  python.on('close', (code) => {
    try {
      const result = JSON.parse(dataString);
      if (!result.success) {
        return res.status(400).json({ status: 'error', message: result.error });
      }

      const face_embedding = result.face_embedding;

      // Check if the unique code exists
      const checkQuery = 'SELECT * FROM users WHERE unique_code = ?';

      db.query(checkQuery, [unique_code], (err, results) => {
        if (err) {
          return res.status(500).json({ status: 'error', message: 'Database error.', details: err.message });
        }

        if (results.length === 0) {
          return res.status(400).json({ status: 'error', message: 'Unique code not found. Registration failed.' });
        }

        // Unique code exists, update the user with real_name and face_embedding
        const updateQuery = 'UPDATE users SET real_name = ?, face_embedding = ? WHERE unique_code = ?';

        db.query(updateQuery, [real_name, JSON.stringify(face_embedding), unique_code], (err) => {
          if (err) {
            return res.status(500).json({ status: 'error', message: 'Error updating user data.', details: err.message });
          }

          return res.status(200).json({ status: 'success', message: 'User registered and data updated successfully.' });
        });
      });

    } catch (err) {
      return res.status(500).json({ status: 'error', message: 'Error parsing Python response.', details: err.message });
    }
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
