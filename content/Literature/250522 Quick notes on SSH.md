---
title: Quick notes on SSH
draft: false
tags: 
date: 2025-05-22
---
## SSH Basics 

**Q: What is the basic syntax for SSH connection?**  
**A:** `ssh username@hostname`

**Q: What port does SSH use by default?**  
**A:** Port 22

**Q: How to generate an SSH key pair?**  
**A:** `ssh-keygen -b 4096 -t ed25519 -f ~/.ssh/name_of_key`

**Q: How to set up passwordless SSH login?**  
**A:** Generate a key pair, then use `ssh-copy-id -i ~/.ssh/name_of_key.pub username@servername`

## File Transfer with SSH

**Q: How to copy a file to a remote server using SCP?**  
**A:** `scp localfile user@hostname:path/to/directory`

**Q: How to copy a file from a remote server using SCP?**  
**A:** `scp user@hostname:path/to/directory localfile`

**Q: What's the advantage of rsync over scp?**  
**A:** rsync only transfers modified files and preserves file attributes

**Q: How to sync directories with rsync?**  
**A:** `rsync -avz /source/dir/ user@hostname:/dest/dir/`

**Q: How to mount a remote filesystem locally?**  
**A:** `sshfs user@remotehost:/path/dir /local/mounting_point/`