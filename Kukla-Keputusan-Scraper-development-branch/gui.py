import tkinter as tk

window = tk.Tk()
window.title('Test')
v = tk.IntVar()
# Add a grid
mainframe = tk.Frame()
mainframe.grid(column=0,row=0)
mainframe.columnconfigure(0, weight = 1,)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 20, padx = 20)

# Create a Tkinter variable
exam = tk.StringVar()
semester = tk.IntVar()

# Dictionary with options
echoices = { ' Ujian Selaras 1': 1,' Ujian Selaras 2':2,' Semester(Gred SPM)':3,' Semester(Gred PNG)':4,' Percubaan SPM':5}
exam.set('pick one') # set the default option
schoices = {1,2,3,4}
semester.set('pick one')

popupMenu = tk.OptionMenu(mainframe, exam, *echoices)
(tk.Label(mainframe, text="Choose exam")).grid(row = 1, column = 0, sticky = "W")
popupMenu.grid(row = 2, column =0, )
popupMenu = tk.OptionMenu(mainframe, semester, *schoices)
(tk.Label(mainframe, text="Choose semester")).grid(row = 3, column = 0, sticky = "W")
popupMenu.grid(row = 4, column =0, )

# on change dropdown value
def change_dropdown(*args):
    print( exam.get() )
# link function to change dropdown
exam.trace('w', change_dropdown)


lblgrade = tk.Label(mainframe, 
          text="With grades?",
          padx = 0
          )
lblgrade.grid(row = 1, column = 1, sticky = "W" )
rbtn_yes = tk.Radiobutton(mainframe,
              text="Yes, with grades",
              padx = 20, 
              variable=v, 
              value=1)
rbtn_yes.grid(row = 2, column = 1, sticky = 'W')
rbnt_no =tk.Radiobutton(mainframe,
              text="No, without grades",
              padx = 20, 
              variable=v, 
              value=2)
rbnt_no.grid(row = 3, column = 1, sticky = 'W')

lbloutput = tk.Label(mainframe,
                     text= "Output file",
                     padx = 20
                        )
lbloutput.grid(row = 4, column =1, sticky = 'W')
ent_output = tk.Entry(mainframe)
ent_output.grid(row = 5, column = 1)

btn_submit = tk.Button(mainframe, text = "Submit")
btn_submit.grid(row = 7, column = 1, sticky = "SE")



window.mainloop()