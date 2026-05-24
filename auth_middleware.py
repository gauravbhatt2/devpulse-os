# Authentication Middleware — JWT refresh flow
# SCRUM-7: review implementation before merging

import jwt

def validate_token(token: str) -> dict:
    # SCRUM-7: handle expired token edge case
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthError("Token expired — refresh required")
#SCRUM-7 handle expired token edge case
