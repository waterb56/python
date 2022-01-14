import PySimpleGUI as sg
import PySimpleGUI as psg



def SelectScript():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Which Script do you want to run?')],
        [psg.Combo(['Create a snapshot',
                    'Add L2BD/VLAN/EPG to ACI',
                    'Add VPC To Leafs 101-102',
                    'Add VPC To Leafs 103-104',
                    'Add Non PC/VPC Interfaces To Switch Profile',
                    'Add Non-VPC Interfaces to EPG',
                    'Add VPC to EPGs',
                    'Delete static port from EPG',
                    'Add description to interface',
                    ],
                   default_value='', key='script')],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Select Which Script You Want To Run', layout, size=(700, 400))
    event, values = window.read()
    window.close()
    script = values['script']
    return script

def LeafInterfaceSelect():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Choose Your Nodes')],
        [sg.Text('Choose Your Node 101 From Port')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
                   default_value='', key='101_from_port')],
        [sg.Text('Choose Your Node 101 To Port')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
                   default_value='', key='101_to_port')],
        [sg.Text('Choose Your Node 102 From Port')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
                   default_value='', key='102_from_port')],
        [sg.Text('Choose Your Node 102 To Port')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
                   default_value='', key='102_to_port')],
        [sg.Text('Choose Your Node 103 From Port')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
                   default_value='', key='103_from_port')],
        [sg.Text('Choose Your Node 103 To Port')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
                   default_value='', key='103_to_port')],
        [sg.Text('Choose Your Node 104 From Port')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
                   default_value='', key='104_from_port')],
        [sg.Text('Choose Your Node 104 To Port')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
                   default_value='', key='104_to_port')],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Add Non PC/VPC ports to leafs', layout, size=(600, 600))
    event, values = window.read()
    window.close()
    l101FromInterfaces = values['101_from_port']
    l101ToInterfaces = values['101_to_port']
    l102FromInterfaces = values['102_from_port']
    l102ToInterfaces = values['102_to_port']
    l103FromInterfaces = values['103_from_port']
    l103ToInterfaces = values['103_to_port']
    l104FromInterfaces = values['104_from_port']
    l104ToInterfaces = values['104_to_port']
    return l101FromInterfaces,l101ToInterfaces, l102FromInterfaces, l102ToInterfaces,\
           l103FromInterfaces, l103ToInterfaces, l104FromInterfaces, l104ToInterfaces

def AddNonVpcInterfaceToEpg():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Choose Your Node 101 Ports')],
        [psg.Listbox(values=[1, 2, 3, 4, 5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15, 16,
                             17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                             39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
                     select_mode='extended', key='node101ports', size=(30, 6))],
        [sg.Text('Choose Your Node 102 Ports')],
        [psg.Listbox(values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                             17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                             39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
                     select_mode='extended', key='node102ports', size=(30, 6))],
        [sg.Text('Choose Your Node 103 Ports')],
        [psg.Listbox(values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                             17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                             39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
                     select_mode='extended', key='node103ports', size=(30, 6))],
        [sg.Text('Choose Your Node 104 Ports')],
        [psg.Listbox(values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                             17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                             39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
                     select_mode='extended', key='node104ports', size=(30, 6))],
        [sg.Text('Choose Your Existing EPGs')],
        [psg.Listbox(values=[28, 64, 65, 66, 67, 68, 69, 76, 77, 80, 90, 91, 97, 98, 99, 100, 103, 106, 107, 108, 109,
                             110, 111, 112, 113, 114, 116, 118, 119, 130, 121, 125, 126, 127, 128, 129, 194, 225,
                             226, 227, 228, 292, 305, 332, 364, 365, 921, 922, 923, 924, 1250],
                     select_mode='extended', key='existingepg', size=(30, 6))],
        [sg.Text('Enter any EPGs not listed above seperated by commas', size=(40, 1)),
         sg.InputText(key='newepg')],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Select Nodes and Interfaces and EPGs', layout, size=(600, 900))
    event, values = window.read()
    window.close()
    l101interfaces = values['node101ports']
    l102interfaces = values['node102ports']
    l103interfaces = values['node103ports']
    l104interfaces = values['node104ports']
    existingepgs = values['existingepg']
    newepg = values['newepg']
    return l101interfaces, l102interfaces, l103interfaces, l104interfaces, existingepgs, newepg

def AddVpc101to102():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('VPC Name ex. Netapp_NAC01-1', size=(25, 1)), sg.InputText(key='vpcname')],
        [sg.Text('Choose Your Node 101-102 From Ports')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                             '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31',
                             '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',
                             '47', '48'],
                     default_value='', key='node101-102fromports')],
        [sg.Text('Choose Your Node 101-102 To Ports')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                             '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31',
                             '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',
                             '47', '48'],
                     default_value='', key='node101-102toports')],
        [sg.Text('Choose Your EPGs')],
        [psg.Listbox(values=[28, 64, 65, 66, 67, 68, 69, 76, 77, 80, 90, 91, 97, 98, 99, 100, 103, 106, 107, 108, 109,
                             110, 111, 112, 113, 114, 116, 118, 119, 130, 121, 125, 126, 127, 128, 129, 194, 225,
                             226, 227, 228, 292, 305, 332, 364, 365, 921, 922, 923, 924, 1250],
                     select_mode='extended', key='epg', size=(30, 6))],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Add VPC to Leafs 101-102', layout, size=(600, 600))
    event, values = window.read()
    window.close()
    vpcName = values['vpcname']
    portFrom = values['node101-102fromports']
    portTo = values['node101-102toports']
    epgs = values['epg']
    return vpcName, portFrom, portTo, epgs

def AddVpc103to104():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('VPC Name ex. Netapp_NAC01-1', size=(25, 1)), sg.InputText(key='vpcname')],
        [sg.Text('Choose Your Node 103-104 From Ports')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                             '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31',
                             '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',
                             '47', '48'],
                     default_value='', key='node103-104fromports')],
        [sg.Text('Choose Your Node 103-104 To Ports')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                             '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31',
                             '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',
                             '47', '48'],
                     default_value='', key='node103-104toports')],
        [sg.Text('Choose Your EPGs')],
        [psg.Listbox(values=[28, 64, 65, 66, 67, 68, 69, 76, 77, 80, 90, 91, 97, 98, 99, 100, 103, 106, 107, 108, 109,
                             110, 111, 112, 113, 114, 116, 118, 119, 130, 121, 125, 126, 127, 128, 129, 194, 225,
                             226, 227, 228, 292, 305, 332, 364, 365, 921, 922, 923, 924, 1250],
                     select_mode='extended', key='epg', size=(30, 6))],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Add VPC to Leafs 103-104', layout, size=(600, 600))
    event, values = window.read()
    window.close()
    vpcName = values['vpcname']
    portFrom = values['node103-104fromports']
    portTo = values['node103-104toports']
    epgs = values['epg']
    return vpcName, portFrom, portTo, epgs

def bulkAddVlanL2BdEpg():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Enter the VLAN/L2BD/EPG Numbers seperated by a comma', size=(45, 1)), sg.InputText(key='bd')],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Add VLAN/L2BD/EPG', layout, size=(700, 600))
    event, values = window.read()
    window.close()
    bd = values['bd']
    return bd

def AddVpcInterfaceToEpg():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Choose Your NodePair')],
        [psg.Combo(['101-102', '103-104'],
                   default_value='', key='nodepair')],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Add VPC to EPGs', layout, size=(400, 200))
    event, values = window.read()
    window.close()
    nodepair = values['nodepair']
    if nodepair == '101-102':
        sg.theme('SandyBeach')
        layout = [
            [sg.Text('Choose Your Existing VPC')],
            [psg.Combo(['7K_VPC'],
                       default_value='', key='vpcs')],
            [sg.Text('Choose Your Existing EPGs')],
            [psg.Listbox(
                values=[28, 64, 65, 66, 67, 68, 69, 76, 77, 80, 90, 91, 97, 98, 99, 100, 103, 106, 107, 108, 109,
                        110, 111, 112, 113, 114, 116, 118, 119, 130, 121, 125, 126, 127, 128, 129, 194, 225,
                        226, 227, 228, 292, 305, 332, 364, 365, 921, 922, 923, 924, 1250],
                select_mode='extended', key='existingepg', size=(30, 6))],
            [sg.Text('Enter any EPGs not listed above seperated by commas', size=(40, 1)),
             sg.InputText(key='newepg')],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Add VPC to EPGs', layout, size=(600, 600))
        event, values = window.read()
        window.close()
        vpc = values['vpcs']
        existingepgs = values['existingepg']
        newepgs = values['newepg']
    elif nodepair == '103-104':
        sg.theme('SandyBeach')
        layout = [
            [sg.Text('Choose Your Existing VPC')],
            [psg.Combo(['MgmtSwitch'],
                       default_value='', key='vpcs')],
            [sg.Text('Choose Your Existing EPGs')],
            [psg.Listbox(
                values=[28, 64, 65, 66, 67, 68, 69, 76, 77, 80, 90, 91, 97, 98, 99, 100, 103, 106, 107, 108, 109,
                        110, 111, 112, 113, 114, 116, 118, 119, 130, 121, 125, 126, 127, 128, 129, 194, 225,
                        226, 227, 228, 292, 305, 332, 364, 365, 921, 922, 923, 924, 1250],
                select_mode='extended', key='existingepg', size=(30, 6))],
            [sg.Text('Enter any EPGs not listed above seperated by commas', size=(40, 1)),
             sg.InputText(key='newepg')],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Add VPC to EPGs', layout, size=(600, 600))
        event, values = window.read()
        window.close()
        vpc = values['vpcs']
        existingepgs = values['existingepg']
        newepgs = values['newepg']
    return nodepair, vpc, existingepgs, newepgs

def addDescriptionToInterface():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Select Node, Port and enter description')],
        [sg.Text('Choose Your Node')],
        [psg.Combo(['101', '102', '103', '104'],
                   default_value='', key='node')],
        [sg.Text('Choose Your Port')],
        [psg.Combo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
                   default_value='', key='port')],
        [sg.Text('Description', size=(10, 1)), sg.InputText(key='description')],
        [psg.Checkbox('Repeat', key='repeat')],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Add description to interface', layout, size=(400, 400))
    event, values = window.read()
    window.close()
    node = values['node']
    port = values['port']
    description = values['description']
    repeat = values['repeat']
    return node, port, description, repeat

def usernamePassword():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Please enter your Username and Password')],
        [sg.Text('Username', size=(10, 1)), sg.InputText(key='username')],
        [sg.Text('Password', size=(10, 1)), sg.InputText(key='password', password_char='*')],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Username and Password', layout, size=(400, 200))
    event, values = window.read()
    window.close()
    username = values['username']
    password = values['password']
    return username, password

def delStaticPortFromEpg():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Select Node, Port and EPG')],
        [sg.Text('Choose Your Node')],
        [psg.Combo(['101', '102', '103', '104'],
                   default_value='', key='node')],
        [sg.Text('Choose Your Ports')],
        [psg.Listbox(values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                             '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
                             '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45',
                             '46', '47', '48'],
                     select_mode='extended', key='port', size=(30, 6))],
        [sg.Text('Choose Your EPG')],
        [psg.Listbox(values=['28', '64', '65', '66', '67', '68', '69', '76', '77', '80', '90', '91', '97', '98', '99', '100',
                    '103', '106', '107', '108', '109', '110', '111', '112', '113', '114', '116', '118', '119', '130',
                    '121', '125', '126', '127', '128', '129', '194', '225', '226', '227', '228', '292', '305', '332',
                    '364', '365', '921', '922', '923', '924', '1250'],
                   select_mode='extended', key='epg', size=(30, 6))],
        [psg.Checkbox('Repeat', key='repeat')],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Delete static port from EPG', layout, size=(400, 500))
    event, values = window.read()
    window.close()
    node = values['node']
    port = values['port']
    epg = values['epg']
    repeat = values['repeat']
    return node, port, epg, repeat

def snapShot():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Description of Snapshot')],
        [sg.Text('Description', size=(10, 1)), sg.InputText(key='description')],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Create a snapshot', layout, size=(400, 200))
    event, values = window.read()
    window.close()
    description = values['description']
    return description

























