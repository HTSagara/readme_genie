// routes.js

const express = require("express");
const router = express.Router();

// Simple route for getting a greeting
router.get("/greet/:name", (req, res) => {
  const name = req.params.name;
  res.send(`Hello, ${name}!`);
});

// Simple route for posting a farewell
router.post("/farewell", (req, res) => {
  const { name } = req.body;
  res.send(`Goodbye, ${name}!`);
});

module.exports = router;
