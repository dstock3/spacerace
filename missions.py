def get_mission_data(id=None):
    missions = [
        {
            'id': 1,
            'name': 'Sputnik 1',
            'launch_date': '1957-10-04',
            'description': 'Sputnik 1 was the first artificial satellite to be launched into space. It was launched by the Soviet Union on October 4, 1957, and was a major milestone in the history of space exploration. The satellite was a small, metal sphere with four antennae attached, and was powered by batteries. It orbited the Earth for three weeks, transmitting radio signals that were picked up by receivers on the ground. The launch of Sputnik 1 sparked the space race between the United States and the Soviet Union, and led to the development of numerous space-related technologies and missions in the following years.',
            'meta': "Sputnik 1 was the first artificial satellite launched into space by the Soviet Union. It was a major milestone in the history of space exploration and sparked the space race between the United States and the Soviet Union.",
            'keywords': [
                "Soviet Union",
                "Cold War",
                "Space exploration",
                "Artificial satellite",
                "1957",
                "4 October",
                "First man-made satellite",
                "Korolev",
                "Vanguard rocket",
                "Explorer 1",
                "Vostok",
                "Yuri Gagarin",
                "Space Race",
                "Tikhonravov",
                "R-7 rocket"
            ],
            'era': 'Space Race'
        },
        {
            'id': 2,
            'name': 'Explorer 1',
            'launch_date': '1958-01-31',
            'description': "The first American satellite to be launched into space, Explorer 1 was a major achievement in the early space race between the United States and the Soviet Union. Launched on January 31, 1958, Explorer 1 was a small spacecraft weighing just over 30 pounds, with instruments on board to measure cosmic rays and the Earth's magnetic field. It was launched into orbit aboard a Jupiter-C rocket, and its success paved the way for further American space exploration in the years to come.",
            "meta": "Explorer 1 was the first American satellite launched in 1958. It weighed over 30 pounds and was used to measure cosmic rays and the Earth's magnetic field.",
            "keywords": [
                "United States",
                "Space exploration",
                "Artificial satellite",
                "1958",
                "31 January",
                "First U.S. satellite",
                "Jupiter-C rocket",
                "Vanguard rocket failure",
                "International Geophysical Year",
                "Van Allen radiation belt",
                "James Van Allen",
                "Wernher von Braun",
                "Army Ballistic Missile Agency"
            ],
            'era': 'Space Race'
        },
        {
            'id': 3,
            'name': 'Vostok 1',
            'launch_date': '1961-04-12',
            'description': "Vostok 1 was a Soviet space mission launched on April 12, 1961. It was the first manned spaceflight, with Yuri Gagarin becoming the first human to orbit the Earth. The spacecraft, Vostok 3KA, was launched from the Baikonur Cosmodrome and completed a single orbit of the Earth in 108 minutes before landing back on the ground. Gagarin's flight marked a major milestone in the space race between the Soviet Union and the United States, and Gagarin became a national hero in the Soviet Union.",
            "meta": "Vostok 1 was the first manned spaceflight, with Yuri Gagarin becoming the first human to orbit the Earth.", 
            "keywords": [
                "Soviet Union",
                "Yuri Gagarin",
                "Human spaceflight",
                "April 12, 1961",
                "Vostok program",
                "Korolev",
                "First manned flight",
                "R-7 rocket",
                "Space Race",
                "One orbit flight",
                "International Geophysical Year",
                "Gagarin's flight",
            ],
            'era': 'Space Race'
        },
        {
            'id': 4,
            'name': 'Mercury-Redstone 3',
            'launch_date': '1961-05-05',
            'description': "Mercury-Redstone 3, also known as Freedom 7, was the first manned spaceflight of the United States. Launched on May 5, 1961, astronaut Alan Shepard became the first American to travel into space. The mission lasted 15 minutes and 22 seconds, and reached an altitude of 116 miles. This mission marked a major milestone in the space race between the United States and Soviet Union.",
            "meta": "Mercury-Redstone 3, also known as Freedom 7, was the first manned spaceflight of the United States. Launched on May 5, 1961, astronaut Alan Shepard became the first American to travel into space.",
            "keywords": [
                "United States",
                "Space Race",
                "Manned spaceflight",
                "Alan Shepard",
                "Mercury program",
                "Redstone rocket",
                "May 5, 1961",
                "First American in space",
                "15 minutes 22 seconds",
                "116 miles"
            ],
            'era': 'Space Race'
        },
        {
            'id': 5,
            'name': 'Voskhod 2',
            'launch_date': '1965-03-18',
            'description': "Voskhod 2 was a Soviet space mission launched on March 18, 1965. It was the first manned spaceflight to feature a spacewalk, with cosmonaut Alexei Leonov becoming the first human to walk in space. The mission lasted 24 hours and 17 minutes, and reached an altitude of 200 miles. This mission marked a major milestone in the space race between the Soviet Union and the United States.",
            "meta": "Voskhod 2 was a Soviet space mission launched on March 18, 1965. It was the first manned spaceflight to feature a spacewalk, with cosmonaut Alexei Leonov becoming the first human to walk in space.",
            "keywords": [
                "Soviet Union",
                "Space Race",
                "Manned spaceflight",
                "Alexei Leonov",
                "Voskhod program",
                "March 18, 1965",
                "First spacewalk",
                "24 hours 17 minutes",
                "200 miles"
            ],
            'era': 'Space Race'
        },
        {
            'id': 6,
            'name': 'Gemini 4',
            'launch_date': '1965-06-03',
            'description': "Gemini 4 was a manned spaceflight of the United States, launched on June 3, 1965. It was the second manned mission of the Gemini program, and astronaut Edward White became the first American astronaut to perform a spacewalk. The mission lasted for four days and orbited the Earth 66 times. Gemini 4 was a major achievement for the United States in the space race, as it demonstrated the capabilities of the Gemini spacecraft and the ability of American astronauts to perform spacewalks.",
            'meta': "Gemini 4 was the second manned mission of the Gemini program, astronaut Edward White performed the first American spacewalk and orbited the Earth for 4 days in 1965.",
            'keywords': [
                "United States",
                "Space exploration",
                "Human spaceflight",
                "Gemini program",
                "Edward White",
                "Spacewalk",
                "Jim McDivitt",
                "NASA",
                "Space Race",
                "First American spacewalk",
            ]
        },
        {
            'id': 7,
            'name': 'Gemini 8',
            'launch_date': '1966-03-16',
            'description': "Gemini 8 was a manned spaceflight of the United States, launched on March 16, 1966. It was the sixth manned mission of the Gemini program, and astronaut Neil Armstrong became the first person to dock two spacecraft in space. The mission lasted for just under 12 hours before an emergency splashdown. Gemini 8 was a major achievement for the United States in the space race, as it demonstrated the capabilities of the Gemini spacecraft and the ability of American astronauts to perform docking maneuvers.",
            'meta': "Gemini 8 was the sixth manned mission of the Gemini program, astronaut Neil Armstrong became the first person to dock two spacecraft in space. The mission lasted for 12 hours before an emergency splashdown in 1966.",
            'keywords': [
                "United States",
                "Space exploration",
                "Human spaceflight",
                "Gemini program",
                "Neil Armstrong",
                "Docking",
                "David Scott",
                "NASA",
                "Space Race",
                "First spacecraft docking",
            ]
        },
        {
            'id': 8,
            'name': 'Apollo 11',
            'launch_date': '1969-07-16',
            'description': "Apollo 11 was a NASA mission that launched on July 16, 1969. It was the first manned mission to land on the Moon, piloted by Neil Armstrong and Buzz Aldrin. Armstrong became the first human to set foot on the Moon, famously saying, 'That's one small step for man, one giant leap for mankind.' The mission was a major milestone in the space race and solidified the United States as a leader in space exploration.",
            "meta": "Apollo 11 was the first manned mission to land on the Moon, piloted by Neil Armstrong and Buzz Aldrin.",
            "keywords": [
                "United States",
                "NASA",
                "Moon landing",
                "July 20, 1969",
                "Neil Armstrong",
                "Buzz Aldrin",
                "Michael Collins",
                "Apollo program",
                "Saturn V rocket",
                "Eagle",
                "Sea of Tranquility",
                "First human on the moon",
                "One Small Step for Man"
            ],
            'era': 'Space Race'
        },
        {
            'id': 9,
            'name': 'Skylab',
            'launch_date': '1973-05-14',
            'description': "Skylab was a space station launched by NASA in 1973. It was the first space station operated by the United States and was designed to be a manned laboratory for studying the effects of long-term space flight on humans. It contained living quarters, a workshop, and various scientific instruments. Skylab orbited Earth for six years and was visited by three manned missions, during which astronauts conducted experiments in a variety of fields including solar physics, Earth observations, and medical studies. The space station was decommissioned in 1979 and re-entered the Earth's atmosphere, with most of its debris falling harmlessly into the Indian Ocean and Western Australia.",
            "meta": "Skylab was a space station launched by NASA in 1973. It was designed to be a manned laboratory for studying the effects of long-term space flight on humans.",
            "keywords": [
                "United States",
                "NASA",
                "Space station",
                "1973-1974",
                "First U.S. space station",
                "Saturn V rocket",
                "Skylab program",
                "Orbital Workshop",
                "Solar observation",
                "Skylab 2",
                "Skylab 3",
                "Skylab 4"
            ],
            'era': 'Space Race'
        },
        {
            'id': 10,
            'name': 'Apollo-Soyuz Test Project',
            'launch_date': '1975-07-15',
            'description': "The Apollo-Soyuz Test Project was a joint space mission between the United States and Soviet Union. Launched on July 15, 1975, it was the first international manned space flight and marked the end of the space race between the two nations. The mission consisted of the American Apollo spacecraft and the Soviet Soyuz spacecraft docking in orbit and the exchange of two astronaut crews. The mission was seen as a symbol of the improving relations between the United States and Soviet Union during the Cold War.",
            "meta": "The Apollo-Soyuz Test Project was a joint space mission between the United States and Soviet Union. It was the first international manned space flight and marked the end of the space race between the two nations.",
            "keywords": [
                "United States",
                "Soviet Union",
                "Joint space mission",
                "International manned space flight",
                "Space Race",
                "Apollo spacecraft",
                "Soyuz spacecraft",
                "Orbit",
                "Astronaut crews",
                "Cold War",
                "1975",
                "July 15"
            ],
            'era': 'Space Race'
        },
        {
            'id': 11,
            'name': 'Voyager 1',
            'launch_date': '1977-09-05',
            'description': "Voyager 1 is a space probe launched by NASA on September 5, 1977. It was designed to study the outer solar system and interstellar space. The probe carries a golden record containing images and sounds that represent Earth and humanity, in the event that it is found by extraterrestrial life. Voyager 1 became the first human-made object to leave the Solar System and is still in operation today, sending back valuable data about interstellar space.",
            "meta": "Voyager 1 is a space probe launched by NASA in 1977 to study the outer solar system and interstellar space. It carries a golden record representing Earth and humanity.",
            "keywords": [
                "NASA",
                "Space probe",
                "Outer solar system",
                "Interstellar space",
                "Golden record",
                "Extraterrestrial life",
                "Solar System",
                "Voyager program",
                "1977",
                "Jupiter",
                "Saturn",
                "Pioneer program"
            ],
            'era': 'Post Space Race'
        },
        {
            'id': 12,
            'name': 'Mir',
            'launch_date': '1986-02-19',
            'description': 'The first modular space station, launched by the Soviet Union in 1986. Mir was in operation for 15 years, during which time it was visited by a total of 28 long-term expeditions and over 100 short-term missions. It was also the site of various space-based scientific experiments, as well as being the first space station to be visited by space shuttles from the United States. Mir was decommissioned in 2001 and deorbited in March of that year.',
            "meta": "Mir was the first modular space station, launched by the Soviet Union in 1986. It was in operation for 15 years, during which time it was visited by a total of 28 long-term expeditions and over 100 short-term missions.",
            "keywords": [
                "Societ Union",
                "Russia",
                "Space station",
                "1986-2001",
                "Longest-serving space station",
                "Proton-K rocket",
                "Mir program",
                "International cooperation",
                "ISS precursor",
                "Cosmonauts",
                "Space Shuttle"
            ],
            'era': 'Post Space Race'
        },
        {
            'id': 13,
            'name': 'Hubble Space Telescope',
            'launch_date': '1990-04-24',
            'description': "The Hubble Space Telescope is a telescope in orbit around Earth, launched into space in 1990. It is named after the American astronomer Edwin Hubble and is one of the most important astronomical instruments in history. The telescope is capable of capturing images of distant galaxies and has made many groundbreaking discoveries, such as the accelerating expansion of the universe. It has also been instrumental in the study of black holes and dark matter.",
            "meta": "The Hubble Space Telescope is a telescope launched in 1990, in orbit around Earth. It is named after Edwin Hubble and has made many groundbreaking discoveries.",
            "keywords": [
                "Space telescope",
                "Earth orbit",
                "Edwin Hubble",
                "Astronomy",
                "1990",
                "Distant galaxies",
                "Expanding universe",
                "Black holes",
                "Dark matter",
                "NASA",
                "STS-31 mission"
            ],
            'era': 'Post Space Race'
        },
        {
            'id': 14,
            'name': 'International Space Station',
            'launch_date': '1998-11-20',
            'description': 'The International Space Station (ISS) is a habitable, habitable spacecraft that orbits Earth and is home to a rotating crew of astronauts from various countries. The ISS is a collaboration between NASA, the Russian space agency Roscosmos, the European Space Agency, the Japanese space agency JAXA, and the Canadian space agency CSA. It was launched in 1998 and has been continuously inhabited since 2000, making it the longest-occupied space station in history. The ISS is used for research in a variety of fields, including biology, physics, and astronomy, as well as for testing new technologies and conducting experiments in microgravity. The ISS is an important symbol of international cooperation in space exploration, and it serves as a stepping stone for future human missions to other destinations in the solar system.',
            "meta": "The International Space Station (ISS) is a habitable, habitable spacecraft that orbits Earth and is home to a rotating crew of astronauts from various countries.",
            "keywords": [
                "International Space Station",
                "ISS",
                "orbital research",
                "microgravity",
                "astronauts",
                "space exploration",
                "NASA",
                "ESA",
                "space station",
                "orbit",
                "low Earth orbit",
                "astronomy",
                "cosmology",
                "science experiments",
                "human spaceflight",
                "satellite"
            ],
            'era': 'Post Space Race'
        },
        {
            'id': 15,
            'name': 'Mars Curiosity Rover',
            'launch_date': '2011-11-26',
            'description': "The Mars Curiosity Rover is a robotic vehicle designed to explore the surface of Mars and search for signs of past or present microbial life. It was launched in 2011 and has been active on the surface of Mars ever since. The rover is equipped with a variety of scientific instruments and tools, including cameras, spectrometers, and drill bits, which it uses to analyze the chemical and mineral composition of rocks and soil. It is also equipped with a weather station and a laser-induced breakdown spectroscope, which it uses to study the planet's atmosphere and search for organic molecules. The rover's primary mission is to determine whether Mars has ever had the potential to support microbial life, and to help pave the way for future manned missions to the planet.",
            "meta": "The Mars Curiosity Rover is a robotic vehicle designed to explore the surface of Mars and search for signs of past or present microbial life.",
            "keywords": [
                "Mars Curiosity Rover",
                "MSL",
                "Mars Science Laboratory",
                "NASA",
                "JPL",
                "Jet Propulsion Laboratory",
                "Mars Exploration Program",
                "Curiosity",
                "red planet",
                "rovers",
                "mars",
                "planetary science",
                "geology",
                "astrobiology",
                "search for life",
                "Mount Sharp",
                "sample analysis"
            ],
            'era': 'Post Space Race'
        },
        {
            'id': 16,
            'name': "Chang'e 4",
            'launch_date': '2018-12-07',
            'description': "Chang'e 4 is a Chinese lunar exploration mission that aims to land a rover on the far side of the Moon. The mission, which was launched on December 7, 2018, is named after the Chinese moon goddess Chang'e. The mission's primary goals include conducting scientific research on the Moon's composition, studying the interaction between solar wind and the lunar surface, and searching for resources that could be used in future lunar exploration missions. Additionally, Chang'e 4 aims to demonstrate the feasibility of using the far side of the Moon as a base for future space exploration. The mission successfully landed on the far side of the Moon on January 3, 2019, making it the first spacecraft to do so.",
            "meta": "Chang'e 4 is a Chinese lunar exploration mission that aims to land a rover on the far side of the Moon.",
            "keywords": [
                "Chang'e 4",
                "China National Space Administration",
                "CNSA",
                "lunar exploration",
                "moon",
                "Yutu-2",
                "landing",
                "far side of the moon",
                "lunar rover",
                "lunar surface",
                "planetary science",
                "astrogeology",
                "space science"
            ],
            'era': 'Post Space Race'
        },
        {
            'id': 17,
            'name': 'Artemis 1',
            'launch_date': '2022-11-01',
            'description': 'Artemis 1 is a mission planned by NASA as part of the Artemis program, which aims to land humans on the Moon by 2024. Artemis 1 is an unmanned test flight of the Space Launch System rocket and the Orion spacecraft, which will be used for future manned missions to the Moon and potentially beyond. The mission will also include a number of scientific payloads to study the lunar environment and collect data for future missions. Artemis 1 is currently scheduled to launch in November 2022.',
            "meta": "Artemis 1 is a mission planned by NASA as part of the Artemis program, which aims to land humans on the Moon by 2024.",
            "keywords": [
                "Artemis 1",
                "NASA",
                "Space Launch System",
                "Orion",
                "moon",
                "moon mission",
                "lunar exploration",
                "human spaceflight",
                "moon landing",
                "deep space exploration",
                "Gateway",
                "sustainability",
                "international cooperation",
                "Artemis program"
            ],
            'era': 'Post Space Race'
        }
    ]

    if id is None:
        return missions

    for mission in missions:
        if mission['id'] == id:
            return mission
    raise ValueError(f'No mission found with id: {id}')