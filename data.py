# THIS MODULE STORES DATA.

data = {
  "name" : "",
  "job" : 0,
  "flowers_smelled" : False
}


def getter(key):
  return data.get(key)


def setter(key, value):
  data[key] = value