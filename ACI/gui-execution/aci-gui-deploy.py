import AciGuiLayouts as agl
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.infra
import cobra.model.pol
import cobra.model.fv
import cobra.model.fvns
import cobra.model.pol
import myfunctions
import requests
import json
import urllib3

select_script = agl.SelectScript()
variables1 = agl.usernamePassword()
username = variables1[0]
password = variables1[1]
while any(select_script[0::]) == True:
    # Add Interfaces to VM Interface Profile
    if select_script == 'Add Non PC/VPC Interfaces To Switch Profile':
        variables = agl.LeafInterfaceSelect()
        l101FromInterfaces = variables[0]
        l101ToInterfaces = variables[1]
        l102FromInterfaces = variables[2]
        l102ToInterfaces = variables[3]
        l103FromInterfaces = variables[4]
        l103ToInterfaces = variables[5]
        l104FromInterfaces = variables[6]
        l104ToInterfaces = variables[7]

        # log into an APIC and create a directory object
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', username, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        infraInfra = cobra.model.infra.Infra(polUni)
        infraAccPortP = cobra.model.infra.AccPortP(infraInfra, 'Switch101_SwProfile_ifselector')
        infraAccPortP2 = cobra.model.infra.AccPortP(infraInfra, 'Switch102_SwProfile_ifselector')
        infraAccPortP3 = cobra.model.infra.AccPortP(infraInfra, 'Switch103_SwProfile_ifselector')
        infraAccPortP4 = cobra.model.infra.AccPortP(infraInfra, 'Switch104_SwProfile_ifselector')
        if l101FromInterfaces != '':
            # build the request using cobra syntax
            infraHPortS = cobra.model.infra.HPortS(infraAccPortP, annotation='', descr='For non PC/VPC interfaces',
                                                   name='Leaf_101_VM_Interfaces', nameAlias='', ownerKey='',
                                                   ownerTag='', type='range')
            infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation='', fexId='101',
                                                               tDn='uni/infra/funcprof/accportgrp-CDP_LLDP_Enable')
            infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation='', descr='', fromCard='1',
                                                     fromPort=l101FromInterfaces, name=F'block{l101FromInterfaces}',
                                                     nameAlias='', toCard='1', toPort=l101ToInterfaces)
        else:
            pass

        if l102FromInterfaces != '':
            # build the request using cobra syntax
            infraHPortS = cobra.model.infra.HPortS(infraAccPortP2, annotation='', descr='For non PC/VPC interfaces',
                                                   name='Leaf_102_VM_Interfaces', nameAlias='', ownerKey='',
                                                   ownerTag='', type='range')
            infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation='', fexId='101',
                                                               tDn='uni/infra/funcprof/accportgrp-CDP_LLDP_Enable')
            infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation='', descr='', fromCard='1',
                                                     fromPort=l102FromInterfaces, name=F'block{l102FromInterfaces}',
                                                     nameAlias='', toCard='1', toPort=l102ToInterfaces)
        else:
            pass

        if l103FromInterfaces != '':
            # build the request using cobra syntax
            infraHPortS = cobra.model.infra.HPortS(infraAccPortP3, annotation='', descr='For non PC/VPC interfaces',
                                                   name='Leaf_103_VM_Interfaces',nameAlias='', ownerKey='',
                                                   ownerTag='', type='range')
            infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation='', fexId='101',
                                                               tDn='uni/infra/funcprof/accportgrp-CDP_LLDP_Enable')
            infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation='', descr='', fromCard='1',
                                                     fromPort=l103FromInterfaces, name=F'block{l103FromInterfaces}',
                                                     nameAlias='', toCard='1', toPort=l103ToInterfaces)
        else:
            pass

        if l104FromInterfaces != '':
            # build the request using cobra syntax
            infraHPortS = cobra.model.infra.HPortS(infraAccPortP4, annotation='', descr='For non PC/VPC interfaces',
                                                   name='Leaf_104_VM_Interfaces', nameAlias='', ownerKey='',
                                                   ownerTag='', type='range')
            infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation='', fexId='101',
                                                               tDn='uni/infra/funcprof/accportgrp-CDP_LLDP_Enable')
            infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation='', descr='', fromCard='1',
                                                     fromPort=l104FromInterfaces, name=F'block{l104FromInterfaces}',
                                                     nameAlias='', toCard='1', toPort=l104ToInterfaces)
        else:
            pass


        # commit the generated code to APIC
        c = cobra.mit.request.ConfigRequest()
        c.addMo(infraAccPortP)
        md.commit(c)

        c = cobra.mit.request.ConfigRequest()
        c.addMo(infraAccPortP2)
        md.commit(c)

        c = cobra.mit.request.ConfigRequest()
        c.addMo(infraAccPortP3)
        md.commit(c)

        c = cobra.mit.request.ConfigRequest()
        c.addMo(infraAccPortP4)
        md.commit(c)

    # Add Non VPC Interface to EPGs
    if select_script == 'Add Non-VPC Interfaces to EPG':
        variables = agl.AddNonVpcInterfaceToEpg()
        username = variables1[0]
        password = variables1[1]
        l101interfaces = variables[0]
        l102interfaces = variables[1]
        l103interfaces = variables[2]
        l104interfaces = variables[3]
        epgs = variables[4]
        newepgsstr = variables[5]
        newepgslist = newepgsstr.split(sep=',')
        if newepgslist[0] == '':
            newepgs = []
        else:
            newepgs = [int(i) for i in newepgslist]
        # log into an APIC and create a directory object
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', username, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        fvTenant = cobra.model.fv.Tenant(polUni, 'Bobby_Tenant')
        fvAp = cobra.model.fv.Ap(fvTenant, 'Bobby_Tenant_AP')

        # build the request using cobra syntax
        if len(epgs) > 0:
            for epg in epgs:
                fvAEPg = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled',
                                             fwdCtrl='', hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne',
                                             name=f'VLAN{epg}_EPG', nameAlias='', pcEnfPref='unenforced',
                                             prefGrMemb='exclude', prio='unspecified', shutdown='no')
                if len(l101interfaces) > 0:
                    for int in l101interfaces:
                        fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                               instrImedcy='immediate', mode='regular', primaryEncap='unknown',
                                                               tDn=f'topology/pod-1/paths-101/pathep-[eth1/{int}]')
                else:
                    pass
                if len(l102interfaces) > 0:
                    for int in l102interfaces:
                        fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                               instrImedcy='immediate', mode='regular', primaryEncap='unknown',
                                                               tDn=f'topology/pod-1/paths-102/pathep-[eth1/{int}]')
                else:
                    pass
                if len(l103interfaces) > 0:
                    for int in l103interfaces:
                        fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                               instrImedcy='immediate', mode='regular', primaryEncap='unknown',
                                                               tDn=f'topology/pod-1/paths-103/pathep-[eth1/{int}]')
                else:
                    pass
                if len(l104interfaces) > 0:
                    for int in l104interfaces:
                        fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                               instrImedcy='immediate', mode='regular', primaryEncap='unknown',
                                                               tDn=f'topology/pod-1/paths-104/pathep-[eth1/{int}]')
                else:
                    pass

            # commit the generated code to APIC
            c = cobra.mit.request.ConfigRequest()
            c.addMo(fvAp)
            md.commit(c)
        if len(newepgs) > 0:
            for epg in newepgs:
                fvAEPg = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled',
                                             fwdCtrl='', hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne',
                                             name=f'VLAN{epg}_EPG', nameAlias='', pcEnfPref='unenforced',
                                             prefGrMemb='exclude', prio='unspecified', shutdown='no')
                if len(l101interfaces) > 0:
                    for int in l101interfaces:
                        fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                               instrImedcy='immediate', mode='regular',
                                                               primaryEncap='unknown',
                                                               tDn=f'topology/pod-1/paths-101/pathep-[eth1/{int}]')
                else:
                    pass
                if len(l102interfaces) > 0:
                    for int in l102interfaces:
                        fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                               instrImedcy='immediate', mode='regular',
                                                               primaryEncap='unknown',
                                                               tDn=f'topology/pod-1/paths-102/pathep-[eth1/{int}]')
                else:
                    pass
                if len(l103interfaces) > 0:
                    for int in l103interfaces:
                        fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                               instrImedcy='immediate', mode='regular',
                                                               primaryEncap='unknown',
                                                               tDn=f'topology/pod-1/paths-103/pathep-[eth1/{int}]')
                else:
                    pass
                if len(l104interfaces) > 0:
                    for int in l104interfaces:
                        fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                               instrImedcy='immediate', mode='regular',
                                                               primaryEncap='unknown',
                                                               tDn=f'topology/pod-1/paths-104/pathep-[eth1/{int}]')
                else:
                    pass

            # commit the generated code to APIC
            c = cobra.mit.request.ConfigRequest()
            c.addMo(fvAp)
            md.commit(c)

    # Add VPC and EPGs to Nodes 101 and 102
    if select_script == 'Add VPC To Leafs 101-102':
        variables = agl.AddVpc101to102()
        user = variables1[0]
        password = variables1[1]
        vpcName = variables[0]
        portFrom = variables[1]
        portTo = variables[2]
        epgs = variables[3]
        # Step 1 Add VPC Policy Group
        # log into an APIC and create a directory object
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        infraInfra = cobra.model.infra.Infra(polUni)
        infraFuncP = cobra.model.infra.FuncP(infraInfra)

        # build the request using cobra syntax
        infraAccBndlGrp = cobra.model.infra.AccBndlGrp(infraFuncP, annotation='', descr='', lagT='node',
                                                       name=f'{vpcName}_VPC_PolGrp', nameAlias='', ownerKey='',
                                                       ownerTag='')
        infraRsLacpPol = cobra.model.infra.RsLacpPol(infraAccBndlGrp, annotation='', tnLacpLagPolName='LACP_Active')
        infraRsNetflowMonitorPol = cobra.model.infra.RsNetflowMonitorPol(infraAccBndlGrp, annotation='', fltType='ipv4',
                                                                         tnNetflowMonitorPolName='netflow-monitor')
        infraRsLldpIfPol = cobra.model.infra.RsLldpIfPol(infraAccBndlGrp, annotation='', tnLldpIfPolName='LLDP_Enable')
        infraRsCdpIfPol = cobra.model.infra.RsCdpIfPol(infraAccBndlGrp, annotation='', tnCdpIfPolName='CDP_Enable')
        infraRsAttEntP = cobra.model.infra.RsAttEntP(infraAccBndlGrp, annotation='',
                                                     tDn='uni/infra/attentp-Bobby_Tenant_AAEP')

        # commit the generated code to APIC
        myfunctions.NiceOutput('Deploying VPC Policy Group')
        c = cobra.mit.request.ConfigRequest()
        c.addMo(infraFuncP)
        md.commit(c)

        # Step 2 Add Acces Port Selector to Leaf Interface Profile Lf101_102_IntProf
        # log into an APIC and create a directory object

        # log into an APIC and create a directory object
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        infraInfra = cobra.model.infra.Infra(polUni)
        infraAccPortP = cobra.model.infra.AccPortP(infraInfra, 'Lf101-102_IntProf')

        # build the request using cobra syntax
        infraHPortS = cobra.model.infra.HPortS(infraAccPortP, annotation='', descr='', name=f'VPC_To_{vpcName}',
                                               nameAlias='',
                                               ownerKey='', ownerTag='', type='range')
        infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation='', fexId='101',
                                                           tDn=F'uni/infra/funcprof/accbundle-{vpcName}_VPC_PolGrp')
        infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation='', descr='', fromCard='1', fromPort=portFrom,
                                                 name='block2', nameAlias='', toCard='1', toPort=portTo)

        myfunctions.NiceOutput(f'Adding interfaces {portFrom} to {portTo} to VPC {vpcName} on Leafs 101 and 102')
        # commit the generated code to APIC
        c = cobra.mit.request.ConfigRequest()
        c.addMo(infraAccPortP)
        md.commit(c)

        # Add EPGs tp VPC
        # log into an APIC and create a directory object
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        fvTenant = cobra.model.fv.Tenant(polUni, 'Bobby_Tenant')
        fvAp = cobra.model.fv.Ap(fvTenant, 'Bobby_Tenant_AP')

        # build the request using cobra syntax
        for epg in epgs:
            fvAEPg = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled',
                                         fwdCtrl='', hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne',
                                         name=f'VLAN{epg}_EPG', nameAlias='', pcEnfPref='unenforced',
                                         prefGrMemb='exclude', prio='unspecified', shutdown='no')
            fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                   instrImedcy='immediate', mode='regular', primaryEncap='unknown',
                                                   tDn=f'topology/pod-1/protpaths-101-102/pathep-[{vpcName}_VPC_PolGrp]')

        # commit the generated code to APIC
        c = cobra.mit.request.ConfigRequest()
        c.addMo(fvAp)
        md.commit(c)

    # Add VPC and EPGs to Nodes 103 and 104
    if select_script == 'Add VPC To Leafs 103-104':
        variables = agl.AddVpc103to104()
        user = variables1[0]
        password = variables1[1]
        vpcName = variables[0]
        portFrom = variables[1]
        portTo = variables[2]
        epgs = variables[3]
        # Step 1 Add VPC Policy Group
        # log into an APIC and create a directory object
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        infraInfra = cobra.model.infra.Infra(polUni)
        infraFuncP = cobra.model.infra.FuncP(infraInfra)

        # build the request using cobra syntax
        infraAccBndlGrp = cobra.model.infra.AccBndlGrp(infraFuncP, annotation='', descr='', lagT='node',
                                                       name=f'{vpcName}_VPC_PolGrp', nameAlias='', ownerKey='',
                                                       ownerTag='')
        infraRsLacpPol = cobra.model.infra.RsLacpPol(infraAccBndlGrp, annotation='', tnLacpLagPolName='LACP_Active')
        infraRsNetflowMonitorPol = cobra.model.infra.RsNetflowMonitorPol(infraAccBndlGrp, annotation='', fltType='ipv4',
                                                                         tnNetflowMonitorPolName='netflow-monitor')
        infraRsLldpIfPol = cobra.model.infra.RsLldpIfPol(infraAccBndlGrp, annotation='', tnLldpIfPolName='LLDP_Enable')
        infraRsCdpIfPol = cobra.model.infra.RsCdpIfPol(infraAccBndlGrp, annotation='', tnCdpIfPolName='CDP_Enable')
        infraRsAttEntP = cobra.model.infra.RsAttEntP(infraAccBndlGrp, annotation='',
                                                     tDn='uni/infra/attentp-Bobby_Tenant_AAEP')

        # commit the generated code to APIC
        myfunctions.NiceOutput('Deploying VPC Policy Group')
        c = cobra.mit.request.ConfigRequest()
        c.addMo(infraFuncP)
        md.commit(c)

        # Step 2 Add Acces Port Selector to Leaf Interface Profile Lf103_104_IntProf
        # log into an APIC and create a directory object
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        infraInfra = cobra.model.infra.Infra(polUni)
        infraAccPortP = cobra.model.infra.AccPortP(infraInfra, 'Lf103_104_IntProf')

        # build the request using cobra syntax
        infraHPortS = cobra.model.infra.HPortS(infraAccPortP, annotation='', descr='',
                                               name=f'VPC_To_{vpcName}', nameAlias='', ownerKey='', ownerTag='',
                                               type='range')
        infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation='',
                                                           fexId='101',
                                                           tDn=f'uni/infra/funcprof/accbundle-{vpcName}_VPC_PolGrp')
        infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation='', descr='', fromCard='1', fromPort=portFrom,
                                                 name=f'block{portFrom}', nameAlias='', toCard='1', toPort=portTo)

        # commit the generated code to APIC
        myfunctions.NiceOutput(f'Adding interfaces {portFrom} to {portTo} to VPC {vpcName} on Leafs 103 and 104')
        c = cobra.mit.request.ConfigRequest()
        c.addMo(infraAccPortP)
        md.commit(c)
        # log into an APIC and create a directory object
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        fvTenant = cobra.model.fv.Tenant(polUni, 'Bobby_Tenant')
        fvAp = cobra.model.fv.Ap(fvTenant, 'Bobby_Tenant_AP')

        # build the request using cobra syntax
        for epg in epgs:
            fvAEPg = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled',
                                         fwdCtrl='', hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne',
                                         name=f'VLAN{epg}_EPG', nameAlias='', pcEnfPref='unenforced',
                                         prefGrMemb='exclude', prio='unspecified', shutdown='no')
            fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                   instrImedcy='immediate', mode='regular', primaryEncap='unknown',
                                                   tDn=f'topology/pod-1/protpaths-103-104/pathep-[{vpcName}_VPC_PolGrp]')

        # commit the generated code to APIC
        c = cobra.mit.request.ConfigRequest()
        c.addMo(fvAp)
        md.commit(c)

    # Bulk Add L2BD/VLAN/EPG to ACI
    if select_script == 'Add L2BD/VLAN/EPG to ACI':
        variables = agl.bulkAddVlanL2BdEpg()
        user = variables1[0]
        password = variables1[1]
        bdstring = variables
        bdliststr = bdstring.split(sep=',')
        vlanEpgBdNumber = [int(i) for i in bdliststr]
        print(f'You are adding {vlanEpgBdNumber} VLANs to ACI')
        for item in vlanEpgBdNumber:
            print(f'You are deploying EPG VLAN{item}_EPG and BD VLAN{item}_BD')
        proceed = input('If you want to proceed press enter if you want to stop pres ctrl-C')
        # Step 1. Deploy VLANS to Bobby_Tenant_DC_VLPool
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        infraInfra = cobra.model.infra.Infra(polUni)

        # build the request using cobra syntax
        myfunctions.NiceOutput('Deploying VLANS to Bobby_Tenant_DC_VLPool')
        fvnsVlanInstP = cobra.model.fvns.VlanInstP(infraInfra, allocMode='static', annotation='', descr='',
                                                   name='Bobby_Tenant_DC_VLPool', nameAlias='', ownerKey='', ownerTag='')
        for vlan in vlanEpgBdNumber:
            fvnsEncapBlk = cobra.model.fvns.EncapBlk(fvnsVlanInstP, allocMode='static', annotation='', descr='',
                                                     from_=f'vlan-{vlan}', name='', nameAlias='', role='external',
                                                     to=f'vlan-{vlan}')

        # commit the generated code to APIC
        c = cobra.mit.request.ConfigRequest()
        c.addMo(infraInfra)
        md.commit(c)
        myfunctions.NiceOutput('Completed deploying VLANS to Bobby_Tenant_DC_VLPool')

        # Step 2. Deploy BDs
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        fvTenant = cobra.model.fv.Tenant(polUni, 'Bobby_Tenant')

        # build the request using cobra syntax
        myfunctions.NiceOutput('Deploying the BDs to the Non_DMZ vrf in the Bobby_Tenant tenant')
        for bd in vlanEpgBdNumber:
            fvBD = cobra.model.fv.BD(fvTenant, OptimizeWanBandwidth='no', annotation='', arpFlood='yes', descr='',
                                     epClear='no',
                                     epMoveDetectMode='garp', hostBasedRouting='no', intersiteBumTrafficAllow='no',
                                     intersiteL2Stretch='no', ipLearning='yes', ipv6McastAllow='no',
                                     limitIpLearnToSubnets='yes',
                                     llAddr='::', mac='00:22:BD:F8:19:FF', mcastAllow='no', multiDstPktAct='bd-flood',
                                     name=f'VLAN{bd}_BD', nameAlias='', ownerKey='', ownerTag='', type='regular',
                                     unicastRoute='no',
                                     unkMacUcastAct='proxy', unkMcastAct='flood', v6unkMcastAct='flood',
                                     vmac='not-applicable')
            fvRsMldsn = cobra.model.fv.RsMldsn(fvBD, annotation='', tnMldSnoopPolName='')
            fvRsIgmpsn = cobra.model.fv.RsIgmpsn(fvBD, annotation='', tnIgmpSnoopPolName='')
            fvRsCtx = cobra.model.fv.RsCtx(fvBD, annotation='', tnFvCtxName='Non_DMZ')
            fvRsBdToEpRet = cobra.model.fv.RsBdToEpRet(fvBD, annotation='', resolveAct='resolve', tnFvEpRetPolName='')
            fvRsBDToNdP = cobra.model.fv.RsBDToNdP(fvBD, annotation='', tnNdIfPolName='')

        # commit the generated code to APIC
        c = cobra.mit.request.ConfigRequest()
        c.addMo(fvTenant)
        md.commit(c)
        myfunctions.NiceOutput('Completed deploying the BDs to the Non_DMZ vrf in the Bobby_Tenant tenant')

        # Step 3. Deploy EPGs
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        fvTenant = cobra.model.fv.Tenant(polUni, 'Bobby_Tenant')
        fvAp = cobra.model.fv.Ap(fvTenant, 'Bobby_Tenant_AP')

        # build the request using cobra syntax
        myfunctions.NiceOutput('Deploying the EPGss to the Bobby_Tenant_AP application profile')
        for epg in vlanEpgBdNumber:
            fvAEPg = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled',
                                         fwdCtrl='',
                                         hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne',
                                         name=f'VLAN{epg}_EPG',
                                         nameAlias='', pcEnfPref='unenforced', prefGrMemb='exclude', prio='unspecified',
                                         shutdown='no')
            vRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, annotation='', tnQosCustomPolName='')
            fvRsBd = cobra.model.fv.RsBd(fvAEPg, annotation='', tnFvBDName=f'VLAN{epg}_BD')

        # commit the generated code to APIC
        c = cobra.mit.request.ConfigRequest()
        c.addMo(fvAp)
        md.commit(c)
        myfunctions.NiceOutput('Completed deploying the EPGss to the Bobby_Tenant_AP application profile')

    # VPC to EPGs
    if select_script == 'Add VPC to EPGs':
        variables = agl.AddVpcInterfaceToEpg()
        user = variables1[0]
        password = variables1[1]
        nodepair =variables[0]
        vpc = variables[1]
        existingepgs = variables[2]
        newepgsstr = variables[3]
        newepgslist = newepgsstr.split(sep=',')
        if newepgslist[0] == '':
            newepgs = []
        else:
            newepgs = [int(i) for i in newepgslist]
        # log into an APIC and create a directory object
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', user, password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()

        # the top level object on which operations will be made
        polUni = cobra.model.pol.Uni('')
        fvTenant = cobra.model.fv.Tenant(polUni, 'Bobby_Tenant')
        fvAp = cobra.model.fv.Ap(fvTenant, 'Bobby_Tenant_AP')

        # build the request using cobra syntax
        if len(existingepgs) > 0:
            for epg in existingepgs:
                fvAEPg = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled',
                                             fwdCtrl='', hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne',
                                             name=f'VLAN{epg}_EPG', nameAlias='', pcEnfPref='unenforced',
                                             prefGrMemb='exclude', prio='unspecified', shutdown='no')
                fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                       instrImedcy='immediate', mode='regular', primaryEncap='unknown',
                                                       tDn=f'topology/pod-1/protpaths-{nodepair}/pathep-[{vpc}_VPC_PolGrp]')

            # commit the generated code to APIC
            c = cobra.mit.request.ConfigRequest()
            c.addMo(fvAp)
            md.commit(c)
        if len(newepgs) > 0:
            for epg in newepgs:
                fvAEPg = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled',
                                             fwdCtrl='', hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne',
                                             name=f'VLAN{epg}_EPG', nameAlias='', pcEnfPref='unenforced',
                                             prefGrMemb='exclude', prio='unspecified', shutdown='no')
                fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, annotation='', descr='', encap=f'vlan-{epg}',
                                                       instrImedcy='immediate', mode='regular', primaryEncap='unknown',
                                                       tDn=f'topology/pod-1/protpaths-{nodepair}/pathep-[{vpc}_VPC_PolGrp]')

            # commit the generated code to APIC
            c = cobra.mit.request.ConfigRequest()
            c.addMo(fvAp)
            md.commit(c)

    # Update Description on Interface
    if select_script == 'Add description to interface':
        repeat = True
        while repeat == True:
            variables2 = agl.addDescriptionToInterface()
            username = variables1[0]
            password = variables1[1]
            node = variables2[0]
            port = variables2[1]
            description = variables2[2]
            repeat = variables2[3]
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            # log into an APIC and create a directory object
            ls = cobra.mit.session.LoginSession('https://sandboxapicdc.cisco.com/', username, password)
            md = cobra.mit.access.MoDirectory(ls)
            md.login()

            # the top level object on which operations will be made
            polUni = cobra.model.pol.Uni('')
            infraInfra = cobra.model.infra.Infra(polUni)

            # build the request using cobra syntax
            infraHPathS = cobra.model.infra.HPathS(infraInfra, annotation='', descr=description, name=f'{node}_eth1_{port}',
                                                   nameAlias='', ownerKey='', ownerTag='')
            infraRsHPathAtt = cobra.model.infra.RsHPathAtt(infraHPathS, annotation='',
                                                           tDn=f'topology/pod-1/paths-{node}/pathep-[eth1/{port}]')

            # commit the generated code to APIC
            c = cobra.mit.request.ConfigRequest()
            c.addMo(infraInfra)
            md.commit(c)

    # Delete static port from EPG
    if select_script == 'Delete static port from EPG':
        repeat = True
        while repeat == True:
            variables2 = agl.delStaticPortFromEpg()
            username = variables1[0]
            password = variables1[1]
            node = variables2[0]
            ports = variables2[1]
            epgs = variables2[2]
            repeat = variables2[3]
            for epg in epgs:
                for port in ports:
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    url = "https://sandboxapicdc.cisco.com//api/aaaLogin.json"
                    payloadDict = {
                        "aaaUser": {
                            "attributes": {
                                "name": username,
                                "pwd": password
                            }
                        }
                    }
                    payloadJson = json.dumps(payloadDict)
                    header = {
                        'Content-Type': 'application/json',
                    }
                    token = requests.post(url, verify=False, data=payloadJson, headers=header, auth=(username, password))
                    tokenJson = token.json()
                    imdata = tokenJson['imdata']
                    imdataDict = imdata[0]
                    aaaLogin = imdataDict['aaaLogin']
                    attribute = aaaLogin['attributes']
                    token = attribute['token']
                    payload = "{\"fvRsPathAtt\":{\"attributes\":{\"dn\":\"uni/tn-Bobby_Tenant/ap-Bobby_Tenant_AP/epg-VLAN" + epg + "_EPG/rspathAtt-[topology/pod-1/paths-" + node + "/pathep-[eth1/" + port + "]]\",\"status\":\"deleted\"},\"children\":[]}}"
                    url = f"https://sandboxapicdc.cisco.com//api/node/mo/uni/tn-Bobby_Tenant/ap-Bobby_Tenant_AP/epg-VLAN{epg}_EPG/rspathAtt-[topology/pod-1/paths-{node}/pathep-[eth1/{port}]].json"
                    header = {
                        'Cookie': f'APIC-cookie={token}',
                        'Authorization': 'Bearer' + ' ' + token
                    }
                    request = requests.post(url, headers=header, data=payload, verify=False)
                    response = request.status_code
                    print(response)

    # Create Snapshot
    if select_script == 'Create a snapshot':
        variables2 = agl.snapShot()
        username = variables1[0]
        password = variables1[1]
        description = variables2
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        url = "https://sandboxapicdc.cisco.com//api/aaaLogin.json"
        payloadDict = {
            "aaaUser": {
                "attributes": {
                    "name": username,
                    "pwd": password
                }
            }
        }
        payloadJson = json.dumps(payloadDict)
        header = {
            'Content-Type': 'application/json',
        }
        token = requests.post(url, verify=False, data=payloadJson, headers=header, auth=(username, password))
        tokenJson = token.json()
        imdata = tokenJson['imdata']
        imdataDict = imdata[0]
        aaaLogin = imdataDict['aaaLogin']
        attribute = aaaLogin['attributes']
        token = attribute['token']
        payload = payload = "{\"configExportP\":{\"attributes\":{\"dn\":\"uni/fabric/configexp-defaultOneTime\",\"name\":\"defaultOneTime\",\"snapshot\":\"true\",\"targetDn\":\"\",\"adminSt\":\"triggered\",\"rn\":\"configexp-defaultOneTime\",\"status\":\"created,modified\",\"descr\":\"" + description + "\"},\"children\":[]}}"
        url = "https://sandboxapicdc.cisco.com//api/node/mo/uni/fabric/configexp-defaultOneTime.json"
        header = {
            'Cookie': f'APIC-cookie={token}',
            'Authorization': 'Bearer' + ' ' + token
        }
        request = requests.post(url, headers=header, data=payload, verify=False)
        response = request.status_code
        print(response)
    select_script = agl.SelectScript()
