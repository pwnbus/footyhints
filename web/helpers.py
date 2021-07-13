
# Help from https://mobiforge.com/design-development/build-a-mobile-and-desktop-friendly-application-django-15-minutes

MOBILE_UAS = [
    'w3c ',
    'acs-',
    'alav',
    'alca',
    'amoi',
    'audi',
    'avan',
    'benq',
    'bird',
    'blac',
    'blaz',
    'brew',
    'cell',
    'cldc',
    'cmd-',
    'dang',
    'doco',
    'eric',
    'hipt',
    'inno',
    'ipaq',
    'java',
    'jigs',
    'kddi',
    'keji',
    'leno',
    'lg-c',
    'lg-d',
    'lg-g',
    'lge-',
    'maui',
    'maxo',
    'midp',
    'mits',
    'mmef',
    'mobi',
    'mot-',
    'moto',
    'mwbp',
    'nec-',
    'newt',
    'noki',
    'oper',
    'palm',
    'pana',
    'pant',
    'phil',
    'play',
    'port',
    'prox',
    'qwap',
    'sage',
    'sams',
    'sany',
    'sch-',
    'sec-',
    'send',
    'seri',
    'sgh-',
    'shar',
    'sie-',
    'siem',
    'smal',
    'smar',
    'sony',
    'sph-',
    'symb',
    't-mo',
    'teli',
    'tim-',
    'tosh',
    'tsm-',
    'upg1',
    'upsi',
    'vk-v',
    'voda',
    'wap-',
    'wapa',
    'wapi',
    'wapp',
    'wapr',
    'webc',
    'winw',
    'winw',
    'xda',
    'xda-',
]

MOBILE_UA_HINTS = [
    'SymbianOS',
    'Opera Mini',
    'iPhone'
]


def mobile_browser(request):
    ''' Super simple device detection, returns True for mobile devices '''

    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]

    if (ua in MOBILE_UAS):
        mobile_browser = True
    else:
        for hint in MOBILE_UA_HINTS:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True

    return mobile_browser
