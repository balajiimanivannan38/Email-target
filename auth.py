from jose import jwt
from datetime import datetime, timedelta

SECRET = "secret"
def create_token(user_id):
    return jwt.encode({"user_id": user_id, "exp": datetime.utcnow()+timedelta(hours=5)}, SECRET, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])["user_id"]
    except:
        return None