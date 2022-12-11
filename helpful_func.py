import json


def json_restructured(json_file, model):

    with open(json_file, "r", encoding="utf-8") as json_f:
        data = json.load(json_f)

        result_list = []

        for dict_element in data:
            fields_item = dict(dict_element)
            del fields_item["id"]
            result_list.append(
                {
                    "model": model,
                    "pk": dict_element["id"],
                    "fields": fields_item
                }
            )

        return result_list


def data_to_json_file(json_file, json_newfile, model):
    with open(json_newfile, "w", encoding="utf-8") as json_f_new:
        data = json_restructured(json_file, model)
        json_f_new.write(json.dumps(data, ensure_ascii=False))


a = json_restructured("ads_wn.json", "ads.ad")
b = json_restructured("categories.json", "ads.category")
print(a)
print(b)


output3 = data_to_json_file("ads_wn.json", "ads_fixt.json", "ads.ad")
output4 = data_to_json_file("categories.json", "categories_fixt.json", "ads.category")

