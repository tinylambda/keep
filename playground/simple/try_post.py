import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:8000/home/"
    payload = {
        "offer": "98046",
        "first_name": "BillTT",
        "last_name": "SmithTT",
        "email": "testingqiao@refersion.com",
        "password": "7En~8Mk!6Ze$0Yb",
        "send_welcome": "FALSE",
    }
    headers = {
        "Accept": "application/json",
        "Refersion-Public-Key": "pub_a47c93e5256d4b80ca98",
        "Refersion-Secret-Key": "sec_73bda89d061c2d47e4e8",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
