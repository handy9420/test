# 散列表存储广播台及其覆盖的州，这里键的值都用集合，包括下面所有数据都用集合，方便交并补
stations = dict()
stations["k1"] = set(["id", "nv", "ut"])
stations["k2"] = set(["wa", "id", "mt"])
stations["k3"] = set(["or", "nv", "ca"])
stations["k4"] = set(["nv", "ut"])
stations["k5"] = set(["ca", "az"])
# 需要被覆盖的州，每轮更新
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# 最终选择的广播台， 每轮更新
stations_selected = set()
while states_needed:
    # 每轮选择的广播台能覆盖的未被覆盖的州的最大个数，每轮都要进行重置！！！
    states_covered_max = set()
    for key, value in stations.items():  # 字典怎么迭代？.items()
        if len(value & states_needed) > len(states_covered_max):  # 与需要被覆盖的州的交集就是此时广播台的广播能力
            states_covered_max = value
            station = key  # 当前选择的广播台
    states_needed -= states_covered_max
    stations_selected.add(station)
print(stations_selected)

# 运行结果：
# {'k2', 'k3', 'k1', 'k5'}
# 合理使用调试，因为之前进入了死循环，原因是没有对states_covered_max 的值重置
