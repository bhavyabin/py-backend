import bs4
import requests
import json

session = requests.Session()
session.get("https://city.imd.gov.in/citywx/responsive/")



def get_weather_info(city):

    with open("station_ids.json", "r") as file:
        data = json.load(file)
        return get_weather_info_using_station_id(data["data"][city])


def get_weather_info_using_station_id(station_id):
    buffer_response = requests.get("https://city.imd.gov.in/citywx/city_weather_test_try_warnings.php?id=" + str(station_id))
    new_soup = bs4.BeautifulSoup(buffer_response.text, 'html.parser')

    print("https://city.imd.gov.in/citywx/city_weather_test_try_warnings.php?id=" + str(station_id), "\n")

    table_tags = new_soup.find_all("table")

    x_data = table_tags[1].find_all("font")

    buffer_seven_day_data = table_tags[2].find_all("tr")

    print(len(buffer_seven_day_data))

    seven_day_data = [
        buffer_seven_day_data[1].find_all("td"),
        buffer_seven_day_data[2].find_all("td"),
        buffer_seven_day_data[3].find_all("td"),
        buffer_seven_day_data[4].find_all("td"),
        buffer_seven_day_data[5].find_all("td"),
        buffer_seven_day_data[6].find_all("td"),
        buffer_seven_day_data[7].find_all("td"),
    ]



    file = open("station_ids_rev.json", "r")
    city = json.load(file)[str(station_id)]
    imd_api_res = native_json(station_id)
    file.close()

    print("got the the data needed!🤞")

    data = {
        "today": {
            "city": city,
            "day": seven_day_data[1][0].text
            .replace("\n", "")
            .replace("\t", "")
            .replace("\r", ""),
            "max_temp": x_data[2].text
            .replace("\n", "")
            .replace("\t", "")
            .replace("\r", ""),
            "min_temp": x_data[6].text
            .replace("\n", "")
            .replace("\t", "")
            .replace("\r", ""),
            "sunset_today": x_data[16].text
            .replace("\n", "")
            .replace("\t", "")
            .replace("\r", ""),
            "sunrise_tomorrow": x_data[18].text
            .replace("\n", "")
            .replace("\t", "")
            .replace("\r", ""),
            "moon_rise": x_data[22].text
            .replace("\n", "")
            .replace("\t", "")
            .replace("\r", ""),
            "moon_set": x_data[20].text
            .replace("\n", "")
            .replace("\t", "")
            .replace("\r", ""),
            "rainfall": float(imd_api_res[0]["rainfall"]) * (10 ** -2) if imd_api_res[0]["rainfall"] is not None else "--",
            "rh0830": imd_api_res[0]["rh0830"] + "%" if imd_api_res[0]["rh0830"] is not None else "--",
            "rh1730": imd_api_res[0]["rh1730"] + "%" if imd_api_res[0]["rh1730"] is not None else "--",
            "rh0000": (imd_api_res[0]["rh0830"] + "%" if imd_api_res[0]["rh0830"] is not None else "--") + " | " + (imd_api_res[0]["rh1730"] + "%" if imd_api_res[0]["rh1730"] is not None else "--")
        },

        "six_day": {
            "city": city,
            "day_1": {
                "day": seven_day_data[1][0].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),
                "min_temp": seven_day_data[1][1].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),
                "max_temp": seven_day_data[1][2].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", "")
                ,
                "forecast": seven_day_data[1][4].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "warnings": seven_day_data[1][6].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

            },
            "day_2": {
                "day": seven_day_data[2][0].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "min_temp":
                    seven_day_data[2][1].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "max_temp":
                    seven_day_data[1][2].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "forecast": seven_day_data[2][4].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "warnings": seven_day_data[2][6].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

            },
            "day_3": {
                "day": seven_day_data[3][0].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "min_temp":
                    seven_day_data[3][1].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "max_temp":
                    seven_day_data[3][2].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "forecast": seven_day_data[3][4].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "warnings": seven_day_data[3][6].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

            },
            "day_4": {
                "day": seven_day_data[4][0].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "min_temp":
                    seven_day_data[4][1].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "max_temp":
                    seven_day_data[4][2].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "forecast": seven_day_data[4][4].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "warnings": seven_day_data[4][6].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

            },
            "day_5": {
                "day": seven_day_data[5][0].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "min_temp":
                    seven_day_data[5][1].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "max_temp":
                    seven_day_data[5][2].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "forecast": seven_day_data[5][4].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "warnings": seven_day_data[4][6].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

            },
            "day_6": {
                "day": seven_day_data[6][0].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "min_temp":
                    seven_day_data[6][1].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "max_temp":
                    seven_day_data[6][2].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", "")
                ,
                "forecast": seven_day_data[6][4].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),

                "warnings": seven_day_data[6][6].text
                .replace("\n", "")
                .replace("\t", "")
                .replace("\r", ""),
            },
        }
    }

    print("response 👍 \n")
    return data

def native_json(station_id):
    json_data = {
        "ID" : station_id
    }
    response = session.post("https://city.imd.gov.in/citywx/responsive/api/fetchCity_static.php", data=json_data)

    return response.json()



if __name__ == "__main__":
    print(get_weather_info("Faridabad"))
