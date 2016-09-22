from slacker import Slacker

class SlackProgress(object):
    def __init__(self, token, channel, suffix='%'):
        self.suffix = suffix
        self.channel = channel
        self.slack = Slacker(token)

    def new(self):
        res = self.slack.chat.post_message(self.channel, self._makebar(0))
        bar = ProgressBar(self)
        bar.msg_ts = res.body['ts']
        bar.channel_id = res.body['channel']
        return bar

    def _update(self, chan, msg_ts, pos):
        self.slack.chat.update(chan, msg_ts, self._makebar(pos))

    def _makebar(self, pos): 
        bar = (round(pos / 5) * chr(9608))
        return '{} {}{}'.format(bar, pos, self.suffix)

class ProgressBar(object):
    msg_ts = None
    channel_id = None
    def __init__(self, sp):
        self._sp = sp

    def update(self, pos):
        self._sp._update(self.channel_id, self.msg_ts, pos)
