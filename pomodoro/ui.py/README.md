# Pomodoro Timer

A minimalist Pomodoro timer built with Python's `tkinter`. Tracks focus/break cycles and keeps a streak count of completed work sessions, with a sound alert when a session ends.

## Features

- 25-minute focus sessions, 5-minute breaks (auto-switches between them)
- Start/Pause and Reset controls
- 🔥 Streak counter for completed focus sessions
- Cross-platform sound alert (Windows, macOS, Linux)
- Clean dark-mode UI

## Requirements

- Python 3.x
- No external libraries — uses only the standard library (`tkinter`, `os`, `platform`)

## How to Run

```bash
python pomodoro.py
```

## How It Works

- Click **START** to begin a 25-minute focus session.
- When time runs out, a sound plays and the app automatically switches to a 5-minute break.
- Your streak count increases by 1 each time a focus session completes.
- **RESET** stops the timer and returns to a fresh 25:00 focus session.

## Possible Future Improvements

- Customizable work/break durations
- Long break after every 4 sessions
- Session history/log
- Notification popup in addition to sound

## License

MIT — feel free to use or modify.