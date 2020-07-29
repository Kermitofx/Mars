#!/usr/bin/python3

from telegram import InlineKeyboardButton

not_interface = False
default_time = 0.0
roots = [560950095]
limit = 2000000000
seconds_limits_album = 40000
max_songs = 400
telegram_file_api_limit = 1500000000
telegram_audio_api_limit = 50000000
db_file = "dwsongs.db"
loc_dir = "Songs/"
ini_file = "settings.ini"
photo = "https://telegra.ph/file/8d8723bde601369520302.jpg"
bot_name = "MarsRobot"
api_chart = "https://api.deezer.com/chart"
api_artist = "https://api.deezer.com/artist/%s"
api_type1 = "https://api.deezer.com/search/{}/?q={}"
api_type2 = "https://api.deezer.com/search/?q={}:\"{}\""
song_default_image = "https://e-cdns-images.dzcdn.net/images/cover/1000x1000-000000-80-0-0.jpg"
services_supported = ["spotify", "deezer"]
comandss = ["start", "settings", "info", "shazam", "help"]
settingss = ["quality", "tongue"]
qualities = ["FLAC", "MP3_320", "MP3_256", "MP3_128"]
send_image_track_query = "🎧 Track: %s \n👤 Artist: %s \n💽 Album: %s \n📅 Date: %s \n🤖 Robot: @MarsRobot"
send_image_album_query = "💽 Album: %s \n👤 Artist: %s \n📅 Date: %s \n🎧 Tracks amount: %d \n🤖 Robot: @MarsRobot"
send_image_artist_query = "👤 Artist: %s \n💽 Album numbers: %d \n👥 Fans on Deezer: %d \n🤖 Robot: @MarsRobot"
tags_query = "💽 Album: %s\n📅 Date: %s\n📀 Label: %s\n🎵 Genre: %s"
info_msg = "🌍 Version: %s\n💬 Name: @%s\n✒️ Creator: @%s\n💵 Donation: %s\n📣 Forum: %s\n👥 Users: %d\n📊 Total downloads: %d"
send_image_playlist_query = "📅 Creation: %s \n👤 User: %s \n🎧 Tracks amount: %d \n🤖 Robot: @MarsRobot"
insert_query = "INSERT INTO DWSONGS (id, query, quality) values ('%s', '%s', '%s')"
where_query = "SELECT query FROM DWSONGS WHERE id = '{}' and quality = '{}'"
user_exist = "SELECT chat_id FROM CHAT_ID where chat_id = '%d'"
share_message = "tg://msg?text=Start @%s For Download All The Songs Which You Want ❤" % bot_name
start_message = "Welcome To @%s \nPress '/' To Get Commands List" % bot_name
not_supported_links = "Sorry 😥 The Bot Doesn't Support This Link %s 🙄"
rate_link = "https://t.me/HelpBdarija/21"
end_message = "FINISHED ❤ Rate Me Here %s" % rate_link

help_message = (
	"/start: Start The Bot" +
	"\n\n/settings: Manage Settings" +
	"\n\n/shazam: Identify A Song By A Voice Or Audio Message (You Can Do Without Calling This Command, Just Send The Media)" +
	"\n\n/help: Show This Message" +
	"\n\n" +
	"Just Send A Spotify Or Deezer Link To Download, Or Type What You Are Looking For"
)

end_keyboard = [
	[
		InlineKeyboardButton(
			"🔥 SHARE 🔥",
			url = share_message
		)
	]
]

qualities_keyboard = [
	[
		InlineKeyboardButton(
			qualities[a],
			callback_data = qualities[a]
		),
		InlineKeyboardButton(
			qualities[a + 1],
			callback_data = qualities[a + 1]
		)
	] for a in range(
		0, len(qualities), 2
	)
]

first_time_keyboard = [
	[
		InlineKeyboardButton(
			"✅ START ✅",
			url = "t.me/%s?start" % bot_name
		)
	]
]

queries = {
	"top": {
		"query": "%s/top?limit=30",
		"text": "TOP 30 🔝"
	},

	"albums": {
		"query": "%s/albums",
		"text": "ALBUMS 💽"
	},

	"radio": {
		"query": "%s/radio",
		"text": "RADIO 📻"
	},

	"related": {
		"query": "%s/related",
		"text": "RELATED 🗣"
	},

	"download": {
		"text": "Download ⬇️"
	},

	"info": {
		"text": "Info ❕"
	},

	"back": {
		"text": "BACK 🔙"
	},

	"s_art": {
		"query": "Artist: %s",
		"text": "Search By Artist 👤"
	},

	"s_alb": {
		"query": "Album: %s",
		"text": "Search By Album 💽"
	},

	"s_pla": {
		"query": "Playlist: %s",
		"text": "Search Playlist 📂"
	},

	"s_lbl": {
		"query": "Label: %s",
		"text": "Search label 📀"
	},

	"s_trk": {
		"query": "Track: %s",
		"text": "Search track 🎧"
	},

	"s_": {
		"query": "%s",
		"text": "Global Search 📊"
	}
}
