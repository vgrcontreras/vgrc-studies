from airflow.sdk import asset, Asset, Context
from typing import Any

@asset(
    schedule='@daily',
    uri='https://randomuser.me/api'
)
def user(self) -> dict[str, Any]:
    import requests

    response = requests.get(self.uri)
    return response.json()


@asset.multi(
    schedule=user,
    outlets=[
        Asset(name='user_location'),
        Asset(name='user_login')
    ]
)

def user_info(user: Asset, context: Context) -> list[dict[str,Any]]:
    user_data = context['ti'].xcom_pull(
        task_ids=user.name,
        dag_id=user.name,
        include_prior_dates=True
    )

    return {
        user_data['results'][0]['location'],
        user_data['results'][0]['login']
    }