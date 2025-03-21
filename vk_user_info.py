import requests

def get_vk_user_info(user_id, access_token):

    url = "https://api.vk.com/method/users.get"
    params = {
        "user_ids": user_id,
        "access_token": access_token,
        "v": "5.131",
        "fields": "bdate",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "response" in data and data["response"]:
            user_info = data["response"][0]
            return {
                "first_name": user_info.get("first_name", "Not specified"),
                "last_name": user_info.get("last_name", "Not specified"),
                "bdate": user_info.get("bdate", "Not specified"),
            }
        else:
            return {"error": "The user was not found or the profile is hidden."}

    except requests.exceptions.RequestException as e:
        return {"error": f"request execution error: {e}"}
