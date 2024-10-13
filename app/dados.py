import requests
from fastapi import HTTPException  # Import necessário

def obter_dados_externos():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-23.5505&longitude=-46.6333&daily=temperature_2m_max,temperature_2m_min&timezone=America/Sao_Paulo"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao obter os dados externos")
    data = response.json()
    return data['daily']  # Retorna a previsão diária