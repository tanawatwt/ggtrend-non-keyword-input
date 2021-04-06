import pandas as pd                        
from pytrends.request import TrendReq
import json

pytrend = TrendReq()
rising_df_all = pd.DataFrame()
kw_list=[""]

pytrend.build_payload(kw_list,cat=3, timeframe='today 1-m',geo="TH") 



# Form Request
related_payload = dict()
request_json = pytrend.related_queries_widget_list[0]
# print(request_json)
related_payload["req"] = json.dumps(request_json["request"])
related_payload["token"] = request_json["token"]
related_payload["tz"] = pytrend.tz
# print(related_payload)

# Send Request
req_json = pytrend._get_data(
    url=TrendReq.RELATED_QUERIES_URL,
    method=TrendReq.GET_METHOD,
    trim_chars=5,
    params=related_payload,
)
result_json = pd.DataFrame(req_json)

result_json.to_json('result.json', force_ascii = False)

rising_df = pd.DataFrame(req_json['default']['rankedList'][1]["rankedKeyword"])
# print(req_json['default']['rankedList'][1]["rankedKeyword"])
# rising_df.to_json('result.json')
rising_df = rising_df[['query', 'value']]
rising_df_all = rising_df_all.append(rising_df, ignore_index=True)

# print(rising_df_all)


