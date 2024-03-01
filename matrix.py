#!/usr/bin/env python3

import json
import uuid
import requests

MATRIX_HOST = "https://matrix-client.matrix.org"
MATRIX_TOKEN = ""
MATRIX_ROOM = ""

def generate_messages():
    message = (
        f"Hello World!"
    )

    message_html = (
        f"<b>Hello World!</b>"
    )
    return message, message_html

def send_matrix_message(message, message_html):
    matrix_host = MATRIX_HOST
    matrix_token = MATRIX_TOKEN
    matrix_room = MATRIX_ROOM

    # Data send to Matrix
    matrix_data_dict = {
        "msgtype": "m.text",
        "body": message,
        "format": "org.matrix.custom.html",
        "formatted_body": message_html,
    }
    matrix_data = json.dumps(matrix_data_dict)
    matrix_data = matrix_data.encode("utf-8")

    # Random transaction ID
    txn_id = str(uuid.uuid4())

    # Authorization headers
    matrix_headers = {"Authorization": "Bearer " + matrix_token, "Content-Type": "application/json", "Content-Length": str(len(matrix_data))}

    # Request
    req = requests.put(url=f"{matrix_host}/_matrix/client/r0/rooms/{matrix_room}/send/m.room.message/{txn_id}", data=matrix_data, headers=matrix_headers)

    if req.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {req.status_code}")

# Run
try:
    message, message_html = generate_messages()
    send_matrix_message(message, message_html)
except Exception as e:
    print(f"An error occurred: {e}")