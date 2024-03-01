#!/usr/bin/env python3

import json
import uuid
import requests

MATRIX_HOST = "https://matrix-client.matrix.org"
MATRIX_TOKEN = ""
MATRIX_ROOM = ""

def create_messages():
    message = (
        f"Hello World!"
    )

    message_html = (
        f"<b>Hello World!</b>"
    )
    return message, message_html

def send(message, message_html):
    # Data send to Matrix
    matrix_data_dict = {
        "msgtype": "m.text",
        "body": message,
        "format": "org.matrix.custom.html",
        "formatted_body": message_html,
    }
    matrix_data = json.dumps(matrix_data_dict).encode("utf-8")

    # Authorization headers
    matrix_headers = {"Authorization": "Bearer " + MATRIX_TOKEN, "Content-Type": "application/json", "Content-Length": str(len(matrix_data))}

    # Request
    request = requests.put(url=f"{MATRIX_HOST}/_matrix/client/r0/rooms/{MATRIX_ROOM}/send/m.room.message/{str(uuid.uuid4())}", data=matrix_data, headers=matrix_headers)

    if request.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {request.status_code}")

# Run
try:
    message, message_html = create_messages()
    send(message, message_html)
except Exception as e:
    print(f"An error occurred: {e}")