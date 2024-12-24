import json

FOLLOWING_PATH = 'following.json'
FOLLOWER_PATH = 'followers_1.json'

# JSON 파일 읽기
with open(FOLLOWER_PATH, 'r', encoding='utf-8') as file:
    followers_json_data = json.load(file)

# "value" 값만 모으는 배열 생성
followers_values = []
for item in followers_json_data:
    # "string_list_data"가 item에 있을 경우만 처리
    if "string_list_data" in item:
        for string_data in item["string_list_data"]:
            # "value"가 string_data에 있을 경우만 처리
            if "value" in string_data:
                followers_values.append(string_data["value"])

# # 결과 출력
print('팔로워 수: ', len(followers_values))

# JSON 파일 읽기
with open(FOLLOWING_PATH, 'r', encoding='utf-8') as file:
    following_json_data = json.load(file)

# "value" 값만 모으는 배열 생성
following_values = []
for item in following_json_data.get("relationships_following", []):
    if "string_list_data" in item:
        for string_data in item["string_list_data"]:
            if "value" in string_data:
                following_values.append(string_data["value"])

# # 결과 출력
print('팔로잉 수: ', len(following_values))
print('차이값: ', abs(len(followers_values) - len(following_values)))

# unique_values = list(set(followers_values).symmetric_difference(following_values))
unique_values = list(set(following_values)^set(followers_values))

# 결과 출력
print("중복되지 않은 값: ", unique_values)