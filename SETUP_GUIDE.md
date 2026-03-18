# Smart Expense Splitter SETUP GUIDE

## Prerequisites
Before you begin, ensure you have the following installed:
- [Node.js](https://nodejs.org/en/) (version 14 or above)
- [npm](https://www.npmjs.com/) (Node Package Manager)
- A database (e.g., MongoDB, PostgreSQL, etc.)

## Installation Steps
1. **Clone the Repository**  
   Open your terminal and run:
   ```bash
   git clone https://github.com/<owner>/smart-expense-splitter.git
   cd smart-expense-splitter
   ```
2. **Install Dependencies**  
   Once you are in the project directory, run:
   ```bash
   npm install
   ```

## Running the Server
To start the server, use the following command:
```bash
npm start
```
This will start the application, and it will be accessible at `http://localhost:3000`.

## Using the API Endpoints
The application exposes several API endpoints:
- **GET /api/expenses** - Retrieve all expenses
- **POST /api/expenses** - Create a new expense
- **PUT /api/expenses/:id** - Update an expense
- **DELETE /api/expenses/:id** - Delete an expense

Refer to the API documentation for detailed usage of each endpoint and required parameters.

## Database Setup
1. **Set up your database**: Ensure your database service is running and create a database for the application.
2. **Configure the database connection**: Update the database configuration in the `.env` file or `config.js` with your database credentials.
3. **Migrate the database**: Run the migration scripts if required:
   ```bash
   npm run migrate
   ```

## Conclusion
Once you have completed these steps, you should be able to use the Smart Expense Splitter application. For more information, check the documentation or reach out for support.