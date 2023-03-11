import requests
import time



def getcaptcha(apikey,sitekey,url):

    url = f"http://2captcha.com/in.php?key={apikey}&method=hcaptcha&sitekey={sitekey}&pageurl={url}"
    response = requests.get(url)
    if "|" not in response.text:
        print(f"could not create captcha task: {response.text}")
        exit()
    else:
        task_id = response.text.split("|")[1]
    for x in range(0,30):
        time.sleep(5)
        url = f"http://2captcha.com/res.php?key={apikey}&action=get&id={task_id}"
        response = requests.get(url)

        if response.text != "CAPCHA_NOT_READY":
            return response.text.replace("OK|", "")

    return None




if __name__ == '__main__':
    APIKEY=""
    SITEKEY =""
    URL =""

    result = getcaptcha(APIKEY,SITEKEY,URL)
