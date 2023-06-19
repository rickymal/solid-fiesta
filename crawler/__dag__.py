from bs4 import BeautifulSoup
import bs4
import requests
from datetime import datetime
import re
import psycopg2
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def get_html_soup(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_price(ctx : bs4.element.Tag):

    div = ctx.find('div',{'data-testid' : 'ad-price-wrapper'})
    if div:
        h2 = div.find('h2', {'data-ds-component': 'DS-Text'})
        if h2:
            return h2
        else:
            return None
    else:
        return None
    

def get_description(ctx : bs4.element.Tag):
    div = ctx.find('div',{'data-section' : 'description'})
    if div:
        inner_divs = div.find_all('div', recursive=False)
        if len(inner_divs) == 2:
            inner_div = inner_divs[1].find('div')
            p_tag = inner_div.find('p')
            return inner_div.find('p').find('span')
    else:
        return None


def get_extra_info(ctx : bs4.element.Tag, tag = "Condição"):
    divs = ctx.find('span', string = tag).find_parent('div').find_parent('div')
    return divs.find_all('div')[1]



def scrape():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    urls = [
        'https://pa.olx.com.br/regiao-de-belem/celulares/iphone-11-pro-max-256gb-1193748642?lis=listing_1000',
        'https://pa.olx.com.br/regiao-de-belem/celulares/apple-iphone-11-64gb-branco-1192530393?lis=listing_3000',
        'https://pa.olx.com.br/regiao-de-belem/celulares/samsung-a11-1195356339?lis=listing_3000',
        'https://pa.olx.com.br/regiao-de-belem/celulares/celular-a31-128-gb-1195627012?lis=listing_3060',
        'https://pa.olx.com.br/regiao-de-belem/celulares/iphone-7-34gb-1195626842?lis=listing_3060',
        'https://pa.olx.com.br/regiao-de-belem/celulares/iphone-7-34gb-1195626842?lis=listing_3060',
        'https://pa.olx.com.br/regiao-de-belem/celulares/celular-1195626622?lis=listing_3060',
        'https://pa.olx.com.br/regiao-de-belem/celulares/redmi-note-11-pro-1195624868?lis=listing_3060',
        'https://pa.olx.com.br/regiao-de-belem/celulares/iphone-11-pro-max-256gb-1193748642?lis=listing_1000',
        'https://pa.olx.com.br/regiao-de-belem/celulares/samsung-a11-1195356339?lis=listing_3000',
    ]

    connection = psycopg2.connect(
        user = "postgres",
        password = "123456789",
        host = 'localhost',
        port = '5432',
        database = 'OLX'
    )

    cursor = connection.cursor()

    try:
        for url in urls:
            ctx = get_html_soup(url, headers)
            if ctx.find('h2',string = "A página não foi encontrada...") is not None:
                # O celular foi retirado do anúncio eu acho
                continue 

            
            price = get_price(ctx).text
            description = get_description(ctx).text

            hsh = {
                'date' : datetime.now().isoformat(),
                'source' : 'OLX',
                'SO' : 'Android' if re.search("iphone", url, re.IGNORECASE) is None else 'IOS',
                'url' : url, 
                'price' : int(re.sub(r'\D', '', price)), # O ideal seria ser float
                'description' : description,
            }


            for option in ["Modelo","Condição","Memória interna","Cor", "Saúde da bateria"]:
                hsh[option] = get_extra_info(ctx, tag = option).text

            llof = []
            for key in ['date','SO','url','price','description','Modelo','Condição','Memória interna','Cor','Saúde da bateria']:
                if isinstance(hsh[key], str):
                    llof.append(f"\'{hsh[key]}\'")
                    continue
            
                llof.append(str(hsh[key]))

            part_of_query = ','.join(llof)
            insert_sql = f"INSERT INTO product(inserted_at, OS, url, price, description, model, condition, memory, color, battery) values({part_of_query});"
            cursor.execute(insert_sql)
        connection.commit()
    except:
        print("Algo de errado não está certo mi hermano")
    finally:
        cursor.close() 
        connection.close()

dag = DAG(
    'scrap_olx',
    description='Fazendo scraping dos dados de celulares da OLX',
    start_date=datetime(2023, 6, 9),
    schedule_interval='@once'
)

t1 = PythonOperator(
    task_id='scrap_olx',
    python_callable=scrape,
    dag=dag
)

