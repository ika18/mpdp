# -*- coding:utf-8 -*-

import json
import xml.etree.ElementTree as etree
import io

class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with io.open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree
    

def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)

def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    # 和例子上不一样，报错捕获之后不能继续。。。。
    # sqlite_factory = connection_factory('data/person.sq3')
    # print()

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))

    print('found: {} person'.format(len(liars)))

    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        # python 3
        # [print('phone number ({})'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]
        for p in liar.find('phoneNumbers'):
            print('phone number ({})'.format(p.attrib['type']), p.text)
    print()

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))

    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        for t in donut['topping']:
            print('topping: {} {}'.format(t['id'], t['type']))


if __name__ == '__main__':
    main()