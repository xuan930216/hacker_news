#import the BigQuery libraries
from google.cloud import bigquery

def query_hackernews(keyword):
    #create bigquery client object
    client = bigquery.Client.from_service_account_json('searchengine/keyfile.json')
    
    #query public data set - hacker news
    query_job = client.query("""
        SELECT title, 
               LENGTH(title) AS title_length
        FROM `bigquery-public-data.hacker_news.stories` 
        WHERE title LIKE '%{}%'
        ORDER BY title_length DESC
        LIMIT 1000""".format(keyword))

    results = query_job.result()  # Waits for job to complete.

    return results


if __name__ == '__main__':
    query_hackernews('test your service')

