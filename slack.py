import config

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=config.usertoken)

@app.event("message")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hello, User! *OIT HD Coverage Bot* would like to know certain details before requesting coverage.\n\n *Please Select Shift Position*"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "radio_buttons",
					"options": [
						{
							"text": {
								"type": "plain_text",
								"text": "Level 1 HD"
							},
							"value": "value-0"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "Level 2 HD"
							},
							"value": "value-1"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "Level 2 Apps/Email"
							},
							"value": "value-2"
						}
					],
					"action_id": "actionId-0"
				}
			]
		},
		{
			"type": "input",
			"element": {
				"type": "datepicker",
				"initial_date": "2022-01-01",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date"
				},
				"action_id": "datepicker-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Date and Time of Shift"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "timepicker",
					"placeholder": {
						"type": "plain_text",
						"text": "Input Shift Start Time"
					},
					"action_id": "actionId-0"
				},
				{
					"type": "timepicker",
					"placeholder": {
						"type": "plain_text",
						"text": "Input Shift End Time"
					},
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Request Coverage"
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		}
	],
        text=f"<@{message['user']}>, summoned the OIT Coverage Bot"
    )

@app.action("actionId-2")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(
        blocks = [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "*Coverage has been requested*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "```Hello, \n\n I am unable to work the following shift(s): \n\n  • Ex: Sunday 1/16, From 1630-0030 \n\n Please let me and/or the scheduling team (hd_scheduling@oit.rutgers.edu) know that if you can cover the shift fully or partially .\n\n Thank you for understanding, \n \\\\TODO: USER \n \\\\TODO: USER TITLE \n OIT Help Desk```"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "The aforementioned email has been sent to the following NetIDs:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Ex: aaa000, bbb111, ccc222"
			}
		}
	], text=f"Coverage has been requested"
	)


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, config.apptoken).start()