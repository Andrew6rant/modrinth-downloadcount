import requests

def get_downloads(id):
    r = requests.get('https://api.modrinth.com/api/v1/user/'+id+'/mods')
    a = r.json()
    for x in a:
        b = requests.get('https://api.modrinth.com/api/v1/mod/'+x)
        print(b.json())
    else:
        print("done")

if __name__ == '__main__':
    get_downloads('IV9h2DkJ')
