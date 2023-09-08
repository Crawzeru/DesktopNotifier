from plyer import notification
title=input("Write your title: ")
message=input("Write your message: ")
app_icon=input("Write your app icon path(It's not necassary): ")

notification.notify(
    title=title,
    message=message,
    app_icon=app_icon,
    timeout=5,

)
print("Here is your notification!")