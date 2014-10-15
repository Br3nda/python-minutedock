import requests

class MinuteDockClient:
  rest_api_url = 'https://minutedock.com/api/v1'
  def __init__(self, key):
    self.key = key
  
  def __fetch__(self, thing, params={}):
    params['api_key'] = self.key
    response = requests.get('{url}/{thing}.json'.format(url=self.rest_api_url, thing=thing), params=params)
    return response.json()

  def __new__(self, thing, params={}):
    params['api_key'] = self.key
    response = requests.post('{url}/{thing}.json'.format(url=self.rest_api_url, thing=thing), params=params)
    print response.text
    return response.json()

  def __update__(self, thing, thing_id):
    params['api_key'] = self.key
    response = requests.put('{url}/{thing}/{thing_id}.json'.format(url=self.rest_api_url, thing=thing, thing_id=thing_id), params=params)
    return response.json()

  def accounts(self):
    return self.__fetch__('accounts')

  def users(self):
    return self.__fetch__('users')

  def entries(self):
    return self.__fetch__('entries')

  def log_entry(self, description, duration ):
    params = {'api_key': self.key, "entry['description']": description, "entry['duration']": duration}
    response = requests.post('{url}/entries/current/log.json'.format(url=self.rest_api_url), params=params)
    print response.text
    return response.json()

  def projects(self):
    return self.__fetch__('projects')

  def new_project(self, name):
    return self.__new__('projects', {"project['name']": name})
    

  def new_entry(self, **kwargs):
    pass

  def tasks(self):
    return self.__fetch__('tasks')

  def new_task(self, name):
    return self.__new__('tasks', {"task['name']": name})


