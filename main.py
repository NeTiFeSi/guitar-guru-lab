from random import randint, choice, shuffle

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def create_exercise():
    start_house = randint(1, 19)
    finger_sequence = list(range(1, 5))
    shuffle(finger_sequence)
    return {
            'type': 'psychometric',
            'metronome_configuration': randint(30, 70),  # 250
            'number_of_time_divisions': choice(range(1, 3)),  # 5
            'finger_sequence': '-'.join(str(i) for i in finger_sequence),
            'start_house': start_house,
            'direction': choice(['up', 'down']),
            'final_sequence': '-'.join(
                [str(start_house + i) for i in finger_sequence]
            ),
    }
