#!/usr/bin/python
#

# Original script can be found at https://developer.skype.com/wiki/Skype4Py/examples
# To use this script as a one want XMPP transport install and configure sendxmpp, run this script and pipe the
# logfile to sendxmpp
# tail -f /tmp/skype.log | sendxmpp -t yourname@gmail.com

import sys
import Skype4Py

# ----------------------------------------------------------------------------------------------------
# Fired on attachment status change. Here used to re-attach this script to Skype in case attachment is lost. Just in case.
def OnAttach(status):
	print 'API attachment status: ' + skype.Convert.AttachmentStatusToText(status)
	if status == Skype4Py.apiAttachAvailable:
		skype.Attach();

		if status == Skype4Py.apiAttachSuccess:
			print('******************************************************************************');
# opn a file
fileHandle = open ( '/tmp/skype.log', 'a' )
# ----------------------------------------------------------------------------------------------------
# Fired on chat message status change. 
# Statuses can be: 'UNKNOWN' 'SENDING' 'SENT' 'RECEIVED' 'READ'        

def OnMessageStatus(Message, Status):
	if Status == 'RECEIVED':
                fileHandle = open ( '/tmp/skype.log', 'a' )
                fileHandle.write ('\n');
                fileHandle.write (Message.FromDisplayName + ': ' + Message.Body);
                fileHandle.close() 
	#	print(Message.FromDisplayName + ': ' + Message.Body);
	if Status == 'SENT':
                fileHandle = open ( '/tmp/skype.log', 'a' )
                fileHandle.write ('\nMyself: ' + Message.Body);
                fileHandle.close() 
		#print('Myself: ' + Message.Body);


# ----------------------------------------------------------------------------------------------------
# Creating instance of Skype object, assigning handler functions and attaching to Skype.
skype = Skype4Py.Skype();
skype.OnAttachmentStatus = OnAttach;
skype.OnMessageStatus = OnMessageStatus;

print('******************************************************************************');
print 'Connecting to Skype..'
skype.Attach();

# ----------------------------------------------------------------------------------------------------
# Looping until user types 'exit'
Cmd = '';
while not Cmd == 'exit':
        Cmd = raw_input('');

