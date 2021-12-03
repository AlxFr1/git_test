def parse(query: str) -> dict:
    dct = {}
    if 'name' not in query:
        return dct
    new_query = query.split('?')[1].split('&')
    for pair in new_query:
        if '=' in pair:
            key, value = pair.split('=')
            dct.update({key: value})
    return dct


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?example') == {}
    assert parse('http://example.com/?????') == {}
    assert parse('http://example.com/?name=Anton') == {'name': 'Anton'}
    assert parse('http://example.com/error/') == {}
    assert parse('http://example.com.com.ua/?name=Anton?/') == {'name': 'Anton'}
    assert parse('http://example.com/http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?/?') == {}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple?') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/?///?') == {}
    assert parse('http://example.com/?name=Stas&color=green-blue?') == {'name': 'Stas', 'color': 'green-blue'}


def parse_cookie(query: str) -> dict:
    dct = {}
    txt = query.split(';')
    for i in txt:
        if '=' in i:
            i = i.split('=')
            dct.update({i[0]: '='.join(i[1:])})
    return dct


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima;age=54;') == {'name': 'Dima', 'age': '54'}
    assert parse_cookie('name=Dima;gender=male;') == {'name': 'Dima', 'gender': 'male'}
    assert parse_cookie('name=Sveta;gender=female;') == {'name': 'Sveta', 'gender': 'female'}
    assert parse_cookie('??????????') == {}
    assert parse_cookie('name=Dima;:') == {'name': 'Dima'}
    assert parse_cookie('name=Dima;;') == {'name': 'Dima'}
    assert parse_cookie(';name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('None') == {}
    assert parse_cookie('True/False') == {}
    assert parse_cookie('name=Dima;age=94;color=purple;') == {'name': 'Dima', 'age': '94', 'color': 'purple'}
