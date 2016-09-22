# slack-progress

A realtime progress bar for Slack

![screencap][screencap]

## Installing

```bash
pip install slack-progress
```

## Usage

### Manual
The % completed can also be set manually:

```python
from slack_progress import SlackProgress

sp = SlackProgress('SLACK_TOKEN', 'CHANNEL_NAME')
pbar = sp.new()
for i in range(1,101):
    pbar.update(i)
```

[screencap]: http://i.imgur.com/103z4Io.gif "slack-progress"
