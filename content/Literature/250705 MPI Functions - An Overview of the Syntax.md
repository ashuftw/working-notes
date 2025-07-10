---
title: MPI Functions - An Overview of the Syntax
draft: false
tags: 
date: 2025-07-05
---

| **Function**      | Syntax                                                                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- |
| **MPI_Init**      | `int MPI_Init(int* argc, char*** argv);`                                                                              |
| **MPI_Finalize**  | `int MPI_Finalize(void);`                                                                                             |
| **MPI_Comm_size** | `int MPI_Comm_size(MPI_Comm com, int* size);`                                                                         |
| **MPI_Comm_rank** | `int MPI_Comm_rank(MPI_Comm com, int* rank);`                                                                         |
| **MPI_Send**      | `int MPI_Send(void* data, int count, MPI_Datatype datatype, int destination, int tag, MPI_Comm com);`                 |
| **MPI_Recv**      | `int MPI_Recv(void* data, int count, MPI_Datatype datatype, int source, int tag, MPI_Comm com, MPI_Status* status);`  |
| **MPI_Reduce**    | `int MPI_Reduce(void* sendbuf, void* recvbuf, int count, MPI_Datatype datatype, MPI_Op op, int root, MPI_Comm comm);` |
| **MPI_Bcast**     | `int MPI_Bcast(void *buffer, int count, MPI_Datatype datatype, int root,MPI_Comm comm);`                              |

**Note**: `MPI_COMM_WORLD` is not a function but a predefined constant used in most of these functions as the `comm` parameter.

| MPI_COMM_WORLD | `MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);` |
| -------------- | --------------------------------------------- |

**Parameters:**
- `argc`, `argv`: Command line arguments (passed by reference)
- `com`: MPI communicator (typically `MPI_COMM_WORLD`)
- `size`: Pointer to store number of processes
- `rank`: Pointer to store process rank
- `data`: Pointer to data buffer
- `count`: Number of elements to send/receive
- `datatype`: MPI data type (e.g., `MPI_INT`, `MPI_CHAR`)
- `destination/source`: Target/source process rank
- `tag`: Message tag for identification
- `status`: Status object for receive operations

All functions return an integer status code indicating success or failure.
on operations: `MPI_SUM`, `MPI_MAX`, `MPI_MIN`, `MPI_PROD`

**Quick Reference:**
- Single values: use `&`
- Arrays: no `&` (e.g., `MPI_Send(array, 10, MPI_INT, ...)`)
- Common datatypes: `MPI_INT`, `MPI_DOUBLE`, `MPI_FLOAT`, `MPI_CHAR`
- Common operations: `MPI_SUM`, `MPI_MAX`, `MPI_MIN`, `MPI_PROD`
