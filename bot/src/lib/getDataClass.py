import requests, json, re

class GetJsonData:
    def __init__(self):
        self.time_url = "https://www.jma.go.jp/bosai/amedas/data/latest_time.txt"
        self.latest_time = self.getLatestDateStr()
        self.latest_temp_data = self.getTempData()
        pass

    def getLatestDateStr(self):
        time_str = requests.get(self.time_url).text
        pattern = "(\d+)"
        results = re.findall(pattern, time_str)
        return "".join(results[:-2])

    def getTempData(self):
        url = "https://www.jma.go.jp/bosai/amedas/data/map/{}".format(self.latest_time+".json")
        res = requests.get(url)
        return json.loads(res.text)
