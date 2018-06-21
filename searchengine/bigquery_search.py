#import the BigQuery libraries
from google.cloud import bigquery
import datetime
import os.path


def query_hackernews(*args):
    #create bigquery client object

    BASE = os.path.dirname(os.path.abspath(__file__))
    client = bigquery.Client.from_service_account_json(os.path.join(BASE, "keyfile.json"))
    
    #get title, text and date from arguments, then convert title and text to lower case
    title = args[0].lower()
    text = args[1].lower()
    date = args[2]

    if date:
        year, month, day = date.split('-')
        date = datetime.date(int(year), int(month), int(day))
        sql = """
        SELECT  title, url, text, DATE(time_ts) as date
        FROM `bigquery-public-data.hacker_news.stories` 
        WHERE REGEXP_CONTAINS(title, '(?i){}') 
              AND REGEXP_CONTAINS(text, '(?i){}')
              AND DATE(time_ts) = DATE({}, {}, {})
        """.format(title, text, int(year), int(month), int(day))
    else:
        sql = """
        SELECT  title, url, text, DATE(time_ts) as date
        FROM `bigquery-public-data.hacker_news.stories` 
        WHERE REGEXP_CONTAINS(title, '(?i){}') AND REGEXP_CONTAINS(text, '(?i){}')
        """.format(title, text)

        
    #query public data set - hacker news
    query_job = client.query(sql)

    results = query_job.result()  # Waits for job to complete.

    return results


if __name__ == '__main__':
    query_hackernews('test your service')

