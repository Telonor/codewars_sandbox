"""
Solution for "Extract the domain name from a URL" kata:
https://www.codewars.com/kata/514a024011ea4fb54200004b
"""
import re
pattern = re.compile(r'(?:(?:https?):\/\/)?(?:\w+\.)*(?P<domain>\w+)\.(?:\w+)(?:\/.*)?')


def domain_name(url):
    m = re.match(pattern, url)
    if m:
        return m.group('domain')
