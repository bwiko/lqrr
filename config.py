from lib.ui_main import *

from PIL import Image
from pyzbar.pyzbar import decode
import os 
class Main(QWidget, Ui_QrReader ):
    def __init__(self,parent=None):
        
        os.system('import /tmp/qrcodeimg.png')
        QWidget.__init__(self)
        self.initIcon()
        self.setupUi(self)  
        Globalcenter(self)
        self.label.setPixmap(QPixmap(u"/tmp/qrcodeimg.png"))
        img = Image.open("/tmp/qrcodeimg.png")
        qr_decodes = decode(img)
        listtext = []
        if qr_decodes : 
            for qr_code in qr_decodes : 
                listtext.append(qr_code.data.decode('utf-8'))
        
            self.setQrText(listtext[0])
    def setQrText(self,text) : 
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">"+text+"</span></p></body></html>", None)) 
    def initIcon(self) : 
        icon = QIcon('/opt/tools/LRqr/icon/qr-code.png') #
        self.setWindowIcon(icon)

def Globalcenter(window):
    
    centerPoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    fg = window.frameGeometry()
    fg.moveCenter(centerPoint)
    window.move(fg.topLeft())