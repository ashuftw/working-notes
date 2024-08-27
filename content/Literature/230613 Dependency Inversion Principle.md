   

The DIP principle says that High level modules should not depend on Low level modules that are volatile. Instead they both of them should depend on abstractions. 

### Problem
![[Pasted image 20230613113116.png|300]]
- ML4 is directly dependent on LL8 
- Changes in LL8 have a direct impact on ML4
- ML4 can only work with objects of LL8
- ML4 can‘t be reused without LL8
### Solution
![[Pasted image 20230613114017.png|300]]
- ML4 is now depending on an interface called ML4Server.
- Changes in LL8 won‘t influence the ML4.
- ML4 can be reused.
- ML4 can control any object which implements the interface of ML4Server. 





