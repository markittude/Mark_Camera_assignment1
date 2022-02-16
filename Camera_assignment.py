import requests
import ast


class camera:

    def __init__(self):
        self.response = ast.literal_eval(requests.get('https://run.mocky.io/v3/57ae8489-caa8-40ac-967f-f19609ec4349').text)
        self.response1 = ast.literal_eval(requests.get('https://run.mocky.io/v3/a7ddb4d3-ad1d-4343-b020-8c077c2a6a61').text)
        self.cresponse = {}
        for key in self.response:
            for key1 in self.response1:
                if key['name'] == key1['name']:
                    self.cresponse[key['id']] = {**key, **key1}
                    break

    def setPort(self, x: int):
        """ Set Port of the requested ID\n
            Args: \n
                x： [required] ID number
            Return: \n
                String: return response with key port
        """
        for ele in self.cresponse:
            if str(self.cresponse[ele]['id']) == str(x):
                self.cresponse[ele]['port'] = self.cresponse[ele]['port_path'].split("/")[6]
        return self.cresponse


    def getPort(self, x: int):
        """ get name and port path of the requested ID\n
            Args: \n
                x： [required] ID number
            Return: \n
                String: return response with name and port path
        """
        for ele in self.cresponse:
            if str(self.cresponse[ele]['id']) == str(x):
                return str(self.cresponse[ele]['name']) + str(self.cresponse[ele]['port_path'])


    def getMinIdElement(self):
        """ Retrieve the minimum `id` element in the dict.\n
            Return: \n
                dict: return dictionary of the minimum ID
        """
        self.currentMinId = []
        for ele in self.cresponse: self.currentMinId.append(self.cresponse[ele]['id'])
        for ele in self.cresponse:
            if self.cresponse[ele]['id'] == str(min(self.currentMinId)):
                return self.cresponse[ele]

    def getUpgradableDevice(self):
        """-- Retrieve all the "name" in the dict which "SupportUpgrade" is "Ture".
        Return: \n
                List: return list of names with SupportUpgrade == True
        """

        lst = []
        for ele in self.cresponse:
            if self.cresponse[ele]['SupportUpgrade'] == True:
                lst.append(self.cresponse[ele]['name'])
        return lst


    def removeInvalidDevice(self):
        """-- Remove all the elements which "cameras": "candidate",
        "microphones" : "candidate", and "speakecresponse" : "candidate" are all "False"."""

        filter = ["cameras", "microphones", "speakers"]
        for ele in self.cresponse.copy():
            isdel = False
            for ele1 in filter:
                if not self.cresponse[ele][ele1][0]['candidate']:
                    isdel = True
                else:
                    isdel = False
            if isdel:
                del self.cresponse[ele]


if __name__ == '__main__':
    main = camera()
    print(main.setPort(1))
    print(main.getPort(2))
    print(main.getMinIdElement())
    print(main.getUpgradableDevice())
    main.removeInvalidDevice()
