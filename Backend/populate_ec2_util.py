'''
This is one cool script, that allows us to reset our EC2 instance
and populate the presentation data anew. Use with care.
'''
import requests

HOST = 'http://ec2-34-244-59-141.eu-west-1.compute.amazonaws.com:8000/'


def create_votings():
    presidential_elections = {
        'name': 'Wybory prezydenckie 2020',
        'category': 'Wybory',
        'description': 'Minions ipsum baboiii hana dul sae jeje bee do bee do bee do.',
        'image': 'https://www.polska-ie.com/wp-content/uploads/2020/05/made-in-poland-e1536569723765-768x432.jpg',
        'is_active': True,
        'answers': [
            {
                'description': 'Robert Biedroń'
            },
            {
                'description': 'Krzysztof Bosak'
            },
            {
                'description': 'Andrzej Sebastian Duda'
            },
            {
                'description': 'Szymon Franciszek Hołownia'
            },
            {
                'description': 'Marek Jakubiak'
            },
            {
                'description': 'Władysław Marcin Kosiniak-Kamysz'
            },
            {
                'description': 'Mirosław Mariusz Piotrowski'
            },
            {
                'description': 'Paweł Jan Tanajno'
            },
            {
                'description': 'Rafał Kazimierz Trzaskowski'
            },
            {
                'description': 'Waldemar Włodzimierz Witkowski'
            },
            {
                'description': 'Stanisław Józef Żółtek'
            },
        ],
    }
    green_paths_data = {
        'name': 'Ścieżki spacerowe Zaspa',
        'category': 'Budżet obywatelski',
        'description': 'Minions ipsum baboiii hana dul sae jeje bee do bee do bee do.',
        'image': 'https://images.unsplash.com/photo-1519331379826-f10be5486c6f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80',
        'is_active': True,
        'answers': [
            {
                'description': 'Jestem za projektem Ścieki spacerowe Zaspa'
            },
            {
                'description': 'Jestem przeciwny'
            },
        ],
    }
    bicycle_paths_data = {
        'name': 'Ścieżka rowerowa centrum',
        'category': 'Zagospodarowanie przestrzenne',
        'description': 'Minions ipsum baboiii hana dul sae jeje bee do bee do bee do.',
        'image': 'https://images.unsplash.com/photo-1416103292956-1f6aff3d93fb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80',
        'is_active': True,
        'answers': [
            {
                'description': 'ul. Rajska'
            },
            {
                'description': 'ul. Jana Heweliusza'
            },
            {
                'description': 'ul. Wałowa'
            },
            {
                'description': 'ul. 3 Maja'
            },
            {
                'description': 'ul. Bielańska'
            },
        ],
    }

    requests.post(
        HOST + 'voting',
        json=presidential_elections,
    )
    requests.post(
        HOST + 'voting',
        json=green_paths_data,
    )
    requests.post(
        HOST + 'voting',
        json=bicycle_paths_data,
    )


# Run functions
create_votings()
