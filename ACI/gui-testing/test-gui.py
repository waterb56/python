import AciGuiLayouts as agl



select_script = agl.SelectScript()
variables1 = agl.usernamePassword()
username = variables1[0]
password = variables1[1]
# Individual GUI Testing
# if select_script[5] == True:
#     variables = agl.AddVpcInterfaceToEpg()
#     user = variables[0]
#     password = variables[1]
#     nodepair =variables[2]
#     vpc = variables[3]
#     existingepgs = variables[4]
#     newepgsstr = variables[5]
#     newepgslist = newepgsstr.split(sep=',')
#     newepgs = [int(i) for i in newepgslist]
#     print(newepgs)

# All GUI Testing
while select_script != '':
    # Add Interfaces to VM Interface Profile
    if select_script == 'Add Non PC/VPC Interfaces To Switch Profile':
        variables2 = agl.LeafInterfaceSelect()
        username = variables1[0]
        password = variables1[1]
        print(username, password)
    # Add Non VPC Interface to EPGs
    if select_script == 'Add Non-VPC Interfaces to EPG':
        variables = agl.AddNonVpcInterfaceToEpg()
    # Add VPC and EPGs to Nodes 101 and 102
    if select_script == 'Add VPC To Leafs 101-102':
        variables = agl.AddVpc101to102()
    # Add VPC and EPGs to Nodes 103 and 104
    if select_script == 'Add VPC To Leafs 103-104':
        variables = agl.AddVpc103to104()
    # Bulk Add BD/VLAN/EPG to ACI
    if select_script == 'Add L2BD/VLAN/EPG to ACI':
        variables = agl.bulkAddVlanL2BdEpg()
    # Add VPC Interface to EPGs
    if select_script == 'Add VPC to EPGs':
        variables = agl.AddVpcInterfaceToEpg()
    # Add Description to Interface
    if select_script == 'Add description to interface':
        username = variables1[0]
        password = variables1[1]
        repeat = True
        while repeat == True:
            variables2 = agl.addDescriptionToInterface()
            repeat = variables2[3]
    # Delete static port from EPG
    if select_script == 'Delete static port from EPG':
        username = variables1[0]
        password = variables1[1]
        repeat = True
        while repeat == True:
            variables2 = agl.delStaticPortFromEpg()
            repeat = variables2[3]
    # Take a snapshot
    if select_script == 'Create a snapshot':
        variables = agl.snapShot()
        description = variables
        print(description)
    select_script = agl.SelectScript()











