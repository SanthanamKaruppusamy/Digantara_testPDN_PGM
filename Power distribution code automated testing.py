import csv
import time
import random
from datetime import datetime

# ------------------------------
# Simulated Instrument Functions
# ------------------------------

def setup_power_supply():
    print("Power Supply Set to 5V, Current Limit 3A")
    time.sleep(1)


def setup_load(current):
    print(f"Electronic Load Set to {current} A")
    time.sleep(1)


def capture_waveform():
    # Simulate ripple measurement
    ripple = round(random.uniform(0.02, 0.08), 3)
    return ripple


# ------------------------------
# Test Execution
# ------------------------------

def run_test():

    loads = [0.5, 1.0, 2.0, 3.0]
    results = []

    for load in loads:

        setup_load(load)

        ripple = capture_waveform()

        status = "PASS" if ripple < 0.05 else "FAIL"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        results.append([timestamp, load, ripple, status])

        print(f"Load: {load}A | Ripple: {ripple}V | {status}")

        time.sleep(1)

    return results


# ------------------------------
# Save Results to CSV
# ------------------------------

def save_results(data):

    with open("test_results.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Timestamp", "Load(A)", "Ripple(V)", "Result"])

        writer.writerows(data)

    print("CSV file created: test_results.csv")


# ------------------------------
# Main Program
# ------------------------------

setup_power_supply()

results = run_test()

save_results(results)

print("Test completed")                                              