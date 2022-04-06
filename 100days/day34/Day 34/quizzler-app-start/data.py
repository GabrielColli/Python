import requests

parameters = {
    "amount" : 15,
    "type" : "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)



# ['results'][0]['question']   use this to call specific questions
data = response.json()
question_data = data['results']  # this is a list type containing dictionaries



