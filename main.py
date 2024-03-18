# import yaml
#
# data = {
#     'Name': 'John Doe',
#     'Position': 'DevOps Engineer',
#     'Location': 'England',
#     'Age': '26',
#     'Experience': {'GitHub': 'Software Engineer', 'Google': 'Technical Engineer', 'Linkedin': 'Data Analyst'},
#     'Languages': {'Markup': ['HTML'], 'Programming': ['Python', 'JavaScript', 'Golang']}
# }
#
# data_yaml = yaml.dump(data)
# print(data_yaml)


import yaml

data = {
    'Name': 'Mukhammad',
    'Position': 'DevOps Engineer',
    'Location': 'Uzbekistan',
    'Age': '15',
    'Experience': {'GitHub': '1bragimov', 'Google': 'ibragimovmukhammad020'},
    'Languages': {'Markup': ['Python Beckend'], 'Programming': ['Python', 'JavaScript', 'Django']}
}

with open("data.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)


