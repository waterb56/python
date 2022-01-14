import PySimpleGUI as sg

# define layout
sg.theme('SandyBeach')
layout1 = [[sg.Text('Username', size=(10, 1)), sg.InputText(key='username')],
           [sg.Text('Password', size=(10, 1)), sg.InputText(key='password', password_char='*')]]
layout2 = [[sg.Text('Choose Your Tenant')],
           [sg.Combo(['common', 'FSC_Austin', 'FSC_Demo', 'FSC_Script_Test', 'infra', 'mgmt'], default_value='',
                     key='tenant')]]
layout3 = [[sg.Text('Last Job', size=(10, 1)), sg.Input('', key='eLastJ')],
           [sg.Text('From Date', size=(10, 1)), sg.Input('', key='eJFdt')],
           [sg.Text('To Date', size=(10, 1)), sg.Input('', key='eJTdt')],
           [sg.Text('Company Name', size=(10, 1)), sg.Input('', key='eLJcmpy')],
           [sg.Button('Save Experience Details')]]
# Define Layout with Tabs
tabgrp = [
    [sg.TabGroup([[sg.Tab('Username and Password', layout1, border_width=10),
                   sg.Tab('Tenant', layout2, title_color='Black', background_color='Blue'),
                   sg.Tab('Experience', layout3, title_color='Black', background_color='Blue',
                          tooltip='Enter  your Lsst job experience')]], tab_location='centertop',
                 title_color='Red', tab_background_color='Purple', selected_title_color='Green',
                 selected_background_color='Gray', border_width=5), [sg.Submit(), sg.Cancel()]]]

window = sg.Window("ACI Configuration", tabgrp)
event, values = window.read()
window.close()
user = values['username']
password = values['password']
tenant = values['tenant']
print(user, password, tenant)
