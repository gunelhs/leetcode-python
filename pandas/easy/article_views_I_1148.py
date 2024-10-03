import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    equal = views[views["author_id"] == views["viewer_id"]][["author_id"]]
    duplicates = equal.drop_duplicates()
    sorting = duplicates.sort_values(by = "author_id", ascending = True)
    renamed = sorting.rename(columns = {"author_id": "id"})
    
    return renamed

views = [
    {'article_id': 1, 'author_id': 3, 'viewer_id': 5, 'view_date': '2019-08-01'},
    {'article_id': 1, 'author_id': 3, 'viewer_id': 6, 'view_date': '2019-08-02'},
    {'article_id': 2, 'author_id': 7, 'viewer_id': 7, 'view_date': '2019-08-01'},
    {'article_id': 2, 'author_id': 7, 'viewer_id': 6, 'view_date': '2019-08-02'},
    {'article_id': 4, 'author_id': 7, 'viewer_id': 1, 'view_date': '2019-07-22'},
    {'article_id': 3, 'author_id': 4, 'viewer_id': 4, 'view_date': '2019-07-21'},
    {'article_id': 3, 'author_id': 4, 'viewer_id': 4, 'view_date': '2019-07-21'}
]

df = pd.DataFrame(views)

df = article_views(df)

print(df)