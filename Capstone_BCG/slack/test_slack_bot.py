import pytest

input = [{'type': 'message', 'channel': 'D9F72FLAU', 'user': 'U9E0RG84R', 'text': 'dasda', 'ts': '1519801024.000103', 'source_team': 'T9DT55SHE', 'team': 'T9DT55SHE'}]


@pytest.fixture
def slackCommunication():
	from slack_bot import slackCommunication
	return slackCommunication()


@pytest.fixture
def mainFunc():
	from slack_bot import mainFunc
	return mainFunc()

@pytest.mark.skip(reason = "Fully tested")
def test_slackConnect(slackCommunication):
	assert slackCommunication.slackConnect() == True

def test_parseSlackInput(slackCommunication):
	assert slackCommunication.parseSlackInput(input, "U9E0RG84R") == ["U9E0RG84R", "dasda", "D9F72FLAU"]

def test_getBotID(slackCommunication):
	assert slackCommunication.getBotID("nlpbot_test") == 'U9E0RG84R'

def test_writeToSlack(slackCommunication):
	assert slackCommunication.writeToSlack("D9F72FLAU", "Testing writing to slack.")['ok'] == True

@pytest.mark.skip(reason = "Not fully implemented")
def test_slackReadRTM(slackCommunication):
	slackCommunication.slackConnect()
	print(slackCommunication.slackReadRTM)

def test_decideWhethertotakeAction_message(mainFunc):
	input = ["U9E0RG84R", "dasda", "D9F72FLAU"]
	assert mainFunc.decideWhethertotakeAction(input)

def test_decideWhethertotakeAction_None(mainFunc):
	input = [None, None, None]
	assert mainFunc.decideWhethertotakeAction(input)
