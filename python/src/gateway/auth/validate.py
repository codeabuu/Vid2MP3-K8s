import os
import requests

def token(request):
    if "Authorization" not in request.headers:
        return None, ("Missing creds", 401)
    
    token = request.headers["Authorization"]
    if not token:
        return None, ("Missing creds", 401)
    
    # Handle the case where the token doesn't have the "Bearer" prefix
    if " " in token:
        token = token.split(" ")[1]  # Extract the actual token part

    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS', '127.0.0.1:5000')}/validate",
        headers={"Authorization": token}
    )
    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)