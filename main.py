from n2yo_client import N2yoClient
from openmeteo_client import OpenMeteoClient
from config import Config
from nominatim_client import NominatimClient

def main():
    cidade_usuario = input("- Digite o nome do local que seja obter os dados. Recomendamos que use o nome da cidade e estado.\n- Exemplo: São Paulo/SP\n")
    
    # Obtém as coordenadas da cidade informada utilizando a API Nominatim
    coordenadas = NominatimClient.obter_coordenadas_nominatim(cidade_usuario)
    latitude = coordenadas[0]
    longitude = coordenadas[1]
    
    # Cria um objeto de configuração com as coordenadas da cidade
    config = Config(latitude, longitude)
    
    # Cria um cliente N2yo e obtém as passagens da ISS para as coordenadas fornecidas
    n2yo = N2yoClient(config)
    all_passes = n2yo.display_passes()
    
    # Obtém os dados meteorológicos para cada passagem
    weather_data_id = []
    id = 1
    for item in all_passes:
        start_time = item['start']
        openmeteo = OpenMeteoClient()
        weather_data = openmeteo.get_weather_data(latitude, longitude, start_time)
        weather_data_id.append({
            "id": id,
            "weather": weather_data
        })
        id += 1
        
    # Extrai os dados de cada lista
    for pass_data, weather_data in zip(all_passes, weather_data_id):
        pass_id = pass_data['id']
        pass_start = pass_data['start']
        pass_duration = pass_data['duration']
        weather = weather_data['weather']
        temp = weather['temperature_2m']
        cloudcover = weather['cloudcover']
        visibility = weather['visibility']
        humidity = weather['relative_humidity_2m']
        is_day = "Day" if weather['is_day'] == 1 else "Night"
        
        # Exibe os dados
        print(f"Passagem {pass_id}:")
        print(f"  Horário: {pass_start} (Duração: {pass_duration} segundos)")
        print(f"  Clima na hora:")
        print(f"    Temperatura: {temp:.1f}°C")
        print(f"    Nuvens: {cloudcover}%")
        print(f"    Visibilidade: {visibility / 1000:.1f} km")
        print(f"    Umidade: {humidity}%")
        print(f"    Período: {is_day}")
        print("-" * 50)
    
if __name__ == "__main__":
    main()