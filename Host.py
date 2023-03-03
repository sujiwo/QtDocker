'''
Created on 21 Feb 2023

@author: sujiwo
'''

import docker
import subprocess
import re
from xml.dom.minidom import parseString
import json


nvidia_smi_re = '^GPU ([0-9]+): ([\-\s\w]+) \(UUID: ([\-0-9A-Za-z]+)\)'


class Host(docker.DockerClient):
    '''
    classdocs
    '''

    def __init__(self, url):
        docker.DockerClient.__init__(self, base_url=url)
        if (url.startswith('ssh')):
            self.remote = True
            self.ssh_client = self.api._custom_adapter.ssh_client
        else: self.remote = False
        self.lastInfo = self.info()
        x = self.hasGpu()
        pass
    
    def hasNvidiaContainerSupport(self):
        pass
    
    # Parse more complete XML output from nvidia-smi
    # XXX: Unfinished
    def hasGpu(self):
        self.gpuList = []
        try:
            if self.remote==False:
                cmdoutput = subprocess.run(['nvidia-smi', '-q', '-x'], capture_output=True)
            else:
                stdin, stdout, stderr = self.ssh_client.exec_command('nvidia-smi -q -x')
                cmdoutput = stdout.read().decode('utf-8')
            gpudom = parseString(cmdoutput)
            i = 0
            for g in gpudom.getElementsByTagName('gpu'):
                uuid = g.getElementsByTagName('uuid')[0].childNodes[0].data.strip()
                name = g.getElementsByTagName('product_name')[0].childNodes[0].data.strip()
                ram = g.getElementsByTagName('fb_memory_usage')[0].getElementsByTagName('total')[0].childNodes[0].data.strip()
                b_has_mig = g.getElementsByTagName('current_mig')[0].childNodes[0].data.strip()
                if b_has_mig=='N/A':
                    has_mig = False
                    mig_status = 'N/A'
                elif b_has_mig=='Disabled' or b_has_mig=='Enabled':
                    has_mig = True
                    mig_status = b_has_mig
                self.gpuList.append({
                        'id':i,
                        'name':name,
                        'uuid':uuid,
                        'ram':ram,
                        'has_mig':has_mig,
                        'mig_status':mig_status
                    })
                i += 1
            return True
        except:
            return False
            
    
    # XXX: Need to fix
    def getContainerList(self):
        containerList = []
        if self.remote==True:
            stdin, stdout, stderr = self.ssh_client.exec_command('docker container ls -a --format \'{{json .}}\'')
            ctnlines = stdout.readlines()
        else:
            cmdoutput = subprocess.run(['docker', 'container', 'ls', '-a', '--format', '{{json .}}'], capture_output=True)
            ctnlines = cmdoutput.stdout.decode('utf-8').strip().splitlines()
        for l in ctnlines:
            ctn = json.loads(l)
            ctn['Name'] = ctn['Names']
            containerList.append(ctn)
        return containerList
    
    def getImageList(self):
        imageList = []
        if self.remote==True:
            stdin, stdout, stderr = self.ssh_client.exec_command('docker image ls --format \'{{json .}}\'')
            imglines = stdout.readlines()
        else:
            cmdoutput = subprocess.run(['docker', 'image', 'ls', '--format', '{{json .}}'], capture_output=True)
            imglines = cmdoutput.stdout.decode('utf-8').strip().splitlines()
        for l in imglines:
            img = json.loads(l)
            img['Name'] = img['Repository']+':'+img['Tag']
            imageList.append(img)
        return imageList

        