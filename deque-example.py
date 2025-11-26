from collections import deque

# Membuat deque kosong
dq = deque()

# Menambahkan elemen
dq.append(10)        # push_back
dq.appendleft(20)    # push_front
dq.append(30)

print("Isi deque:", dq)

# Menghapus elemen
dq.pop()             # pop_back
dq.popleft()         # pop_front

print("Setelah dihapus:", dq)
