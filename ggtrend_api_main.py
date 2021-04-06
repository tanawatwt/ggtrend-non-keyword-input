import pandas as pd                        
from pytrends.request import TrendReq
import json
import get_json_cat

pytrend = TrendReq()

cate_lv1 = get_json_cat.all_cat_id

# rising_full_data = []
# rising_full_df = pd.DataFrame()
rising_df_all = pd.DataFrame()

kw_list=[""]

for cat_id in cate_lv1 : 

    pytrend.build_payload(kw_list,cat=cat_id, timeframe='today 1-m',geo="TH") 


    # Form Request
    related_payload = dict()
    request_json = pytrend.related_queries_widget_list[0]
    related_payload["req"] = json.dumps(request_json["request"])
    related_payload["token"] = request_json["token"]
    related_payload["tz"] = pytrend.tz

    # Send Request
    req_json = pytrend._get_data(
        url=TrendReq.RELATED_QUERIES_URL,
        method=TrendReq.GET_METHOD,
        trim_chars=5,
        params=related_payload,
    )

    # Tabulate Rising & Top searches.
    try:
        top_df = pd.DataFrame(req_json["default"]["rankedList"][0]["rankedKeyword"])
        top_df = top_df[["query", "value"]]
    except KeyError:
        # in case no top queries are found, the lines above will throw a KeyError
        top_df = None

    # rising queries
    try:
        rising_df = pd.DataFrame(req_json['default']['rankedList'][1]["rankedKeyword"])
        rising_df = rising_df[['query', 'value']]
        rising_df_all = rising_df_all.append(rising_df, ignore_index=True)

    except KeyError:
        # in case no rising queries are found, the lines above will throw a KeyError
        rising_df = None

rising_df_all.to_excel("result.xlsx")
# rising_full_df = pd.concat(rising_full_data, ignore_index=True)

# print(rising_full_df)