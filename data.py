# THIS MODULE STORES DATA.

data = {
  "name" : "",
  "job" : 0,
  "flowers_smelled" : False
}


def get_data(key):
  return data.get(key)


def set_data(key, value):
  data[key] = value