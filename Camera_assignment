import requests
import ast

class camera:

    def __init__(self):
        self.response = ast.literal_eval(requests.get('https://run.mocky.io/v3/57ae8489-caa8-40ac-967f-f19609ec4349').text)
        self.response1 = ast.literal_eval(requests.get('https://run.mocky.io/v3/a7ddb4d3-ad1d-4343-b020-8c077c2a6a61').text)
        self.rs = {}
        for p in self.response:
            for p1 in self.response1:
                if p['name'] == p1['name']:
                    self.rs[p['id']] = {**p, **p1}
                    break

    def setPort(self, x: int):
        """setPort(x) -- Add a new key "port" for "id" x element in the dict, and set the usb port number
            only from the sibling "port_path"."""

    def getPort(self, x: int):
        for ele in self.rs:
            if str(self.rs[ele]['id']) == str(x):
                return str(self.rs[ele]['name']) + str(self.rs[ele]['port_path'])


    def getMinIdElement(self):
        """Retrieve the "port" with "name" from "id" x element in the dict."""
        self.currentMinId = []
        for j in self.rs: self.currentMinId.append(self.rs[j]['id'])
        for k in self.rs:
            if self.rs[k]['id'] == str(min(self.currentMinId)):
                return self.rs[k]

    def getUpgradableDevice(self):
        """-- Retrieve all the "name" in the dict which "SupportUpgrade" is "Ture"."""
        lst = []
        for ele in self.rs:
            if self.rs[ele]['SupportUpgrade'] == True:
                lst.append(self.rs[ele]['name'])
        return lst


    def removeInvalidDevice(self):
        """-- Remove all the elements which "cameras": "candidate",
        "microphones" : "candidate", and "speakers" : "candidate" are all "False"."""

        filter = ["cameras", "microphones", "speakers"]
        for j in self.rs.copy():
            isdel = False
            for f in filter:
                if not self.rs[j][f][0]['candidate']:
                    isdel = True
                else:
                    isdel = False
            if isdel:
                del self.rs[j]
        print(self.rs)


if __name__ == '__main__':
    main = camera()
    main.getPort(2)
    # main.getUpgradableDevice()
    # main.removeInvalidDevice()
    # print(main.getMinIdElement())
