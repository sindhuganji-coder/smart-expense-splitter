// Main JavaScript functionality for the Smart Expense Splitter

// Function to get current date and time in UTC
function getCurrentDateTime() {
    const now = new Date();
    return now.toISOString().replace('T', ' ').substr(0, 19);
}

// Function to split expenses
function splitExpenses(expenses, participants) {
    const totalExpenses = expenses.reduce((sum, expense) => sum + expense.amount, 0);
    const splitAmount = totalExpenses / participants.length;

    return participants.map(participant => ({
        name: participant,
        amountOwed: splitAmount
    }));
}

// Log the current date and time
console.log('Current Date and Time (UTC):', getCurrentDateTime());

// Example usage
const expenses = [
    { amount: 50 },
    { amount: 75 }
];
const participants = ['Alice', 'Bob', 'Charlie'];

const splitResult = splitExpenses(expenses, participants);
console.log(splitResult);