import wx

# Cria um novo app e não redireciona o stdout/stderr para a janela
app = wx.App(False)
# Um frame é uma janela de nivel superior
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
# Mostra o frame
frame.Show(True)
app.MainLoop()