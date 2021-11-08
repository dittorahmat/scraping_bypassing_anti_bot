import requests
import pandas as pd
import time

url = "https://www.adorebeauty.co.nz/api/cat#94dbea9e-66de-44cc-9bd4-f8ccf145e3ab"

res=[]

def extract_page(x):
    try:
        time.sleep(3)

        querystring = {"identifier":"skin-care","p":f"{x}","locale":"en-NZ"}

        payload = ""
        headers = {
            # "cookie": "SSRT=OvWDYQADAA; SSOD=AFaHAAAAEADtBgAAAQAAADr1g2E69YNhAAA",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.adorebeauty.co.nz/skin-care.html",
            "X-Forwarded-Proto": "https",
            "Connection": "keep-alive",
            # "Cookie": "_pxhd=Usd9ECiLKZcpcq0/R51CJo3mybI1/KQ7nYZD/xXu5DdUzXkcwItRfZzgbER//bjs0jbfGxeDSI/ij-7EP6lJsg==:FSlx4crcm7RcwfEdZhSC37WBIz89H7dEbk8m3hblMUPYFFMLvw-m7xLiOjeoAW1vWMPxD-K7TEQG910a5s9gjI800NbkjnZKYLWB/1oXiF0=; _px3=f0105acfc226466ab1ea24e8fbc8d7fa474ae289c4a3a113badd5e42708092d4:irRHFG7KfR0N9rVCKWRbJf9+FoyYB+kSoW7elukqtJInwkSVPLQF0LkJ6CE5X26TiaMzwFI2vOwb1f7YLV+xLA==:1000:aodMtkGDWwORB/UN6Xuv5UV2alGzfeZq8JMO/CAW5tOs73da2ITo8CVVzRCVjiMhrTIR7IWW2eYirYdtootFFxswNXp2MJBw2P8fP7P1aISEfMX1cbBt/cCjXxX2yKcOpIETbLdsMoe9QQxjE+trm8ABFv2AVQFpjifraek4GgctxhbHYUyRE7w6KqaPHhYLnkHAcC/1bhxD49B74ovGMA==; pxcts=776564b0-3d7e-11ec-a899-af517fd2cedd; _pxvid=7598bbae-3d7e-11ec-a788-6e666b675543; __pxvid=7808bf45-3d7e-11ec-8ed4-0242ac120003; SSID=CAAA_h0AAAAAAAAj84NhWhLANCPzg2EBAAAAAAAAAAAAI_ODYQChQw; SSSC=2.G7026727176162513498.1|0.0; SSRT=KPODYQADAA; sectionio_geo=ID; locale=en-NZ; _ga=GA1.1.2059449416.1636037426; _gid=GA1.3.366055308.1636037426; _ALGOLIA=anonymous-a240d04b-a603-4eb9-9922-45b3c2c74b74; strumsession=ee95fe3b-3896-4e11-8908-57bf2f3a63e7; strumuser=042bcabb-5a3e-475f-9bfc-55f4be6fe1a1; utag_main=v_id:017ceb6e224100063cd0e5930d8b0004e002c00d009dc`n:1`s:0`t:1636039294972`:1636037435970%3Bexp-session`n:1%3Bexp-session`revpage:undefined%3Bexp-1636041095023`:1`:9%3Bexp-session`:ap-east-1%3Bexp-session; BW_Most_Recent_Category=43; _hjid=533bc7e9-45a3-4d54-a171-efd631383d8b; _hjFirstSeen=1; G_ENABLED_IDPS=google; forterToken=c5805acc4e5344b68d584f02b0826796_1636037456357__UDF43-mnf_9ck; _ga_BDXS1VKSP7=GS1.1.1636037456.1.0.1636037462.54; Most_Recent_Brand=; Most_Recent_Hair_Concern=; Most_Recent_Skin_Concerns=; Most_Recent_Eye_Concern=; Most_Recent_Skin_Type=; Most_Recent_Age=; Most_Recent_Choices=; Most_Recent_Key_Ingredients=; Most_Recent_Hair_Texture=; Most_Recent_Hair_Curl_Type=; Most_Recent_Price_Range=; Most_Recent_Selected_Coverage=; Most_Recent_Finish_Foundation=; Most_Recent_Finish_Powder=; _uetsid=a169c4203d7e11ec9a63053fc798ef13; _uetvid=a169e3803d7e11ec80f1ede59240d484; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; ftr_ncd=6; outbrain_cid_fetch=true; _tq_id.TV-18813609-1.5245=982f099425ddba1f.1636037465.0.1636037465..; _fbp=fb.2.1636037465376.1838083594; _pin_unauth=dWlkPU4yUTJZMkUwTkRBdE5tTXdaaTAwT0RObExXSTFNak10TmpBMU9UZzBZMkpqWkdOaA; _scid=73e890a5-af1a-4ecb-bce6-6fcc06230a1a; scarab.visitor=%221D041FE34FAC960%22; _sctr=1|1635958800000; cto_bundle=gP55G19zMUJCRU91RiUyRjA3cHh1OEozTmlYTU11SUdUd29wc0pPdWxoV1piQyUyQmJPcFJyRTJ3UmIxJTJGS2ZNMDJ3Q2hmdm54UHViUjRiQnJiVmRYTllIRiUyQlp3MU5mZGl4djNPMlRDZWYlMkJ6WUxqUWNXMDklMkZQNGQ2QTdxdkJpcG91OW5yTEpJdkZoejdKcmN2b1BKdGlOZXM5VzhSUHclM0QlM0Q; __zlcmid=16tkSKoZI58WF8d",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers"
        }

        r = requests.request("GET", url, data=payload, headers=headers, params=querystring,
                             proxies={
                                 "http": "Enter proxy here",
                                 "https": "Enter proxy here"
                             }
                             )

        data = r.json()
        # print(data['products'])
        for p in data['products']:
            res.append(p)
        print(f'Finish scraping page{x}')
    except:
        print(f'Failed at page {x}, retrying ...')
        extract_page(x)

for x in range(1, 127):
    extract_page(x)

df = pd.json_normalize(res)

df.to_csv('adore.csv',index=False)
df.to_json('adore.json')
