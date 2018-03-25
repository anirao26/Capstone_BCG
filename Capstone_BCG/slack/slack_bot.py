from slackclient import SlackClient
import time


class slackCommunication(object):
	def __init__(self):
		self.slack_client = SlackClient('')
		self.appName = "nlpbot_test"

	def slackConnect(self):	
		return self.slack_client.rtm_connect()

	def slackReadRTM(self):
		return self.slack_client.rtm_read()

	def parseSlackInput(self, input, botID):
		botATID = botID
		if input and len(input) > 0:
			input = input[0]
			if 'text' in input and botATID in input['text']:
				user = input['user']
				message = input['text']
				channel = input['channel']
				return [str(user), str(message), str(channel)]
			else:
				return [None, None, None]

	def getBotID(self, botusername):
		api_call = self.slack_client.api_call('users.list')
		users = api_call['members']
		for user in users:
			if botusername in user.get('name') and not user.get('deleted'):
				return user.get('id')

	def writeToSlack(self, channel, message):
		self.slack_client.api_call('chat.postMessage', channel = channel, text = "Chatbot")


class mainFunc(slackCommunication):
	def __init__(self):
		super().__init__()

	def decideWhethertotakeAction(self, input):
		if input:
			user, message, channel = input
			return self.writeToSlack(channel, message)
	
	def run(self):
		self.slackConnect()
		BOTID = self.getBotID(self.appName)
		while True:
			self.decideWhethertotakeAction(self.parseSlackInput(self.slackReadRTM(), BOTID))
			time.sleep(1)


if __name__ == '__main__':
	instance = mainFunc()
	instance.run()
