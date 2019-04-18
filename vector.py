class Vector:
  def __init__ (self, lst):
    self._values = list(lst)
  @classmethod
  def zero(cls, dim):
    return cls([0] * dim)
  def __repr__(self):
    return "Vector({})".format(self._values)
  def __str__(self):
    return "({})".format(", ".join(str(e) for e in self._values))
  def __len__(self):
    return len(self._values)
  def __getitem__(self, index):
    return self._values[index]
  # 迭代器
  def __iter__(self):
    return self._values.__iter__()
  # 加法
  def __add__(self, another):
    assert len(self) == len(another), \
      "向量维度需要相同"
    return Vector([a + b for a, b in zip(self, another)])
  # 减法
  def __sub__(self, another):
    assert len(self) == len(another), \
      "向量维度需要相同"
    return Vector([a - b for a, b in zip(self, another)])
  # 乘法
  def __mul__(self, k):
    return Vector([k * e for e in self])
  def __rmul__(self, k):
    return self * k
  # 取正
  def __pos__(self):
    return 1 * self
  # 取负
  def __neg__(self):
    return -1 * self