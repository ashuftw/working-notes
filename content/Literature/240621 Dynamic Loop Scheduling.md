Status: #finished 
## Self Scheduling: 
- An idle processor requests for work. 
- Master processor keeps record of available and assigned work. 

**Execution time**

$$
T_P = \frac{P}{N}(B+\sigma(N))
$$

**Speed up**

$$
S = \frac{T_s }{T_p } = \frac{P B}{P\sigma+\frac{PB}{N}}= \frac{B}{\sigma(N)+B/N}
$$


$$
\lim_{N \to \infty} S = \frac B {\sigma_\infty}
$$

where, 
- $P\rightarrow$ Number of work items to be distributed
- $N\rightarrow$ Available processors
- $B\rightarrow$ Average execution time of a work item
- $\sigma(N)\rightarrow$ Dispatch time of work item  
![[Pasted image 20240626163844.png|center|400]]
*Replace P by N*
> Note:  The dispatch time grows asymptotically with the number of parallel requests i.e. weak scaling

## Chunk Scheduling
The overhead of self-scheduling can be reduced by chunking a fixed number of iterations $k$ together.  Here $k$ is known as the chunk size. 
**Execution Time**


$$
T_P = \frac{N}{k\cdot P}\left(k\cdot B+\sigma\left (P/k\right)\right )
$$

**Speed-up**

$$
\lim _{p \rightarrow \infty} S=\frac{k^2  B}{\sigma_{\infty}}
$$

> Note: Chunk Scheduling is $k^2$ times faster than **self scheduling**. 
## Guided Self Scheduling 
 Here the Chunk size $k$ keeps varying. Usually starts with a larger chunk and gets smaller over time. The chunks are allotted based on available compute (idling processor). This method has better load balancing. 


---
# References
