import requests
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)
print("조회결과 상태코드 : " + str(response.status_code))

user = response.json()
#print(user)
print ("사용자 아이디 : " + str(user["id"]))
print ("사용자 이  름 : " + user["name"])
print ("사용자 이메일 : " + user["email"])

