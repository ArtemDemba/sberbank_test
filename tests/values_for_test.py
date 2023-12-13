input_dicts_for_splitting = [
    {
        'dict1': {'key1': 'value1'},
        'dict2': {'key2': 'value2'}
    },
    {
        'dict1': {
            'key1': 'value1',
            'key2': 'value2'
        },
        'dict2': {
            'key3': 'value3',
            'key4': {
                'key5': 'value5'
            }
        }
    }
]

expected_dicts_for_splitting = [
    [
        {'key1': 'value1'},
        {'key2': 'value2'}
    ],
    [
        {
            'key1': 'value1',
            'key2': 'value2'
        },
        {
            'key3': 'value3',
            'key4': {
                'key5': 'value5'
            }
        }
    ]
]

first_dict = {
    'key1': 'value1',
    'key2': {
        'key3': 'value3'
    }
}

second_dict = {
    'key2': {
        'key4': 'value4'
    },
    'key6': {
        'key8': 'value8'
    }
}

expected_result = {
    'key1': 'value1',
    'key2': {
        'key3': 'value3',
        'key4': 'value4'
    },
    'key6': {
        'key8': 'value8'
    }
}
