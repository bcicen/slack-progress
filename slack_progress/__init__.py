from slacker import Slacker

class SlackProgress(object):
    def __init__(self, token, channel, start_pos=0, suffix='%'):
        self.suffix = suffix
        self.channel = channel
        self.slack = Slacker(token)

        res = self.slack.chat.post_message(
                self.channel,
                self.make_bar(start_pos)
              )
        self.msg_ts = res.body['ts']
        self.channel_id = res.body['channel']

    def update_bar(self, pos):
        self.slack.chat.update(self.channel_id,
                               self.msg_ts,
                               self.make_bar(pos))

    def make_bar(self, pos): 
        bar = (round(pos / 5) * chr(9608))
        return '{} {}{}'.format(bar, pos, self.suffix)
