import wx

class MyFrame(wx.Frame):
    # Derivamos uma nova classe de Frame.
    def __init__(self, parent, title):
        wx.Frame.__init__(self,parent,title=title, size=(500,300))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)


# Cria um novo app e não redireciona o stdout/stderr para a janela
app = wx.App(False)
# Um frame é uma janela de nivel superior. 
# A nossa janela não tem tem pai e deixamos que wxWidgets escolha um ID com wx.ID_ANY
# Não há razões para escolher um ID apesar de que você pode escolher um
# Por fim temos o titulo da janela que é o "Hello World"
frame = MyFrame(None,"Simple Editor")
# Mostra o frame tornando ele visivel
app.MainLoop()