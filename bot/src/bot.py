from lib.getDataClass import GetJsonData
from lib.calkDiscomfortIndexClass import CalcDiscomfotIndexClass
from lib.twitterSenderClass import TwitterSenderClass
import json, os
import datetime, time

LIST_DIR = os.path.join("..", "..", "bot_list.json")

def main():
    # 全ての観測データを取得
    gjd = GetJsonData()
    temp_dict = gjd.latest_temp_data
    date_str = gjd.latest_time[:-2]
    now_date = datetime.datetime.strptime(date_str, '%Y%m%d%H%M')

    # 投稿したい地域の情報を取得する
    json_open = open(LIST_DIR, 'r')
    locate_json = json.load(json_open)

    # 各観測地についての不快指数を計算
    for location in locate_json:

        locate_dict = locate_json[location]
        access_token = locate_dict["api_key"]["access_token"]
        access_token_secret = locate_dict["api_key"]["access_token_secret"]
        key = locate_dict["api_key"]["key"]
        secret_key = locate_dict["api_key"]["secret_key"]
        # その場所の不快指数を取得
        cdic = CalcDiscomfotIndexClass(temp_dict[locate_dict["id"]])

        index = cdic.calk()

        text = "【" + str(now_date) + "】現在\n"

        if index < 55:
            text += "🧊不快指数は{}（寒くてたまらない）です。\nしっかりと厚着をして出かけましょう".format(str(round(index, 2)))
        elif index >= 55 and index < 55:
            text += "🥶不快指数は{}（寒い）です。\n出かける時は上着を着ていきましょう".format(str(round(index, 2)))
        elif index >= 55 and index < 60:
            text += "😥不快指数は{}（肌寒い）です。\n一枚上着を持って出ましょう".format(str(round(index, 2)))
        elif index >= 60 and index < 65:
            text += "😐不快指数は{}（何も感じない）です。\n何も感じないそうです".format(str(round(index, 2)))
        elif index >= 65 and index < 70:
            text += "🙂不快指数は{}（快い）です。\n過ごしやすい気候です".format(str(round(index, 2)))
        elif index >= 70 and index < 75:
            text += "😑不快指数は{}（暑くない）です。\n暑くないそうです".format(str(round(index, 2)))
        elif index >= 75 and index < 80:
            text += "😓不快指数は{}（やや暑い）です。\n意識してこまめに水分をとりましょう".format(str(round(index, 2)))
        elif index >= 80 and index <85:
            text += "🥵不快指数は{}（暑くて汗が出る）です。\n暑いので水分をしっかりととりましょう".format(str(round(index, 2)))
        elif index >= 85:
            text += "👹不快指数は{}（暑くてたまらない）です。\nとても暑いので外出の際は熱中症に気をつけましょう".format(str(round(index, 2)))

        text += "\n気温：" + str(temp_dict[locate_dict["id"]]["temp"][0]) + "  湿度：" + str(str(temp_dict[locate_dict["id"]]["humidity"][0]))
        print(text)
        tsc = TwitterSenderClass(
            text=text,
            consumer_key=key,
            consumer_secret=secret_key,
            access_token=access_token,
            access_token_secret=access_token_secret
            )
        try:
            tsc.push()
        except Exception as e:
            print(e)
            continue


        print(location, ":", index)
if __name__ == "__main__":
    main()