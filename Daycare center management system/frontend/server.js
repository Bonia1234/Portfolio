const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 8080;

// Set up EJS as the view engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// Middleware for parsing JSON bodies
app.use(bodyParser.json());

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Route for login page
app.get('/login', (req, res) => {
  res.render('login');
});

// Handle login form submission
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  // Example authentication logic
  if (username === 'admin' && password === 'password') {
    res.redirect('/dashboard');
  } else {
    res.send('Invalid credentials. Please try again.');
  }
});

// Route for dashboard
app.get('/dashboard', (req, res) => {
  res.render('dashboard');
});

// Routes for CRUD pages
app.get('/facility', (req, res) => {
  res.render('facility');
});

app.get('/classroom', (req, res) => {
  res.render('classroom');
});

app.get('/teacher', (req, res) => {
  res.render('teacher');
});

app.get('/child', (req, res) => {
  res.render('child');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}/login`);
});
