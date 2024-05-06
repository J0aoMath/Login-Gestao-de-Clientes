from tkinter import *
import customtkinter as ctk
import openpyxl 
import pathlib 
#aparencia padrao
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.appearence()
        
    def layout_config(self):
        self.title("Sistema de Gestao de Clientes")
        self.geometry('700x500')
        self.todo_sistema()
        
    def appearence(self):
        self.lb_apm = ctk.CTkLabel(self,text='Tema',bg_color='transparent', text_color=['#000','#fff']).place(x=50,y=430)
        self.opt_apm = ctk.CTkOptionMenu(self,values=['Light','Dark','System'],command=self.change_apm).place(x=50,y=460)
        
    def change_apm(self, nova_aparencia):
        ctk.set_appearance_mode(nova_aparencia)

    def todo_sistema(self):
        frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color='teal',fg_color='teal')
        frame.place(x=0,y=10)
        title = ctk.CTkLabel(frame,text='Sistema de Gestao de Clientes', font=('Century Gothic bold',24), text_color='#fff' ).place(x=190,y=10)
        span = ctk.CTkLabel(self,text='Por favor, preencher todos os campos do formulário.', font=('Century Gothic bold',24), text_color=['#000','#fff']).place(x=50,y=70)

        ficheiro = pathlib.Path('Clientes.xlsx')
        
        if ficheiro.exists():
            pass
        else:
            ficheiro = openpyxl.Workbook()
            folha=ficheiro.active
            folha['A1']='Nome Completo'
            folha['B1'] = 'Contato'
            folha['C1'] = 'Idade'
            folha['D1'] = 'Genero'
            folha['E1'] = 'Endereço'
            folha['F1'] = 'Observações'
                
            ficheiro.save("Clientes.xlsx")

        def submit(): 
            #pegando dados dos entrys
            name = name_value.get()
            contact = contact_value.get()
            age = age_value.get()
            gender = gender_combobox.get()
            address = adress_value.get()
            obs = obs_entry.get(0.0,END)
            
            ficheiro = openpyxl.load_workbook('Clientes.xlsx')
            folha = ficheiro.active
            folha.cell(column=1, row=folha.max_row+1, value=name)
            folha.cell(column=2, row=folha.max_row, value=contact)
            folha.cell(column=3, row=folha.max_row, value=age)
            folha.cell(column=4, row=folha.max_row, value=gender)
            folha.cell(column=5, row=folha.max_row, value=address)
            folha.cell(column=6, row=folha.max_row, value=obs)
            
            ficheiro.save(r'Clientes.xlsx') 
            
        def clear():
            name_value.set('')
            contact_value.set('')
            age_value.set('')
            adress_value.set('')
            obs_entry.delete(0.0, END)
 
 
        #Text variables
        name_value = StringVar()
        contact_value = StringVar()
        age_value = StringVar()
        adress_value = StringVar()
        
        
        #Entries
        name_entry = ctk.CTkEntry(self,textvariable=name_value, width=350, font=('Century Gothic bold', 16),fg_color='transparent')
        contact_entry = ctk.CTkEntry(self,textvariable=contact_value, width=200, font=('Century Gothic bold', 16),fg_color='transparent')
        age_entry = ctk.CTkEntry(self,textvariable=age_value, width=150, font=('Century Gothic bold', 16),fg_color='transparent')
        adress_entry = ctk.CTkEntry(self,textvariable=adress_value, width=200, font=('Century Gothic bold', 16),fg_color='transparent')
        
        #Combobox
        gender_combobox = ctk.CTkComboBox(self,values=['Masculino','Feminino'], font=('Century Gothic bold', 14))
        gender_combobox.set('Masculino')
        
        #Entrada de Obs
        obs_entry = ctk.CTkTextbox(self, width=500,height=150, font=('arial',18),border_color='#aaa',border_width=2,fg_color='transparent')
        
        
        #labels
        lb_name = ctk.CTkLabel(self,text='Nome Completo:', font=('Century Gothic bold',16), text_color=['#000','#fff'])
        lb_contact = ctk.CTkLabel(self,text='Contato', font=('Century Gothic bold',16), text_color=['#000','#fff'])
        lb_age = ctk.CTkLabel(self,text='Idade', font=('Century Gothic bold',16), text_color=['#000','#fff'])
        lb_gender = ctk.CTkLabel(self,text='Genero', font=('Century Gothic bold',16), text_color=['#000','#fff'])
        lb_adress = ctk.CTkLabel(self,text='Endereço', font=('Century Gothic bold',16), text_color=['#000','#fff'])
        lb_obs = ctk.CTkLabel(self,text='Observações', font=('Century Gothic bold',16), text_color=['#000','#fff'])
        btn_submit = ctk.CTkButton(self, text='Salvar dados'.upper(),command=submit,fg_color='#151',hover_color='#131' ).place(x=300,y=420)
        btn_submit = ctk.CTkButton(self, text='Limpar campos'.upper(),command=clear,fg_color='#555',hover_color='#333' ).place(x=500,y=420)
        #Posicionar elementos
        lb_name.place(x=50,y=120)
        name_entry.place(x=50,y=150)
        lb_contact.place(x=450,y=120)
        contact_entry.place(x=450,y=150)
        lb_adress.place(x=50,y=190)
        adress_entry.place(x=50,y=220)
        lb_age.place(x=300,y=190)
        age_entry.place(x=300,y=220)
        lb_gender.place(x=500,y=190)
        gender_combobox.place(x=500,y=220)
        lb_obs.place(x=50,y=260)
        obs_entry.place(x=150,y=260)
        
if __name__=='__main__':
    app = App()
    app.mainloop()