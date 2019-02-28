import shodan

# Configs
SHODAN_API_KEY = "no so fast cowboy"
api = shodan.Shodan(SHODAN_API_KEY)
filteredList = []
searchTerm = ''
closeProgram = False

# Functions / Methods
def printOptions():
    print('[1] Search webcamxp')
    print('[2] Search webcam')
    print('[3] Other...')
    print('[4] Exit')
    print('')

def printBanner():
    print('-------------------------------------------------------------------------')
    print(' __________    ____________________________________.____     __________')
    print(' \______   \  /  _  \__    ___/\____    /\______   \    |    \____    /')
    print('  |       _/ /  /_\  \|    |     /     /  |       _/    |      /     / ')
    print('  |    |   \/    |    \    |    /     /_  |    |   \    |___  /     /_ ')
    print('  |____|_  /\____|__  /____|   /_______ \ |____|_  /_______ \/_______ \\')
    print('         \/         \/                 \/        \/        \/        \/')
    print('--------------------------------------------------------------------------')
    print('')
    print('SHODAN API FILTERED SEARCH PYTHON by R4TZ')
    print('')


def mainProgram():
    try:
        if optionInput == '1':
            searchTerm = 'webcamxp'
        elif optionInput == '2':
           searchTerm = 'webcam'
        elif optionInput == '3':
            searchTerm = input('Write an API search term: ')
        else:
           print('Plz select a valid option')
           printOptions()
           return

        results = api.search(searchTerm)
        print('Rzlts found: {}'.format(results['total']))
        for result in results['matches']:
            dataList = result['data'].split()
            if dataList[1] == '200' and dataList[4] != 'close':
                filteredList.append(result)

        print('Filtered rzlts found: {}'.format(len(filteredList)))
        print('--------------------------------------------')
        for filteredResult in filteredList:
            print('IP: {}:{}'.format(filteredResult['ip_str'] , filteredResult['port']))
            print('HOSTN4ME: {}'.format(filteredResult['hostnames']))
            if userInput2 == 'y' or userInput2 == 'Y' or optionInput == '3' or userInput2 == '':
               print(filteredResult['data'])
            print('--------------------------------------------')
            print('')
    except shodan.APIError as e:
          print('Error :( : ----> {}'.format(e))



# Program Start
printBanner()
while not closeProgram:
    printOptions()
    optionInput = input('S3l3ct da option: ')
    if optionInput != '4':
        if optionInput != '3' and optionInput != '':
            userInput2 = input('Sh0w da d4ta? Y/n: ')
        else:
           userInput2 = ''

        mainProgram()
    else:
        break


