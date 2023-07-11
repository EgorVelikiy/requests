import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        name = file_path.split('\\')[-1]
        params = {
            "path": name
        }
        headers = {
            "Authorization" : token
        }
        response = requests.get(url, headers=headers, params=params)
        file_path = response.json().get('href', '')
        with open(path_to_file, 'rb') as file:
            response2 = requests.put(file_path, files={"file": file})


if __name__ == '__main__':
    path_to_file = input("Введите путь до файла: ")
    token = input("Введите свой токен: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)