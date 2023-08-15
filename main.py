import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd

URL_EMBER_CLIMATE = 'https://ember-climate.org/data/data-tools/carbon-price-viewer/'
URL_FLOURISH = 'https://flo.uri.sh/visualisation/{}/embed?auto=1'


def get_ember_climate_info() -> dict:
    flourish_data = None

    response = requests.get(URL_EMBER_CLIMATE)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    flourish_tag = soup.find('div', class_='flourish-embed flourish-chart')

    data_src = flourish_tag['data-src']

    match = re.search(r'/(\d+)\?', data_src)
    if match:
        url_number = match.group(1)

        url_flourish_full = URL_FLOURISH.format(url_number)
        response_nueva = requests.get(url_flourish_full)

        html_content = response_nueva.content

        soup_nueva = BeautifulSoup(html_content, 'html.parser')

        script_tag = soup_nueva.find('script', text=re.compile(r'_Flourish_data\s*=\s*{.*}', re.DOTALL))

        script_content = script_tag.string

        match_data = re.search(r'_Flourish_data\s*=(.*?)_Flourish_visualisation_id\s*=', script_content, re.DOTALL)
        if match_data:
            json_data = match_data.group(1).strip()
            json_data = json_data.splitlines()[0]
            json_data = re.sub(r'\'', '"', json_data)
            json_data = json_data[:-1]

            try:
                flourish_data = json.loads(json_data)
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("The _Flourish_data variable was not found in the script.")
    else:
        print("Link number not found in data-src.")

    return flourish_data


def save_ember_climate_info(ember_climate_info=None) -> None:
    if ember_climate_info is None:
        ember_climate_info = {'data': []}

    dataset_eur = []
    dataset_gbp = []

    for entry in ember_climate_info['data']:
        metadata = entry.get('metadata', [])
        label = entry.get('label')
        value = entry.get('value')

        if '€' in metadata:
            dataset_eur.append({'label': label, 'currency': '€', 'value': float(value[0])})
        elif '£' in metadata:
            dataset_gbp.append({'label': label, 'currency': '£', 'value': float(value[0])})

    df_eur = pd.DataFrame(dataset_eur)
    df_gbp = pd.DataFrame(dataset_gbp)

    excel_writer = pd.ExcelWriter('datasets.xlsx', engine='xlsxwriter')
    df_eur.to_excel(excel_writer, sheet_name='Dataset_EUR', index=False)
    df_gbp.to_excel(excel_writer, sheet_name='Dataset_GBP', index=False)
    excel_writer._save()

    print("Datasets guardados en 'datasets.xlsx'")


if __name__ == '__main__':
    climate_info = get_ember_climate_info()
    save_ember_climate_info(climate_info)
