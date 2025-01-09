# Django Application with Prometheus Logging Integration

This project demonstrates how to set up a Django application that logs events and integrates with Prometheus to monitor log metrics.

---

## Features
- **Django Logging**: Logs INFO, WARNING, and ERROR messages.
- **Prometheus Monitoring**: Exposes log-related metrics via a `/metrics` endpoint.
- **Metrics Visualization**: Designed for integration with Prometheus and Grafana.

---

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8+
- Virtual environment support
- Prometheus installed and running

---

## Getting Started

Follow these steps to set up and run the project:

### Step 1: Clone the Repository
Clone this repository to your local machine:
```
git clone https://github.com/oluwabunmifife/logger-demo.git
cd logger-demo
```

### Step 2: Create a virtual environment
Create a virtual environment to isolate project dependencies:
```
python3 -m venv venv
```

### Step 3: Activate the environment
macOS/Linux
```
source venv/bin/activate
```

Windows
```
venv\Scripts\activate
```

### Step 4: Install dependencies
Install the project dependencies from the requirements.txt file:
```
pip install -r requirements.txt
```
