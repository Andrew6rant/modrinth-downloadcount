import requests

def get_downloads(id):
    r = requests.get('https://api.modrinth.com/api/v1/user/'+id+'/mods')
    number_of_mods = r.json()
    total_downloads = 0
    for mod_id in number_of_mods:
        b = requests.get('https://api.modrinth.com/api/v1/mod/'+mod_id)
        e = b.json()
        print(int(e["downloads"]))
    else:
        print("done")

if __name__ == '__main__':
    get_downloads('IV9h2DkJ')
