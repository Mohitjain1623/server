import httpx

TOKEN = {'Authorization': 'Token 30012b2236c3de024a1e224edfaaa807f4be1856'}

def judgement_list(keyword, page=1):
    items = []
    URL = f'https://api.indiankanoon.org/search/?formInput={keyword}&pagenum={page}'
    with httpx.Client() as client:
        client.headers.update(TOKEN)
        results = client.post(URL)
    if results.status_code == 200:
        for r in results.json()['docs']:
            item = dict()
            item['tid'] = r['tid']
            item['title'] = r['title']
            item['headline'] = r['headline']
            item['url'] = r['url']
            items.append(item)
        return items
    return None


def judgement_detail(tid):
    URL = f'https://api.indiankanoon.org/doc/{tid}/'
    with httpx.Client() as client:
        client.headers.update(TOKEN)
        doc_id = 1584447
        results = client.post(URL)
    if results.status_code == 200:
        data = results.json()
        detail = dict()
        detail['tid'] = data['tid']
        detail['title'] = data['title']
        detail['doc'] = data['doc']
        detail['citedbyList'] = data['citedbyList']
    
        return detail
    else:
        return None





