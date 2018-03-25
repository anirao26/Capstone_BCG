import sys
from slacker import Slacker
slack = Slacker('xoxb-321240529424-a3ChiZdGsz10U0zvADdscaz6')

#General message
message = "Hello there!"
slack.chat.post_message('#general', message)
