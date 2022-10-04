# import requests


# headers = {"apikey": "f6b13440-bd22-11eb-9c9a-534758a4026f"}

# # params = (("codes", "10005,51503"),)
# params = (("codes", "44600"), ("country", "NP"))


# response = requests.get(
#     "https://app.zipcodebase.com/api/v1/search", headers=headers, params=params
# )
# print(response.text)

import requests

headers = {"apikey": "f6b13440-bd22-11eb-9c9a-534758a4026f"}

params = (("country", "np"),)

response = requests.get(
    "https://app.zipcodebase.com/api/v1/country/province",
    headers=headers,
    params=params,
)
print(response.text)
