def disconnected_users(net, users, source, crushes):
    net, _ = fine_nodes(net, crushes)

    disconnected_sum = 0

    source_nodes = set()
    source_nodes.add(source)
    connected_nodes = connections(source_nodes, net, source)
    for x in users:
        if x not in connected_nodes:
            disconnected_sum += users[x]
    return disconnected_sum

def fine_nodes(net, crushes):
    for one_net in net:
        for crush in crushes:
            if crush in one_net:
                net.remove(one_net)
                return fine_nodes(net, crushes)
    return net, crushes


def connections(user_nodes, good_nodes, source):
    if good_nodes == []:
        return user_nodes
    else:
        for user in user_nodes:
            if user in good_nodes[0]:
                user_nodes.add(good_nodes[0][0])
                user_nodes.add(good_nodes[0][1])
                break
        return connections(user_nodes, good_nodes[1:], source)

if __name__ == '__main__':
# These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

assert disconnected_users([
    ['A', 'B'],
    ['B', 'D'],
    ['A', 'C'],
    ['C', 'D']
], {
    'A': 10,
    'B': 0,
    'C': 0,
    'D': 40
},
    'A', ['B']) == 0, "Second"

assert disconnected_users([
    ['A', 'B'],
    ['A', 'C'],
    ['A', 'D'],
    ['A', 'E'],
    ['A', 'F']
], {
    'A': 10,
    'B': 10,
    'C': 10,
    'D': 10,
    'E': 10,
    'F': 10
},
    'C', ['A']) == 50, "Third"

print('Done. Try to check now. There are a lot of other tests')
