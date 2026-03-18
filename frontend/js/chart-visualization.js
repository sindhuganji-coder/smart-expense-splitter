// Import Chart.js
import Chart from 'chart.js';

// Function to create a chart visualization
function createChart(ctx, data, labels) {
    const myChart = new Chart(ctx, {
        type: 'bar', // The type of chart
        data: {
            labels: labels,
            datasets: [{
                label: 'My Dataset',
                data: data,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Example usage (to be called with actual canvas context, data, and labels)
// createChart(document.getElementById('myChart').getContext('2d'), [10, 20, 30], ['Label1', 'Label2', 'Label3']);
