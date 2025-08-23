import tracemalloc

tracemalloc.start()

# 模拟内存分配
data = [list(range(1000)) for _ in range(100)]

# 拍照
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')  # 按行号统计

print("内存占用前5名:")
for stat in top_stats[:5]:
    print(stat)