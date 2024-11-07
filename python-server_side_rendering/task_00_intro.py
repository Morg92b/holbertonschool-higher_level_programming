#!/usr/bin/python3

def generate_invitations(template, attendees):
	"""
		Generate invitations from a template with attendees

		Args:
			- template : Template to use
			- attendees: List of attendees (dictionary)
	"""
	if not isinstance(template, str):
		print("The argument 'template' must be a string.")
		return
	if len(template) == 0:
		print("Template is empty, no output files generated.")
		return
	if not isinstance(attendees, list):
		print("The argument 'attendees' must be a list of dictionaries.")
	else:
		if len(attendees) == 0:
			print("No data provided, no output files generated.")
		elif not isinstance(attendees[0], dict):
			print("The argument 'attendees' must be a list of dictionaries.")
			return
	
	try:
		for i in range(0, len(attendees)):
			invitation = template
			keys = ["name", "event_title", "event_date", "event_location"]
			for k in keys:
				placeholder = "{" + k + "}"
				replaced_by = attendees[i].get(k)
				if replaced_by == None:
					replaced_by = "N/A"
				invitation = invitation.replace(placeholder, replaced_by)
				print(invitation)
			output = "output_{}.txt".format(i + 1)
			with open(output, 'w') as file:
				file.write(invitation)
	except Exception as e:
		print("{}".format(e))
		

