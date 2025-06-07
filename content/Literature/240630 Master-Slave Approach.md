---
title: Master-Slave Approach
draft: false
date: 2024-06-30
---

## Intuition

![[Pasted image 20240628151022.png|center|600]]
## Example
### Serial
```cpp
# include <header.h>

int main(int argc, char **argv)
{
    int number_of_processes = 1;

    <variable definitions>
    <variable definitions>

    local_integral = <customFunction(local a, local b)>

    // send / receive

    result += local_integral;

    return 0;
}
```
### Parallel
```cpp
#include <header.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv); // MPI_Init( int *argc, char ***argv )
    int number_of_processes = 1;
    int my_rank = 0;
    int tag = 0; 
    <variable definitions>
    <variable definitions>

    MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);  
    MPI_Comm_size(MPI_COMM_WORLD,&number_of_processes);

    local_integral = <integrationfunction>

    // send / receive
    // set up an if statement such that:
    // - only the slaves are sent with the calculation

    if (my_rank !=0){           // slaves 
        int receiver_id = 0;
        MPI_Send(&local_integral,1, MPI_DOUBLE, receiver_id, tag, MPI_COMM_WORLD );
    }
    else{                       // master
        double receive_buffer;
        MPI_Status status; 
        for (int source_id=1;source_id<number_of_processes; source_id++){
        MPI_Recv(&receive_buffer,1,MPI_DOUBLE,source_id,tag,MPI_COMM_WORLD,&status);
        result+=receive_buffer;
        }
    }
    result += local_integral;
    MPI_Finalize();
    return 0;
}
```



