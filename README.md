# slack-progress

A realtime progress bar for Slack

## Installing

```bash
pip install slack-progress
```

## Usage

```python
from time import sleep
from slack_progress import SlackProgress

progress_bar = SlackProgress('SLACK_TOKEN', 'CHANNEL_NAME')
for i in range(1,101):
    s.update_bar(a)
    sleep(.2)
```
