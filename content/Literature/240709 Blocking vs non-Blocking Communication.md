Status: #finished 

## Blocking Communication 
Here the rest of the code does not get executed until the the communication process is completed. 
Ex: **MPI_Send, MPI_Receive**
- Don't have to worry about synchronisation. 
- Less efficient
## non-Blocking Communication 
Here the rest of the code gets executed as the communication process is completes in the background. 
Ex: **MPI_Isend, MPI_Ireceive**
- Need additional functions like **MPI_Wait()** in order to ensure synchronization. 
- Efficient use of computational resources. 
```c
MPI_Request send_request, recv_request;

// Non-Blocking Send
MPI_Isend(send_buffer, count, MPI_INT, dest, tag, MPI_COMM_WORLD, &send_request);
// Code execution continues immediately

// Non-Blocking Receive
MPI_Irecv(recv_buffer, count, MPI_INT, source, tag, MPI_COMM_WORLD, &recv_request);
// Code execution continues immediately

// Perform other useful work here while send/receive operations are in progress

// Ensure send and receive are complete before accessing the buffers
MPI_Wait(&send_request, MPI_STATUS_IGNORE);
MPI_Wait(&recv_request, MPI_STATUS_IGNORE);
```



