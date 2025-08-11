---
title: MPI Send Modes
draft: false
tags: 
date: 2025-08-03
---
## Overview Table

|Mode|Blocking|Non-blocking|
|---|---|---|
|**Standard**|`MPI_Send`|`MPI_Isend`|
|**Buffered**|`MPI_Bsend`|`MPI_Ibsend`|
|**Synchronous**|`MPI_Ssend`|`MPI_Issend`|
|**Ready**|`MPI_Rsend`|`MPI_Irsend`|

_Note: "I" = immediate (non-blocking)_

## Communication Modes
***Standard Mode***
- **Behavior**: May buffer (implementation-dependent)
- **Returns**: Immediately for small messages, blocks for large
- **Use**: Default choice

***Buffered Mode***
- **Behavior**: Always uses user-provided buffer
- **Returns**: Immediately after buffer copy
- **Setup**: Needs `MPI_Buffer_attach/detach`

***Synchronous Mode***
- **Behavior**: Waits for receiver handshake
- **Returns**: Only after receiver starts receiving
- **Warning**: Causes deadlock in ring patterns

***Ready Mode***
- **Behavior**: Assumes receiver is waiting
- **Returns**: Immediately (no checks)
- **Risk**: Crashes if receiver not ready

## Quick Examples

```c
// Deadlock with synchronous
P0: MPI_Ssend → P1; MPI_Recv ← P1
P1: MPI_Ssend → P0; MPI_Recv ← P0

// Safe with non-blocking
MPI_Isend(..., &req1);
MPI_Irecv(..., &req2);
MPI_Waitall(2, requests, statuses);
```

## Key Points

- Use `MPI_Send` unless you need specific behavior
- Use `MPI_Ssend` for debugging/testing
- Use non-blocking to prevent deadlocks
- Ready mode is fastest but dangerous