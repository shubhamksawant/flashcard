questions = [
    {
        "question": """What is a process in an operating system?""",
        "answer": """A process is a program in execution. It includes the program code, current activity (program counter, registers), and process stack and heap. Each process has its own memory space and resources allocated by the OS.""",
        "topic": "os"
    },
    {
        "question": """What is the difference between a process and a thread?""",
        "answer": """A process is an independent program with its own memory space, while threads are lightweight units of execution within a process. Threads share the same memory space and resources of their parent process but have their own stack and register set.""",
        "topic": "os"
    },
    {
        "question": """What is virtual memory?""",
        "answer": """Virtual memory is a memory management technique that provides an idealized abstraction of the storage resources that are actually available on a given machine. It allows programs to use more memory than physically available by using disk space as an extension of RAM.""",
        "topic": "os"
    },
    {
        "question": """What is a page fault?""",
        "answer": """A page fault occurs when a program tries to access a page that is mapped in the virtual address space but not loaded in physical memory. The OS must then load the required page from disk into memory, potentially removing other pages to make room.""",
        "topic": "os"
    },
    {
        "question": """What is process scheduling?""",
        "answer": """Process scheduling is the activity of the process manager that handles the removal of the running process from the CPU and the selection of another process based on a particular strategy. Common algorithms include Round Robin, FCFS (First Come First Serve), and Priority Scheduling.""",
        "topic": "os"
    },
    {
        "question": """What is a deadlock and what are its conditions?""",
        "answer": """A deadlock is a situation where two or more processes are unable to proceed because each is waiting for resources held by another. Four conditions for deadlock: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.""",
        "topic": "os"
    },
    {
        "question": """What is the purpose of an inode in a file system?""",
        "answer": """An inode (index node) is a data structure that stores metadata about a file including: file size, owner, permissions, timestamps, and disk block locations. Every file in the filesystem has a unique inode number.""",
        "topic": "os"
    },
    {
        "question": """What is the difference between hard and soft links?""",
        "answer": """A hard link is a direct reference to the physical file (same inode), while a soft link (symbolic link) is a reference to the file path. Hard links can't cross filesystems and can't link to directories, while soft links can do both.""",
        "topic": "os"
    },
    {
        "question": """What is context switching?""",
        "answer": """Context switching is the process of saving the state of a running process and restoring the state of a different process when switching between them. It includes saving/restoring CPU registers, memory maps, and other resources.""",
        "topic": "os"
    },
    {
        "question": """What is the difference between kernel space and user space?""",
        "answer": """Kernel space is where the kernel (core OS) executes and provides its services. User space is where user applications run. The separation provides protection and security, as user processes can't directly access kernel resources without using system calls.""",
        "topic": "os"
    },
]
