"""
Script leverages the WebexTeamssdk
Sends a webex teams message 
Will create room if not created
Deletes a supplied webex room
"""
import sys
sys.path.append('./')
# import logging
from webexteamssdk import WebexTeamsAPI
from .credenitials import WEBEX_TEAMS_ACCESS_TOKEN, WEBEX_ROOM_NAME, WEBEX_EMAIL_ADDRESS


# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

api = WebexTeamsAPI(WEBEX_TEAMS_ACCESS_TOKEN)


def send_webex_message(message, webex_room=WEBEX_ROOM_NAME,
                       webex_email=WEBEX_EMAIL_ADDRESS, token=WEBEX_TEAMS_ACCESS_TOKEN):
    # Send a message to a supplied webex room
    # Creates room if not listed
    rooms = api.rooms.list()
    aci_room = [room.id for room in rooms if room.title == webex_room]
    if aci_room:
        api.messages.create(aci_room[0], markdown=message)
        # api.messages.create(aci_room[0], text='\n', attachments=cards)
    else:
        webex_room = api.rooms.create(webex_room)
        api.memberships.create(webex_room.id, personEmail=webex_email)
        api.messages.create(webex_room.id, text=message)

def delete_webex_room(token=WEBEX_TEAMS_ACCESS_TOKEN, webex_room=WEBEX_ROOM_NAME):
    # Deletes supplied webex room
    rooms = api.rooms.list()
    aci_room = [room.id for room in rooms if room.title == webex_room]
    if aci_room:
        api.rooms.delete(aci_room[0])
        print(f"Sucessfully deleted {webex_room}")
    else:
        print(f"Webex room {webex_room}: Not Found")

if __name__ == "__main__":
    message = input("Enter: ")
    send_webex_message(message)
