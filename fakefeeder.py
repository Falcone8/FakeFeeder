from pyrogram import *

#RICORDA DI AGGIORNARE LE IMPOSTAZIONE SULLA PRIVACY


api_id = 
api_hash = ""
phnumber = ""



processchat = "@"  #NOT SELF

app = Client("mysession",api_id, api_hash,phone_number= phnumber)
@app.on_message(filters.command("setfeedname", "/"))
def setfeedname(Client,message):
    if message.from_user.id == app.get_me().id:
        try:    
            app.update_profile(first_name=message.text.split("/setfeedname")[1])
            app.edit_message_text(message.chat.id, message.message_id,"✅ **FeederName impostato a ** [ __{}__ ] ✅".format(app.get_me().first_name),parse_mode="markdown")
        except Exception as error: app.edit_message_text(message.chat.id, message.message_id,"✖ ERRORE ✖ \n{Errore}".format(Errore = error))


@app.on_message(filters.command("createfeed", "/"))
def setfeedname(Client,message):
    if message.from_user.id == app.get_me().id:    
        try:
            app.send_message(processchat, message.text.split("/createfeed")[1])
            app.get_history(processchat, 1)[0].forward(message.chat.id)
            app.edit_message_text(message.chat.id, message.message_id,"✅ **FEEDBACK CREATO** ✅", parse_mode="markdown")
        except Exception as error: app.edit_message_text(message.chat.id, message.message_id,"✖ ERRORE ✖ \n{Errore}".format(Errore = error))


@app.on_message(filters.command("info","/"))
def info(Client,message):
    app.edit_message_text(message.chat.id, message.message_id, "**+FeederBot Plus \nVersione Bot: 1.1**", parse_mode="markdown")

app.run()


