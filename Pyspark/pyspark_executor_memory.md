Total Executor Memory (4 GB)
├── Reserved Memory (~300 MB)         ❌ Fixed, not configurable
│
├── Usable Memory (~3.7 GB)
    ├── Spark Memory (default: 60%)   ➡️ spark.memory.fraction = 0.6
    │   ├── Execution Memory (50%)    ➡️ spark.memory.storageFraction = 0.5
    │   └── Storage Memory (50%)      ➡️ For caching, broadcast vars
    │
    └── User Memory (40%)             ➡️ Your code (e.g., UDFs, drivers, Python objects)



**Component         | Size (approx)     | Purpose**
Reserved Memory     | 300 MB            | Spark internal bookkeeping (non-configurable)
Usable Memory       | 3.7 GB            | The rest after reservation
├── Spark Memory    | 2.2 GB            | Execution + Storage
│   **├── Execution | 1.1 GB            | Read partitions, Joins, shuffles, aggregations**
│   **└── Storage   | 1.1 GB            | Cached RDDs, broadcast tables / vars**
└── User Memory     | 1.5 GB            | User functions, Python objects, logs


rdd = df.rdd
# Estimate size of each partition
partition_sizes = rdd.glom().map(lambda part: sys.getsizeof(part)).collect()


# Spark UI (More Accurate, Visual Way) to check the size of data used from partition
├── Open **Spark UI** → Go to **Stages** → Select a Stage → Click on a **Task**
    ├── Input Size / Records
    ├── Shuffle Read / Write
    ├── Memory Spilled


