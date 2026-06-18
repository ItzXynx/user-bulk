import sys
import urllib.request
import json

def get_user(token, uid):
    req = urllib.request.Request(
        f"https://discord.com/api/v9/users/{uid}",
        headers={"Authorization": token}
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

if __name__ == "__main__":
    token = sys.argv[1]
    ids = sys.argv[2:]
    for uid in ids:
        try:
            u = get_user(token, uid)
            print(f"{uid}: {u.get('username')} flags={u.get('public_flags', 0)}")
        except:
            print(f"{uid}: not found")
# updated
