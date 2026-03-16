# Digantara_testPDN_PGM

Here is a professional README.md file you can upload to your GitHub repository for this project.

You can create a file called README.md and paste the following content.

⸻

:::writing{variant=“standard” id=“48261”}

Power Distribution Automated Test Script

Overview

This project demonstrates a Python-based automated test script used for validating a power distribution or power supply system.
The script simulates an Automated Test Equipment (ATE) workflow where different load conditions are applied and ripple voltage measurements are recorded.

The results are automatically evaluated as PASS or FAIL and stored in a CSV file for analysis.

⸻

Features
	•	Simulates power supply configuration
	•	Applies multiple electronic load conditions
	•	Simulates ripple voltage measurement
	•	Automatic PASS / FAIL decision
	•	Logs results with timestamp
	•	Saves results into a CSV report

⸻

Technologies Used
	•	Python 3
	•	CSV module (data logging)
	•	Random module (measurement simulation)
	•	Datetime module (timestamp generation)

⸻

Test Workflow

The script performs the following sequence:
	1.	Configure the power supply to 5V with 3A current limit
	2.	Apply multiple load conditions:
	•	0.5 A
	•	1.0 A
	•	2.0 A
	•	3.0 A
	3.	Measure ripple voltage (simulated)
	4.	Compare ripple value against threshold (0.05 V)
	5.	Mark the result as PASS or FAIL
	6.	Store the test results in a CSV file

⸻

Example Output (Terminal)

Power Supply Set to 5V, Current Limit 3A
Electronic Load Set to 0.5 A
Load: 0.5A | Ripple: 0.032V | PASS
Electronic Load Set to 1.0 A
Load: 1.0A | Ripple: 0.048V | PASS
Electronic Load Set to 2.0 A
Load: 2.0A | Ripple: 0.061V | FAIL
Electronic Load Set to 3.0 A
Load: 3.0A | Ripple: 0.043V | PASS
Test completed


⸻

Output File

The script generates a file:

test_results.csv

Example CSV content:

Timestamp	Load(A)	Ripple(V)	Result
2026-03-12 10:15:22	0.5	0.032	PASS
2026-03-12 10:15:24	1.0	0.048	PASS
2026-03-12 10:15:26	2.0	0.061	FAIL


⸻

Project Structure

Power-Distribution-Automation
│
├── power_distribution_test.py
├── test_results.csv
└── README.md


⸻

How to Run the Script
	1.	Install Python (version 3.x)
	2.	Clone the repository

git clone https://github.com/yourusername/repository-name.git

	3.	Navigate to the project folder

cd repository-name

	4.	Run the script

python power_distribution_test.py


⸻

Future Improvements

Possible enhancements for this project:
	•	Integration with PyVISA for real instrument control
	•	Oscilloscope waveform capture
	•	Automated plotting of ripple data
	•	Integration with CI/CD testing pipelines
	•	Support for additional load profiles

⸻

Author

Santhanam Karuppusamy

⸻

License

This project is for educational purposes

⸻
