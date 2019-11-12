#!/usr/bin/python

from __future__ import print_function

page_head="""apiVersion: v1
kind: Service
metadata: 
  name: knp-portforwarding
spec: 
  ports:"""

page_bottom="""
  selector: 
    app: nginx
  type: NodePort"""


with open('./knp-generated-service.yaml', 'w+') as output_file:
  output_file.write(page_head)

  for i in range (30000,30002):
    page_mid="""
    -
      nodePort: {0}
      port: {0}
      name: knp{0}""".format(str(i))
    output_file.write(page_mid)
    
  output_file.write(page_bottom)
  output_file.close()
