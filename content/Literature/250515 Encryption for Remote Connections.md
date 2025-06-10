---
title: Encryption for Remote Connections (SSH)
draft: false
tags: 
date:
---

## Symmetric Algorithm

It is a type of encryption where a **single key** or **algorithm** can be use to both encrypt and decrypt a message. 
![[content/Files/Pasted image 20250515152635.png|center|400]]

> **Note:** Both the sender and the receiver have a copy of the **algorithm** or **key**.

## Asymmetric Algorithm

Asymmetric algorithms are used in when no secure channel to share key exists. Both the sender and the receiver have a **personal** and **public key**. 

![[content/Files/Pasted image 20250515153738.png]]

## Q&A

**Q: What are the two main types of encryption algorithms?**  
**A:** Symmetric (same key to encrypt/decrypt) and asymmetric (public/private key pair)

**Q: What encryption does SSH use?**  
**A:** SSH uses both asymmetric encryption for key exchange and authentication, then symmetric encryption for the actual data transfer

**Q: Why is asymmetric encryption important for SSH?**  
**A:** It allows secure communication without having to share a secret key over an insecure channel

