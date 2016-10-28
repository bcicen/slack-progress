# slack-progress

[![PyPI version](https://badge.fury.io/py/slack-progress.svg)](https://badge.fury.io/py/slack-progress)

A realtime progress bar for Slack

![screencap][screencap]

## Installing

```bash
pip install slack-progress
```

## Usage

Create a SlackProgress object with your Slack token and channel name:
```python
from slack_progress import SlackProgress
sp = SlackProgress('SLACK_TOKEN', 'CHANNEL_NAME')
```

Now you can simply wrap any iterator:
```python
for i in sp.iter(range(500)):
    time.sleep(.2)
```

The bar position can also be set manually:

```python
pbar = sp.new()
pbar.update(10)
time.sleep(1)
pbar.update(50)
time.sleep(1)
pbar.update(100)
time.sleep(1)
```

[screencap]: http://i.imgur.com/103z4Io.gif "slack-progress"
