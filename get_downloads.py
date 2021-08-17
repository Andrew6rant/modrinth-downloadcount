import requests

def get_downloads(user_id):
    r = requests.get('https://api.modrinth.com/api/v1/user/'+user_id+'/mods')
    number_of_mods = r.json()
    total_downloads = 0
    for mod_id in number_of_mods:
        b = requests.get('https://api.modrinth.com/api/v1/mod/'+mod_id)
        mod_json = b.json()
        total_downloads += mod_json["downloads"]
    print(total_downloads)

if __name__ == '__main__':
    get_downloads('IV9h2DkJ')
