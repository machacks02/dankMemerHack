# Dank Memer Hack
This hacks the dank memes bot on discord! check out my [YouTube channel](https://www.youtube.com/channel/UCUfiGXxeA1mXTa8VlsUnHow), Officially Mad

> Here is how to go about using the code yourself **_(est time for completion 5-10 mins)_**:
> **MAKE SURE PYTHON 3.8 AND ABOVE IS ALREADY INSTALLED ON YOUR COMPUTER BEFORE DOING THIS!**

## Step 1:
- Download all the files provided and keep them in the same folder

## Step 2:
- Go to https://discord.com/developers/applications
- Create an application

> On the left hand side of the screen, it should say 'bot', under OAuth2.
> Click on this, and then click 'Add bot'. Scroll down to bot permissions and tick the permission that says 'Admin'.
> Once this is done, go back to the left side of your screen and click on 'OAuth2'
> Within the 'scopes' section, tick the 'bot' checkbox.
> Now a new set of checkboxes should appear, and in here click the 'Administrator' checkbox.
> Right above this set of checkboxes you will see a link something similar to: https://discord.com/api/oauth2/authorize?client_id=824227361926414338&permissions=8&scope=bot
> Go to this link and add the bot to a server of your choice.

## Step 3:

- Go to your terminal/command line and type in `python3 -m pip install pynput`. After that, do `python3 -m pip install discord`.

## Step 4:

- Go back to the discord developer website you were at earlier and go to 'General Information', right above 'OAuth2'. Here see where it says your 'Client secret', click reveal and then copy it.

- Go to the file called `config.json`, open it, and where it says `"PUT YOUR APPLICATIONS TOKEN INSIDE THE QUOTATION MARKS"`, replace it with the text you copied earlier, but make sure to surround it with quotation marks like these: `""`

**And now your done!**

> Simply run the main.py file, and then after run the pythonKeyboardController.py file. Be sure to do it in this order, because the second file controls your keyboard and makes > it difficult to run the main.py file. Now you can leave your computer running with discord open and it will continuously send the messages!
