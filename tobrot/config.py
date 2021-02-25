from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1683970873:AAGyYwQ1eBeMGHsQd2_X2TVLCHGRU26VutE"
    APP_ID = 1815432
    API_HASH = "168849a53b72ceed26914aa5e8e00ab7"
    OWNER_ID = 885190545
    AUTH_CHANNEL = [-1001409146277]
    DESTINATION_FOLDER = "Uploaders Team Drive [Backup1]" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    INDEX_LINK = "https://uploaders.mirrortgbot.workers.dev/0:"
    RCLONE_CONFIG = """
[Bot]
type = drive
client_id = 264229571506-ng71pa27j76eep5a7rjqf8hkp71cc8bg.apps.googleusercontent.com
client_secret = 9IDr8Yx6hqTf9kAn6FR_b_8S
scope = drive
root_folder_id = 
token = {"access_token":"ya29.A0AfH6SMDbC1ryHTbYVYk4ujuC7jjQox8E1D9U4OXMYC_aIVf4sZ8ciQSWtT7qY9vel4T0ruJ1aK0Wv5MphfiWKxjgYjeNo5ybRqzBohUQmEacldl5DzDtV2s2n6HmLNK-6HnYlaawCLmQxQ2L1_EO2nby11HI","token_type":"Bearer","refresh_token":"1//0gmiD_MSuCCEOCgYIARAAGBASNwF-L9IrAkw803bUoGzB_RGuaCdQdVlnvhqbYcyE-aJgJUTwQu5rJIYg8WO_OF8gjuDbLwYF27Y","expiry":"2021-02-21T11:51:54.2390726+05:30"}
team_drive = 0AJfqo9HM61itUk9PVA
"""
