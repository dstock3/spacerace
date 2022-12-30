def get_mission_data(id):
    missions = [
        {
            'id': 1,
            'name': 'Sputnik 1',
            'launch_date': '1957-10-04',
            'description': 'The first artificial satellite to be launched into space.'
        },
        {
            'id': 2,
            'name': 'Explorer 1',
            'launch_date': '1958-01-31',
            'description': 'The first American satellite to be launched into space.'
        },
        {
            'id': 3,
            'name': 'Vostok 1',
            'launch_date': '1961-04-12',
            'description': 'The first manned spaceflight, piloted by Yuri Gagarin.'
        },
        {
            'id': 4,
            'name': 'Apollo 11',
            'launch_date': '1969-07-16',
            'description': 'The first manned mission to land on the Moon, piloted by Neil Armstrong and Buzz Aldrin.'
        },
        {
            'id': 5,
            'name': 'Skylab',
            'launch_date': '1973-05-14',
            'description': 'The first American space station, launched by NASA.'
        },
        {
            'id': 6,
            'name': 'Mir',
            'launch_date': '1986-02-19',
            'description': 'The first modular space station, launched by the Soviet Union.'
        },
        {
            'id': 7,
            'name': 'International Space Station',
            'launch_date': '1998-11-20',
            'description': 'A collaborative space station project involving multiple countries.'
        },
        {
            'id': 8,
            'name': 'Mars Curiosity Rover',
            'launch_date': '2011-11-26',
            'description': 'A Mars rover mission to explore the Gale Crater and search for signs of past microbial life.'
        },
        {
            'id': 9,
            'name': "Chang'e 4",
            'launch_date': '2018-12-07',
            'description': 'A Chinese mission to land a rover on the far side of the Moon.'
        },
        {
            'id': 10,
            'name': 'Artemis 1',
            'launch_date': '2022-11-01',
            'description': 'The first Artemis mission, which will test the Space Launch System rocket and the Orion spacecraft for future lunar exploration.'
        }
    ]

    for mission in missions:
        if mission['id'] == id:
            return mission
    return None