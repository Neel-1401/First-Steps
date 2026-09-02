# Internet Speedometer

A lightweight Tkinter desktop app that measures your download speed by timing a real file download — no external speed-test service or API key needed.

## Features

- One-click download speed test (Mbps)
- Runs the network request on a background thread so the UI never freezes
- Minimal dark-themed interface
- Clear status feedback (testing / complete / failed)

## How It Works

The app downloads a 10MB test file from a public test server (`speedtest.tele2.net`) and measures the time taken, then calculates your effective download speed in megabits per second.

> Note: results reflect real-world throughput to that specific server, so they may differ slightly from dedicated speed-test tools like Ookla's Speedtest, which use multiple servers/connections and also measure upload + ping.

## Requirements

- Python 3.x
- Tkinter (included with most standard Python installations)

No external packages needed — everything used (`threading`, `time`, `urllib.request`) is part of Python's standard library.

## How to Run

```bash
python internet_speedometer.py
```

## Usage

1. Click **START TEST**.
2. Wait a few seconds while it downloads the test file in the background.
3. Your download speed in Mbps will be displayed once complete.

## License

Free to use and modify.