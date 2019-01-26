import requests
import time
import config
import random
from api_models import User, Message


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    delay = 2
    for tryn in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=timeout)
        except requests.exceptions.RequestException:
            if tryn == max_retries-1:
                 raise
        except Exception as e:
            print(e)
        else:
            return response
        time.sleep(delay)
        delay = backoff_factor * (2 ** tryn)
    return None


def get_friends(user_id, fields):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"

    domain = "https://api.vk.com/method"
    access_token = config.VK_CONFIG['access_token']
    user_id = user_id

    query_params = {
        'domain': domain,
        'access_token': access_token,
        'user_id': user_id,
        'fields': fields
    }

    query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields=" \
            "{fields}&v=5.53".format(**query_params)
    response = get(query).json()
    try:
        response = response['response']['items']
    except:
        return []
    for num, friend in enumerate(response):
        user = User(id= friend['id'], first_name=friend['first_name'], last_name=friend['last_name'],
                    online=friend['online'])
        try:
            user.bdate = friend['bdate']
        except:
            pass
        response[num] = user
    return response


def messages_get_history(user_id, offset=0, count=200):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    messages = []
    domain = "https://api.vk.com/method"
    access_token = config.VK_CONFIG['access_token']
    user_id = 313933490
    while count > 200:
        query_params = {
            'domain': domain,
            'access_token': access_token,
            'user_id': user_id,
            'offset': offset,
            'count': 200
        }
        query = "{domain}/messages.getHistory?access_token={access_token}&user_id={user_id}&offset={offset}&count=" \
                "{count}&v=5.53".format(**query_params)
        response = get(query)
        messages.extend(response.json()['response']['items'])
        time.sleep(0.5)
        count -= 200
        offset += 200

    query_params = {
        'domain': domain,
        'access_token': access_token,
        'user_id': user_id,
        'offset': offset,
        'count': count
    }
    query = "{domain}/messages.getHistory?access_token={access_token}&user_id={user_id}&offset={offset}&count={count}" \
            "&v=5.53".format(**query_params)
    response = get(query)
    messages.extend(response.json()['response']['items'])
    for num,message in enumerate(messages):
        message = Message(text = message['body'], date = message['date'])
        messages[num] = message
    return messages
