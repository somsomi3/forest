# from django.shortcuts import render

# import requests
# import json



# # Create your views here.


# # API 키와 엔드포인트 설정
# API_KEY = ''  # 발급받은 API 키
# ENDPOINT = ''

# def get_forest_fire_data():
#     # API 요청 URL
#     url = f"http://apis.data.go.kr/1400377/forestPoint/forestPointListGeongugSearch?serviceKey=인증키(URL Encode)&numOfRows=10&pageNo=1&excludeForecast=0&_type=xml
# "

#     # GET 요청 보내기
#     response = requests.get(url)

#     # 요청이 성공했는지 확인
#     if response.status_code == 200:
#         # JSON 데이터 파싱
#         data = response.json()
#         return data
#     else:
#         print(f"Failed to fetch data: {response.status_code}")
#         return None
    


# def forest_fire_view(request):
#     # API 데이터 가져오기
#     data = get_forest_fire_data()
    
#     if data:
#         # 필요한 데이터만 필터링할 수 있습니다.
#         forest_fire_info = data.get('data', [])
#     else:
#         forest_fire_info = []

#     # 템플릿에 데이터 전달
#     context = {
#         'forest_fire_info': forest_fire_info,
#     }

#     return render(request, 'forest_fire/forest_fire_info.html', context)



from django.shortcuts import render
import requests

# API 키와 엔드포인트 설정
API_KEY = '3NGyz4Bzn5iJJf9ARy736G2xqYijQqHatiL7gL3ERUUigFxXJx%2FjZ%2BypJXIMZyrQlH2eyl93ASjq3pfIfx1XGw%3D%3D'
ENDPOINT = 'http://apis.data.go.kr/1400377/forestPoint/forestPointListGeongugSearch'

def get_forest_fire_data():
    # API 요청 URL
    # url = f"{ENDPOINT}?serviceKey={API_KEY}&numOfRows=10&pageNo=1&excludeForecast=0&_type=json"
    url = f"{ENDPOINT}?serviceKey={API_KEY}&numOfRows=10&pageNo=1&excludeForecast=0&_type=xml"
    
    # GET 요청 보내기
    response = requests.get(url)

    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # JSON 데이터 파싱
        data = response.json()
        return data
        # print(data)
    
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def forest_fire_view(request):
    # API 데이터 가져오기
    data = get_forest_fire_data()
    
    if data:
        forest_fire_info = data.get('response', {}).get('body', {}).get('items', [])
    else:
        forest_fire_info = []

    # 템플릿에 데이터 전달
    context = {
        'forest_fire_info': forest_fire_info,
    }

    return render(request, 'fires/forest_fire_info.html', context)

