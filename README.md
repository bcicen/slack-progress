# slack-progress

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
    print(i)
    sleep(.2)
```

The bar position can also be set manually:

```python
pbar = sp.new()
for i in range(1,101):
    pbar.update(i)
```

[screencap]: http://i.imgur.com/103z4Io.gif "slack-progress"
