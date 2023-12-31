import requests

def get_manga(name):
    response = requests.post('https://graphql.anilist.co', json={'query': f'''
            query {{
                Media(search: "{name}", type: MANGA) {{
                    title {{
                        romaji
                    }}
                    description
                    startDate {{
                        year
                        month
                        day
                    }}
                    staff {{
                        edges {{
                            node {{
                                name {{
                                    full
                                }}
                            }}
                        }}
                    }}
                    chapters
                    status
                    genres
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
    man_tit = data['data']['Media']['title']['romaji']
    man_des = data['data']['Media']['description']
    man_pub = f"{data['data']['Media']['startDate']['year']}-{data['data']['Media']['startDate']['month']}-{data['data']['Media']['startDate']['day']}"
    staff_members = data['data']['Media']['staff']['edges']
    main_author = staff_members[0]['node']['name']['full'] if staff_members else "N/A"
    man_chap = data['data']['Media']['chapters']
    man_sta = data['data']['Media']['status']
    man_gen = ', '.join(data['data']['Media']['genres'])
    man_ave = "{:.0f}%/100% positive vote".format(data['data']['Media']['averageScore'])
    man_cov = data['data']['Media']['coverImage']['large']
    
    res = [man_tit, man_des, man_pub, main_author, man_chap, man_sta, man_gen, man_ave, man_cov]
    return res