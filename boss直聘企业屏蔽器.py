import requests
# https://www.zhipin.com/?ka=header-home-logo
# 抓包 zpToken?v=....
# 找到cookie --[header]
# 找到zp_token -- [Response]
def get_cookie():
    # cookie
    return ""

def get_zp_token():
    # zp_token
    return ""

def main():
    # 企业匹配列表
    od_query_list = ["中软国际", "东软集团", "博彦科技", "博朗软件", "中电金信", "文思海辉", "法本信息", "奥博杰天", "浪潮", "软通动力", "福瑞博德",
                  "信必优", "大展科技", "恒生电子", "日电卓越软件", "大连华信", "和中软件", "新致软件", "艾斯克雷", "海隆软件", "大宇宙信息", "晟峰软件",
                  "富士通信息", "NTTDATA", "宏智科技", "神州信息", "凌志软件", "音泰思", "微生物软件", "佰钧成", "瑞友科技", "云测", "京北方", "宇信科技", "中科软", "汉克时代",
                  "赢时胜", "纬创软件", "联想利泰", "海通安恒", "德科信息", "云腾未来", "网新新思", "讯方技术", "易诚互动", "易联达", "润和软件", "柯莱特", "艾融", "易立德", "新致软件",
                  "科蓝软件", "亚信科技", "浩鲸科技", "德科信息", "易宝软件", "赛意信息", "安硕信息", "南天信息", "江苏红网", "时代银通", "领雁科技", "汉得信息", "四方精创", "川准达信息",
                  "慧博云通", "华路时代", "广联达", "鼎捷软件", "天阳科技", "亿达信息", "信雅达", "长亮科技", "全速创想", "金桥信息", "乌鸦科技", "久远银海"]

    for query in od_query_list:
        resp_json = requests.get(f"https://www.zhipin.com/wapi/zpgeek/maskcompany/suggest.json?query={query}", headers={"cookie": get_cookie()}).json()
        if resp_json:

            if resp_json["message"] == "Success":
                zp_data_json = resp_json["zpData"]
                suggest_list_json = zp_data_json["suggestList"]
                checkall = 1
                total_count = zp_data_json["totalCount"]
                name = query
                com_ids = ""
                for i in suggest_list_json:
                    suggest_json = i
                    com_ids += "," + suggest_json["encryptComId"]
                result1 = requests.get(f"https://www.zhipin.com/wapi/zpgeek/maskcompany/add.json?checkall={checkall}&totalCount={total_count}&name={name}&comIds={com_ids}", headers={"cookie": get_cookie(), "zp_token": get_zp_token()}).text
                print(f"公司名称: {name}，屏蔽结果：{result1}")

if __name__ == "__main__":
    main()