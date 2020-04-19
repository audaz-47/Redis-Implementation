# Redis-Implementation
1. This project has been coded using python language. Python is good for quick development. It help in writing a better readable code and can always be used unless it doesn't cause bottleneck in speed or scale. It is good for dummy projects like this.
2. An Improvement that can be made is to regularly remove the elements from the sorted list whose TTL has expired. This will save the memory from being stacked up with unnecessary elements.
3. Python Dictionary has been used for the project since this data structure allows to store and retrieve key value pairs efficiently. The keys can be inserted and deleted in O(1) time complexity and the sorted list can be maintained in O(logn) time complexity.
4. My current implementation does not support multi-threading as the shared variables can be modified by more than one process leading to race condition. This can be solving by using a locking mechanism on the write methods.
