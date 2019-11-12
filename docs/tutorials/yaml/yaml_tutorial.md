`YAML`
=

[YAML tutorial](https://gettaurus.org/docs/YAMLTutorial/)

YAML (YAML Ain’t Markup Language) - еще один текстовый формат для записи данных.

YAML более приятен для восприятия человеком, чем JSON, поэтому его часто используют для 
описания сценариев в ПО. Например, в Ansible, Docker.

Как и Python, YAML использует отступы для указания структуры документа. 
Но в YAML можно использовать только пробелы и нельзя использовать знаки табуляции.

Еще одна схожесть с Python: комментарии начинаются с символа # и продолжаются до конца строки.

```
# test.yml

# create dictionary person: value
person:
  # keys: values
  # create anchor &name_id
  name: &name_id alex
  # convert into float type -> 30.0
  age: !!float 30
  # convert into str --> "36.6"
  temperature: !!str 36.6
  convert_string_to_integer: !!int "30"
  male: true
  profession: python dev
  # create k: [list]
  hobbies:
    - music
    - synthesizers
    - football
    - guitar
    - web dev
  # create k: [list]
  fav_genres: ["cinematic", "dark-drone metal"]
  # create list of dictionaries
  # 'friends': [{'name': 'oleg', 'age': 56}, {'name': 'alex', 'age': 28}]
  friends:
    - name: oleg
      age: 56
    - name: alex
      age: 28
  # ">" tells YAML to render all these text as a single line
  description: >
    Lorem Ipsum is simply dummy text of the printing
    and typesetting industry. Lorem Ipsum has been
    the industrys standard dummy text ever since the
    1500s.
  # "|" tells YAML to preserve formatting
  signature: |
    email
      alex
    a.shchegretsov@gmail.com
  # anchering
  # name: &name_id alex
  id: *name_id
  # whole object anchoring
  parameter: &repeat_param
    param_1: ok_1
    param_2: ok_2
    param_3:
      - ok_3.1: value_3.1
      - ok_3.2
      - ok_3.3
  # use whole object anchor and add some k:v
  repeat_param:
    <<: *repeat_param
    param_4: ok_4

```

`Чтение из файла`
==

`pip install pyyaml`

```
import yaml

with open("test.yml", "r") as f:
    temp = taml.safe_load(f)

print(temp)



{'person': {
    'name': 'alex', 
    'age': 30.0, 
    'temperature': '36.6', 
    'convert_string_to_integer': 30, 
    'male': True, 
    'profession': 'python dev', 
    'hobbies': ['music', 'synthesizers', 'football', 'guitar', 'web dev'], 
    'fav_genres': ['cinematic', 'dark-drone metal'], 
    'friends': [
        {'name': 'oleg', 'age': 56}, 
        {'name': 'alex', 'age': 28}
    ], 
    'description': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.\n", 
    'signature': 'email\n  alex\na.shchegretsov@gmail.com\n', 
    'id': 'alex', 
    'parameter': {
        'param_1': 'ok_1', 
        'param_2': 'ok_2', 
        'param_3': [{'ok_3.1': 'value_3.1'}, 'ok_3.2', 'ok_3.3']
    }, 
    'repeat_param': {
        'param_1': 'ok_1', 
        'param_2': 'ok_2', 
        'param_3': [{'ok_3.1': 'value_3.1'}, 'ok_3.2', 'ok_3.3'], 'param_4': 'ok_4'}
    }
}

```

`Запись объектов python в YAML`
=

```
import yaml

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_yaml = {'trunk': trunk_template, 'access': access_template}

with open("new.yml", "w") as f:
    yaml.dump(to_yaml, f)

with open("new.yml", "r") as f:
    print(f.read())




access:
- switchport mode access
- switchport access vlan
- switchport nonegotiate
- spanning-tree portfast
- spanning-tree bpduguard enable
trunk:
- switchport trunk encapsulation dot1q
- switchport mode trunk
- switchport trunk native vlan 999
- switchport trunk allowed vlan

```
