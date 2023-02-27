import PySimpleGUI as sg

menu_layout = [
	[
    sg.Text("Vendég neve: ", font=("Arial", 14)), 
    sg.Input(key="-NAME-", expand_x=True, font=("Arial", 14))
  ],[
    sg.CalendarButton("Válassz dátumot", target="-DATE-", font=("Arial", 14), format="%Y/%m/%d"), 
    sg.Input(key="-DATE-", expand_x=True, font=("Arial", 14))
  ],[
    sg.Text("Kezdő időpont: ", font=("Arial", 14)), 
    sg.Input(key="-START-", expand_x=True, font=("Arial", 14))
  ],[
    sg.Text("Végső időpont: ", font=("Arial", 14)), 
    sg.Input(key="-END-", expand_x=True, font=("Arial", 14))
  ],[
    sg.Text("Székek száma: ", font=("Arial", 14)), 
    sg.Input(key="-CHAIR-", expand_x=True, font=("Arial", 14))
  ],[
    sg.Radio("Beltéri", "-radioG1-", key="-IN-", default=True, font=("Arial", 14)),
    sg.Radio("Kültéri", "-radioG1-", key="-OUT-", font=("Arial", 14)),
    sg.Text("", expand_x=True),
    sg.Button("Mégse", key="-EXIT-", font=("Arial", 14)),
    sg.Button("Mentés", key="-SAVE-", font=("Arial", 14)),
  ],
]

window = sg.Window('Foglalás - Rögzítés', menu_layout, resizable=False, size=(600, 200))

def run():
  while True:
    event, values = window.read()
    print(event, values)

    match event:
      case sg.WIN_CLOSED | "-EXIT-": break

  window.close()
