import requests

def get_anime(name):
    response = requests.post('https://graphql.anilist.co', json={'query': f'''
                query {{
                    Media(search: "{name}", type: ANIME) {{
                        title {{
                            romaji
                        }}
                        description
                        startDate {{
                            year
                            month
                            day
                        }}
                        studios {{
                            nodes {{
                                name
                            }}
                        }}
                        episodes
                        status
                        genres
                        duration
                        averageScore
                        coverImage {{
                            large
                        }}
                    }}
                }}
            '''})
    data = response.json()
    # Check if the API response contains data
    if 'errors' in data:
        raise Exception(data['errors'][0]['message'])
    # Extract the relevant data from the API response
    ani_tit= data['data']['Media']['title']['romaji']
    ani_des= data['data']['Media']['description']
    ani_pub = f"{data['data']['Media']['startDate']['year']}-{data['data']['Media']['startDate']['month']}-{data['data']['Media']['startDate']['day']}"
    ani_stu = data['data']['Media']['studios']['nodes'][0]['name']
    ani_epi = data['data']['Media']['episodes']
    ani_sta = data['data']['Media']['status']
    ani_gen = ', '.join(data['data']['Media']['genres'])
    ani_dur = data['data']['Media']['duration']
    ani_ave = "{:.0f}%/100% positive vote".format(data['data']['Media']['averageScore'])
    ani_cov = data['data']['Media']['coverImage']['large']
    result = [ani_tit, ani_des, ani_pub, ani_stu, ani_epi, ani_sta, ani_gen, ani_dur, ani_ave, ani_cov]
    return result