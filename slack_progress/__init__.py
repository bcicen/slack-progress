from slacker import Slacker

class SlackProgress(object):
    def __init__(self, token, channel, suffix='%'):
        self.suffix = suffix
        self.channel = channel
        self.slack = Slacker(token)

    def new(self, total=100):
        """
        Instantiate and return a new ProgressBar object
        params:
         - total(int): total number of items
        """
        res = self.slack.chat.post_message(self.channel, self._makebar(0))
        bar = ProgressBar(self, total)
        bar.msg_ts = res.body['ts']
        bar.channel_id = res.body['channel']
        return bar

    def iter(self, iterable):
        """
        Wraps an iterable object, automatically creating
        and updating a progress bar
        """
        bar = self.new(total=len(iterable)-1)
        for idx, item in enumerate(iterable):
            yield(item)
            bar.done = idx

    def _update(self, chan, msg_ts, pos):
        self.slack.chat.update(chan, msg_ts, self._makebar(pos))

    def _makebar(self, pos):
        bar = (round(pos / 5) * chr(9608))
        return '{} {}{}'.format(bar, pos, self.suffix)

class ProgressBar(object):

    msg_ts = None
    channel_id = None

    def __init__(self, sp, total):
        self._sp = sp
        self._pos = 0
        self._done = 0
        self.total = total

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, val):
        self._done = val
        self.pos = round((val/self.total) * 100)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, val):
        if val != self._pos:
            self._sp._update(self.channel_id, self.msg_ts, val)
            self._pos = val
