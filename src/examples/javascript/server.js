// server.js

const express = require("express");
const app = express();
const routes = require("./routes");

// Middleware for parsing JSON requests
app.use(express.json());

// Use the routes from routes.js
app.use("/api", routes);

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
