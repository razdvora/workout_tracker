APP_ID ="847efce3"
API_KEY ="6111086bd4eae6ee4332562b34b42f28"
import requests
import requests
from _datetime import datetime
GENDER = "male"
WEIGHT_KG = "78"
HEIGHT_CM = "171"
AGE = "25"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result["exercises"][0]["name"])
#nf_calories

sheet_endpoint = 'https://api.sheety.co/8939d800e5f4a497d289e425dd6bb49d/myWorkouts/workouts';
#   let body = {
#     workout: {
#       ...
#     }
#   }
#   fetch(url, {
#     method: 'POST',
#     body: JSON.stringify(body)
#   })
#   .then((response) => response.json())
#   .then(json => {
#     // Do something with object
#     console.log(json.workout);
#   });

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

print(sheet_response.text)
