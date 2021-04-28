#! /usr/bin/env python3
# -*-coding:utf-8  -*-
"""ref: https://zetcode.com/pyqt/qnetworkaccessmanager/
TL:DR
For understanding purposes
QNetworkAccessManager allows application to send network requests and receive reply.
QNetworkRequest: holds request to be sent with the network manager
QNetworkReply: contains data & headers returned for a response
Has an asynchronous API{its methods always return immediately and do not wait until
they are finished}
A signal is emitted when request is done, we handle the response in the method attached to the 
finished signal
Original Author: Jan Bodnar
website: zetcode.com
"""
import sys
from PyQt5 import QtNetwork
from PyQt5.QtCore import QCoreApplication, QUrl

class Example:

    def __init__(self):

        self.doRequest()


    def doRequest(self):

        url = 'http://webcode.me' # url to receive html from
        req = QtNetwork.QNetworkRequest(QUrl(url)) #request instance

        self.nam = QtNetwork.QNetworkAccessManager() # create the manager object
        self.nam.finished.connect(self.handleResponse) # handle response when requist is finished
        self.nam.get(req)


    def handleResponse(self, reply):
        """Receives a QNetworkReply Object, contains data and headers
        for the request that was sent, if  there is no error in network reply
        """

        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:

            bytes_string = reply.readAll()
            print(str(bytes_string, 'utf-8'))

        else:
            print("Error occured: ", er)
            print(reply.errorString())

        QCoreApplication.quit()


def main():

    app = QCoreApplication([])
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()