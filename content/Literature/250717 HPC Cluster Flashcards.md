---
title: HPC Cluster Flashcards
draft: false
tags: 
date: 2025-07-17
---
****### **Card 1: What is an HPC System?**

**Front:** What is the fundamental purpose and design of a High-Performance Computing (HPC) system?

**Back:** 
- An HPC system, or cluster, is a multi-user system designed for performance through **parallelized computing**. 
- It uses a different architecture with many CPUs and/or GPUs spread across multiple servers called nodes.
- Its purpose is to run complex simulations and process massive datasets for fields like CFD, physics, and weather forecasting.
- Most HPC systems run on Linux-based operating systems.


---

### **Card 2: What are HPC Tiers?**

**Front:** How are HPC systems categorized, and what do the categories mean?

**Back:** HPC systems are categorized into **Tiers** bases system's **computing capacity** and **scale**:

- **Tier 0 (European):** The most powerful systems in Europe, for highly complex international projects (e.g., JUWELS in Jülich).
- **Tier 1 (National):** Major national supercomputing centers.
- **Tier 2 (Supraregional):** Serve a wide region of users.
- **Tier 3 (Regional):** Local clusters for a specific university or institution, like the Phoenix cluster in Braunschweig.

---

### **Card 3: HPC vs. Home Computer**

**Front:** What are the key architectural and operational differences between an HPC cluster and a home computer?

**Back:**
- **Architecture & Hardware:** An HPC is a multi-user system built from many "server-grade" nodes designed for 24/7 operation. It uses a different architecture from consumer computers.
- **Environment:** They are housed in specialized buildings to manage their extreme power and cooling needs.
- **Operation:** They are almost always Linux-based. Access to computing resources is not direct but is managed by a **job scheduler** that uses a queue system.

---

### **Card 4: What are the 3 Vital Components of a Cluster?**

**Front:** Name and describe the three most vital hardware components that make an HPC cluster function.

**Back:**
1. **Compute Nodes:** The individual servers that execute jobs and perform the actual calculations. There are different types, like standard nodes, **GPU nodes** for highly parallel tasks, and **fat nodes** with large amounts of RAM.
2. **Fast Network:** A high-speed, low-latency network (like **Infiniband**) that connects all the nodes. This is crucial for parallel tasks where nodes must communicate very quickly.
3. **Shared Filesystem:** Centralized storage servers that provide a filesystem accessible to all nodes. This means files do not need to be copied between nodes to be read or written.

---

### **Card 5: Why Use the Lmod Module System?**

**Front:** Why must users on an HPC system use a tool like Lmod instead of installing software themselves?

**Back:** Using the Lmod module system is necessary for several reasons:
- **User Privileges:** Users do not have administrator rights, so they cannot use system package managers (like `apt` or `zypper`) to install software.
- **Hardware Optimization:** The pre-installed software available through modules is often specifically compiled and optimized by administrators for the cluster's unique hardware, ensuring better performance.
- **Dependency Management:** Lmod automatically handles all software/library dependencies and correctly sets environment variables (`PATH`, etc.), which is a very tedious and difficult process to do manually.

---

### **Card 6: What is a Job Scheduler like SLURM?**
**Front:** What is a job scheduler, and why is it essential for an HPC system?

**Back:** A job scheduler like **SLURM** (Simple Linux Utility for Resource Management) is a tool that manages access to the cluster's compute resources. It is essential because:
- **Prevents Chaos:** Clusters are multi-user systems, and a scheduler prevents chaos by controlling who can use the compute nodes and when.
- **Manages Allocation:** It allocates compute nodes to users for a specific amount of time based on a job queue.
- **Enforces Priority:** Job scheduling is based on factors like job priority and a user's previously consumed CPU hours, ensuring fair access.

---

### **Card 7: The HPC Simulation Workflow**

**Front:** Describe the step-by-step process of preparing and running a simulation on an HPC cluster.

**Back:**

1. **Connect:** Remotely connect to the cluster's **login node** via SSH.
2. **Prepare Environment:** Use `module load <module-name>` to load the specific software and libraries you need for your job.
3. **Create Job Script:** Write a bash script containing the commands for your simulation. Use `#SBATCH` directives at the top to tell the scheduler what resources you need (e.g., `#SBATCH --nodes=2`, `#SBATCH --time=01:00:00`).
4. **Submit Job:** Submit your script to the scheduler using the `sbatch` command. The job is placed in a queue and runs when the resources become available.
---

### **Card 8: Visual Access Method 1: X-Forwarding**

**Front:** How can you get basic, single-application visual access to an HPC system?

**Back:** You can use **X-Forwarding** via SSH. This method requires a **visualization node** with a graphics card.
- **How it works:** You connect using `ssh -X` or `ssh -Y`. This forwards the graphical output of an application from the HPC directly to your local machine's display.
- **Use Case:** Good for launching a single GUI application from the terminal.
- **Drawback:** It requires high bandwidth and can be slow or laggy.

---

### **Card 9: Visual Access Method 2: Remote Desktop (VNC)**

**Front:** How can you get a full graphical desktop environment on an HPC system?

**Back:** You can use a remote desktop protocol like **VNC (Virtual Network Computing)**, which is more bandwidth-efficient than X-forwarding.
- **How it works:** It provides a full desktop environment on the remote visualization node.
- **Process:**
    1. Start a VNC server session on the visualization node (e.g., using the`vncserver` command).
    2. Use a VNC client program on your local computer to connect to that server session.