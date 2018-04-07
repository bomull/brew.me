from xml.etree import ElementTree as et

def malts(file):
    '''take a (fermentables) beerxml file and return a list with each (fermentable) as a dict in the list'''

    xml_fermentables = et.parse(file)
    catalogue = xml_fermentables.getroot()

    fermentables = []

    for item in catalogue:
        newentry = {}

        for tag in item:
            attribute = tag.tag
            newentry[attribute] = item.find(attribute).text

        fermentables.append(newentry)
        '''
        newentry['NAME'] = item.find('NAME').text
        newentry['VERSION'] = item.find('VERSION').text
        newentry['TYPE'] = item.find('TYPE').text
        newentry['AMOUNT'] = item.find('AMOUNT').text
        newentry['YIELD'] = item.find('YIELD').text
        newentry['COLOR'] = item.find('COLOR').text
        newentry['ADD_AFTER_BOIL'] = item.find('ADD_AFTER_BOIL').text
        newentry['ORIGIN'] = item.find('ORIGIN').text
        newentry['SUPPLIER'] = item.find('SUPPLIER').text
        newentry['NOTES'] = item.find('NOTES').text
        newentry['COARSE_FINE_DIFF'] = item.find('COARSE_FINE_DIFF').text
        newentry['MOISTURE'] = item.find('MOISTURE').text
        newentry['DIASTATIC_POWER'] = item.find('DIASTATIC_POWER').text
        newentry['PROTEIN'] = item.find('PROTEIN').text
        newentry['MAX_IN_BATCH'] = item.find('MAX_IN_BATCH').text
        newentry['RECOMMEND_MASH'] = item.find('RECOMMEND_MASH').text
        newentry['IBU_GAL_PER_LB'] = item.find('IBU_GAL_PER_LB').text
        newentry['DISPLAY_AMOUNT'] = item.find('DISPLAY_AMOUNT').text
        newentry['INVENTORY'] = item.find('INVENTORY').text
        newentry['POTENTIAL'] = item.find('POTENTIAL').text
        newentry['DISPLAY_COLOR'] = item.find('DISPLAY_COLOR').text
        '''

        # print(fermentables)
        # print(newentry)
        # for x in fermentables:
            # print(x['NAME'])
    # print(fermentables)
    # for x in fermentables:
        # print(x['NAME'])

    newlist = []
    for x in fermentables:
        if 'NAME' in x:
            newlist.append({"text":x['NAME']})

    new_list = [{"text":x['NAME']} for x in fermentables if 'NAME' in x]


    print(newlist)
    print(new_list)

    # new_list = []
    # for i in old_list:
        # if filter(i):
            # new_list.append(expressions(i))

            # You can obtain the same thing using list comprehension:

    # new_list = [expression(i) for i in old_list if filter(i)]


    return fermentables



malts('grain.xml')
