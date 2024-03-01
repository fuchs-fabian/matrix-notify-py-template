# matrix-notify-py

> Simple Python script for sending html messages to a matrix room

![Example](/images/example.png)

## Requirements

- a Home Server URL, e.g., for a standard Matrix user `https://matrix-client.matrix.org`

  > It's available in account settings.

- a Matrix (Bot) User and its user token

  > Create a special user! Don't use your main account!  
  > It's available in account settings.  
  > To get it in [Element](https://element.io/), log in as the created (Bot) User, tap on the profile picture on the top left, and go to `all settings → Help and Info`.
  > There should be a dropdown menu on the bottom (Access token).

- a Room ID

  > **You have to join** with this special (Bot) account to **this room** before!  
  > It's available in room settings.

> With this script it is also possible to send messages to an _encrypted_ room. However, the message sent by the script itself is not encrypted.

## Usage

The following must be adjusted in the code:

```
MATRIX_TOKEN = ""
MATRIX_ROOM = ""
```

If necessary also:

```
MATRIX_HOST = "https://matrix-client.matrix.org"
```

## Inspiration

- [Checkmk-Matrix-Notifications](https://github.com/fuchs-fabian/Checkmk-Matrix-Notifications)
