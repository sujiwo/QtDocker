'''
Created on 21 Feb 2023

@author: sujiwo
'''

import docker
import subprocess
import re
from xml.dom.minidom import parseString


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
                        'gpuid':i,
                        'gpuname':name,
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
        return self.containers.list(all=True, sparse=True)
    
    def getImageList(self):
        return self.images.list()
    

        